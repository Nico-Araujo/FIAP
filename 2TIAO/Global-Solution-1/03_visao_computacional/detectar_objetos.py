"""

Objetivo:
  - Detectar e RASTREAR objetos em movimento rápido contra o fundo
    do céu / nuvens (usando OpenCV).
  - Extrair propriedades visuais do objeto: cor, formato
    (esférico / tic-tac), proporção das asas.

Abordagem:
  Usamos subtração de fundo (Background Subtraction) do OpenCV, que é
  uma versão SIMPLIFICADA e leve para detectar movimento — ideal para
  céu limpo. 

Como rodar:
    pip install opencv-python numpy
    python detectar_objetos.py --video ceu.mp4
    # ou use a webcam:
    python detectar_objetos.py --webcam
"""

import cv2
import numpy as np
import argparse


def classificar_formato(contorno):
    """
    Analisa a geometria do contorno para classificar o formato.
    Retorna: ('esferico' | 'tic-tac' | 'alongado/asas', proporcao)
    """
    x, y, largura, altura = cv2.boundingRect(contorno)
    if altura == 0:
        return "indefinido", 0.0

    proporcao = largura / float(altura)  # aspect ratio

    if 0.85 <= proporcao <= 1.15:
        formato = "esferico"          # quase quadrado -> esfera/disco visto de frente
    elif proporcao > 2.5:
        formato = "tic-tac/alongado"  # bem mais largo que alto -> tic-tac ou asas
    else:
        formato = "ovalado"

    return formato, proporcao


def cor_media(frame, contorno):
    """Extrai a cor média (BGR) dentro do contorno do objeto."""
    mascara = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.drawContours(mascara, [contorno], -1, 255, -1)
    media = cv2.mean(frame, mask=mascara)  # (B, G, R, _)
    return (int(media[2]), int(media[1]), int(media[0]))  # devolve em RGB


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, help="Caminho do arquivo de vídeo")
    parser.add_argument("--webcam", action="store_true", help="Usar a webcam")
    args = parser.parse_args()

    if args.webcam:
        captura = cv2.VideoCapture(0)
    elif args.video:
        captura = cv2.VideoCapture(args.video)
    else:
        print("Use --video caminho.mp4  OU  --webcam")
        return

    # Subtrator de fundo: separa o objeto em movimento do céu parado
    subtrator = cv2.createBackgroundSubtractorMOG2(
        history=500, varThreshold=40, detectShadows=False
    )

    # Para rastrear o objeto e medir velocidade entre frames
    centro_anterior = None

    while True:
        ok, frame = captura.read()
        if not ok:
            break

        # 1) Detecta movimento
        mascara = subtrator.apply(frame)
        mascara = cv2.medianBlur(mascara, 5)
        _, mascara = cv2.threshold(mascara, 200, 255, cv2.THRESH_BINARY)

        # 2) Encontra os contornos dos objetos em movimento
        contornos, _ = cv2.findContours(
            mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for c in contornos:
            area = cv2.contourArea(c)
            if area < 100:  # ignora ruído pequeno
                continue

            x, y, w, h = cv2.boundingRect(c)
            cx, cy = x + w // 2, y + h // 2  # centro do objeto

            # 3) Extrai propriedades visuais
            formato, proporcao = classificar_formato(c)
            rgb = cor_media(frame, c)

            # 4) Calcula deslocamento (proxy de velocidade) entre frames
            velocidade_px = 0
            if centro_anterior is not None:
                velocidade_px = int(
                    np.hypot(cx - centro_anterior[0], cy - centro_anterior[1])
                )
            centro_anterior = (cx, cy)

            # 5) Desenha na tela
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            texto = f"{formato} | RGB:{rgb} | vel:{velocidade_px}px"
            cv2.putText(
                frame, texto, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
            )

            # Imprime no terminal 
            print(
                f"Objeto -> formato={formato}, proporcao={proporcao:.2f}, "
                f"cor_rgb={rgb}, deslocamento={velocidade_px}px/frame"
            )

        cv2.imshow("Detector de UAPs", frame)
        if cv2.waitKey(30) & 0xFF == ord("q"):  # tecla 'q' para sair
            break

    captura.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


