import time
from threading import Thread
from datetime import datetime
import example2


def wite_words(word_count, file_name):
    with open(file_name, 'w+', encoding= 'utf8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Парашут № {i}, \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_func = datetime.now()
a = wite_words(10,file_name='example1.txt')
b = wite_words(30,file_name='example2.txt')
c = wite_words(200,file_name='example3.txt')
d = wite_words(100,file_name='example4.txt')
finish_func = datetime.now()

print(f'Время работы функций {finish_func - start_func}, сек.')

start_potok = datetime.now()

potok5 = Thread(wite_words(10, 'example5.txt'))
potok6 = Thread(wite_words(30, 'example6.txt'))
potok7 = Thread(wite_words(200, 'example7.txt'))
potok8 = Thread(wite_words(100, 'example8.txt'))

#start_potok = datetime.now()

potok8.start()
potok7.start()
potok6.start()
potok5.start()

potok5.join()
potok6.join()
potok7.join()
potok8.join()

finish_potok = datetime.now()
print(f'Время работы потоков {finish_potok - start_potok}, сек.')
