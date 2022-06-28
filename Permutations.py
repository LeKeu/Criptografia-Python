import itertools as it
import cProfile


def per1():
    n = int(input('Digite um número: '))
    my_list = [x for x in range(n)]
    list_of_permutations = it.permutations(my_list)
    cnt = 0
    for permutations in list_of_permutations:
        cnt += 1
    print(f'{len(my_list)} --> {cnt}')


def per2RECURSAO(n):
    if n <= 1:
        return n
    else:
        return per2RECURSAO(n - 1) * n


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    for i in range(1, num + 1):
        print(per2RECURSAO(i))

    cProfile.run("counter(per2RECURSAO(11))")

