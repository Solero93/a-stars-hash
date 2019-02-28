import numpy as np
import itertools as it

def parse_input(filename):
    with open(filename, 'r') as f:
        number_of_images = map(lambda x: int(x), f.readline().split())
        matrix = [[char for char in line.strip().split(' ')] for line in f]
        new_matrix = [[i, line[0], line[2:]] for i, line in enumerate(matrix)]
    return new_matrix


def algorithm(matrix):
    horizontals = [line for line in matrix if line[1] is 'H']
    verticals = [line for line in matrix if line[1] is 'V']
    horizontals_without_one_tag = [line for line in horizontals if len(line[2]) > 1]

    # Two verticals with highest score

    all_verticals = verticals
    verticals_to_not_visit = []
    pairs = []
    for vertical in verticals:
        if vertical not in verticals_to_not_visit:
            max_vertical = max(all_verticals, key=lambda x: score(vertical[2], x[2]))
            all_verticals.remove(max_vertical)
            all_verticals.remove(vertical)
            verticals_to_not_visit.append(vertical)
            verticals_to_not_visit.append(max_vertical)
            pairs.append([[vertical[0], max_vertical[0]], 'S', np.intersect1d(vertical[2], max_vertical[2])])

    slides = [*horizontals, *pairs]
    all_slides = slides
    slides_to_not_visit = []
    finalSlides = []

    slide = slides[0]
    slides_to_not_visit.append(slide)
    all_slides.remove(slide)

    if slide[1] is 'S':
        finalSlides.append(str(slide[0][0]) + ' ' + str(slide[0][1]))
    else:
        finalSlides.append(str(slide[0]))

    while all_slides:
        # if slide not in slides_to_not_visit:

        max_slide = max(all_slides, key=lambda x: score(slide[2], x[2]))
        all_slides.remove(max_slide)

        slides_to_not_visit.append(max_slide)

        if max_slide[1] is 'S':
            finalSlides.append(str(max_slide[0][0]) + ' ' + str(max_slide[0][1]))
        else:
            finalSlides.append(str(max_slide[0]))

        slide = max_slide

    # for slide in slides:
    #     if slide not in slides_to_not_visit:
    #         max_slide = max(all_slides, key=lambda x: score(slide[2], x[2]))
    #         all_slides.remove(max_slide)
    #         all_slides.remove(slide)
    #         slides_to_not_visit.append(slide)
    #         slides_to_not_visit.append(max_slide)
    #
    #         if slide[1] is 'S':
    #             finalSlides.append(str(slide[0][0]) + ' ' + str(slide[0][1]))
    #         else:
    #             finalSlides.append(str(slide[0]))
    #
    #         if max_slide[1] is 'S':
    #             finalSlides.append(str(max_slide[0][0]) + ' ' + str(max_slide[0][1]))
    #         else:
    #             finalSlides.append(str(max_slide[0]))

    #sorted_combinations = sorted(it.combinations(verticals, r=2), key=lambda x: score(x[0][2], x[1][2]))

    # resultX = []
    #
    # for s in finalSlides:
    #     if s[1] is 'S':
    #         resultX.append(str(s[0][0]) + ' ' + str(s[0][1]))
    #     else:
    #         resultX.append(str(s[0]))

    return set(finalSlides)




def score(set1, set2):
    intersection = np.intersect1d(set1, set2)
    return min(len(set1) - len(intersection), len(set2) - len(intersection), len(intersection))


def write_result(result, filename):
    length = len(result)
    with open(filename + '.txt', 'w') as result_file:
        result_file.write(str(length) + '\n')
        result_file.writelines('\n'.join(result))


filename = 'data_set/c_memorable_moments.txt'
matrix = parse_input(filename)
result = algorithm(matrix)
write_result(result, filename)

print('')