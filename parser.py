import numpy

def parse_input(filename):
    with open(filename, 'r') as f:
        number_of_images = map(lambda x: int(x), f.readline().split())
        matrix = [[char for char in line.strip().split(' ')] for line in f]
        new_matrix = [[line[0], line[2:]] for line in matrix]
    return new_matrix


def algorithm(matrix):
    horizontals = [line for line in matrix if line[0] is 'H']
    verticals = [line for line in matrix if line[0] is 'V']
    horizontals_with_one_tag = [line for line in horizontals if len(line[1]) is 1]
    horizontals_without_one_tag = [line for line in horizontals if line not in horizontals_with_one_tag]

    # Two verticals with highest score


def score(set1, set2):
    intersection = numpy.intersect1d(set1, set2)
    return min(len(set1) - len(intersection), len(set2) - len(intersection), len(intersection))


def write_result(result, filename):
    length = len(result)
    with open('result_' + filename, 'w') as result_file:
        result_file.write(str(length) + '\n')
        for line in result:
            result_file.write(' '.join(str(elem) for elem in line) + '\n')

filename = 'example_input'
matrix = parse_input(filename)
result = algorithm(matrix)
write_result(result, 'example')

print('')
