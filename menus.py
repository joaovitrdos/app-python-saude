from calcs import calc_bmi, calc_bmr
import os

def welcome () :
    print('Bem-vindo ao Unesc Saúde\n')

def get_info() :
    patient_info = []

    while True :
        try :
            patient_name = str(input("Digite seu nome: ")).strip().upper().capitalize()
            if not patient_name.isalpha():
                print("O nome deve ter conter apenas letras.")
            elif len(patient_name) < 3:
                print("O nome deve ter mais de 3 caracteres.")
            elif patient_name in ['CU', 'FODA', 'FILHA DA PUTA', 'PUTA', 'CARRALHO', 'CARAI', 'PIKA', 'ROLA', 'CUZAO',] : #Tratando nomes não permitindos (Enzo é um exemplo)
                print(f'{patient_name} não são aceitos.')
            elif patient_name :
                patient_info.append(patient_name)
                break
            else :
                print('O campo nome não pode estar em branco.')
        except ValueError :
                print('Digite um nome válido (Ex: Enzo')

    while True :
        try :
            patient_height = float(input("Digite sua altura: "))
            if 0.54 <= patient_height <= 2.51 : #Tratando alturas fora do padrão (Maior e menor seres humanos vivos.).
                patient_info.append(patient_height)
                break
            else :
                print('A altura inserida não é válida.')
        except ValueError:
                    print('Digite uma altura válida. (Ex: 1.75)')

    while True :
        try :
            patient_weight = float(input("Digite seu peso: "))
            if 6.5 <= patient_weight <= 595 : #Tratando pesos fora do padrão.
                patient_info.append(patient_weight)
                break
            else :
                print('O peso inserido não é válida.')
        except ValueError :
                print('Digite um peso válido. (Ex: 80 | 80.7)')

    while True:
        try:
            patient_age = int(input("Digite a idade (em anos completos): "))
            if 2 <= patient_age <= 18: # Tratando idade fora do padrão.
                patient_info.append(patient_age)
                print('Aviso: O cálculo do IMC não é recomendado para crianças e adolescentes.')
                break
            elif patient_age:
                patient_info.append(patient_age)
                break
            else:
                print('Digite a idade válida. (Ex: 30 | 50 | 18)')
        except ValueError:
            print('Digite uma idade válida. (Ex: 50)')

    while True :
        try :
            patient_gender = input("Digite seu gênero biológico (M - Masculino/F - Feminino): ").upper()
            if patient_gender in ['M', 'F'] :
                patient_info.append(patient_gender)
                break
            else:
                print('Você deve digitar o gênero corretamente (M|F)')
        except ValueError :
                print("Digite o gênero biológico correto (M - Masculino/F - Feminino).")

    return patient_info

def want_comeback () :
    while True :
        choice_menu = input('Deseja voltar ao menu anterior? (S/N): ').upper()
        match choice_menu :
            case "S" :
                return True
                break
            case "N" :
                os.system("cls")
                print('Obrigado por utilizar o Unesc Saúde.')
                choice_menu = False
                break
            case _:
                print('Digite uma opção válida.')
                choice_menu = True

def show_menu (patient_info: list) :
    back_menu = True
    while back_menu == True :
        print("""_-_-_-MENU-_-_-_-
        
            [1] - Calcular IMC
            [2] - Calcular Taxa Metabólica Basal
            [3] - Sair
            
            """)

        option = int (input("Digite a opção desejada: "))

        match option :
            case 1 :
                calc_bmi(patient_info)
                back_menu = want_comeback()
            case 2 :
                calc_bmr(patient_info)
                back_menu = want_comeback()
            case 3 :
                os.system("cls")
                print('Obrigado por utilizar o Unesc Saúde.')
                back_menu = False
            case _:
                print('Opção inválida.')
