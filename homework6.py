dict = {}
with open('file6.txt', 'r') as file6:
    for line in file6:
        subject, lecture, practice, lab = line.split()
        dict[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {dict}')
