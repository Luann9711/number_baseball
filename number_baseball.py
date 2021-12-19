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

# 서로 다른 숫자 3개를 랜덤한 순서로 추출
def generate_numbers():
    numbers = random.sample(range(1, 10), 3)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers


# 사용자로부터 서로 다른 3개의 숫자를 입력 받음  (1~9 까지 중복 없이)
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess) < 3:
        number_1 = int(input('{}번째 숫자를 입력하세요 : '.format(len(new_guess) + 1)))
        
        if number_1 > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif number_1 in new_guess:
            print('중복된 숫자입니다.')
        else:
            new_guess.append(number_1)
    
    return new_guess

# 위 두 함수의 결과 값을 리스트화 해서 대조 
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        # 위치와 번호 같으면 스트라이크
        if guesses[i] == solution[i]:
            strike_count += 1
        # 같은 같이 리스트 안에 존재하지만 위치가 다르면 볼
        elif guesses[i] in solution and guesses[i] != solution[i]:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1

    # 반복문 안에서 변수선언을 해야 무한루프에 빠지지 않는다
    INPUTNUMBER = take_guess()
    s, b = get_score(INPUTNUMBER, ANSWER)
    print("{}S {}B\n".format(s, b))

    if s == b:
        break
    
    
        

    

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))