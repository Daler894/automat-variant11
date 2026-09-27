

NUM_STATES = 9


delta = [[0, 0] for _ in range(NUM_STATES)]

for i in range(3):
    for j in range(3):
        s = i * 3 + j
        delta[s][0] = ((i + 1) % 3) * 3 + j   # по 'a'
        delta[s][1] = i * 3 + ((j + 1) % 3)   # по 'b'

START = 0  # (0,0)

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
    """Прогон ДКА на цепочке. Возвращает True/False."""
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


def print_table(tests):
    print("+----------------------+----------+")
    print("| Цепочка              | Результат|")
    print("+----------------------+----------+")

    for t in tests:
        word = ''.join(t) if t else "(пустая)"
        res = accepts(t)
        result = "Accept" if res else "Reject"
        print(f"| {word:<20} | {result:<8} |")



def main():
    tests = [
        ['a'],
        ['aa'],
        ['aaa'],
        ['aaaa'],
        ['ab'],
        ['aab'],
        ['abb'],
        ['aabb'],
        ['aaabbb'],
        ['aaaaabbb'],
    ]
    print_table(tests)


if __name__ == "__main__":
    main()