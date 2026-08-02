"""
Script principal para criar o banco de dados 'gs_database.db'.

O que ele faz:
- Lê os 5 arquivos JSON do projeto.
- Cria a estrutura de todas as tabelas necessárias.
- Insere os dados dos JSONs nas tabelas correspondentes.

A ideia é rodar este script uma vez para ter o banco de dados pronto.
"""

import sqlite3
import json
import os

DB_FILE = "gs_database.db"

def load_json_data(file_name):
    # Função para carregar um arquivo JSON.
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"ERRO: Arquivo '{file_name}' não encontrado. Ele precisa estar na mesma pasta que este script.")

def create_connection(db_file):
    # Conecta no arquivo do banco de dados.
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar com o banco: {e}")
        return None

def create_tables(conn):
    # Cria todas as tabelas de uma vez só.
    # O 'IF NOT EXISTS' é uma segurança para não dar erro se rodarmos o script de novo.
    sql_script = """
        CREATE TABLE IF NOT EXISTS sensores_parametros (nome_parametro TEXT PRIMARY KEY, unidade TEXT NOT NULL, ideal_min REAL, ideal_max REAL, critico_min REAL, critico_max REAL);
        CREATE TABLE IF NOT EXISTS tipos_solo (id_solo INTEGER PRIMARY KEY, nome_solo TEXT NOT NULL UNIQUE, profundidade TEXT, drenagem TEXT, fertilidade TEXT, resistencia_erosao TEXT, ph_natural TEXT);
        CREATE TABLE IF NOT EXISTS planos_recuperacao (id_plano INTEGER PRIMARY KEY, id_solo INTEGER NOT NULL, tipo_desastre TEXT NOT NULL, tecnicas_recuperacao TEXT, fertilizante_recomendado TEXT, quantidade_fertilizante_kg_ha REAL, custo_recuperacao_reais_ha REAL, tempo_recuperacao_meses INTEGER, FOREIGN KEY (id_solo) REFERENCES tipos_solo (id_solo));
        CREATE TABLE IF NOT EXISTS desastres_historico (id_desastre TEXT PRIMARY KEY, ano INTEGER, mes INTEGER, tipo_desastre TEXT, estado TEXT, area_afetada_km2 REAL, populacao_afetada INTEGER, custo_recuperacao_milhoes REAL, impacto_compactacao TEXT, impacto_erosao TEXT, impacto_perda_materia_organica TEXT, impacto_alteracao_ph TEXT, impacto_contaminacao TEXT);
        CREATE TABLE IF NOT EXISTS clima_estados (estado_sigla TEXT PRIMARY KEY, nome_estado TEXT NOT NULL, regiao TEXT, temperatura_media REAL, precipitacao_anual_mm REAL, ph_solo_medio REAL, tipo_solo_predominante TEXT);
        CREATE TABLE IF NOT EXISTS casos_sucesso (id_caso TEXT PRIMARY KEY, titulo TEXT, estado TEXT, municipio TEXT, area_hectares REAL, tipo_desastre TEXT, ph_inicial REAL, ph_final REAL, umidade_inicial REAL, umidade_final REAL, tempo_recuperacao_meses INTEGER, custo_total_reais REAL, taxa_sucesso_percent REAL);
        CREATE TABLE IF NOT EXISTS tecnicas_aplicadas_sucesso (id_tecnica INTEGER PRIMARY KEY, id_caso TEXT NOT NULL, tecnica TEXT, custo_reais REAL, FOREIGN KEY (id_caso) REFERENCES casos_sucesso (id_caso));
    """
    try:
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar as tabelas: {e}")

#Funções para popular cada tabela 

def populate_sensores(conn, data):
    sql = 'INSERT OR IGNORE INTO sensores_parametros(nome_parametro, unidade, ideal_min, ideal_max, critico_min, critico_max) VALUES(?,?,?,?,?,?)'
    cursor = conn.cursor()
    for nome_param, dados in data.items():
        critico_min = dados['faixa_critica'].get('muito_seco') or dados['faixa_critica'].get('muito_frio') or dados['faixa_critica'].get('muito_acido') or dados['faixa_critica'].get('muito_baixa')
        critico_max = dados['faixa_critica'].get('muito_umido') or dados['faixa_critica'].get('muito_quente') or dados['faixa_critica'].get('muito_alcalino') or dados['faixa_critica'].get('muito_alta')
        cursor.execute(sql, (nome_param, dados['unidade'], dados['faixa_ideal']['minimo'], dados['faixa_ideal']['maximo'], critico_min, critico_max))
    conn.commit()

