def computegrade(a):
    if 0.0 <= a <= 1.0:
        if a >= 0.9:
            return "A"
        if a >= 0.8:
            return "B"
        if a >= 0.7:
            return "C"
        if a >= 0.6:
            return "D"
        return "F"

    return 'Bad score'


input_score = input('Enter score: ')
score = 0.0

try:
    score = float(input_score)
except ValueError:
    print('Bad score')
    quit()

grade = computegrade(score)
print(grade)
