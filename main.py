print("=== CONVERSOR DE KB PARA MB ===")

bytes = float(input("Digite a quantidade de bytes: "))
kb = float(input("Digite a quantidade de KB: "))
mb = float(input("Digite a quantidade de MB: "))

resultado_kb = bytes / 1024
resultado_mb = kb / 1024
resultado_gb = mb / 1024

print("\n=== RESULTADOS ===")

print(f"{bytes} Bytes = {resultado_kb:.2f} KB")
print(f"{kb} KB = {resultados_mb:.2f} MB")
print(f"{mb} MB = {resultados_gb:.2f} GB")

