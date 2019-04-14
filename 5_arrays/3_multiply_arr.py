# Multiply two numbers together
# Both numbers are represented as an array of itengers
# 123 -> <1, 2, 3>

def multiplyTwoNumbers(num1, num2):
    # Calculate the sign (Python version of ternary operator)
    # ^ is XOR
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1

    # Make both numbers positive
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # Make num2 an int
    num2 = int(''.join(str(i) for i in num2))

    # Multiply each place in num1 * num2
    i, answer = 1, 0
    for num in reversed(num1):
        answer += num * i * num2
        i *= 10

    return answer * sign

# main
if __name__ == "__main__":
    list1, list2 = [1, 2 ,3], [-4, 5, 6]
    answer = multiplyTwoNumbers(list1, list2)
    print(answer)