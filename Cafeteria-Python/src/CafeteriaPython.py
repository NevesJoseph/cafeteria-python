# ==========================================
# SISTEMA COMPLETO - CAFETERIA PYTHON ☕
# Projeto Final - Série Lógica de Programação
# Caffè con Python - VERSÃO INTERATIVA
# ==========================================

print("=" * 50)
print("  ☕ BEM-VINDO À CAFETERIA PYTHON! ☕")
print("=" * 50)

# ============================================
# PARTE 1: CONFIGURAÇÃO (Variáveis)
# ============================================

# Cardápio - Preços
cafe_preco = 5.00
suco_preco = 4.00
bolo_preco = 6.00

# Estoque - Quantidade disponível
cafe_estoque = 10
suco_estoque = 8
bolo_estoque = 5

# Controle - Vendas do dia
total_vendas = 0
clientes_atendidos = 0

print("\n✅ Sistema iniciado com sucesso!")

# ============================================
# PARTE 2: FUNÇÃO CARDÁPIO (Operações)
# ============================================

def mostrar_cardapio():
    """Função para mostrar o cardápio atualizado"""
    print("\n" + "=" * 50)
    print("  📋 CARDÁPIO DO DIA")
    print("=" * 50)
    print(f"1. Café ☕ - R$ {cafe_preco:.2f} (Estoque: {cafe_estoque})")
    print(f"2. Suco 🧃 - R$ {suco_preco:.2f} (Estoque: {suco_estoque})")
    print(f"3. Bolo 🍰 - R$ {bolo_preco:.2f} (Estoque: {bolo_estoque})")
    print("=" * 50)

# ============================================
# PARTE 3: INPUT INTERATIVO (NOVO! 🎮)
# ============================================

print("\n🎮 MODO INTERATIVO ATIVADO!")
print("Você vai escolher os pedidos! 🎯\n")

# Perguntar quantos clientes atender
while True:
    try:
        clientes_na_fila = int(input("👥 Quantos clientes deseja atender? (1-10): "))
        if 1 <= clientes_na_fila <= 10:
            break
        else:
            print("⚠️  Por favor, digite um número entre 1 e 10!")
    except:
        print("⚠️  Digite apenas números!")

print(f"\n✅ Perfeito! Vamos atender {clientes_na_fila} cliente(s)!")
print("🔄 Iniciando atendimento...\n")

# ============================================
# PARTE 4: LOOP DE ATENDIMENTO (While)
# ============================================

while clientes_na_fila > 0:
    clientes_atendidos += 1
    
    print("=" * 50)
    print(f"🔔 ATENDENDO CLIENTE #{clientes_atendidos}")
    print("=" * 50)
    
    # Mostrar cardápio antes de cada pedido
    mostrar_cardapio()
    
    # Loop para garantir opção válida
    while True:
        try:
            opcao = int(input("\n🛒 Digite o número da opção desejada (1-3): "))
            if opcao in [1, 2, 3]:
                break
            else:
                print("⚠️  Opção inválida! Por favor, digite 1, 2 ou 3.")
        except:
            print("⚠️  Digite apenas números!")
    
    print(f"\n✅ Cliente escolheu opção: {opcao}")
    
    # ============================================
    # PARTE 5: PROCESSAR PEDIDO (IF/ELIF)
    # ============================================
    
    if opcao == 1:
        item = "Café ☕"
        preco = cafe_preco
        estoque_atual = cafe_estoque
        tipo = "cafe"
        
    elif opcao == 2:
        item = "Suco 🧃"
        preco = suco_preco
        estoque_atual = suco_estoque
        tipo = "suco"
        
    elif opcao == 3:
        item = "Bolo 🍰"
        preco = bolo_preco
        estoque_atual = bolo_estoque
        tipo = "bolo"
    
    print(f"📦 Item selecionado: {item}")
    
    # ============================================
    # PARTE 6: VERIFICAR ESTOQUE (IF/ELSE)
    # ============================================
    
    print(f"🔍 Verificando estoque...")
    
    if estoque_atual > 0:
        print(f"✅ Produto disponível! (Estoque: {estoque_atual})")
        
        # Aplicar desconto especial para 3º cliente ou mais
        if clientes_atendidos >= 3:
            desconto = preco * 0.10
            preco_final = preco - desconto
            print(f"\n🎉 DESCONTO ESPECIAL DE 10%!")
            print(f"   Valor original: R$ {preco:.2f}")
            print(f"   Desconto: R$ {desconto:.2f}")
            print(f"   Valor final: R$ {preco_final:.2f}")
        else:
            preco_final = preco
            print(f"\n💰 Valor: R$ {preco_final:.2f}")
        
        # Confirmar pedido
        print("\n✅ PEDIDO CONFIRMADO!")
        print(f"   Cliente: #{clientes_atendidos}")
        print(f"   Item: {item}")
        print(f"   Total a pagar: R$ {preco_final:.2f}")
        
        # Atualizar estoque (Operações)
        if tipo == "cafe":
            cafe_estoque = cafe_estoque - 1
        elif tipo == "suco":
            suco_estoque = suco_estoque - 1
        elif tipo == "bolo":
            bolo_estoque = bolo_estoque - 1
        
        # Atualizar vendas totais
        total_vendas = total_vendas + preco_final
        
        print(f"\n📊 Total de vendas até agora: R$ {total_vendas:.2f}")
        
    else:
        print(f"\n❌ PRODUTO EM FALTA!")
        print(f"😢 Desculpe, {item} está sem estoque")
        print("💡 Este pedido não será processado")
        print("   Escolha outro item na próxima vez!")
    
    # Próximo cliente (While)
    clientes_na_fila = clientes_na_fila - 1
    
    if clientes_na_fila > 0:
        print(f"\n👥 Ainda há {clientes_na_fila} cliente(s) na fila")
        print("⏳ Próximo cliente...")
        input("\n[Pressione ENTER para continuar]")
    
    print("\n" + "-" * 50)

