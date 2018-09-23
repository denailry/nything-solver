black_piece = []
white_piece = []

str_white = "WHITE"
str_black = "BLACK"

def read_file(file_name):
    data_file = open(file_name, 'r')
    
    for row in data_file:
        arr_row = row.split()
        if (arr_row[0] == str_white):
            for i in range(0, int(arr_row[2])):
                white_piece.append(arr_row[1][0])
        else:
            for i in range(0, int(arr_row[2])):
                print(arr_row[1][0])
                black_piece.append(arr_row[1][0])

read_file('input1.txt')
print(black_piece)
print(white_piece)