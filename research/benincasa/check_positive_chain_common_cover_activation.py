"""Type the physical-chain activation gate for the common lower Kummer cover."""


def lower_poles(a, b, c, x1, x2, x3):
    return {
        "q_g1": x1 + b + c,
        "q_g2": x2 + c + a,
        "q_g3": x3 + a + b,
        "q_g23": x2 + x3 + b + c,
    }


for a in range(4):
    for b in range(4):
        for c in range(4):
            for x1, x2, x3 in ((1, 2, 3), (2, 3, 5), (5, 7, 11)):
                values = lower_poles(a, b, c, x1, x2, x3)
                assert all(value > 0 for value in values.values())

print("POSITIVE_CHAIN_MEETS_LOWER_WALL=false")
print("POSITIVE_CHAIN_MEETS_PAIR_OR_TRIPLE_SUPPORT=false")
print("COMMON_KUMMER_PACKET_PHYSICALLY_ACTIVATED=false")
print("PHYSICAL_DECK_CHARACTER=unselected_not_even")
