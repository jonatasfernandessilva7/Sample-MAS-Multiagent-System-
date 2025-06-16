import asyncio
import random

from collections import deque

trafego_de_rede = deque()

async def agente_monitor():
    while True:
        ip = f"192.168.0.{random.randint(1,10)}"
        tipo_de_pacote = random.choice(["normal", "normal", "suspeito"])
        pacote = {"ip": ip, "tipo": tipo_de_pacote}
        trafego_de_rede.append(pacote)
        print(f"[Monitor] Pacorte capturado: {pacote}")
        await asyncio.sleep(1)

async def agente_detector_de_anomalias(filas_alertas):
    while True:
        if trafego_de_rede:
            pacote = trafego_de_rede.popleft()
            if pacote["tipo"] == "suspeito":
                print(f"[Detectpr] Anomalia detectada no IP: {pacote['ip']}")
                filas_alertas.append(pacote['ip'])
        await asyncio.sleep(1.2)

async def agente_respostas(filas_alertas):
    blacklist = set()
    while True:
        if filas_alertas:
            ip_suspeito = filas_alertas.popleft()
            if ip_suspeito not in blacklist:
                blacklist.add(ip_suspeito)
                print(f"[Resposta]: IP bloqueado: {ip_suspeito}")
        await asyncio.sleep(1)

async def sistema_multiagentes():
    filas_alertas = deque()
    await asyncio.gather(
        agente_monitor(),
        agente_detector_de_anomalias(filas_alertas),
        agente_respostas(filas_alertas)
    )

if __name__ == "__main__":
    try:
        asyncio.run(sistema_multiagentes())
    except KeyboardInterrupt:
        print("\n sistema encerrado")