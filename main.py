def perceptron_AND(x1, x2):
    return 1 if x1 * 1 + x2 * 1 + -1.5 >= 0 else 0
def perceptron_OR(x1, x2):
    return 1 if x1 * 1 + x2 * 1 + -0.5 >= 0 else 0
def perceptron_NAND(x1, x2):
    return 1 if x1 * 1 + x2 * 1 + 1.5 >= 0 else 0


users = {
    'Alessio': {'activity_level': 6, 'stress_level': 3, 'social_score': 7},
    'Laura': {'activity_level': 2, 'stress_level': 9, 'social_score': 4},
    'Pino': {'activity_level': 8, 'stress_level': 4, 'social_score': 5}
}

for u, i in users.items():
    x1 = 1 if i['activity_level'] >= 5 else 0
    x2 = 1 if i['stress_level'] < 5 else 0
    check_AND = perceptron_AND(x1, x2)
    if check_AND == 1:
        print(f'You need to work out {u}!')
        continue
    x1 = 1 if i['stress_level'] >= 7 else 0
    x2 = 1 if i['activity_level'] <= 3 else 0
    check_OR = perceptron_OR(x1, x2)
    if check_OR == 1:
        print(f'You need to relax {u}!')
        continue
    x1 = 1 if i['stress_level'] >= 7 else 0
    x2 = 1 if i['activity_level'] <= 3 else 0
    check_NAND = perceptron_NAND(x1, x2)
    if check_NAND == 1:
        print(f'Have a chat with someone {u} 😊!')
        continue