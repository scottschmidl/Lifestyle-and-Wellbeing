
def find_min_max_possible(q1_2_a, q3_4_7_8_9_a, q10_11_12_14_15_16_18_20_a, q5_17_19_a, q6_13_a):

    '''returns the min and max possible scores using the
        numerical answers'''

    min_possible_score = q1_2_a[0] * 2 + q3_4_7_8_9_a[0] * 5 + q10_11_12_14_15_16_18_20_a[0] * 8 + q5_17_19_a[0] * 3 + q6_13_a[0] * 2
    max_possible_score = q1_2_a[-1] * 2 + q3_4_7_8_9_a[-1] * 5 + q10_11_12_14_15_16_18_20_a[-1] * 8 + q5_17_19_a[-1] * 3 + q6_13_a[-1] * 2

    return min_possible_score, max_possible_score

def main():

    q1_2_a = list(range(1, 11))
    q3_4_7_8_9_a = list(range(0,11))
    q10_11_12_14_15_16_18_20_a = list(range(0, 11))
    q5_17_19_a = list(range(0, 6))
    q6_13_a = [1,2]

    min_max_possible_scores = find_min_max_possible(q1_2_a, q3_4_7_8_9_a, q10_11_12_14_15_16_18_20_a, q5_17_19_a, q6_13_a)

    print(min_max_possible_scores)

if __name__ == '__main__':
    main()