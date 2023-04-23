import sys
from roman import Roman

s = input('Give a Roman Number to check if it is correct!: ').upper()
roman = Roman()
result = roman.correctRoman(s)
if result is not True:
    print(result)
    print('Unfortunately, the given number is incorrect.')
else:
    ans = input('Your Roman number is written correct! Do you want to convert your number - Y/N?: ').upper()
    if ans=='Y':
        choice = input('Choose how you want to convert the number: \n'
                       'Binary - enter B \n'
                       'Integer - enter I \n').upper()
        if choice == 'B':
            print('function not implemented')
        if choice == 'I':
            roman_int = roman.romanToInt(s)
            print(roman_int)
        else:
            print('You have given the wrong letter.')
    elif ans=='N':
        print("Ok!")
        sys.exit(0)
    else:
        print('You have given the wrong letter.')

