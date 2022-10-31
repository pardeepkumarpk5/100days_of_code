''' Treasure map game '''

# creating list containg our treasure chest
row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}\n')

position = input('where do you want to put the treasure ')

vertical = int(position[0])-1
horizontal = int(position[1])-1
map[vertical][horizontal] = 'X'


print(f'{row1}\n{row2}\n{row3}\n')
