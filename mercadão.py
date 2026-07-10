import time

mensagens1 = [
    "Olá, bem-vindo ao mercado dos mercados, o mercado mais mercado que os outros mercados :)",
    "Os nossos preços são fantásticos! Fazer o que né? É o mercado dos mercados kkkk.",
    "Estamos com promoção na maçã: a partir de 5 maçãs, você leva 30% de desconto.",
    "Fique à vontade para olhar nossos produtos."
]

for i in mensagens1:
    print(i)
    time.sleep(2.5)

mensagens2 = [
    "Procurando algo pra comprar...",
    "MEU DEUS! O CÉSIO 137 subiu de preço, como vou alimentar meus filhos? :( ...",
    "Ah é! Tá faltando fruta lá em casa."
]

for i in mensagens2:
    print(i)
    time.sleep(1.5)

macapreco = 5
perapreco = 3.50
uvapreco = 0.50
melanciapreco = 18
kitkatpreco = 5.50

quantidademacas = int(input(f"Cada maçã está R${macapreco}, quantas vai levar? "))
quantidadeperas = int(input(f"Cada pera está R${perapreco}, quantas vai levar? "))
quantidadeuvas = int(input(f"Cada uva está R${uvapreco}, quantas vai levar? "))
quantidademelancia = int(input(f"Cada melancia está R${melanciapreco}, quantas vai levar? "))
quantidadekitkat = int(input(f"Cada KitKat está R${kitkatpreco}, quantos vai levar? "))

totalmaca = macapreco * quantidademacas
if quantidademacas >= 5:
    totalmaca *= 0.7
    print(f"Parabéns! Você ganhou desconto! Valor total das maçãs com desconto: R${totalmaca:.2f}")

totalpera = perapreco * quantidadeperas
totaluvas = uvapreco * quantidadeuvas
totalmelancia = melanciapreco * quantidademelancia
totalkitkat = kitkatpreco * quantidadekitkat

cesta = totalmaca + totalpera + totaluvas + totalmelancia + totalkitkat

if cesta == 0:
    print("Você não vai sair daqui sem comprar nada! Vai levar um KitKat.")
    cesta += kitkatpreco

print(f"Total da compra: R${cesta:.2f}")

saldo = float(input("Quanto tenho de saldo? R$"))

senha = 2222
aproxouins = input("Inserir/aproximar? (não escreva com letra maiúscula): ")
dialogosenha = int(input("Insira a senha numérica de 4 dígitos: "))

if aproxouins == "inserir":
    if dialogosenha == senha:
        print("Senha correta, prosseguindo com a transação.")
    else:
        print("Você errou a senha, lamento, mas encerramos por aqui!")
        exit()

if aproxouins == "aproximar":
    print(dialogosenha)
    if dialogosenha == senha:
        print("Senha correta, prosseguindo com a transação.")
    else:
        print("Você errou a senha, lamento mas encerramos por aqui!")
        exit()
        
    mensagensaprox = [
        "Analisando...",
        "Carregando...",
        "Isso pode levar um tempo..."
    ]
    for i in mensagensaprox:
        print(i)
        time.sleep(3)

if saldo >= cesta:
    print("Compra aprovada.")
else:
    print("Saldo insuficiente.")

troco = saldo - cesta
if troco < 0:
    print(f"Você está devendo ao mercado R${abs(troco):.2f}")
elif troco == 0:
    print("Não haverá troco. O valor foi exato!")
else:
    print(f"Seu troco é de R${troco:.2f}")

print("Obrigado e volte sempre!")