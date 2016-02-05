spam_file_1 = 'webspam-uk2006-set1-labels.txt'
spam_file_2 = 'webspam-uk2006-set2-labels.txt'


def read_file(file_name):

    file_reader = open(file_name)

    host_scores = {}

    line_count = 0

    for file_line in file_reader:
        line_count += 1
        host_classification = file_line.split()
        if len(host_classification) >= 3:
            host_rating = int(100*float(host_classification[2]))
            if host_rating in host_scores.keys():
                host_scores[host_rating] += 1
            else:
                host_scores[host_rating] = 1

    return sorted(host_scores.items()), line_count


print read_file(spam_file_1)
print read_file(spam_file_2)