# ============================================
# RESUMO FINAL (Operações)
# ============================================

print("\n" + "=" * 50)
print("  📊 RESUMO DO DIA")
print("=" * 50)

print(f"\n✅ Clientes atendidos: {clientes_atendidos}")
print(f"💰 Total vendido: R$ {total_vendas:.2f}")

# Calcular média por cliente (Operações - Post 2)
if clientes_atendidos > 0:
    media = total_vendas / clientes_atendidos
    print(f"📈 Média por cliente: R$ {media:.2f}")

print(f"\n📦 ESTOQUE FINAL:")
print(f"   Café ☕: {cafe_estoque} unidade(s)")
print(f"   Suco 🧃: {suco_estoque} unidade(s)")
print(f"   Bolo 🍰: {bolo_estoque} unidade(s)")

# Verificar produtos em falta
print(f"\n⚠️  ALERTAS:")
produtos_em_falta = False

if cafe_estoque == 0:
    print("   🚨 Café ESGOTADO! Reabastecer urgente!")
    produtos_em_falta = True
if suco_estoque == 0:
    print("   🚨 Suco ESGOTADO! Reabastecer urgente!")
    produtos_em_falta = True
if bolo_estoque == 0:
    print("   🚨 Bolo ESGOTADO! Reabastecer urgente!")
    produtos_em_falta = True

if not produtos_em_falta:
    print("   ✅ Todos os produtos ainda disponíveis!")

print("\n" + "=" * 50)
print("🎉 EXPEDIENTE ENCERRADO COM SUCESSO!")
print("☕ Obrigado por usar a Cafeteria Python!")
print("💪 Feito com Python - Caffè con Python")
print("=" * 50)

print("\n💡 DICA: Execute novamente para fazer mais pedidos!")

# ==========================================
# FIM DO PROJETO FINAL - VERSÃO INTERATIVA
# ==========================================
# 
# 🏆 PARABÉNS POR COMPLETAR A SÉRIE!
# 
# 🎮 NOVIDADE: Agora com INPUT INTERATIVO!
# Você aprendeu:
# ✅ input() - capturar dados do usuário
# ✅ int() - converter texto para número
# ✅ try/except - tratar erros (bônus!)
# ✅ Validação de entrada
# 
# Além de todos os conceitos da série:
# 📦 Variáveis (Post 1)
# 🔢 Operações (Post 2)
# 🔀 IF/ELSE (Post 3)
# 🎯 ELIF (Post 4)
# 🔄 WHILE (Post 5)
#
# 🎓 VOCÊ É OFICIALMENTE UM DESENVOLVEDOR PYTHON!
#
# 🎯 Próximos desafios:
# 1. Adicione mais 3 itens ao cardápio
# 2. Crie sistema de pontos de fidelidade
# 3. Permita comprar múltiplas unidades
# 4. Adicione opção de cancelar pedido
# 5. Crie sistema de troco (pagamento)
# 6. Salve vendas em arquivo texto
# 7. Adicione senha de administrador
# 8. Crie relatório detalhado por produto
#
# 🙏 Obrigado por fazer parte dessa jornada!
# 
# ☕ Caffè con Python - @_caffeconpython
# 
# ==========================================