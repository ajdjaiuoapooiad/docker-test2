def test(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# result2 = test(3)
# print(result2)  # Output: 120

def sum_num(test_string):
    try:
        number = int(test_string)
        if number <= 0:
            return "ERROR"
        else:
            total_sum = sum(range(1, number + 1))
            return str(total_sum)
    except ValueError:
        return "ERROR"

# テスト例
print(sum_num("5"))  
print(sum_num("10")) 




