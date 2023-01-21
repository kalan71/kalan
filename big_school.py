# school_class =int(input('В каком ты классе? '))
school_class = input('В каком ты классе? ')
while not school_class.isdigit() or int(school_class) < 1 or int(school_class) > 10:
    school_class = input('В каком ты классе? ')
int_school_class = int(school_class)
while int_school_class < 11:
    if int_school_class == 4:
        int_school_class += 1
        continue
    int_school_class += 1
    print(int_school_class)
print('и всё')
