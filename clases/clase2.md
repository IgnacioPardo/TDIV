---
title: "TDIV: Clase 2"
output: pdf_document
date: 2022-07-01
---
<!-- markdownlint-disable MD033 -->

## Introducción a las Redes de Computadoras Parte 2

### Encolamiento de Paquetes

Cola de paquetes aguardando a ser transmitidos

<!-- <iframe scrolling="no" width="650" height="500" src="https://computerscience.unicam.it/marcantoni/reti/applet/QueuingAndLossInteractive/1.html"> -->

### Circuit Switching

Se produce una reserva previa de recursos para la comunicación entre dos interlocutores
Recursos dedicados
Un circuito permanece inactivo si no esta siendo utilizado en una conexión
Usualmente utilizado en redes telefónicas

#### FDM

Multiplexación por División de Frencuencias

- Ancho de banda total dividido en bandas de frecuencias
- Cada conexión recibe su propia banda

#### TDM

Multiplexación por División de Tiempo

- Tiempo dividido en intervalos (slots)
- Cada conexión recibe intervalos periódicos durante las cuales puede transmitir empleando todo el ancho de banda

### Conmutación de paquetes vs circuitos

- Conmutación de paquetes: ideal para datos "en ráfagas".
  - Recursos compartidos
  - No precisa una etapa de reserva de recursos

- Posible de sufrir congestion: latencias altas y perdidas de paquetes por buffers saturados
  - Se debe contar con protocolos confiables y con control de congestión.

### Tipos de Latencia

$$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

$L$: Longitud del paquete (bits)
$R$: Tasa de transmisión (bits/segundo)

- delay de procesamiento
- delay de transmisión: L/R
- delay de propagación: d/s (d: long del enlace físico, s: velocidad de propagación)

### Internet: red de redes

- Los hosts se conectan a Internet a través de los ISPs

### Delays y rutas en internet

Permite ver la ruta (_hops_) de un paquete de un host a otro, ofreciendo estimaciones de delay hacia cada router intermedio

    traceroute -P ICMP www.google.com

## Stack de protocolos de internet

- **Capa de Aplicación** (HTTP, FTP, IMAP, SMTP, DNS)
    Soporte para aplicaciones
- **Capa de Transporte** (TCP, UDP)
    Transferencia de datos entre procesos
- **Capa de Red** (IP, OSPF, BGP)
    Ruteo de datagramas de origen a destino
- **Capa de Enlace** (Ethernet, 802.11, WLAN)
    Transferencia de datos entre dispositivos de red adyacentes
- **Capa de Física**
    Transferencia de bits en el medio físico
