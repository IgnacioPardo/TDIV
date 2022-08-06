# Guía de Ejercicios - 1

## Introducción a las Redes de Computadoras

<!-- markdownlint-disable MD007 -->

- 1. Supongamos que los usuarios comparten un link de 2 Mbps, y que cada usuario transmite continuamente a 1 Mbps, pero sólo transmiten el 20% del tiempo.
    - a. Cuando se utiliza conmutación de circuitos (circuit switching), ¿Cuántos usuarios pueden transmitir simultáneamente?
    - b. Supongamos que se utiliza conmutación de paquetes.
        - ¿Por qué no se generaría delay en las colas de los routers si dos o menos usuarios transmitieran información simultáneamente?
        - ¿Por qué sí se generaría delay si más de dos usuarios transmitieran al
mismo tiempo?
    - c. ¿Cuál es la probabilidad de que un determinado usuario esté transmitiendo?
    - d. Suponiendo que tenemos tres usuarios.
        - ¿Cuál es la probabilidad de que los tres transmitan simultáneamente?
        - ¿Qué fracción del tiempo las colas de los routers encolan paquetes?

- 2. ¿Cuánto tarda un paquete con un tamaño de 1000 bytes en propagarse sobre un enlace de 2500 km, con una velocidad de propagación de 2.5 x 108 m/s, y una tasa de transmisión de 2 Mbps? ¿Cuánto tarda en propagarse un paquete de tamaño L sobre un link de longitud d, con una velocidad de propagación s, y una tasa de transmisión R bps? ¿Depende del tamaño del paquete y de la tasa de transmisión?

- 3. Supongamos que el host A quiere enviar un archivo grande al host B. El camino desde el
host A hasta el host B tiene tres secciones (enlaces), con tasas de transmisión de R1 =
500 kbps, R2 = 2 Mbps, y R3 = 1 Mbps.
    - a. Asumiendo que no hay tráfico en la red, ¿Cuál es el throughput para la transferencia del archivo?
    - b. Supongamos que el archivo pesa 4 millones de bytes. ¿Cuánto tardaría en transferirse al host B?
    - c. Repetir (a) y (b), pero ahora R2 se reduce a 100 kbps.

- 4. ¿Cuáles son las cinco capas en el stack de protocolos de internet? ¿Cuáles son las
principales responsabilidades de cada capa?
- 5. ¿Qué capas procesa un router? ¿Cuáles maneja un switch? ¿Cuáles procesa un host?
- 6. Consideremos dos hosts A y B conectados por un enlace simple con una tasa de R bps. Supongamos que los dos hosts están separados m metros y la velocidad de propagación
por el enlace es de s metros/seg. El host A envía un paquete de tamaño L bits al host B.
    - a. Expresar el delay de propagación dprop en términos de m y s.
    - b. Determinar el tiempo de transmisión del paquete dtrans en términos de L y R.
    - c. Ignorando el delay de encolamiento y de procesamiento, obtener una expresión
para el delay end-to-end.
    - d. Supongamos que el host A comienza a transmitir el paquete en un tiempo t = 0.
Determinar dónde está el último bit del paquete en el instante t = dtrans
    - e. Supongamos que dprop es mayor a dtrans. Determinar dónde está el primer bit del paquete en el instante t = dtrans,.f. Dado s = 2.5 x 108, L = 1500 bytes, R = 10 Mbps, determinar la distancia para la cual dprop es igual a dtrans.
- 7. Considerar un paquete de longitud L que comienza en el host A y viaja a través de tres
enlaces al host de destino. Estos tres enlaces están conectados por dos packet switches, siendo di , si y Ri la longitud del link, la velocidad de propagación y la tasa de transmisión del enlace i respectivamente (para i = 1, 2, 3). El tiempo de procesamiento en cada packet switch es dproc. Asumiendo que no hay delay de encolamiento:
    - a. ¿Cuál es el delay end-to-end total para el paquete?
    - b. ¿Cuál es el delay end-to-end considerando los siguientes datos?:
        - Un paquete de 1.500 bytes;
        - Velocidad de propagación de 2,5x108 m/s y tasa de transmisión de 2,5
Mbps en los tres enlaces;
        - Delay de procesamiento de cada packet switch de 3 ms;
        - Longitud del primer link de 5.000 km, del segundo de 4.000 km, y del
último de 1.000 km.
