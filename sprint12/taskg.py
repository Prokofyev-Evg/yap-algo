val = int(input())


def test(out_val, in_val):
    if in_val <= 1:
        return out_val + str(in_val)
    return test(out_val, in_val // 2) + str(in_val % 2)


print(test("", val))
