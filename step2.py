import copy


li = [
    ['R','R','W'],
    ['G','C','W'],
    ['G','B','B']
]


def index_word_seperate(words_list):
    for index, word in enumerate(words_list):
        if word in "'":
            words_ldash = words_list[index-1] + words_list[index]
            words_list.pop(index)
            words_list[index-1] = words_ldash

    for index, word2 in enumerate(words_list):
        if word2 == "L'":
            j = 0
            print(word2)

            for i in range(0, len(li)-1):
                common_i(i,j)
            
            li_print(li)

        elif word2 == "L":
            print(word2)

            j = 0
            for i in range(len(li)-1, 0, -1):
                common_i_reverse(i,j)

            li_print(li) 
        elif word2 == 'R':
            print(word2)
            j = 2
            for i in range(0, len(li)-1):
                common_i(i,j)

            li_print(li)


        elif word2 == "R'":
            print(word2)

            j = 2
            for i in range(len(li)-1, 0, -1):
                common_i_reverse(i,j)

            li_print(li)
        elif word2 == "U":
            print(word2)

            i = 0
            for j in range(0, len(li)-1):
                common_j(i,j)
            
            li_print(li) 

        elif word2 == "U'":
            print(word2)

            i = 0
            for j in range(len(li)-1, 0, -1):
                common_j_reverse(i,j)
            
            li_print(li) 
        elif word2 == "B'":
            print(word2)

            i = 2
            for j in range(0, len(li)-1):
                common_j(i,j)
            
            li_print(li) 
        elif word2 == "B":
            print(word2)

            i = 2
            for j in range(len(li)-1, 0, -1):
                common_j_reverse(i,j)
            
            li_print(li) 


def common_i(i,j):
    temp1 = li[i][j]
    li[i][j] = li[i + 1][j]
    li[i + 1][j] = temp1
    return li


def common_i_reverse(i,j):
    temp1 = li[i][j]
    li[i][j] = li[i-1][j]
    li[i-1][j] = temp1
    return li


def common_j(i,j):
    temp1 = li[i][j]
    li[i][j] = li[i][j+1]
    li[i][j+1] = temp1
    return li 


def common_j_reverse(i,j):
    temp1 = li[i][j]
    li[i][j] = li[i][j-1]
    li[i][j-1] = temp1
    return li


def li_print(li):
    for x, y, z in li:
        print(x, y, z)  

def step2_while(msg):
    li_deepcopy = copy.deepcopy(li)

    while True:
        try:
            words = input(msg)
            if words.upper() == 'Q':
                raise

            words_list = []
            words_list.extend(words.upper())

            li_print(li_deepcopy)
            index_word_seperate(words_list)
        except Exception as e:
            if words.upper() == 'Q':
                print('Bye~')
                return


step2_while('CUBE> ')