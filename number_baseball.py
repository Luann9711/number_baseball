import random, time

# 이렇게도 가능
# def generate_numbers():
#     numbers = []
    
#     while len(numbers) < 3:
#         new_number = random.randint(0,9)
#         if new_number not in numbers:
#             numbers.append(new_number)

#     print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
#     return numbers

def generate_numbers():
    numbers = random.sample(range(1, 10), 3)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess) < 3:
        number_1 = int(input('1번째 숫자를 입력하세요 : '))
        
        if (number_1 > 9) or (number_1 < 0):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            break
        number_2 = int(input('2번째 숫자를 입력하세요 : '))
        number_3 = int(input('3번째 숫자를 입력하세요 : '))
    
    return new_guess

print(take_guess())