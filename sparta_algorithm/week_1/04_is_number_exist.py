input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for element in array:       # array의 길이만큼 아래 연산
        if number == number:    # 비교 연산 1번 실행
            return True         # 총 N * 1 = N만큼의 시간 복잡도
    return False


result = is_number_exist(3, input)
print(result)