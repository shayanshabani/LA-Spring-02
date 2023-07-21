import numpy as np
import re


number_of_sentences = int(input())
sentences = []
regex = re.compile('[^a-zA-Z\\s]')
# number of all words
number_of_words = 0
all_of_words = []
# get each sentences
for i in range(number_of_sentences + 1):
    each = input()
    # remove commas, dots, ...
    each = regex.sub('', each)
    # lowercase the string
    each = each.lower()
    # append the sentences to the array of sentences
    sentences.append(each)
    if i == number_of_sentences:
        for word in each.split():
            if word not in all_of_words:
                all_of_words.append(word)
                number_of_words += 1

# build the matrix of frequency for sentences
matrix_of_frequency = np.array([])
# for each sentence ...
for sentence in sentences:
    frequency = np.array([])
    for word in all_of_words:
        occurrences = 0
        # number of occurrences of the word in the sentence
        for each in sentence.split():
            if each == word:
                occurrences += 1
        frequency = np.hstack((frequency, occurrences / len(sentence.split())))
    # vertically appending the matrix
    if len(matrix_of_frequency) == 0:
        matrix_of_frequency = frequency.copy()
    else:
        matrix_of_frequency = np.vstack((matrix_of_frequency, frequency))


# now we shall find the common matrix
matrix_of_common = np.array([])
# in how many sentences has this word occurred -> babai mige baba gave mige ma ma
# ye toop daram ghelghleie sorkh o sefid o abie mizanam zamin hava mire nemidooni ta koja mire man in toop ro nadashtam mashghamo khoob neveshtam babam behem eidi dad ye toope ghelghli dad.

for word in all_of_words:
    occurrences = 0
    for i in range(number_of_sentences):
        if word in sentences[i].split():
            occurrences += 1
    # ln of number of all the sentences divided by number of sentences which contain this word
    if occurrences == 0:
        matrix_of_common = np.hstack((matrix_of_common, 0))
    else:
        matrix_of_common = np.hstack((matrix_of_common, np.array([np.log(number_of_sentences / occurrences)])))


# now we shall find the matrix of representation
matrix_of_representation = np.multiply(matrix_of_frequency, matrix_of_common)

index = 0
max_angle = 0
for i in range(number_of_sentences):
    current_angle = np.dot(matrix_of_representation[i], matrix_of_representation[number_of_sentences])
    if current_angle > max_angle and np.linalg.norm(matrix_of_representation[i]) != 0:
        max_angle = current_angle
        index = i + 1

# print the index of a sentence which has the most similarity with the final sentence
print(index)

