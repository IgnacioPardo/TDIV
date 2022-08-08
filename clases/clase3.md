---
title: "TDIV: Clase 3"
output: pdf_document
date: 2022-07-01
---
<!-- markdownlint-disable MD033 MD007-->

## Introducción a las Redes de Computadoras Parte 3

### Nivel Aplicación

Protocolos: HTTP, FTP, SMTP, DNS, SSH, Telnet, etc.

Software que corre en distintos hosts
La comunicación se da a través de la red
Por ejemplo, un browser web (Chrome) se comunica con un servidor web
No se requiere software para dispositivos en el núcleo de la red
Estos dispositivos (routers/switches) no corren aplicaciones de usuario
Las apps en los hosts permiten agilizar el desarrollo y la adopción de las mismas

#### Aplicaciones en red

Software corre en distintos hosts

### Paradigma cliente servidor

### Paradigma peer-to-peer

### Sockets

- Los procesos envían y reciben mensajes a través de sockets.
- Interfaz de comunicación que oficia como una puerta
    - El proceso emisor despacha mensajes por la puerta
    - Se apoya en la infraestructura de transporte para entregar los mensajes a la puerta del proceso receptor
    - Dos sockets involucrados, uno en cada extremo.

#### 3 tipos de sockets

- Datagram sockets
    - se montan sobre el protocolo de transporte UDP (no confiable)
- Stream sockets
    - se montan sobre el protocolo de transporte TCP (confiable y orientado a conexión)
- Sockets Raw
    - se montan sobre el protocolo de transporte a nivel usuario (no kernel del SO)

### Puertos y direccionamiento de procesos

Para intercambiar mensajes, es necesario identificar procesos
El host tiene una dirección IP de 32 bits.
No alcanza para identificar los procesos en una red de hosts.

El identificador incluye tanto la dirección IP como el puerto asociado al proceso.

Puerto 443: HTTPS
Puerto 80: HTTP
Puerto 22: SSH
Puerto 25: SMTP
Puerto 53: DNS
Puerto 8080: Telnet

### Servicios requeridos a nivel de transporte

- Integridad
- Delay
- Throughput
- Seguridad

### Servicios de la capa de transporte

#### Servicio TCP

- Transporte confiable
- Control de flujo
- Control de congestion
- Orientado a conexión: etapa de reserva de recursos (handshaking)

#### Servicio UDP

- Transporte no confiable y sin conexión
- No ofrece control de flujo

### Protocolo HTTP

Utiliza TPC

- El cliente abre un socket e inicia una conexión TCP al puerto 80 del server
- El server acepta la conexión
- Se intercambian mensajes HTTP entre el browser y el server
- El cliente cierra la conexión

#### HTTP es stateless

- El servidor no mantiene información de requests anteriores

### Conexiones HTTP

- Conexión persistente: el cliente mantiene la conexión hasta que se cierra
    - Establecimiento de conexión TCP
    - Envío de a lo sumo un objeto
    - Cierre de conexión TCP
- Conexión no persistente: el cliente cierra la conexión
    - Establecimiento de conexión TCP
    - Envío de multiples objetos
    - Cierre de conexión TCP
