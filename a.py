# Программа проверяет условие: (na // 3) > (nb // 3).

def check_a(word):
    """
    word - список символов, например ['a','a','b'].
    Возвращает True, если (na // 3) > (nb // 3).
    """
    na = 0
    nb = 0
    for c in word:
        if c == 'a':
            na += 1
        elif c == 'b':
            nb += 1
        else:
            return False
    return (na // 3) > (nb // 3)


def main():
    tests = [
        ['a','a','a'],
        ['a','a','a','b','b','b'],
        ['a','a','a','a','a','a'],
        ['a','a','a','a','a','a','b','b','b'],
        ['a','a','a','a','a','a','b','b','b','b','b','b'],
        ['a','b'],
        [],
    ]
    for t in tests:
        print("Цепочка:", ''.join(t) if t else "(пустая)")
        res = check_a(t)
        print("Результат:", "ДОПУСТИТЬ" if res else "ОТКЛОНИТЬ")
        print("---")


if __name__ == "__main__":
    main()