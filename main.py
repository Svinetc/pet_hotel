print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


import pack_2


print(dir())
print(dir(pack_2))

pack_2.another_some_func()
