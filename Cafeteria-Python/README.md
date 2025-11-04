
## Documentação

[Documentação](https://link-da-documentação)

# ☕ Cafeteria Python - Sistema Completo

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

![License](https://img.shields.io/badge/license-MIT-green.svg)

![Status](https://img.shields.io/badge/status-active-success.svg)

> Sistema completo de gerenciamento de cafeteria desenvolvido como projeto final da série **Lógica de Programação com Python** do [Caffè con Python](https://instagram.com/_caffeconpython).

![Banner](assets/logo.png)

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [Licença](#licença)
- [Contato](#contato)

---

## 🎯 Sobre o Projeto

Este é um **sistema interativo de gerenciamento de cafeteria** desenvolvido para demonstrar os principais conceitos de **lógica de programação** em Python. O projeto foi criado como culminação de uma série educacional de 6 posts sobre programação básica.

### 🎓 Conceitos Aplicados

- 📦 **Variáveis** - Armazenamento de dados
- 🔢 **Operações** - Cálculos matemáticos
- 🔀 **IF/ELSE** - Tomada de decisões
- 🎯 **ELIF** - Múltiplas condições
- 🔄 **WHILE** - Loops e repetições
- 🎮 **INPUT** - Interação com usuário

---

## ✨ Funcionalidades

- ✅ **Cardápio Dinâmico** - Exibição atualizada de produtos e estoque
- ✅ **Modo Interativo** - Usuário escolhe quantos clientes atender
- ✅ **Controle de Estoque** - Verificação automática de disponibilidade
- ✅ **Sistema de Descontos** - 10% de desconto a partir do 3º cliente
- ✅ **Validação de Entrada** - Tratamento de erros do usuário
- ✅ **Relatório Completo** - Resumo de vendas e estoque final
- ✅ **Alertas Inteligentes** - Notificação de produtos esgotados

---

## 🛠️ Tecnologias

- **Python 3.8+**
- Bibliotecas padrão (sem dependências externas)

---

## 📥 Instalação

### Pré-requisitos

- Python 3.8 ou superior instalado
- Editor de código (VS Code recomendado)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/cafeteria-python.git
cd cafeteria-python
```

2. **Navegue até a pasta do código**
```bash
cd src
```

3. **Execute o programa**
```bash
python cafeteria_python.py
```

---

## 🚀 Como Usar

### Execução Básica
```bash
python src/cafeteria_python.py
```

### Fluxo de Uso

1. **Defina quantos clientes atender** (1-10)
2. **Visualize o cardápio** atualizado
3. **Escolha o item** desejado (1-3)
4. **Confirme o pedido** e veja o resumo
5. **Repita** para próximo cliente
6. **Visualize relatório** final

### Exemplo de Interação
```
👥 Quantos clientes deseja atender? (1-10): 3

==================================================
  📋 CARDÁPIO DO DIA
==================================================
1. Café ☕ - R$ 5.00 (Estoque: 10)
2. Suco 🧃 - R$ 4.00 (Estoque: 8)
3. Bolo 🍰 - R$ 6.00 (Estoque: 5)
==================================================

🛒 Digite o número da opção desejada (1-3): 1
```

---

## 📚 Estrutura do Código

### Organização
```
src/cafeteria_python.py
├── Parte 1: Configuração (Variáveis)
├── Parte 2: Função Cardápio (Operações)
├── Parte 3: Input Interativo
├── Parte 4: Loop de Atendimento (While)
├── Parte 5: Processamento de Pedido (IF/ELIF)
├── Parte 6: Verificação de Estoque (IF/ELSE)
└── Resumo Final (Operações)
```

### Principais Funções

#### `mostrar_cardapio()`
Exibe o cardápio atualizado com preços e estoque.

#### Loop Principal
Gerencia o atendimento de múltiplos clientes com validação de entrada.

Para documentação detalhada, consulte [DOCUMENTATION.md](docs/DOCUMENTATION.md).

---

## 🤝 Contribuindo

Contribuições são **muito bem-vindas**! Este é um projeto educacional e adorariamos receber sugestões.

### Como Contribuir

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

### 💡 Ideias de Contribuição

- [ ] Adicionar mais itens ao cardápio
- [ ] Sistema de pontos de fidelidade
- [ ] Permitir múltiplas unidades por pedido
- [ ] Sistema de troco (pagamento)
- [ ] Salvar vendas em arquivo
- [ ] Interface gráfica (Tkinter)
- [ ] Sistema de login/senha
- [ ] Relatórios em PDF

---

## 🗺️ Roadmap

### Versão Atual: 1.0.0

- ✅ Sistema básico funcional
- ✅ Modo interativo
- ✅ Controle de estoque
- ✅ Sistema de descontos

### Próximas Versões

#### v1.1.0
- [ ] Adicionar mais produtos
- [ ] Sistema de categorias

#### v1.2.0
- [ ] Salvamento de dados
- [ ] Histórico de vendas

#### v2.0.0
- [ ] Interface gráfica
- [ ] Multi-usuário

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 📞 Contato

**Caffè con Python**
- Instagram: [@_caffeconpython](https://instagram.com/_caffeconpython)
- Email: caffeconpython@gmail.com

**Link do Projeto:** [https://github.com/seu-usuario/cafeteria-python](https://github.com/seu-usuario/cafeteria-python)

---

## 🙏 Agradecimentos

- Todos que acompanharam a série de Lógica de Programação
- Comunidade Python Brasil
- Você que está lendo isso! ☕

---

## 📊 Status do Projeto
```
[███████████████████ ] 99% - Projeto Quase Completo!
```

**Desenvolvido com ☕ e 🐍 por Caffè con Python**

---

#### ⭐ Se este projeto te ajudou, deixe uma estrela!

