import math

def calc_bmi (patient_info: list) : 
    print(patient_info[1])
    patient_bmi = patient_info[2] / math.pow(patient_info[1], 2) 
    print(f"Seu IMC é {patient_bmi:.2f}")

def calc_bmr (patient_info: list) :
    height_in_cm = patient_info[1] * 100
    match patient_info[4] :
        case "M" | "m" | "Masculino":
            bmr = 66 + (13.7 * patient_info[2]) + (5 * height_in_cm) - (6.8 * patient_info[3]) 
            print(f"Sua Taxa Metabólica Basal é {bmr} calorias.") 
        case "F" | "f" | "Feminino" :
            bmr = 665 + (9.6 * patient_info[2]) + (1.8 * height_in_cm) - (4.7 * patient_info[3])
            print(f"Sua Taxa Metabólica Basal é {bmr} calorias.")
        case _:
            print("Você não digitou corretamente seu gênero.\nNão podemos calcular o bmr.")