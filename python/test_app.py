import subprocess
import sys

resultado = subprocess.check_output((sys.executable, "app.py"), text=True)
esperado = "Python funcionando" + chr(10) + "Python configurado" + chr(10)
assert resultado == esperado
print("Teste Python aprovado")
