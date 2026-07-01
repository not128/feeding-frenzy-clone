# Recursion

# Viết hàm đệ quy countdown(n) đếm ngược từ n về 0 và in ra mỗi số.
def countdown(n):
    print(n)
    # Code của bạn ở đây
    if n<=0:
        return 0
    return countdown(n-1)
 
# Test
countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# 0

##########################################################
# Viết hàm đệ quy count_up(n) đếm từ 1 đến n và in ra mỗi số.
def count_up(n):
    # Code của bạn ở đây
    if n == 0:
        return 0    
    count_up(n-1)
    print(n)
 
# Test
count_up(5)
# Output:
# 1
# 2
# 3
# 4
# 5

##########################################################
# Viết hàm đệ quy factorial(n) tính giai thừa của n.
def factorial(n):
    # n! = n * (n-1) * ... * 1
    # 5! = 5 * 4 * 3 * 2 * 1 = 120
    if n==1:
        return 1
    if n==0:
        return 0
    return n*factorial(n-1)
 
# Test
print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(3))  # 6
# *** Base case: n = 0 hoặc n = 1, trả về 1


##########################################################
# Viết hàm đệ quy sum_to_n(n) tính tổng các số từ 1 đến n.
def sum_to_n(n):
    # 1 + 2 + 3 + ... + n
    if n ==1:
        return 1
    return n+sum_to_n(n-1)
 
# Test
print(sum_to_n(5))   # 15 (1+2+3+4+5)
print(sum_to_n(10))  # 55

##########################################################
# Viết hàm đệ quy power(base, exp) tính base mũ exp.
def power(base, exp):
    # base^exp
    # 2^3 = 2 * 2 * 2 = 8
    if exp==1:
        return base
    if exp==0:
        return 1
    if base==0:
        return 0
    return base*power(base, exp-1)
 
# Test
print(power(2, 3))  # 8
print(power(5, 2))  # 25
print(power(3, 0))  # 1


##########################################################
# Viết hàm đệ quy fibonacci(n) tính số Fibonacci thứ n.
def fibonacci(n):
    
    # fib(0) = 0, fib(1) = 1
    # fib(n) = fib(n-1) + fib(n-2)
    return 
 
# Test
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8
print(fibonacci(10)) # 55

##########################################################
# Viết hàm đệ quy sum_digits(n) tính tổng các chữ số của một số nguyên.
def sum_digits(n):

    # 123 -> 1 + 2 + 3 = 6
    if n == 0:
        return 0
    if n < 10:
        return n
    return n%10 + sum_digits(n//10)
 
# Test
print(sum_digits(123))   # 6
print(sum_digits(999))   # 27
print(sum_digits(5))     # 5
# ** Gợi ý: Dùng n % 10 để lấy chữ số cuối, n // 10 để bỏ chữ số cuối


##########################################################
# Viết hàm đệ quy count_digits(n) đếm số lượng chữ số của một số nguyên.
def count_digits(n):
    # 123 -> 3 chữ số
    
    if n<10:
        return 1
    
    return 1+ count_digits(n//10)
 
# Test
print(count_digits(123))    # 3
print(count_digits(99999))  # 5
print(count_digits(5))      # 1

##########################################################
# Viết hàm đệ quy reverse_number(n) đảo ngược một số nguyên.
def reverse_number(n,f=0):
    # 123 -> 321
    f = f*10+n%10
    if n<10:
        return(n)
    return reverse_number(n//10,f)
 
# Test
print(reverse_number(123))   # 321
print(reverse_number(5040))  # 405

##########################################################
# Viết hàm đệ quy sum_list(lst) tính tổng các phần tử trong list.
def sum_list(lst):
    # [1, 2, 3, 4, 5] -> 15
    if len(lst)== 0:
        return 0
    return lst[0] + sum_list(lst[1:])

        
 
# Test
print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([10, 20, 30]))     # 60
print(sum_list([]))               # 0
# *** Base case: list rỗng trả về 0


##########################################################
# Viết hàm đệ quy find_max(lst) tìm số lớn nhất trong list.
def find_max(lst):
    if len(lst)==1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))
    
 
# Test
print(find_max([3, 7, 2, 9, 1]))  # 9
print(find_max([5, 5, 5]))        # 5
print(find_max([100]))            # 100

##########################################################
# Viết hàm đệ quy find_min(lst) tìm số nhỏ nhất trong list.
def find_min(lst):
    if len(lst)==1:
        return lst[0]
    return min(lst[0], find_min(lst[1:]))
 
# Test
print(find_min([3, 7, 2, 9, 1]))  # 1
print(find_min([5, 5, 5]))        # 5
print(find_min([100]))            # 100

##########################################################
# Viết hàm đệ quy reverse_string(s) đảo ngược một chuỗi.
def reverse_string(s, f=len()):
    if len(s)==1:
        return s
    if len(s)==0:
        return s
    return reverse_string(s[1:])+s[0]
 
# Test
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
print(reverse_string("a"))       # "a"

##########################################################
# Viết hàm đệ quy is_palindrome(s) kiểm tra chuỗi có phải palindrome không.
def is_palindrome(s):
    # Palindrome: đọc xuôi ngược như nhau
    if len(s)==0:
        return(True)
    if len(s)==1:
        return(True)
    if s[0] == s[-1]:
        return True
    return  is_palindrome(s[1:-1])
    
 
 
# Test
print(is_palindrome("radar"))    # True
print(is_palindrome("hello"))    # False
print(is_palindrome("level"))    # True
print(is_palindrome("a"))        # True

##########################################################
# Viết hàm đệ quy count_char(s, char) đếm số lần xuất hiện của ký tự trong chuỗi.
def count_char(s, char):
    pass
 
# Test
print(count_char("hello", "l"))      # 2
print(count_char("programming", "m")) # 2
print(count_char("python", "z"))     # 0

##########################################################
# Viết hàm đệ quy multiply(a, b) nhân hai số dương bằng cách cộng lặp đi lặp lại.
def multiply(a, b):
    # 3 * 4 = 3 + 3 + 3 + 3 = 12
    # Sử dụng đệ quy, không dùng toán tử *
    pass
 
# Test
print(multiply(3, 4))   # 12
print(multiply(5, 6))   # 30
print(multiply(7, 0))   # 0

##########################################################
# Viết hàm đệ quy gcd(a, b) tính ước số chung lớn nhất của hai số (Euclidean algorithm).
def gcd(a, b):
    # Greatest Common Divisor
    # gcd(48, 18) = 6
    pass
 
# Test
print(gcd(48, 18))  # 6
print(gcd(100, 50)) # 50
print(gcd(17, 13))  # 1
# *** Gợi ý: gcd(a, b) = gcd(b, a % b), base case: b = 0

##########################################################
# Viết hàm đệ quy list_length(lst) tính độ dài của list (không dùng hàm len()).
def list_length(lst):
    pass
 
# Test
print(list_length([1, 2, 3, 4, 5]))  # 5
print(list_length([]))               # 0
print(list_length(["a", "b"]))       # 2

##########################################################
# Viết hàm đệ quy contains(lst, item) kiểm tra item có trong list không.
def contains(lst, item):
    pass
 
# Test
print(contains([1, 2, 3, 4], 3))    # True
print(contains([1, 2, 3, 4], 5))    # False
print(contains([], 1))              # False


##########################################################
# Viết hàm đệ quy print_list(lst) in từng phần tử của list (mỗi phần tử một dòng).
def print_list(lst):
    pass
 
# Test
print_list([1, 2, 3, 4, 5])
# Output:
# 1
# 2
# 3
# 4
# 5
