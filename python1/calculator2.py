def add(x, y):
    """두 수의 합을 반환"""
    return x + y

def subtract(x, y):
    """두 수의 차를 반환"""
    return x - y

def multiply(x, y):
    """두 수의 곱을 반환"""
    return x * y

def divide(x, y):
    """두 수의 나눗셈 결과를 반환. 0으로 나누기를 방지"""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    """사칙연산 계산기"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # 사용자로부터 연산 선택
    choice = input("Enter choice (1/2/3/4): ")

    # 유효한 선택인지 확인
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Invalid input")

# 프로그램 실행
calculator()
