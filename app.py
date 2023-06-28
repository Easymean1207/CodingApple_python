import math

#list
car_info = ['k5','white',5000]

#dictionary -> {key:value,key2:value2, ...}
car_info2 = {
    'brand':'bmw',
    'model':'520d'
}

inventory = 10
car_inventory = ['k5','bmw','morning','spark','starrex','tico']

#item in list
""" if 'k5' in car_inventory :
    print('you can available right now')
else :
    print('k5 is not available') """

""" for item in car_inventory:
    print(item * 3) """

def perimeter(option: int) :
    width = int(input("가로 값 : "))
    length = int(input("세로 값: "))
    return (width + length) * 2 

def width(option: int) :
    width = int(input("가로 값 : "))
    length = int(input("세로 값: "))
    return (width * length) 

def choice(option: int) :
    result = 0

    if option == 1:
        result = perimeter(option)
        return result
    elif option == 2:
        result = width(option)
        return result
    else :
        return -1;

option_val = choice(int(input("옵션을 선택하세요 1-> 둘레 2-> 넓이 : ")))
print(option_val)