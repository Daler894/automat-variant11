
S, P0, P1, C, D, E, F, G = range(8)
NUM_STATES = 8

delta = [[[] for _ in range(3)] for _ in range(NUM_STATES)]

delta[S][2]  = [P0, F]
delta[P0][0] = [P0]
delta[P0][1] = [P1]
delta[P1][0] = [P0]
delta[P1][1] = [P1, C]
delta[C][0]  = [D]
delta[C][1]  = [E]
delta[D][1]  = [E]
delta[E][0]  = [D]
delta[E][1]  = [E]
delta[F][0]  = [G]
delta[F][1]  = [F]
delta[G][1]  = [F]

accepting = {C, E, F, G}

names = {S:"S", P0:"P0", P1:"P1", C:"C", D:"D", E:"E", F:"F", G:"G"}


def epsilon_closure(states):
    closure = set(states)
    stack = list(states)
    while stack:
        s = stack.pop()
        for nxt in delta[s][2]:
            if nxt not in closure:
                closure.add(nxt)
                stack.append(nxt)
    return closure


def move(states, symbol):
    result = set()
    for s in states:
        for nxt in delta[s][symbol]:
            result.add(nxt)
    return epsilon_closure(result)


def accepts(word):
    """Прогон НКА на цепочке. Возвращает True/False."""
    current = epsilon_closure({S})
    for ch in word:
        if ch == '0':
            sym = 0
        elif ch == '1':
            sym = 1
        else:
            return False
        current = move(current, sym)
        if not current:
            return False
    for s in current:
        if s in accepting:
            return True
    return False


def print_table(tests):
    for t in tests:
        word = ''.join(t) if t else "(пустая)"
        res = accepts(t)
        result = "Accept" if res else "Reject"
        print(f"{word:<20} {result}")


def main():
    tests = [
        ['0','0','1','1'],
        ['0','0','1','1','0','0'],
        ['0','0','1','1','0','0','1','1'],
        ['0','0'],
        ['0','1','0'],
        ['1','1','0','0'],
        ['1','1','0','0','1','1'],
        ['1','1','1','1'],
    ]
    print_table(tests)


if __name__ == "__main__":
    main()