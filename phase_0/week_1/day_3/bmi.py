x = eval(input('masukan berat Anda '))
y = eval(input('masukan tinggi Anda '))
y = y/100

def BMI(x,y):
    BMI_Formula = (x/y**2)
    if BMI_Formula <= 18.5:
           return(f'Nilai BMI Anda adalah {BMI_Formula} - underweight')
    elif BMI_Formula <= 24.9:
           return(f'Nilai BMI Anda adalah {BMI_Formula} - normal')
    elif BMI_Formula <= 29.9:
           return(f'Nilai BMI Anda adalah {BMI_Formula} - overweight')
    else:
        return(f'Nilai BMI Anda adalah {BMI_Formula} - very overweight')
print(f'Berat Anda adalah {x}')
print(f'Tinggi Anda adalah {y}')
print(BMI(x,y))

