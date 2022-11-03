import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import ARP , sr
## ARP(op="who-has") me sirve para crear un mensaje de broadcast para
## averiguar la dirección MAC de una IP destino.
#ar_pkt = ARP( op="who-has", psrc= "10.9.26.1", pdst="10.9.0.91")
#pdst es la IP destino
#psrc es la IP origen
#op es el tipo de mensaje
#hwdst es la MAC destino
#hwsrc es la MAC origen
#hwdst y hwsrc son opcionales
ar_pkt = ARP(op="who-has", pdst="10.9.0.91")

# Con summary() podemos ver el contenido del paquete
print(ar_pkt.summary())

## sr() nos sirve para enviar dicho mensaje y esperar su resultado
results, _ = sr(ar_pkt, timeout=1, verbose=0, iface='en0') 

# results es una lista de tuplas (paquete, respuesta)
if len(results) > 0:
    print(results[0])
    query, answer = results[0]
    print(answer.summary())
    #mac_dest = answer.hwsrc
