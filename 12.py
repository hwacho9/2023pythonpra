matrix = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
          [['a', 'b', 'c'], ['d', 'e', 'f']]]

# 괄호 1번 벗기기
print("괄호 한 번 벗기기")
sub_matrix = [row for row in matrix]
print("matrix_sub_matrix :", sub_matrix)

# 괄호 2번 벗기기
print("괄호 두 번 벗기기")
sub_matrix_list = [row_element for row in matrix for row_element in row]
print("matrix_sub_matrix_list : ", sub_matrix_list)

print("괄호 세 번 벗기기")
sub_matrix_list_element = [element for sub_matrix in matrix
                           for sub_matrix_list in sub_matrix
                           for element in sub_matrix_list]

print("matrix_sub_matrix_list_element : ", sub_matrix_list_element)