def populate_solos_e_planos(conn, data):
    sql_solo = 'INSERT OR IGNORE INTO tipos_solo(nome_solo, profundidade, drenagem, fertilidade, resistencia_erosao, ph_natural) VALUES(?,?,?,?,?,?)'
    sql_plano = 'INSERT OR IGNORE INTO planos_recuperacao(id_solo, tipo_desastre, tecnicas_recuperacao, fertilizante_recomendado, quantidade_fertilizante_kg_ha, custo_recuperacao_reais_ha, tempo_recuperacao_meses) VALUES(?,?,?,?,?,?,?)'
    cursor = conn.cursor()
    for nome_solo, dados_solo in data.items():
        caracteristicas = dados_solo['caracteristicas']
        cursor.execute(sql_solo, (nome_solo, caracteristicas['profundidade'], caracteristicas['drenagem'], caracteristicas['fertilidade'], caracteristicas['resistencia_erosao'], caracteristicas['ph_natural']))
        id_solo = cursor.lastrowid if cursor.lastrowid > 0 else cursor.execute("SELECT id_solo FROM tipos_solo WHERE nome_solo = ?", (nome_solo,)).fetchone()[0]
        for desastre_key, plano in dados_solo.items():
            if desastre_key.startswith("pos_"):
                tipo_desastre = desastre_key.replace("pos_", "")
                tecnicas = ", ".join(plano['tecnicas_recuperacao'])
                cursor.execute(sql_plano, (id_solo, tipo_desastre, tecnicas, plano['fertilizante_recomendado'], plano.get('quantidade_fertilizante_kg_ha'), plano.get('custo_recuperacao_reais_ha'), plano.get('tempo_recuperacao_meses')))
    conn.commit()

def populate_desastres(conn, data):
    sql = '''INSERT OR IGNORE INTO desastres_historico(id_desastre, ano, mes, tipo_desastre, estado, area_afetada_km2, populacao_afetada, custo_recuperacao_milhoes, impacto_compactacao, impacto_erosao, impacto_perda_materia_organica, impacto_alteracao_ph, impacto_contaminacao)
             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cursor = conn.cursor()
    for desastre in data:
        impactos = desastre['impactos_solo']
        valores = (
            desastre['id_desastre'], desastre['ano'], desastre['mes'], desastre['tipo_desastre'], desastre['estado'], 
            desastre.get('area_afetada_km2'), desastre.get('populacao_afetada'), desastre.get('custo_recuperacao_milhoes'), 
            impactos.get('compactacao'), impactos.get('erosao'), impactos.get('perda_materia_organica'), 
            impactos.get('alteracao_ph'), impactos.get('contaminacao')
        )
        cursor.execute(sql, valores)
    conn.commit()

def populate_clima(conn, data):
    sql = '''INSERT OR IGNORE INTO clima_estados(estado_sigla, nome_estado, regiao, temperatura_media, precipitacao_anual_mm, ph_solo_medio, tipo_solo_predominante)
             VALUES(?,?,?,?,?,?,?)'''
    cursor = conn.cursor()
    for estado in data:
        valores = (
            estado['estado'], estado['nome_estado'], estado['regiao'], estado.get('temperatura_media'), 
            estado.get('precipitacao_anual_mm'), estado.get('ph_solo_medio'), estado.get('tipo_solo_predominante')
        )
        cursor.execute(sql, valores)
    conn.commit()

def populate_sucesso(conn, data):
    sql_caso = '''INSERT OR IGNORE INTO casos_sucesso(id_caso, titulo, estado, municipio, area_hectares, tipo_desastre, ph_inicial, ph_final, umidade_inicial, umidade_final, tempo_recuperacao_meses, custo_total_reais, taxa_sucesso_percent)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    sql_tecnica = '''INSERT OR IGNORE INTO tecnicas_aplicadas_sucesso(id_caso, tecnica, custo_reais)
                     VALUES(?,?,?)'''
    cursor = conn.cursor()
    for caso in data:
        loc, desastre, cond_ini, resultados, cond_fin = caso['localizacao'], caso['desastre_original'], caso['condicoes_iniciais'], caso['resultados'], caso['resultados']['condicoes_finais']
        valores_caso = (
            caso['id_caso'], caso['titulo'], loc['estado'], loc['municipio'], loc.get('area_hectares'), 
            desastre['tipo'], cond_ini.get('ph_solo'), cond_fin.get('ph_solo'), cond_ini.get('umidade_percent'), 
            cond_fin.get('umidade_percent'), resultados.get('tempo_recuperacao_meses'), 
            resultados.get('custo_total_reais'), resultados.get('taxa_sucesso_percent')
        )
        cursor.execute(sql_caso, valores_caso)
        
        for tecnica_aplicada in caso['tecnicas_aplicadas']:
            cursor.execute(sql_tecnica, (caso['id_caso'], tecnica_aplicada['tecnica'], tecnica_aplicada.get('custo_reais')))
    conn.commit()


def main():
    # Função principal que chama todas as outras na ordem certa.
    print("Iniciando a criação do banco de dados (versão corrigida)...")
    
    try:
        print(" -> Lendo arquivos de dados...")
        dados_sensores = load_json_data('parametros_sensores.json')
        dados_recuperacao = load_json_data('recuperacao_solo.json')
        dados_desastres = load_json_data('desastres_brasil.json')
        dados_clima = load_json_data('clima_brasil.json')
        dados_sucesso = load_json_data('casos_sucesso.json')

        conn = create_connection(DB_FILE)
        if conn:
            print(" -> Criando tabelas...")
            create_tables(conn)
            
            print(" -> Populando tabelas com os dados...")
            populate_sensores(conn, dados_sensores['parametros_sensores'])
            populate_solos_e_planos(conn, dados_recuperacao['tipos_solo'])
            populate_desastres(conn, dados_desastres['dados'])
            populate_clima(conn, dados_clima['dados'])
            populate_sucesso(conn, dados_sucesso['casos'])

            print("\nBanco de dados 'gs_database.db' criado e populado com sucesso!")
            conn.close()

    except Exception as e:
        print(f"\nOcorreu um erro que impediu a criação do banco de dados: {e}")


if __name__ == '__main__':
    main()