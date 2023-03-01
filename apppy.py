# Loops xalqa aylana
# For Loop


# for i in [1,2,3,4]:
#     print(i)
#
# for i in [1,2,3,4]:
#     for x in ('a','b','c'):
#         print(i, x)



# user = {
#     'Ismi': input('Ismingiz:'),
#     'Yoshi': int(input('Yoshingiz:')),
#     'Suzishi': bool(input('Suzib bilasizmi:'))
# }


# user = {
#     'Ismi': 'Kamron',
#     'Yoshi': 12,
#     'Suzishi':False ,
# }
#
# for i in 'Kamron':
#     print(i)
# print(user)
#
# print(2 < 8)



# for item in user:
#     print(item)
#
# for item in user.items():
#     print(item)
#
# for item in user.keys():
#     print(item)
#
# for item in user.values():
#     print(item)

# for key, value in user.items():
#     print(key, value)
#
# for k, v in user.items():
#     print(k, v)

# for item in 1:100:
#     print(item)

# counter
# list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for item in list:
#     counter = counter + item
#     print(counter)
# print(counter)

# Range funksiyasi
# print(range(100))
# for son in range(11):
#     print(son)

# for son in range(10, 50):
#     print(son)
#
# for son in range(10, 20, 2):
#     print(son)
#
# for son in range(10, 0, -1):
#     print(son)

# for son in range(5):
#     print(list(range(10)))

















# Enumerate funksiyasi
# for i, char in enumerate('Hello'):
#     print(i, char)

# for i, char in enumerate([1,2,3,4,5]):
#     print(i, char)


# for i, char in enumerate(list(range(1, 11, 3))):
#   print(i, char)
#     # if char == 5:
#     #     print(f'index of 5 {i}ga teng')

# While Loop
# soat = 9
# while 9 == 9:
#     print('Tur uyg\'on')

# soat = 7
# # while soat == 7:
# #     print('Tur uyg\'on')
# #     break

# son = 0
# while son < 10:
#     print(son)
#     son = son + 1
#
# son = 0
# while son <= 10:
#     print(son)
#     son +=1





# son = 0
# while son < 10:
#     print(son)
#     son +=1
# else:
#     print('Kirishingiz mumkin')


# son = 17
# if son >= 18:
#     print('Kirishingiz mumkin')
#     son +=1
# else:
#     print('Kirishingiz mumkin emas')




# son = 0
# while son < 10:
#     print(son)
#     son +=1
#
# print('tekshirildi')


# son = 0
# while son < 10:
#     print(son)
#     son +=1
#     break
# else:
#     print('tekshirildi')

# for son in [1,2,3]:
#     print(son)
# #
# son = 0
# while son < len([1,2,3]):
#     son +=1
#     print(son)

# while True:
#     print('bajar')
#     break
#
# while True:
#     input('isming nima')
#     break

# while True:
#     input('isming nima')
#
#
# while True:
#     ism = input('isming nima')
#     if (ism == 'Kamron'):
#         print(ism)
#         break

# # continue, pass
# list = [1,2,3]
# for item in list:
#     print(item)
#     continue
# #
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1
#     continue
#
# list = [1,2,3]
# for item in list:
#     continue
#     print(item)
#
# i = 0
# while i < len(list):
#     i+=1
#     continue
#     print(list[i])
#
# list = [1,2,3]
# for item in list:
#     print(item)
#     pass
# #
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1
#     pass
#
# list = [1,2,3]
# for item in list:
#     pass
#
# i = 0
# while i < len(list):
#     print(list[i])
#     i+=1
#     pass

# Our first Gui
# rasmlar = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
# iterate the picture
# for row in rasmlar:
#     for pixel in row:
#         if(pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')






# for row in rasmlar:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end = '')
#         else:
#             print(' ', end='')
#     print('')