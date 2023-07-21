import numpy as np
# getting the dimensions
dimensions_input = input().split()
number_of_documents = int(dimensions_input[0])
number_of_questions = int(dimensions_input[1])
representation_dimenstion = int(dimensions_input[2])
all_statements = number_of_documents + number_of_questions
# constructing an array of all statements
statements = []
matrix = np.array([])
for i in range(all_statements):
    each = input()
    statements.append(each)
# constructing an array consisting of all words, *no duplicate*
all_words = []
for i in range(number_of_documents):
    new_words = statements[i].split()
    for new in new_words:
        if new not in all_words:
            all_words.append(new)
# find the occurances of each word in every document
for word in all_words:
    word_matrix = np.array([])
    for statement in statements:
        words_in_statement = statement.split()
        occurances = 0
        for word_in_statement in words_in_statement:
            if word_in_statement == word:
                occurances += 1
        word_matrix = np.hstack((word_matrix, occurances))
    if len(matrix) == 0:
        matrix = np.array(word_matrix)
    else:
        matrix = np.vstack((matrix, word_matrix))

# SVD decomposition
U, E, V_T = np.linalg.svd(matrix)
U = U[:, :representation_dimenstion]
E = np.diag(E)[:representation_dimenstion, :representation_dimenstion]
V_T = V_T[:representation_dimenstion]
matrix = U @ E @ V_T
matrix = np.transpose(matrix)
# find the best choice in terms of similarity between documents
for i in range(number_of_documents, all_statements):
    best_choice = -1
    maximum_angle = -1
    question_norm = np.linalg.norm(matrix[i])
    for j in range(number_of_documents):
        dot_product = np.dot(matrix[i], matrix[j])
        document_norm = np.linalg.norm(matrix[j])
        angle = dot_product / (question_norm * document_norm)
        if angle >= maximum_angle:
            best_choice = j
            maximum_angle = angle
    print(best_choice)