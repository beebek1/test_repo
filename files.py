# # a = ['ram', 'shyam']
# # f = open("f_file.py", mode= 'w')
# # f.writelines(a)
# # f.close()

# # for i in range(5):
# #     username = input(f"enter username {i+1}")

# # import pickle
# # a = ['ram', 'shyam']
# # with open('sectionc.txt','wb') as f1:
# #     pickle.dump(a,f1)

# # import pickle
# # a = ['ram','shyam']
# # f1=open('sections.txt','wb')
# # print()

# f1=open('abc.txt', mode='r')
# f2= open('python.txt', mode='w')
# posi = f1.seek(4)
# re= f1.read(posi)
# wr = f2.write(re)
# f1.close()
# f2.close()

# a = 1 
# def outer():
#     b = 3
#     def inner():
#         nonlocal b
#         b = b+3
#         c = 13
#         print(b)
#     print(b)
#     print(inner())
#     print(b)
# print(outer())

a = 'programming'
print(a[5:3])

