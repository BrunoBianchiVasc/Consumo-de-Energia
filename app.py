"""
Calculadora de Consumo Eletrico Inteligente.

Estima o consumo mensal de energia (kWh) e o custo aproximado de um
aparelho a partir da potencia e do tempo medio de uso diario.
"""

# Valor medio do kWh no Brasil; usado como referencia para o custo estimado
VALOR_KWH = 0.75

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho (em W): "))
horas_dia = float(input("Digite o tempo medio de uso diario (em horas): "))

# Mes considerado com 30 dias; divide por 1000 para converter Wh em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * VALOR_KWH

print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mes")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mes")