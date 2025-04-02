def pipe_fix(nums):
    # Найти минимальное и максимальное значения в списке
    min_num = min(nums)
    max_num = max(nums)

    # Создать новый список с последовательными числами от min_num до max_num
    return list(range(min_num, max_num + 1))

# Примеры тестов
import codewars_test as test
from solution import pipe_fix

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(pipe_fix([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(pipe_fix([1, 2, 3, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        test.assert_equals(pipe_fix([6, 9]), [6, 7, 8, 9])
        test.assert_equals(pipe_fix([-1, 4]), [-1, 0, 1, 2, 3, 4])
        test.assert_equals(pipe_fix([1, 2, 3]), [1, 2, 3])

# def pipe_fix(nums):
# 	return list(range(nums[0], nums[-1] + 1))

#