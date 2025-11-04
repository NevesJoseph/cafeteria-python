# 📖 Documentação Técnica - Cafeteria Python

> Documentação completa do sistema de gerenciamento de cafeteria

---

## 📑 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Variáveis Globais](#variáveis-globais)
4. [Funções](#funções)
5. [Fluxo de Execução](#fluxo-de-execução)
6. [Tratamento de Erros](#tratamento-de-erros)
7. [Validações](#validações)
8. [Exemplos de Uso](#exemplos-de-uso)

---

## 🎯 Visão Geral

### Objetivo

Sistema interativo para gerenciar pedidos de uma cafeteria, incluindo controle de estoque, cálculo de preços e aplicação de descontos.

### Características

- **Linguagem:** Python 3.8+
- **Paradigma:** Programação procedural
- **Interface:** Terminal/Console
- **Dependências:** Nenhuma (apenas bibliotecas padrão)

---

## 🏗️ Arquitetura

### Estrutura do Programa
```
┌─────────────────────────────────────┐
│         INICIALIZAÇÃO               │
│  - Configuração de variáveis        │
│  - Definição de preços e estoque    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         INPUT DO USUÁRIO            │
│  - Quantos clientes atender?        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         LOOP PRINCIPAL              │
│  ┌─────────────────────────┐        │
│  │ Para cada cliente:      │        │
│  │ 1. Mostrar cardápio     │        │
│  │ 2. Receber escolha      │        │
│  │ 3. Processar pedido     │        │
│  │ 4. Verificar estoque    │        │
│  │ 5. Calcular valores     │        │
│  │ 6. Atualizar estoque    │        │
│  └─────────────────────────┘        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         RESUMO FINAL                │
│  - Total de vendas                  │
│  - Estoque final                    │
│  - Alertas de produtos              │
└─────────────────────────────────────┘
```

---

## 📦 Variáveis Globais

### Preços dos Produtos
```python
cafe_preco = 5.00    # Preço do café em reais
suco_preco = 4.00    # Preço do suco em reais
bolo_preco = 6.00    # Preço do bolo em reais
```

**Tipo:** `float`  
**Uso:** Armazenar os preços fixos dos produtos  
**Modificável:** Sim (alterar no início do código)

---

### Estoque de Produtos
```python
cafe_estoque = 10    # Quantidade de cafés disponíveis
suco_estoque = 8     # Quantidade de sucos disponíveis
bolo_estoque = 5     # Quantidade de bolos disponíveis
```

**Tipo:** `int`  
**Uso:** Controlar quantidade disponível de cada produto  
**Comportamento:** Diminui a cada venda bem-sucedida

---

### Controles de Venda
```python
total_vendas = 0         # Soma de todas as vendas do dia
clientes_atendidos = 0   # Contador de clientes atendidos
```

**Tipo:** `int` / `float`  
**Uso:** Acompanhar métricas de venda  
**Comportamento:** Incrementa durante a execução

---

## 🔧 Funções

### `mostrar_cardapio()`

**Descrição:** Exibe o cardápio atualizado com preços e estoque atual.

**Parâmetros:** Nenhum

**Retorno:** None (apenas imprime na tela)

**Exemplo de Saída:**
```
==================================================
  📋 CARDÁPIO DO DIA
==================================================
1. Café ☕ - R$ 5.00 (Estoque: 10)
2. Suco 🧃 - R$ 4.00 (Estoque: 8)
3. Bolo 🍰 - R$ 6.00 (Estoque: 5)
==================================================
```

**Código:**
```python
def mostrar_cardapio():
    """Função para mostrar o cardápio atualizado"""
    print("\n" + "=" * 50)
    print("  📋 CARDÁPIO DO DIA")
    print("=" * 50)
    print(f"1. Café ☕ - R$ {cafe_preco:.2f} (Estoque: {cafe_estoque})")
    print(f"2. Suco 🧃 - R$ {suco_preco:.2f} (Estoque: {suco_estoque})")
    print(f"3. Bolo 🍰 - R$ {bolo_preco:.2f} (Estoque: {bolo_estoque})")
    print("=" * 50)
```

---

## 🔄 Fluxo de Execução

### 1. Inicialização
```python
# Configura variáveis iniciais
cafe_preco = 5.00
# ... outras variáveis
```

**O que acontece:**
- Define preços dos produtos
- Define estoque inicial
- Inicializa contadores em zero

---

### 2. Input de Clientes
```python
while True:
    try:
        clientes_na_fila = int(input("👥 Quantos clientes? "))
        if 1 <= clientes_na_fila <= 10:
            break
```

**Validações:**
- ✅ Aceita apenas números
- ✅ Deve estar entre 1 e 10
- ✅ Loop até entrada válida

**Possíveis entradas:**
- ✅ `3` → Aceito
- ✅ `10` → Aceito
- ❌ `abc` → Erro tratado
- ❌ `15` → Fora do intervalo

---

### 3. Loop Principal
```python
while clientes_na_fila > 0:
    clientes_atendidos += 1
    mostrar_cardapio()
    # ... processar pedido
    clientes_na_fila -= 1
```

**Comportamento:**
- Executa enquanto houver clientes
- Incrementa contador de atendidos
- Decrementa fila após cada atendimento

---

### 4. Processamento de Pedido

#### 4.1 Receber Escolha
```python
opcao = int(input("\n🛒 Digite a opção (1-3): "))
```

**Validação:**
- Aceita apenas 1, 2 ou 3
- Loop até entrada válida

#### 4.2 Mapear Produto
```python
if opcao == 1:
    item = "Café ☕"
    preco = cafe_preco
    estoque_atual = cafe_estoque
    tipo = "cafe"
elif opcao == 2:
    # ... suco
elif opcao == 3:
    # ... bolo
```

**Saída:** Define item, preço, estoque e tipo

#### 4.3 Verificar Estoque
```python
if estoque_atual > 0:
    # Processar venda
else:
    # Informar falta
```

**Lógica:**
- `estoque > 0` → Venda permitida
- `estoque == 0` → Venda negada

#### 4.4 Calcular Desconto
```python
if clientes_atendidos >= 3:
    desconto = preco * 0.10
    preco_final = preco - desconto
else:
    preco_final = preco
```

**Regra de Negócio:**
- 3º cliente ou mais → 10% de desconto
- 1º e 2º cliente → Preço normal

---

### 5. Atualizar Estoque
```python
if tipo == "cafe":
    cafe_estoque = cafe_estoque - 1
elif tipo == "suco":
    suco_estoque = suco_estoque - 1
elif tipo == "bolo":
    bolo_estoque = bolo_estoque - 1
```

**Comportamento:**
- Diminui em 1 unidade o estoque do produto vendido
- Não afeta outros produtos

---

### 6. Resumo Final
```python
print(f"✅ Clientes atendidos: {clientes_atendidos}")
print(f"💰 Total vendido: R$ {total_vendas:.2f}")

if clientes_atendidos > 0:
    media = total_vendas / clientes_atendidos
    print(f"📈 Média: R$ {media:.2f}")
```

**Informações Exibidas:**
- Total de clientes atendidos
- Valor total vendido
- Média por cliente
- Estoque final de cada produto
- Alertas de produtos esgotados

---

## 🛡️ Tratamento de Erros

### Erro 1: Entrada Não Numérica
```python
try:
    opcao = int(input("Digite: "))
except:
    print("⚠️  Digite apenas números!")
```

**Cenário:** Usuário digita letras  
**Comportamento:** Mostra erro e pede novamente

---

### Erro 2: Número Fora do Intervalo
```python
if 1 <= clientes_na_fila <= 10:
    break
else:
    print("⚠️  Digite entre 1 e 10!")
```

**Cenário:** Usuário digita 0 ou 15  
**Comportamento:** Rejeita e pede novamente

---

### Erro 3: Opção Inválida
```python
if opcao in [1, 2, 3]:
    break
else:
    print("⚠️  Opção inválida!")
```

**Cenário:** Usuário digita 4 ou 0  
**Comportamento:** Rejeita e pede novamente

---

## ✅ Validações

### Tabela de Validações

| Input | Validação | Comportamento |
|-------|-----------|---------------|
| Quantidade de clientes | 1 ≤ x ≤ 10 | Loop até válido |
| Opção do menu | x ∈ {1, 2, 3} | Loop até válido |
| Tipo de dado | Deve ser int | Try/except |
| Estoque | x > 0 | Bloqueia venda se zero |

---

## 💡 Exemplos de Uso

### Exemplo 1: Fluxo Completo

**Input:**
```
Quantos clientes? 2
Opção: 1
Opção: 3
```

**Output:**
```
✅ Clientes atendidos: 2
💰 Total vendido: R$ 11.00
📈 Média: R$ 5.50

Café ☕: 9
Suco 🧃: 8
Bolo 🍰: 4
```

---

### Exemplo 2: Com Desconto

**Input:**
```
Quantos clientes? 3
Opção: 1 (R$ 5.00)
Opção: 1 (R$ 5.00)
Opção: 1 (R$ 4.50 com desconto)
```

**Output:**
```
💰 Total vendido: R$ 14.50
```

---

### Exemplo 3: Produto Esgotado

**Cenário:** `cafe_estoque = 0`

**Output:**
```
❌ PRODUTO EM FALTA!
😢 Desculpe, Café ☕ está sem estoque
```

---

## 🔍 Algoritmos

### Cálculo de Desconto
```
ENTRADA: preco, clientes_atendidos
SAÍDA: preco_final

SE clientes_atendidos >= 3 ENTÃO
    desconto ← preco × 0.10
    preco_final ← preco - desconto
SENÃO
    preco_final ← preco
FIM SE

RETORNAR preco_final
```

---

### Verificação de Estoque
```
ENTRADA: estoque_atual
SAÍDA: venda_permitida (booleano)

SE estoque_atual > 0 ENTÃO
    venda_permitida ← VERDADEIRO
    estoque_atual ← estoque_atual - 1
SENÃO
    venda_permitida ← FALSO
    EXIBIR "Sem estoque"
FIM SE

RETORNAR venda_permitida
```

---

## 📊 Complexidade

### Temporal

- **Melhor caso:** O(n) - onde n = número de clientes
- **Pior caso:** O(n) - mesma complexidade
- **Média:** O(n)

### Espacial

- **Espaço:** O(1) - constante (não depende do input)

---

## 🐛 Debugging

### Pontos de Breakpoint Sugeridos

1. **Linha do input de clientes** - Verificar entrada
2. **Dentro do loop while** - Acompanhar iterações
3. **Após cálculo de desconto** - Validar valores
4. **Atualização de estoque** - Verificar decremento

### Variáveis para Observar
```python
print(f"DEBUG: clientes_atendidos = {clientes_atendidos}")
print(f"DEBUG: total_vendas = {total_vendas}")
print(f"DEBUG: cafe_estoque = {cafe_estoque}")
```

---

## 📈 Melhorias Futuras

### Performance

- [ ] Usar dicionário para produtos (mais escalável)
- [ ] Implementar cache de cálculos

### Funcionalidades

- [ ] Adicionar logger de transações
- [ ] Implementar banco de dados
- [ ] Criar API REST

### Usabilidade

- [ ] Interface gráfica (GUI)
- [ ] Cores no terminal
- [ ] Menu de navegação

---

## 📚 Referências

- [Python Official Docs](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Clean Code Principles](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

---

**Documentação mantida por:** Caffè con Python  
**Última atualização:** 2024  
**Versão:** 1.0.0