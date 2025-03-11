import math

# 1. Tính tổng n số nguyên đầu tiên
# Ví dụ: sum_n(10) sẽ tính 1 + 2 + ... + 10
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

# 2. Tính n! (giai thừa của n)
# Ví dụ: factorial(5) = 5*4*3*2*1 = 120
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
# Phương pháp: sinh dãy Fibonacci theo đệ quy cho đến khi số hiện tại >= n
def is_fibonacci(n, a=0, b=1):
    if a == n:
        return True
    if a > n:
        return False
    return is_fibonacci(n, b, a + b)

# 4. Tìm số Fibonacci thứ n
# Định nghĩa: fibo(0)=0, fibo(1)=1, và fibo(n)=fibo(n-1)+fibo(n-2) với n>=2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 5. Tính tổng n số Fibonacci đầu tiên
# Giả sử "n số Fibonacci đầu tiên" là: fibo(0) + fibo(1) + ... + fibo(n-1)
def sum_fibonacci(n):
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + sum_fibonacci(n - 1)

# 6. Tính tổng căn bậc 2 của n số nguyên đầu tiên
# Ví dụ: sum_sqrt(5) = sqrt(1) + sqrt(2) + sqrt(3) + sqrt(4) + sqrt(5)
def sum_sqrt(n):
    if n == 0:
        return 0
    else:
        return math.sqrt(n) + sum_sqrt(n - 1)


# --- Kiểm tra các hàm đã viết ---

# 1. Tổng n số nguyên đầu tiên
n1 = 10
print("Tổng của", n1, "số nguyên đầu tiên là:", sum_n(n1))
# Kết quả: 1+2+...+10 = 55

# 2. Giai thừa của n
n2 = 5
print(n2, "! =", factorial(n2))
# Kết quả: 5! = 120

# 3. Kiểm tra số có phải số Fibonacci không
number = 21
print("Số", number, "là số Fibonacci không?", is_fibonacci(number))
# Kết quả: True, vì 21 có trong dãy Fibonacci

# 4. Tìm số Fibonacci thứ n
n4 = 10
print("Số Fibonacci thứ", n4, "là:", fibonacci(n4))
# Với định nghĩa: fibo(0)=0, fibo(1)=1, fibo(2)=1, ... => Số Fibonacci thứ 10 (index 10) thường là 55

# 5. Tổng n số Fibonacci đầu tiên
n5 = 10
print("Tổng", n5, "số Fibonacci đầu tiên là:", sum_fibonacci(n5))
# Ví dụ: fibo(0)=0, fibo(1)=1, fibo(2)=1, fibo(3)=2, fibo(4)=3, fibo(5)=5, fibo(6)=8, fibo(7)=13, fibo(8)=21, fibo(9)=34 => Tổng = 0+1+1+2+3+5+8+13+21+34

# 6. Tổng căn bậc 2 của n số nguyên đầu tiên
n6 = 10
print("Tổng căn bậc 2 của", n6, "số nguyên đầu tiên là:", sum_sqrt(n6))
# Kết quả là: sqrt(1)+sqrt(2)+...+sqrt(10)
