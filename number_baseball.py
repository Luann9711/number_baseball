import random, time

def random_three_numbers():
    numbers = random.sample(range(1, 10), 3)
    return numbers


print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
time.sleep(1)
print('Loading.')
time.sleep(1)
print('Loading..')
time.sleep(1)
print('Loading...')
time.sleep(1)

print('숫자 3개를 하나씩 차례대로 입력하세요.')
time.sleep(1)

number_1 = input('1번째 숫자를 입력하세요 : ')
number_2 = input('2번째 숫자를 입력하세요 : ')
number_3 = input('3번째 숫자를 입력하세요 : ')

if (number_1 or number_2 or number_3) >= 10 or (number_1 or number_2 or number_3) == 0:
    print('유효 숫자범위를 이탈했습니다. 다시 입력해 주세요')
    number_1 = input('1번째 숫자를 입력하세요 : ')
    number_2 = input('2번째 숫자를 입력하세요 : ')
    number_3 = input('3번째 숫자를 입력하세요 : ')

elif (number_2 or number_3) == number_1:
    print('첫번째 입력된 숫자와 중복된 숫자입니다 다시 입력해 주세요')
    number_2 = input('2번째 숫자를 입력하세요 : ')
    number_3 = input('3번째 숫자를 입력하세요 : ')
elif number_3 == number_2:
    print('두번째 입력된 숫자와 중복된 숫자입니다 다시 입력해 주세요')
    number_3 = input('3번째 숫자를 입력하세요 : ')