# Discriminative Correlation Filter With Channel and Spatial Realibility CSRT
# 
# Mais lento porém obtém os melhores resultados
# 
# Processo: Seleção do objeto a ser rastreado -> HOG para extração de características -> Gera as probabilidades a partir do Random Markov Test -> Máscara.

import cv2

rastreador = cv2.TrackerCSRT_create()

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