from random import shuffle
n1 = input('escolha um nome: ')
n2 = input('escolha outro nome: ')
n3 = input('escolha outro nome: ')
n4 = input('escolha outro nome: ')
l= [n1,n2,n3,n4]
shuffle(l)
print(f'a ordem sera: {l}.')

#printar todo texto 3 aspas ''' '''
print('''ILorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in 
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
 and more recently with desktop publishing software like Aldus PageMaker including
 versions of Lorem Ipsum.''')