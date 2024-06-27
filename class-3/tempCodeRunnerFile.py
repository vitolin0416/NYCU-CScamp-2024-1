def fibonacci(n):
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    
result = []
for i in range(1, 11):
    result.append(fibonacci(i))  # 把前十項費氏數列放進列表
print(result)