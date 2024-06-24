import math

def my_func(a, b, c):
    ans_1 = float( ( -1*b+math.sqrt(b**2-4*a*c) )/(2*a))# 第一個根 
    ans_2 = float( ( -1*b-math.sqrt(b**2-4*a*c) )/(2*a))# 第二個根
    
    # 輸出兩個根
    print("ans_1: " + str(round(ans_1, 2)))
    print("ans_2: " + str(round(ans_2, 2)))

my_func(1, 4, -7)