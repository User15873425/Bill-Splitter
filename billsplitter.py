from random import choice

num = int(input('Enter the number of friends joining (including you):\n'))
if num > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    names, total = [input() for _ in range(num)], int(input('\nEnter the total bill value:\n'))
    lucky = choice(names) if input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n') == 'Yes' else 0
    bill = dict.fromkeys(names, round(total / (num-1 if lucky else num), 2))
    bill.update({lucky: 0}) if lucky else None
    print(f'\n{lucky} is the lucky one!' if lucky else '\nNo one is going to be lucky', bill, sep='\n\n')
else:
    print('\nNo one is joining for the party')
