

### дано 3-х число найти сумму

# number = int(input())
#
# third = number % 10
# second = (number // 10) % 10
# first = (number //100) % 10
# print(third+second+first)

# totalSeconds = int(input())
# hours = (totalSeconds // 3600) % 24 #сколькло часов
# minutes = (totalSeconds % 3600) // 60 #сколько минут
# second = (totalSeconds % 60)
# time = str(hours) + ":" + str(minutes //10) + str(minutes % 10) + ":" + str(second //10) + str(second % 10)
# print(time)


# n = int(input())
# print(n + 2 - n % 2)
'''
a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and c + a > b:
    if a == b or b == c or a == c:
        print("равнобедренный")
    elif a == b and b == c and c == a:
        print("равностороний")
    else:
        print("paзностор")
else:
    print("нельзя из этих отрезков построить треугольник")
'''



'''
import math
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D)) /(2*a)
    #print("{:.3} {:.3}".format(x1, x2))
    print('%.3f' % x1, '%.3f' % x2)

elif D == 0:
     x1 = (-b+math.sqrt(D))/(2*a)
     print(x1)
else:
    print("NO SOLUTION")
'''



x0 = 5
y0 = 4
r = 5
x = float(input())
y = float(input())

if ((x - x0)**2) + ((y - y0)**2)<=r**2:
    print('YES')
else:
    print('NO')








# import math
# x =float(input())
# y = 0
# res = True
#
# if x < -0.5
#         y = 1 + math.sqrt(math.cos(x))
# elif x >= -0.5 and x <=1
#     y = x + 1
# else:
#     y = 1 - x**2
# print("(:.6)".format(y))


