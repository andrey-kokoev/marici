"""Minimize only the within-group difference between positive and negative counts.
Return all tied pivots. Explore each reachable group once, without choosing a tie winner.
"""
from ramsey_37_pair_rotation_rule import build


def balanced_choices(rows, group):
    if group.bit_count() <= 1:
        return []
    options = []
    for i, row in enumerate(rows):
        if group & (1 << i):
            others = group ^ (1 << i)
            plus = others & row
            minus = others ^ plus
            gap = abs(plus.bit_count() - minus.bit_count())
            options.append((gap, i, plus, minus))
    best = min(gap for gap, *_ in options)
    return [option for option in options if option[0] == best]


def balance_groups(rows):
    pending = [(1 << len(rows)) - 1]
    groups = {}
    while pending:
        group = pending.pop()
        if group not in groups:
            groups[group] = balanced_choices(rows, group)
            for _, _, plus, minus in groups[group]:
                pending.extend((plus, minus))
    return groups


if __name__ == '__main__':
    n = 20
    full = (1 << n) - 1
    rows = [row & full for row in build()[:n]]
    groups = balance_groups(rows)
    for gap, i, plus, minus in groups[full]:
        print(f'pivot {i}: +{plus.bit_count()} / -{minus.bit_count()}, difference {gap}')
    print(f'{len(groups)} reachable groups; all minimum-difference ties retained')
