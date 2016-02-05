f = open('webspam-uk2006-set2-labels.txt')

scores = {}

for i in range(1000):
    temp = f.readline().split()
    rating = int(100*float(temp[2]))
    if rating in scores.keys():
        scores[rating] += 1
    else:
        scores[rating] = 1

print scores
