# The program receives a dictionary of letters and their translations
# It then provides pair of strings, and the goal is to determine
# whether the second is a translation of the first or not

firstline = list(input().split())
letters, pairs = int(firstline[0]), int(firstline[1])

dictt = {}
for i in range(letters):
    translation = input().split()
    if translation[0] not in dictt:
        dictt[translation[0]] = list(translation[1])
    else:
        dictt[translation[0]].append(translation[1])

previous_letters = []


def check_one_letter_tr(input_letter, goal):
    global dictt
    global previous_letters

    if input_letter not in dictt:
        return False

    if goal in dictt[input_letter]:
        return True
    else:
        for another in dictt[input_letter]:
            if another in previous_letters:
                return False
            else:
                previous_letters.append(another)
                return check_one_letter_tr(another, goal)


for n in range(pairs):
    pair = input().split()
    one = str(pair[0])
    two = str(pair[1])
    trans = True

    if len(one) != len(two):
        print("no")
        trans = False
    else:
        for i in range(len(one)):
            if one[i] != two[i]:
                if not check_one_letter_tr(one[i], two[i]):
                    print("no")
                    trans = False
                    break

            previous_letters = []

    if trans:
        print("yes")