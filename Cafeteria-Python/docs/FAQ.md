
# ❓ Perguntas Frequentes (FAQ)

Respostas para as dúvidas mais comuns sobre o Cafeteria Python.

---

## 📑 Índice

- [Geral](#geral)
- [Instalação](#instalação)
- [Uso](#uso)
- [Erros Comuns](#erros-comuns)
- [Personalização](#personalização)
- [Contribuição](#contribuição)

---

## 🌍 Geral

### O que é este projeto?

Um sistema interativo de gerenciamento de cafeteria desenvolvido em Python para ensinar lógica de programação.

### Para quem é este projeto?

- Iniciantes em programação
- Estudantes de Python
- Pessoas aprendendo lógica
- Qualquer um querendo praticar

### Preciso pagar para usar?

Não! O projeto é **totalmente gratuito** e open-source (licença MIT).

### Posso usar em projetos comerciais?

Sim, a licença MIT permite uso comercial.

---

## 📥 Instalação

### Qual versão do Python preciso?

Python **3.8 ou superior**.

Verificar versão:
```bash
python --version
```

### Precisa instalar bibliotecas extras?

Não! O projeto usa apenas bibliotecas padrão do Python.

### Funciona no Windows/Mac/Linux?

Sim, funciona em **todos os sistemas operacionais** que suportam Python 3.8+.

### Como baixo o projeto?

**Opção 1:** Git
```bash
git clone https://github.com/seu-usuario/cafeteria-python.git
```

**Opção 2:** Download ZIP do GitHub

---

## 🎮 Uso

### Como executo o programa?
```bash
cd cafeteria-python/src
python cafeteria_python.py
```

### Quantos clientes posso atender?

Entre **1 e 10 clientes** por execução.

### Como aplico o desconto?

O desconto de **10%** é aplicado **automaticamente** a partir do 3º cliente.

### Posso atender mais de 10 clientes?

Sim! Execute o programa novamente após terminar.

### O estoque zera permanentemente?

Não. O estoque reseta **toda vez** que você executa o programa novamente.

### Como saio do programa?

- **Durante execução:** `Ctrl + C`
- **Após finalizar:** Programa encerra automaticamente

---

## 🐛 Erros Comuns

### "Python não é reconhecido"

**Causa:** Python não está no PATH do sistema

**Solução:**
1. Reinstale Python
2. Marque "Add Python to PATH"
3. Reinicie terminal/computador

### "FileNotFoundError"

**Causa:** Está na pasta errada

**Solução:**
```bash
cd cafeteria-python/src
python cafeteria_python.py
```

### "Invalid syntax"

**Causa:** Versão do Python muito antiga

**Solução:** Atualize para Python 3.8+

### Emojis aparecem como "?"

**Causa:** Terminal não suporta UTF-8

**Solução Windows:**
```bash
chcp 65001
```

**Solução Mac/Linux:**  
Use terminal moderno (já vem configurado)

### Programa não aceita input

**Causa:** Travamento ou bug

**Solução:**
1. Pressione `Ctrl + C`
2. Execute novamente

---

## 🎨 Personalização

### Como mudar os preços?

Edite as linhas ~20-22:
```python
cafe_preco = 7.00  # Mude aqui
suco_preco = 5.00  # Mude aqui
bolo_preco = 8.00  # Mude aqui
```

### Como mudar o estoque inicial?

Edite as linhas ~25-27:
```python
cafe_estoque = 20  # Mude aqui
suco_estoque = 15  # Mude aqui
bolo_estoque = 10  # Mude aqui
```

### Como adicionar mais produtos?

Requer modificação mais complexa. Veja [DOCUMENTATION.md](DOCUMENTATION.md) seção "Melhorias Futuras".

### Como mudar a porcentagem do desconto?

Linha ~140:
```python
desconto = preco * 0.15  # 15% ao invés de 10%
```

### Como mudar quando o desconto é aplicado?

Linha ~138:
```python
if clientes_atendidos >= 5:  # 5º cliente ao invés de 3º
```

---

## 🤝 Contribuição

### Como posso ajudar?

Veja o guia completo em [CONTRIBUTING.md](../CONTRIBUTING.md)

Formas de contribuir:
- Reportar bugs
- Sugerir funcionalidades
- Melhorar documentação
- Escrever código

### Preciso ser expert em Python?

Não! Temos tarefas para **todos os níveis**:
- 🟢 Iniciante
- 🟡 Intermediário
- 🔴 Avançado

### Como reporto um bug?

1. Vá em [Issues](https://github.com/seu-usuario/cafeteria-python/issues)
2. Clique em "New Issue"
3. Use o template de bug
4. Descreva o problema

### Minhas contribuições serão reconhecidas?

Sim! Todos os contribuidores são adicionados ao arquivo `CONTRIBUTORS.md`.

---

## 📚 Aprendizado

### Este projeto me ensina o quê?

- ✅ Variáveis
- ✅ Operações matemáticas
- ✅ Condicionais (if/elif/else)
- ✅ Loops (while)
- ✅ Input do usuário
- ✅ Funções básicas
- ✅ Validação de dados

### É suficiente para aprender Python?

Este projeto ensina os **fundamentos**. Para se tornar proficiente, continue estudando:
- Listas e dicionários
- Funções avançadas
- Orientação a objetos
- Bibliotecas externas

### Onde posso aprender mais?

- Instagram: [@caffeconpython](https://instagram.com/_caffeconpython)
- Documentação oficial: [python.org](https://python.org)
- Curso gratuito: [Python Brasil](https://python.org.br)

---

## 🔧 Técnicas

### Por que não usa classes?

Para manter **simplicidade** e focar em lógica básica. Classes serão abordadas em projetos futuros.

### Por que não usa banco de dados?

Para evitar dependências externas e manter projeto acessível para iniciantes.

### Por que não tem interface gráfica?

Foco é ensinar lógica, não design de interface. GUI pode ser adicionada como melhoria futura.

---

## 📱 Redes Sociais

### Onde acompanhar o projeto?

- **Instagram:** [@caffeconpython](https://instagram.com/caffeconpython)
- **GitHub:** [cafeteria-python](https://github.com/seu-usuario/cafeteria-python)

### Posso compartilhar meu projeto?

Sim! Use a hashtag **#CafféPython** e marque **@caffeconpython**!

---

## ❓ Não Encontrou Sua Dúvida?

1. Procure nas [Issues](https://github.com/seu-usuario/cafeteria-python/issues)
2. Abra uma nova Issue
3. Mande DM no Instagram
4. Confira a [Documentação](DOCUMENTATION.md)

---

**FAQ mantido por:** Caffè con Python  
**Última atualização:** 2024  
**Contribua:** Envie suas dúvidas para adicionarmos aqui!

**Obrigado por usar Cafeteria Python! ☕🐍**




