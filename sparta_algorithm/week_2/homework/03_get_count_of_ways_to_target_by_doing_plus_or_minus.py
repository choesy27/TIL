numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways_count):
    # 구현해보세요!
    if current_index == len(array):     # 탈출 조건
        if current_sum == target:
            all_ways_count += 1         # 마지막 다다랐을 때 합계를 추가
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + array[current_index],
                                                       all_ways_count)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - array[current_index],
                                                       all_ways_count)

# current_index = 0, current_sum = 0: 시작하는 총액이 0, 시작 인덱스도 0
get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_count)
print(result_count)