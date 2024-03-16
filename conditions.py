while True:
    try:
        n = int(input("Enter n: "))
        break
    except ValueError:
        print("Please enter a valid number")

fib_list = [0, 1]

if n == 0:
    print(fib_list[0])
elif n == 1:
    print(fib_list[0] + fib_list[1])
else:
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    print(fib_list)
