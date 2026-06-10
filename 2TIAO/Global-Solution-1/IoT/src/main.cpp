#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <ArduinoJson.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

const int PIN_LED_VERDE = 12;
const int PIN_LED_VERMELHO = 14;

unsigned long anteriorMillis = 0;
const long intervaloPisca = 200; 
bool estadoLedVermelho = LOW;
bool alertaAtivo = false;

// Controle do tempo para o disparo do alarme automático no vídeo
unsigned long tempoInicial = 0;
bool alarmeDisparadoNoVideo = false;

struct DadosAnomalia {
  String status;
  String velocidade;
  String altitude;
  String formato;
};

DadosAnomalia dadosAtuais = {"LIMPO", "---", "---", "---"};

void atualizarDisplay() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("=== SKYGUARD UAP ===");

  lcd.setCursor(0, 1);
  lcd.print("STATUS: ");
  if (alertaAtivo) {
    lcd.print("ANOMALIA!");
  } else {
    lcd.print("CEU SEGURO");
  }

  lcd.setCursor(0, 2);
  lcd.print("V: "); lcd.print(dadosAtuais.velocidade);
  lcd.print(" | A: "); lcd.print(dadosAtuais.altitude);
  
  lcd.setCursor(0, 3);
  lcd.print("Format: "); lcd.print(dadosAtuais.formato);
}

// Função que processa a string JSON (igual ao que viria da serial)
void processarDadosSimulados(String jsonTexto) {
  JsonDocument doc;
  DeserializationError erro = deserializeJson(doc, jsonTexto);

  if (!erro) {
    String alerta = doc["alerta"];
    if (alerta == "POSITIVO_ANOMALIA") {
      alertaAtivo = true;
      dadosAtuais.velocidade = doc["velocidade_estimada"].as<String>();
      dadosAtuais.altitude = doc["altitude"].as<String>();
      dadosAtuais.formato = doc["formato_visao_computacional"].as<String>();
      digitalWrite(PIN_LED_VERDE, LOW);
    }
    atualizarDisplay();
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(PIN_LED_VERDE, OUTPUT);
  pinMode(PIN_LED_VERMELHO, OUTPUT);
  
  // Sistema inicia em segurança total
  digitalWrite(PIN_LED_VERDE, HIGH);
  digitalWrite(PIN_LED_VERMELHO, LOW);

  lcd.init();
  lcd.backlight();
  atualizarDisplay();
  
  tempoInicial = millis(); // Marca o tempo que a placa ligou
  Serial.println("Estacao SkyGuard Inicializada. Monitorando ceu...");
}

void loop() {
  // SIMULAÇÃO AUTOMÁTICA PARA O VÍDEO: 
  // Passados 5 segundos da placa ligada, ela auto-injeta o alerta de UAP
  if (!alarmeDisparadoNoVideo && (millis() - tempoInicial >= 5000)) {
    alarmeDisparadoNoVideo = true;
    Serial.println("\n[ALERTA INJETADO VIA RAG/VISÃO COMPUTACIONAL]");
    
    String jsonMock = "{\"alerta\": \"POSITIVO_ANOMALIA\", \"velocidade_estimada\": \"Mach 4.5\", \"altitude\": \"25.000 pes\", \"formato_visao_computacional\": \"Orb\"}";
    processarDadosSimulados(jsonMock);
  }

  // Efeito de pisca do LED Vermelho se a ameaça estiver ativa
  if (alertaAtivo) {
    unsigned long atualMillis = millis();
    if (atualMillis - anteriorMillis >= intervaloPisca) {
      anteriorMillis = atualMillis;
      estadoLedVermelho = !estadoLedVermelho;
      digitalWrite(PIN_LED_VERMELHO, estadoLedVermelho);
    }
  }
}