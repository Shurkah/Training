firstline = list(input().split())
letters, pairs = int(firstline[0]), int(firstline[1])

dict = {}
for i in range(letters):
    translation = input().split()
    if translation[0] not in dict:
        dict[translation[0]] = list(translation[1])
    else:
        dict[translation[0]].append(translation[1])
print('\n')
for n in range(pairs):
    pair = input().split()
    one = str(pair[0])
    two = str(pair[1])
    trans = True
    if not trans:
        continue

    if len(one) != len(two):
        print("no")
        trans = False
    else:
        for i in range(len(one)):
            if one[i] != two[i]:
                if one[i] not in dict:
                    print("no")
                    trans = False
                    break
                elif two[i] not in dict[one[i]]:
                    print("no")
                    trans = False
                    break
    if trans:
        print("yes")
