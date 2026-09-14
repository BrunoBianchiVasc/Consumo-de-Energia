# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-kWh-FFD43B?style=flat&logo=flash&logoColor=white)

Programa em **Python** que estima o consumo mensal de energia (kWh) e o
custo aproximado de um aparelho elétrico, a partir da potência e do tempo
médio de uso diário. 💡

## 🧮 Fórmula

\`\`\`
consumoMensal (kWh) = (potência_W * horas_por_dia * 30) / 1000
custoEstimado (R$)  = consumoMensal * valor_do_kWh
\`\`\`

## ▶️ Como executar

\`\`\`bash
python app.py
\`\`\`

Digite o nome do aparelho 🔌, a potência ⚡ (em watts) e o tempo médio de
uso diário ⏱️ (em horas).

### Exemplo de saída

\`\`\`
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
\`\`\`
