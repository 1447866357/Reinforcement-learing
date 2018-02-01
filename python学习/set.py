char_list = ['a','b','c','c','d','d','e']
sentence='welcome back to This Tutorial'
print(set(char_list))
print((set(sentence)))
u_list=set(char_list)
u_list.add('x')
u_list.remove('b')
u_list.remove('e')

print(u_list)
print(u_list.difference('a'))