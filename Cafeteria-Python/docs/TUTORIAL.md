# 🎓 Tutorial Completo - Cafeteria Python

> Aprenda a usar o sistema passo a passo

---

## 📑 Índice

1. [Instalação](#instalação)
2. [Primeiro Uso](#primeiro-uso)
3. [Guia Passo a Passo](#guia-passo-a-passo)
4. [Cenários Comuns](#cenários-comuns)
5. [Dicas e Truques](#dicas-e-truques)
6. [Solução de Problemas](#solução-de-problemas)

---

## 📥 Instalação

### 1. Baixar Python

Visite [python.org](https://python.org) e baixe Python 3.8+

**Verificar instalação:**
```bash
python --version
```

### 2. Baixar o Projeto

**Opção A: Git**
```bash
git clone https://github.com/seu-usuario/cafeteria-python.git
cd cafeteria-python
```

**Opção B: Download ZIP**
1. Clique em "Code" → "Download ZIP"
2. Extraia o arquivo
3. Abra a pasta `cafeteria-python`

---

## 🚀 Primeiro Uso

### 1. Abrir Terminal

**Windows:**
- Pressione `Win + R`
- Digite `cmd`
- Enter

**Mac/Linux:**
- Pressione `Ctrl + Alt + T`

### 2. Navegar até a pasta
```bash
cd caminho/para/cafeteria-python
cd src
```

### 3. Executar o programa
```bash
python cafeteria_python.py
```

---

## 📖 Guia Passo a Passo

### Passo 1: Tela de Boas-Vindas
```
==================================================
  ☕ BEM-VINDO À CAFETERIA PYTHON! ☕
==================================================

✅ Sistema iniciado com sucesso!
```

**O que acontece:**
- Sistema carrega preços
- Inicializa estoque
- Prepara para atendimento

---

### Passo 2: Definir Quantidade de Clientes
```
🎮 MODO INTERATIVO ATIVADO!
Você vai escolher os pedidos! 🎯

👥 Quantos clientes deseja atender? (1-10): _
```

**O que fazer:**
- Digite um número entre 1 e 10
- Pressione Enter

**Exemplos:**
```
👥 Quantos clientes deseja atender? (1-10): 3   ✅
👥 Quantos clientes deseja atender? (1-10): 15  ❌ (muito alto)
👥 Quantos clientes deseja atender? (1-10): abc ❌ (não é número)
```

---

### Passo 3: Visualizar Cardápio
```
==================================================
  📋 CARDÁPIO DO DIA
==================================================
1. Café ☕ - R$ 5.00 (Estoque: 10)
2. Suco 🧃 - R$ 4.00 (Estoque: 8)
3. Bolo 🍰 - R$ 6.00 (Estoque: 5)
==================================================
```

**Informações exibidas:**
- Número da opção (1, 2 ou 3)
- Nome do produto
- Preço atual
- Quantidade em estoque

---

### Passo 4: Fazer Pedido
```
🛒 Digite o número da opção desejada (1-3): _
```

**O que fazer:**
- Digite 1, 2 ou 3
- Pressione Enter

**Opções:**
- `1` = Café ☕
- `2` = Suco 🧃
- `3` = Bolo 🍰

---

### Passo 5: Confirmação
```
✅ Cliente escolheu opção: 1
📦 Item selecionado: Café ☕
🔍 Verificando estoque...
✅ Produto disponível! (Estoque: 10)

💰 Valor: R$ 5.00

✅ PEDIDO CONFIRMADO!
   Cliente: #1
   Item: Café ☕
   Total a pagar: R$ 5.00

📊 Total de vendas até agora: R$ 5.00
```

**O que acontece:**
- Sistema verifica estoque
- Calcula preço
- Aplica desconto (se aplicável)
- Confirma pedido
- Atualiza totais

---

### Passo 6: Desconto Especial 🎉

**A partir do 3º cliente:**
```
🎉 DESCONTO ESPECIAL DE 10%!
   Valor original: R$ 6.00
   Desconto: R$ 0.60
   Valor final: R$ 5.40
```

**Quando acontece:**
- 1º cliente: Preço normal
- 2º cliente: Preço normal
- 3º cliente: 10% de desconto
- 4º cliente em diante: 10% de desconto

---

### Passo 7: Próximo Cliente
```
👥 Ainda há 2 cliente(s) na fila
⏳ Próximo cliente...

[Pressione ENTER para continuar]
```

**O que fazer:**
- Pressione Enter
- Sistema mostra cardápio novamente
- Repete processo

---

### Passo 8: Resumo Final
```
==================================================
  📊 RESUMO DO DIA
==================================================

✅ Clientes atendidos: 3
💰 Total vendido: R$ 14.40
📈 Média por cliente: R$ 4.80

📦 ESTOQUE FINAL:
   Café ☕: 8 unidade(s)
   Suco 🧃: 7 unidade(s)
   Bolo 🍰: 4 unidade(s)

⚠️  ALERTAS:
   ✅ Todos os produtos ainda disponíveis!

==================================================
🎉 EXPEDIENTE ENCERRADO COM SUCESSO!
☕ Obrigado por usar a Cafeteria Python!
💪 Feito com Python - Caffè con Python
==================================================
```

**Informações exibidas:**
- Total de clientes
- Total vendido
- Média por cliente
- Estoque final
- Alertas (se houver)

---

## 🎯 Cenários Comuns

### Cenário 1: Produto Sem Estoque
```
❌ PRODUTO EM FALTA!
😢 Desculpe, Café ☕ está sem estoque
💡 Este pedido não será processado
   Escolha outro item na próxima vez!
```

**Quando acontece:**
- Estoque do produto = 0

**O que fazer:**
- Escolher outro produto
- Pedido não é contabilizado

---

### Cenário 2: Opção Inválida
```
🛒 Digite o número da opção desejada (1-3): 5
⚠️  Opção inválida! Por favor, digite 1, 2 ou 3.
```

**Quando acontece:**
- Digitar número fora de 1-3

**O que fazer:**
- Digite novamente um número válido

---

### Cenário 3: Entrada Não Numérica
```
🛒 Digite o número da opção desejada (1-3): abc
⚠️  Digite apenas números!
```

**Quando acontece:**
- Digitar letras ou símbolos

**O que fazer:**
- Digite apenas números

---

## 💡 Dicas e Truques

### 🎮 Testando o Sistema

**Para testar estoque zerado:**
1. Execute o programa
2. Atenda 10 clientes
3. Escolha sempre o mesmo produto
4. Veja o alerta de estoque esgotado

**Para testar desconto:**
1. Atenda pelo menos 3 clientes
2. Observe o desconto aplicado no 3º

**Para testar validação:**
1. Digite letras quando pedir número
2. Digite números fora do intervalo
3. Veja as mensagens de erro

---

### ⚡ Atalhos

**Executar rapidamente:**
```bash
python src/cafeteria_python.py
```

**Ver ajuda do Python:**
```bash
python --help
```

---

### 📝 Personalizações Rápidas

**Mudar preços:** (linha ~20)
```python
cafe_preco = 7.00  # Era 5.00
```

**Mudar estoque:** (linha ~25)
```python
cafe_estoque = 20  # Era 10
```

**Mudar desconto:** (linha ~140)
```python
desconto = preco * 0.20  # 20% ao invés de 10%
```

---

## 🐛 Solução de Problemas

### Problema 1: "Python não é reconhecido"

**Erro:**
```
'python' não é reconhecido como comando interno
```

**Solução:**
1. Reinstale Python
2. Marque "Add Python to PATH"
3. Reinicie o terminal

---

### Problema 2: Arquivo não encontrado

**Erro:**
```
FileNotFoundError: cafeteria_python.py
```

**Solução:**
```bash
# Verifique se está na pasta correta
cd src
ls  # ou dir no Windows

# Deve listar: cafeteria_python.py
```

---

### Problema 3: Programa trava

**Sintomas:**
- Não responde
- Não aceita input

**Solução:**
- Pressione `Ctrl + C` para parar
- Execute novamente

---

### Problema 4: Caracteres estranhos

**Sintomas:**
- Emojis aparecem como `?` ou quadrados

**Solução:**
- Use terminal que suporta UTF-8
- Windows: Use Windows Terminal
- Configure encoding: `chcp 65001`

---

## 🎓 Próximos Passos

Agora que você domina o básico:

1. **Modifique o código**
   - Adicione mais produtos
   - Mude os preços
   - Ajuste o desconto

2. **Crie variações**
   - Sistema de restaurante
   - Loja de roupas
   - Biblioteca

3. **Aprenda mais**
   - Estude funções
   - Aprenda sobre listas
   - Explore orientação a objetos

---

## 📚 Recursos Adicionais

- [Documentação Completa](DOCUMENTATION.md)
- [Como Contribuir](../CONTRIBUTING.md)
- [FAQ](FAQ.md)
- [Instagram @caffeconpython](https://instagram.com/caffeconpython)

---

## ❓ Ainda com Dúvidas?

- Abra uma [Issue](https://github.com/seu-usuario/cafeteria-python/issues)
- Mande DM no Instagram
- Consulte o [FAQ](FAQ.md)

---

**Tutorial criado por:** Caffè con Python  
**Última atualização:** 2024  
**Nível:** Iniciante

**Bom aprendizado! ☕🐍**