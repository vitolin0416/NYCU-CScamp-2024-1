def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
result = []
for i in range(10):
    result.append(fibonacci(i))  # 把前十項費氏數列放進列表
print(result)