import subprocess
import sys
import logging

logging.basicConfig(
    filename="servicios.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("Inicio de la monitorización de servicios")

servicios = ["docker.service", "ssh.socket", "cron.service"]

errores = 0

print("====MONITORIZACIÓN DE SERVICIOS")

for servicio in servicios:
    resultado = subprocess.run(
        ["systemctl", "is-active", "--quiet", servicio],check=False,
    )
    

    if resultado.returncode == 0:
        print(f"OK: {servicio} está activo")
        logging.info(f"{servicio} está activo")
    else:
        print(f"ALERTA: {servicio} no está activo")
        logging.warning(f"{servicio} no está activo")
        errores += 1

print(f"Total de alertas: {errores}")
print("Comprobación finalizada")

if errores > 0:
    sys.exit(1)
else:
    sys.exit(0)

