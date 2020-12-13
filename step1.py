'''
입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
밀려나간 단어는 반대쪽으로 채워진다.
'''
print('입력되는 것은 띄어쓰기로 구분합니다')
words = input('단어, 숫자, L 혹은 R 입력하세요> ')
split_words = words.split()

words_list = []
words_list.extend(split_words[0])
words_num = int(split_words[1])
words_RL =  split_words[2].upper()

if words_num >= 0:
    if words_RL == 'R':
        for _ in range(words_num):
            for i in range(len(words_list) - 1, 0, -1):
                temp = words_list[i]
                words_list[i] = words_list[i - 1]
                words_list[i - 1] = temp
    elif words_RL == 'L':
        for _ in range(words_num):
            for i in range(0, len(words_list) - 1):
                temp = words_list[i]
                words_list[i] = words_list[i + 1]
                words_list[i + 1] = temp
elif words_num < 0:
    words_num = abs(words_num)
    if words_RL == 'L':
        for _ in range(words_num):
            for i in range(len(words_list) - 1, 0, -1):
                temp = words_list[i]
                words_list[i] = words_list[i - 1]
                words_list[i - 1] = temp
    elif words_RL == 'R':
        for _ in range(words_num):
            for i in range(0, len(words_list) - 1):
                temp = words_list[i]
                words_list[i] = words_list[i + 1]
                words_list[i + 1] = temp

print(words_list)