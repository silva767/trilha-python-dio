

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

  excedeu_saldo = valor > saldo

  excedeu_limite = valor > limite

  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print("Operação falhou! Você não tem saldo suficiente.")

  elif excedeu_limite:
    print("Operação falhou! O valor do saque excede o limite.")

  elif excedeu_saques:
    print("Operação falhou! Número máximo de saques excedido.")

  elif valor > 0:
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1

  else:
    print("Operação falhou! O valor informado é inválido.")

  return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato, /):


  if valor > 0:
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

  else:
    print("Operação falhou! O valor informado é inválido.")


  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("==========================================")
  #return saldo, extrato


def criar_usuario(usuarios):
  cpf = input("Digite seu cpf(somente números): ")

  if cpf in usuarios:
    print("CPF já cadastrado!")
    return
  else:
    nome = input("Digite seu nome completo: ")
    data_nasci = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Digite seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({'nome': nome, 'data_nascimento': data_nasci, 'cpf': cpf, 'endereço': endereco})
    print('Usuário criado com sucesso!')

def criar_conta_corrente(agencia, usuarios, numero_conta):
    usuario = input('Digite seu cpf: ')
    if not any(u['cpf'] == usuario for u in usuarios):
      print('Usuário não encontrado, fluxo de criação de conta encerrado, realize seu cadastro em opção u')
    elif usuario in usuarios:
      print('Conta criada com sucesso!')
      return {'agência': agencia, 'numero_conta': numero_conta, 'usuario':usuario}



def menu():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3
  agencia = '0001'
  usuarios = []
  conta_corrente = []

  menu = """

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [u] Criar usuário
  [c] Criar conta corrente
  [q] Sair

  => """


  while True:
    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))
      saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == 's':
      valor = float(input("Informe o valor do saque: "))
      saldo, extrato, numero_saques = saque(saldo = saldo, valor = valor, limite = limite, extrato = extrato, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == 'e':
      exibir_extrato(saldo, extrato = extrato)

    elif opcao == 'u':
      criar_usuario(usuarios)

    elif opcao == 'c':
      num_conta = len(conta_corrente) + 1
      conta = criar_conta_corrente(agencia, usuarios, num_conta)
      if conta:
        conta_corrente.append(conta)

    elif opcao == 'q':
      break

    else:
      print("Opção inválida, selecione novamente.")

menu()
