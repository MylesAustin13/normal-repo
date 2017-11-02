TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))
        
def score(w):
  points = {1:'AEIOULNRST', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
  total = 0
  w = w.upper()
  for char in w:
    
    for v in points.keys():

      if char in points[v]:
        total += v
        #print(total)
  return total
     
def add_word_across(board,word,r,c):
    
    rawvals = {
    "aeioulnrst" : 1,
    "dg"         : 2,
    "bcmp"       : 3,
    "fhvwy"      : 4,
    "k"          : 5,
    "jx"         : 8,
    "qz"         : 10
    }

    word = word.lower()
    total = 0
    char_score = 0
    word_multiplier = 1
    if(len(board[r]) - c < len(word)):
        print("This word doesn't fit!")
        return total
    else:
        i = 0
        for char in word:
            for k in rawvals:
                if char in k:
                    char_score = rawvals[k]
            if(board[r][c+i] == 't'):
                char_score *= 3
            if(board[r][c+i] == 'd'):
                char_score *= 2
            if(board[r][c+i] == 'T'):
                word_multiplier *= 3
            if(board[r][c+i] == 'D'):
                word_multiplier *= 2
            board[r][c+i] = char
            total += char_score
            char_score = 0
            i += 1
    return total * word_multiplier


def add_word_down(board,word,r,c):
    
    rawvals = {
    "aeioulnrst" : 1,
    "dg"         : 2,
    "bcmp"       : 3,
    "fhvwy"      : 4,
    "k"          : 5,
    "jx"         : 8,
    "qz"         : 10
    }

    word = word.lower()
    total = 0
    char_score = 0
    word_multiplier = 1
    if(len(board[r]) - r < len(word)):
        print("This word doesn't fit!")
        return total
    else:
        i = 0
        for char in word:
            for k in rawvals:
                if char in k:
                    char_score = rawvals[k]
            if(board[r+i][c] == 't'):
                char_score *= 3
            if(board[r+i][c] == 'd'):
                char_score *= 2
            if(board[r+i][c] == 'T'):
                word_multiplier *= 3
            if(board[r+i][c] == 'D'):
                word_multiplier *= 2
            board[r+i][c] = char
            total += char_score
            char_score = 0
            i += 1
    return total * word_multiplier

#Test cases
b = make_scrabble_board()
print("Score for this word:",add_word_across(b,"aaaaaaaaaa",0,0))
print_board(b)
print("----------------------------")
c = make_scrabble_board()
print("Score for this word:",add_word_down(c,"hammer",5,5))
print_board(c)
print("----------------------------")

d = make_scrabble_board()
print("Score for this word:",add_word_across(d,"loooooooooooooooooong",0,0))
print_board(d)
