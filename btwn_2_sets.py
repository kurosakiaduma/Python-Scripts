from time import time

def getTotalX(a: list, b: list):
    # Write your code here
    start = time()
    final = set()
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    lower_bound = int((b[0] // 2) + 1)

    for i in range(2, lower_bound):
        a_iters = iter(a)

        while True:
            try:
                a_factor = next(a_iters)
                candidate = a_factor * i
                if candidate <= b[0]:
                    assert (all([not (candidate % i) for i in a]))
                    final.add(candidate)
                    print(f"PASSED {candidate} {final} {a_factor}")
                    break
                else:
                    break
            except AssertionError:
                print(final)
                if candidate in final:
                    final.remove(candidate)
                    print(f"REMOVED {candidate} {final} {a_factor}")

                continue
            except StopIteration:
                break

    if len(a) == 1:
        final.add(a[-1])

    print(final)
    candidates = iter(list(final))

    while True:
        try:
            candidate = next(candidates)
            mult_iters = iter(b)
            while True:
                try:
                    mult = next(mult_iters)
                    if not (mult % candidate):
                        pass
                    else:
                        final.remove(candidate)
                        break
                except (StopIteration, RuntimeError):
                    break
        except StopIteration:
            if len(b) == 1:
                if all([not (b[-1] % i) for i in a]):
                    final.add(b[-1])
                else:
                    print("passed!")
                    pass
            break

    end = time()
    runtime = end - start
    print(final, round(runtime, 12))

    return len(final)


if __name__ == '__main__':
    one = ([1],[100])
    two = ([1], [60])
    three = ([1], [50])
    four = ([2,3,],[240, 60, 120])

    print(getTotalX(three[0], three[1]))
    print(getTotalX(four[0], four[1]))