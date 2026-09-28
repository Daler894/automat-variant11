

NUM_STATES = 9


delta = [[0, 0] for _ in range(NUM_STATES)]

for i in range(3):
    for j in range(3):
        s = i * 3 + j
        delta[s][0] = ((i + 1) % 3) * 3 + j   # по 'a'
        delta[s][1] = i * 3 + ((j + 1) % 3)   # по 'b'

START = 0  # (0,0)

# Допускающие состояния: i > j
accepting = set()
for i in range(3):
    for j in range(3):
        if i > j:
            accepting.add(i * 3 + j)

names = {}
for i in range(3):
    for j in range(3):
        names[i * 3 + j] = f"q_{i}{j}"


def accepts(word):
    """
    Прогон ДКА на цепочке.
    word - список символов, например ['a', 'a', 'b'].
    """
    state = START
    for ch in word:
        if ch == 'a':
            sym = 0
        elif ch == 'b':
            sym = 1
        else:
            return False
        state = delta[state][sym]
    return state in accepting


def main():
    tests = [
        ['a'],
        ['a', 'a'],
        ['a', 'a', 'a'],
        ['a', 'a', 'a', 'a'],
        ['a', 'b'],
        ['a', 'a', 'b'],
        ['a', 'b', 'b'],
        ['a', 'a', 'b', 'b'],
        ['a', 'a', 'a', 'b', 'b', 'b'],
        ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
    ]

    # Заголовок
    print("+----------------------+----------+")
    print("| Цепочка              | Результат|")
    print("+----------------------+----------+")

    for t in tests:
        print("| ", end="")
        for ch in t:
            print(ch, end="")
        for _ in range(20 - len(t)):
            print(" ", end="")
        print("| ", end="")

        res = accepts(t)
        result = "Accept" if res else "Reject"
        print(f"{result:<8} |")

    print("+----------------------+----------+")


if __name__ == "__main__":
    main()