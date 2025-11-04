# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o projeto Cafeteria Python! ☕

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Guia de Estilo](#guia-de-estilo)
- [Commit Guidelines](#commit-guidelines)

---

## 📜 Código de Conduta

Este projeto segue um Código de Conduta. Ao participar, você concorda em manter um ambiente respeitoso e acolhedor.

### Nossos Padrões

✅ **Seja respeitoso** com todos os contribuidores  
✅ **Aceite críticas construtivas**  
✅ **Foque no que é melhor para a comunidade**  
❌ **Não use linguagem ofensiva**  
❌ **Não faça ataques pessoais**  

---

## 💡 Como Posso Contribuir?

### 🐛 Reportando Bugs

Antes de criar um issue:
1. Verifique se o bug já não foi reportado
2. Use um título claro e descritivo
3. Descreva os passos para reproduzir
4. Inclua screenshots se possível

**Template de Bug:**
```markdown
**Descrição do Bug**
Descrição clara do problema

**Como Reproduzir**
1. Vá para '...'
2. Clique em '....'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer

**Screenshots**
Se aplicável

**Ambiente:**
 - OS: [Windows/Mac/Linux]
 - Python: [versão]
```

---

### ✨ Sugerindo Melhorias

**Template de Feature:**
```markdown
**Funcionalidade Sugerida**
Descrição clara da feature

**Por que é útil?**
Justificativa da necessidade

**Exemplo de Uso**
Como seria usado na prática
```

---

### 🔧 Pull Requests

1. **Fork** o repositório
2. Crie uma **branch** (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

---

## 🔄 Processo de Desenvolvimento

### Setup Local
```bash
# Clone seu fork
git clone https://github.com/SEU-USUARIO/cafeteria-python.git

# Entre na pasta
cd cafeteria-python

# Crie uma branch
git checkout -b minha-feature
```

### Testando Localmente
```bash
# Execute o programa
python src/cafeteria_python.py

# Teste diferentes cenários
# - Entradas válidas
# - Entradas inválidas
# - Estoque zerado
```

---

## 📝 Guia de Estilo

### Python

Seguimos **PEP 8**:

✅ **Bom:**
```python
def calcular_total(preco, quantidade):
    """Calcula o total da compra."""
    return preco * quantidade
```

❌ **Ruim:**
```python
def calc(p,q):
    return p*q
```

### Nomenclatura

- **Variáveis:** `snake_case`
- **Funções:** `snake_case`
- **Constantes:** `UPPER_CASE`
- **Classes:** `PascalCase`

### Comentários
```python
# Bom: Explica o POR QUÊ
# Aplicar desconto apenas para clientes VIP
if cliente.vip:
    desconto = 0.10

# Ruim: Explica o ÓBVIO
# Incrementa i
i += 1
```

---

## 📌 Commit Guidelines

### Formato
```
tipo(escopo): mensagem curta

Descrição detalhada (opcional)
```

### Tipos

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas diversas

### Exemplos
```bash
feat(cardapio): adiciona opção de pão de queijo

fix(estoque): corrige bug ao atualizar estoque de suco

docs(readme): atualiza instruções de instalação
```

---

## ✅ Checklist de PR

Antes de submeter:

- [ ] Código segue PEP 8
- [ ] Testei localmente
- [ ] Adicionei comentários onde necessário
- [ ] Atualizei documentação (se aplicável)
- [ ] Commit messages são claros

---

## 🎯 Áreas para Contribuir

### 🟢 Bom para Iniciantes

- Adicionar mais itens ao cardápio
- Melhorar mensagens de erro
- Adicionar emojis
- Corrigir typos na documentação

### 🟡 Nível Intermediário

- Sistema de múltiplas unidades
- Validações adicionais
- Testes automatizados
- Refatoração de código

### 🔴 Avançado

- Interface gráfica
- Banco de dados
- API REST
- Sistema de autenticação

---

## 📞 Precisa de Ajuda?

- Abra uma issue com a tag `question`
- Entre no nosso [Discord](#) (em breve)
- Mande DM no [@caffeconpython](https://instagram.com/caffeconpython)

---

## 🙏 Reconhecimento

Todos os contribuidores serão adicionados ao arquivo `CONTRIBUTORS.md`!

---

**Obrigado por contribuir! ☕🐍**
