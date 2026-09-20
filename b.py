
# Язык: цепочки из {0,1}, где каждое 00 находится перед 11

# Состояния
S, P0, P1, C, D, E, F, G = range(8)
NUM_STATES = 8

delta = [[[] for _ in range(3)] for _ in range(NUM_STATES)]

delta[S][2]  = [P0, F]        # S --eps--> P0, F
delta[P0][0] = [P0]           # P0 --0--> P0
delta[P0][1] = [P1]           # P0 --1--> P1
delta[P1][0] = [P0]           # P1 --0--> P0
delta[P1][1] = [P1, C]        # P1 --1--> P1 или C (недетерминизм)
delta[C][0]  = [D]            # C --0--> D
delta[C][1]  = [E]            # C --1--> E
delta[D][1]  = [E]            # D --1--> E
delta[E][0]  = [D]            # E --0--> D
delta[E][1]  = [E]            # E --1--> E
delta[F][0]  = [G]            # F --0--> G
delta[F][1]  = [F]            # F --1--> F
delta[G][1]  = [F]            # G --1--> F

accepting = {C, E, F, G}

names = {S:"S", P0:"P0", P1:"P1", C:"C", D:"D", E:"E", F:"F", G:"G"}


def epsilon_closure(states):
    """Закрытие множества состояний по epsilon-переходам."""
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
    """Шаг: из множества состояний по символу + epsilon-замыкание."""
    result = set()
    for s in states:
        for nxt in delta[s][symbol]:
            result.add(nxt)
    return epsilon_closure(result)


def accepts(word):
    """
    Запуск НКА на цепочке.
    word - список символов, например ['0','0','1','1'].
    """
    current = epsilon_closure({S})
    print("  старт:", sorted(names[s] for s in current))

    for i, ch in enumerate(word):
        if ch == '0':
            sym = 0
        elif ch == '1':
            sym = 1
        else:
            print("  недопустимый символ:", ch)
            return False

        current = move(current, sym)
        print(f"  после '{ch}' (поз.{i}):",
              sorted(names[s] for s in current))

        if not current:
            print("  множество состояний пусто -> ОТКЛОНИТЬ")
            return False

    for s in current:
        if s in accepting:
            print("  допускающее состояние:", names[s])
            return True
    print("  допускающих состояний нет -> ОТКЛОНИТЬ")
    return False


# ---------- Тесты ----------
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
        [],
    ]
    for t in tests:
        print("Цепочка:", ''.join(t) if t else "(пустая)")
        res = accepts(t)
        print("Результат:", "ДОПУСТИТЬ" if res else "ОТКЛОНИТЬ")
        print("---")


if __name__ == "__main__":
    main()