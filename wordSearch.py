import random

def populate_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = chr(random.randint(97, 122))  # ASCII values for lowercase letters (a-z)

def hide_first_name(name1, matrix):
    col = random.randint(0, 14)
    for row in range(len(name1)):
        matrix[row][col] = name1[row]

def hide_last_name(name2, matrix):
    col = random.randint(0, 14)
    for row in range(len(name2)):
        matrix[row][col] = name2[row]

def answer_key(name1, name2, matrix):
    answer_key = [['.' for _ in range(15)] for _ in range(15)]
    print("\nThe answers to the generated word search are:\n")
    
    for colu in range(len(name1)):
        if name1[0] == matrix[0][colu] and name1[1] == matrix[1][colu] and name1[2] == matrix[2][colu]:
            for row in range(len(name1)):
                answer_key[row][colu] = name1[row]
    
    for r in range(len(name2)):
        if name2[0] == matrix[0][r] and name2[1] == matrix[1][r] and name2[2] == matrix[2][r]:
            for c in range(len(name2)):
                answer_key[c][r] = name2[c]
                
    for row in answer_key:
        print(' '.join(row))

if __name__ == "__main__":
    matrix = [['.' for _ in range(15)] for _ in range(15)]
    populate_matrix(matrix)
    hide_first_name("marie", matrix)
    hide_last_name("muya", matrix)
    
    for row in matrix:
        print(' '.join(row))
        
    answer_key("marie", "muya", matrix)