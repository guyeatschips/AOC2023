file_input = open('.\input.txt', 'r').readlines()

def get_whittled_numbers(nums):
    first_digit = nums[0]
    if len(nums) > 1:
        last_digit = nums[(len(nums) - 1)]
    elif len(nums) == 1:
        last_digit = nums[0]
    whittled_number = first_digit + last_digit
    return whittled_number

def get_numbers(line):
    combined = ""
    for char in line:
        if char.isnumeric():
            combined += char
    return get_whittled_numbers(combined)

if __name__ == '__main__':
    final_answer = 0
    for each in file_input:
        num = get_numbers(each)
        final_answer += int(num)
    print(f"The final answer is {final_answer}")
