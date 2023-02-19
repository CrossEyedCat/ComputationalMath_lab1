import math


def matrix_parser(size):
    main_mas = []
    for i in range(size):
        string = input()
        mas = []
        for j in range(1, size + 1):
            x = "x" + str(j)
            start = string.find(x)
            if start != -1:
                num = 1
                end_plus = string.rfind("+", 0, start)
                end_minus = string.rfind("-", 0, start)
                if end_plus != -1 and end_plus > end_minus:
                    if end_plus + 1 == start:
                        num = 1
                    else:
                        num = float(string[end_plus+1:start])
                elif end_minus != -1 and end_plus < end_minus:
                    if end_minus + 1 == start:
                        num = -1
                    else:
                        num = -float(string[end_minus + 1:start])
                else:
                    num = string[0:start]
                if start==0:
                    num=1
                mas.append(float(num))
            else:
                mas.append(float(0))
        mas.append(float(string[string.find("=") + 1:len(string)]))
        main_mas.append(mas)
    return main_mas

def make_diagonaliti(main_mas):
    for i in range(main_mas.__len__()):
        for j in range(main_mas.__len__()):
            if i!=j and main_mas[i][j] ==max(abs(max(main_mas[i])), abs(min(main_mas[i]))):
                a=main_mas[i]
                main_mas[i]=main_mas[j]
                main_mas[j]=a
    return main_mas





def is_diagonaliti(main_mas):
    for i in range(len(main_mas)):
        main_num = abs(main_mas[i][i])
        sum = 0
        for j in range(len(main_mas)):
            sum =sum + abs(main_mas[i][j])
        if sum > main_num: return False
    return True



def main_log(main_mas, accuracy):
    main_mas = make_diagonaliti(main_mas)
    if not is_diagonaliti(main_mas):
        print("Диагональное преобладание не будет достигнуто.")
    for i in range(main_mas.__len__()):
        num = main_mas[i][i]
        for j in range(main_mas[0].__len__()):
            main_mas[i][j]=main_mas[i][j]/num
    result1 = []
    print("1: ")
    s= main_mas.__len__()
    for i in range(main_mas.__len__()):
        result1.append(main_mas[i][s])
        print(result1[i].__str__()+" ")
    print("\n")
    iterations = 2
    while True:
        result2 = []
        print(iterations.__str__()+": ")
        maxdif = 0
        for i in range(main_mas.__len__()):
            sum=0
            for j in range(main_mas.__len__()):
                if i!=j:
                    sum -=main_mas[i][j]*result1[j]
            sum +=main_mas[i][main_mas.__len__()]
            result2.append(sum)
            dif = abs(result1[i]-result2[i])
            if maxdif<dif:
                maxdif=dif
            print(dif.__str__()+" ")
        print("\n")
        iterations=iterations+1
        result1=result2
        if maxdif<accuracy:
            print("Результаты:")
            ind=1
            for j in result1:
                print("x"+ind.__str__()+": "+round(j, int(math.ceil(math.log(1/accuracy, 10)))).__str__()+"±"+accuracy.__str__())
                ind=ind+1
            break
        elif iterations==500:
            print("Нет сходимости")
            break



if __name__ == '__main__':
    a = int(input('Введите тип ввода данных: 1-консольный, 2-файловый.\n'))
    while a != 1 and a != 2:
        a = int(input('Не правильно, попробуйте снова.\n'))
    accuracy = float(input('Введите погрешность:\n'))
    size = int(input('Введите размерность системы:\n'))
    while size > 20 or size < 0:
        size = int(input('Не правильно, попробуйте снова.\n'))
    print("Введите систему:")
    main_mas = matrix_parser(size)
    main_log(main_mas, accuracy)