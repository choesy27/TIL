input = 20


def find_prime_list_under_number(number):
    # 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
    # 이 부분을 채워보세요!
    prime_list = []

    # range(시작 숫자(생략 가능), 종료 숫자, step(생략 가능))
    for n in range(2, number+1):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)