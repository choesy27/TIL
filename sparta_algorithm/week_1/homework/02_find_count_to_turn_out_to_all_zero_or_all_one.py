input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 0과 1로 이루어진 문자열을 모두 0 또는 1로 만들 수 있는 최소 횟수를 구하여라.
    # 단, 연속된 숫자만을 뒤집을 수 있다.
    # 이 부분을 채워보세요!
    count_to_all_zero = 0
    count_to_all_one = 0

    # 첫 번재 원소가 어떤 숫자인지 확인. 0이 나온 쪽의 숫자로 변환해줘야 한다
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    print("count to all one:", count_to_all_one)
    print("count to all zero:", count_to_all_zero)

    # len(string) - 1의 의미: index
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1

            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)