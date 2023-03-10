def del3(ch: int):
    if ch%3==0:
        return True
    else:
        return False

def del100(ch):
    it=None
    try:
        it=100/ch
    except ValueError:
        print("Введите число")
    except ZeroDivisionError:
        print("Делить на 0 нельзя")
    except Exception as o:
        print("Ошибка:", o)
    return it
def md(d: str):
    d=d.split(".")
    #print(d)
    try:
        if int(d[0])*int(d[1])==int(d[2][2:]):
            return True
        else:
            return False
    except:
        print("Дата должна быть в формате дд.мм.гггг")
def tic(n: str):
    if len(n)%2!=0:
        return "Количество цифр должно быть чётным"
    else:
        s1=0
        s2=0
        for i in range (len(n)//2):
            s1+=int(n[i])
            s2+=int(n[len(n)-1-i])
        if s1==s2:
            return True
        else:
            return False
k=9
print("Проверка числа", k, "на делимость на 3")
print((del3(k)))
k=56
print("Проверка числа", k, "на делимость на 3")
print((del3(k)))

print("\n")
k=4
print("Проверка делимости 100 на число", k)
print((del100(k)))
k=56
print("Проверка делимости 100 на число", k)
print((del100(k)))

print("\n")
k="23.11.2004"
print("Проверка даты",k ,"на магическое значение")
print(md(k))
k="23.00.2000"
print("Проверка даты",k ,"на магическое значение")
print(md(k))

print("\n")
k="190380917"
print("Проверка счастливого номера билета", k)
print(tic(k))
k="190820"
print("Проверка счастливого номера билета", k)
print(tic(k))