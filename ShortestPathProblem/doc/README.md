Universidade Federal da Paraíba

Centro de Informática

Programa de Pós-graduação em Informática

Thiago Ney Evaristo Rodrigues

# Problema do Caminho Mais Curto no Sistema de Metrô de Paris

## Descrição

Imagine que você está navegando pelo Metrô de Paris, uma das redes de metrô mais complexas e densas do mundo. Seu objetivo é viajar de uma estação de origem até uma estação de destino utilizando o menor tempo de viagem possível - não necessariamente o menor número de paradas.

## Definição do Problema

Dado:

- Um grafo representando a rede de metrô, onde:
    - Os nós são as estações de metrô.
    - As arestas representam conexões diretas de trem entre as estações.
    - Cada aresta possui:
        - O tempo de viagem entre as estações conectadas.
        - Um identificador da linha do metrô (ex.: Linha Azul, Linha Amarela, etc.).

Você precisa:

Encontrar a rota mais rápida (ou seja, com o menor tempo total) de uma estação inicial S (E1) até uma estação objetivo G (E12).

## Restrições e Considerações

- Trocas de linha (por exemplo, da Linha Azul para a Linha Amarela) acarretam uma penalidade de tempo, modelada como um custo adicional de baldeação de 4 minutos.
- Heurística: Usar a distância em linha reta (Euclidiana) entre as estações (utilizando suas coordenadas geográficas) como uma estimativa do tempo restante até o destino.
- Estratégia gananciosa: Sempre escolher a próxima estação que parecer mais próxima do destino com base na heurística, mesmo que isso não leve à solução globalmente ótima.

## Algoritmo Guloso

A cada passo:

1. A partir da estação atual, observe todas as estações vizinhas acessíveis.
2. Para cada vizinha:
    - Some o tempo de viagem.
    - Se houver troca de linha (baldeação), adicione a penalidade de transferência.
    - Estime o tempo restante até o destino usando a distância em linha reta.
3. Escolha a vizinha com o menor tempo restante estimado e avance.

## Solução

────────────────────────────────────────────────────────────

Estação Atual: E01

────────────────────────────────────────────────────────────

Estações Possíveis: [E02]

Verificando estação: E02
  - Distância E01 → E02: 11
  - Distância E02 → E12: 23
  - Linha atual: —
  - Próxima linha: Azul
  - Tempo estimado: 68.0 min

→ Melhor estação: E02
→ Melhor tempo: 68.0 min

Rota parcial: [E01, E02]  
Tempo total: 68.0 min

────────────────────────────────────────────────────────────

Estação Atual: E02

────────────────────────────────────────────────────────────

Estações Possíveis: [E01, E03, E09, E10]

Verificando estação: E01
  - Tempo: ∞ (descartada)

Verificando estação: E03
  - Distância E02 → E03: 9
  - Distância E03 → E12: 21
  - Linha atual: Azul
  - Próxima linha: Azul
  - Tempo estimado: 60.0 min

→ Melhor estação: E03  
→ Melhor tempo: 60.0 min

Verificando estação: E09
  - Distância E02 → E09: 11
  - Distância E09 → E12: 12
  - Linha atual: Azul
  - Próxima linha: Amarela
  - Tempo estimado: 50.0 min

→ Melhor estação: E09  
→ Melhor tempo: 50.0 min

Verificando estação: E10
  - Melhor estação permanece: E09  
  - Melhor tempo permanece: 50.0 min

Rota parcial: [E01, E02, E09]  
Tempo total: 118.0 min

────────────────────────────────────────────────────────────

Estação Atual: E09

────────────────────────────────────────────────────────────

Estações Possíveis: [E02, E03, E08, E11]

Verificando estação: E02
  - Distância E09 → E02: 11
  - Distância E02 → E12: 23
  - Linha atual: Amarela
  - Próxima linha: Amarela
  - Tempo estimado: 68.0 min

Verificando estação: E03
  - Distância E09 → E03: 10
  - Distância E03 → E12: 21
  - Linha atual: Amarela
  - Próxima linha: Vermelha
  - Tempo estimado: 66.0 min

Verificando estação: E08
  - Distância E09 → E08: 9
  - Distância E08 → E12: 7
  - Linha atual: Amarela
  - Próxima linha: Amarela
  - Tempo estimado: 32.0 min

→ Melhor estação: E08  
→ Melhor tempo: 32.0 min

Verificando estação: E11
  - Melhor estação permanece: E08  
  - Melhor tempo permanece: 32.0 min

Rota parcial: [E01, E02, E09, E08]  
Tempo total: 150.0 min

────────────────────────────────────────────────────────────

Estação Atual: E08

────────────────────────────────────────────────────────────

Estações Possíveis: [E04, E05, E09, E12]

Verificando estação: E04
  - Distância E08 → E04: 13
  - Distância E04 → E12: 21
  - Linha atual: Amarela
  - Próxima linha: Verde
  - Tempo estimado: 72.0 min

→ Melhor estação: E04  
→ Melhor tempo: 72.0 min

Verificando estação: E05
  - Distância E08 → E05: 21
  - Distância E05 → E12: 27
  - Linha atual: Amarela
  - Próxima linha: Amarela
  - Tempo estimado: 96.0 min

Verificando estação: E09
  - Distância E08 → E09: 9
  - Distância E09 → E12: 12
  - Linha atual: Amarela
  - Próxima linha: Amarela
  - Tempo estimado: 42.0 min

Verificando estação: E12
  - Distância E08 → E12: 7
  - Distância E12 → E12: 0
  - Linha atual: Amarela
  - Próxima linha: Verde
  - Tempo estimado: 18.0 min

→ Melhor estação: E12  
→ Melhor tempo: 18.0 min

Rota final: [E01, E02, E09, E08, E12]  
Tempo total: 168.0 min

────────────────────────────────────────────────────────────
