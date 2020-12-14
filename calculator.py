# เครื่องคิดเลขแบบธรรมดา

# เป็น function สำหรับบวกเลข 2 ตัว
def add(x, y):
    return x + y

# เป็น function สำหรับลบเลข 2 ตัว
def subtract(x, y):
    return x - y

# เป็น function สำหรับคูณเลข 2 ตัว
def multiply(x, y):
    return x * y

# เป็น function สำหรับบวกหาร 2 ตัว
def divide(x, y):
    return x / y

#เป็นส่วนของตัวเลือก function ว่าจะทำอะไร
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # รับค่าเข้ามา
    choice = input("Enter choice(1/2/3/4): ")

    # เช็คช้อยว่าเป็น ตัวเลือกไหน และก็รับค่าตัวเลข 2 ตัว
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")