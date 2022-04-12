# Kernel Correlation Filters (KCF)
# 
# Algoritmo rápido, mas tem dificuldade em encontrar objetos que se movem muito rápido
# 
# Processo: Inicialização -> Translação e estimação das caixas delimitadoras -> Estimação da escala -> Estimação da translação.

import cv2

rastreador = cv2.TrackerKCF_create()

video = cv2.VideoCapture('race.mp4')

# leitura ok, frame do vídeo
ok, frame = video.read()

# Caixa delimitadora do primeiro frame
bbox = cv2.selectROI(frame)

ok = rastreador.init(frame, bbox)

while True:
    ok, frame = video.read()

    if not ok: 
        break
    
    # Caixa delimitadora
    ok, bbox = rastreador.update(frame)
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2, 1)
    else:
        cv2.putText(frame, 'Erro', (100, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

    cv2.imshow('Rastreamento', frame)

    if cv2.waitKey(1) & 0XFF == 27: # Espera pela tecla ESC
        break