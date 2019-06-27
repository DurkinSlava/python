""" Пример циклической очереди """
a = []

MAX = 10
# initialization
for i in range(MAX):
    a.append(0)

spos = 0
rpos = 0


def store_element():
    """ Добавление элемента в очередь"""

    # Очередь переполняется, когда
    # spos на единицу меньше
    # rpos, либо когда
    # spos указывает
    # на конец
    # массива, а rpos - на начало.
    # Для корректной работы оставляем одну ячейку пустой


    global spos, rpos, a

    while True:

        value = input('Input a value № %s:' % str(spos + 1))

        if value:

            if (spos + 1) == rpos or (spos + 1 == MAX and not rpos):
                print('Queue is full')
                return

            a[spos] = value
            spos += 1

            if spos == MAX:
                spos = 0

            #print('rpos = %d, spos = %d'% (rpos, spos))
        else:
            return

        list_queue()


def delete_element():
    """ Удаление элемента из очереди """
    global spos, rpos, MAX

    if rpos == MAX:
        rpos = 0

    if rpos == spos:
        print('Queue is empty.')
        return

    rpos += 1;

    #print('rpos = %d, spos = %d' % (rpos, spos))

    list_queue()


def list_queue():
    """ Печать очереди """

    global spos, rpos, MAX

    i = rpos

    if i == MAX:
        i = 0


    while not i == spos:

        print(a[i], end=' ')
        i += 1

        if i == MAX:
            i = 0

    print('')


while True:

    print("(S)tore")
    print("(D)elete")
    print("(L)ist")
    print("(Q)uit")
    print("The queue of %s elements" % MAX)

    select = input('Choice:')

    menu = select.upper()
    if menu == 'S':
        store_element()
    elif menu == 'D':
        delete_element()
    elif menu == 'L':
        list_queue()
    elif menu == 'Q':
        exit(0)


