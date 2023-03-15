str_list = ['Penélope', 'Bibi','Caio']

for name in str_list:
    for c in name:
        if c in 'aeiou':
            print(c)