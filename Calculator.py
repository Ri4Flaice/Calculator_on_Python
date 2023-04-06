while True: 
    sign = input("sign (-, +, *, /, **, %): ")
    if sign == '0':
        break
    if sign in ('-', '+', '*', '/', '**', '%'):
        TheFirstNumber = int(input('Введите первую переменную: '))
        TheSecondNumber = int(input('Введите вторую переменную: '))
        if sign == '-':
            minus = TheFirstNumber - TheSecondNumber
            print(f'{TheFirstNumber} - {TheSecondNumber} = {minus}')
        elif sign == '+':
            plus = TheFirstNumber + TheSecondNumber
            print(f'{TheFirstNumber} + {TheSecondNumber} = {plus}')
        elif sign == '*':
            proizvedenie = TheFirstNumber * TheSecondNumber
            print(f'{TheFirstNumber} * {TheSecondNumber} = {proizvedenie}')
        elif sign == '/':
            if TheSecondNumber != 0:
                divide = TheFirstNumber / TheSecondNumber
                print(f'{TheFirstNumber} / {TheSecondNumber} = {divide}')
            else:
                print("division by zero")
        elif sign == '**':
            vozvedenie_v_stepen = TheFirstNumber ** TheSecondNumber
            print(f'{TheFirstNumber} ^ {TheSecondNumber} = {vozvedenie_v_stepen}')
        elif sign == '%':
            divide_po_model = TheFirstNumber % TheSecondNumber
            print(f'{TheFirstNumber} % {TheSecondNumber} = {divide_po_model}')
    else:
        print("invalid operation sign")