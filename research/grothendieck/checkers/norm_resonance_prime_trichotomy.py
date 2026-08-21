cases = {
    "identity": (1, 1),
    "C4->C2": (2, 2),
    "A4->C3": (4, 6),
    "A4->1": (12, 6),
}
primes = (2, 3, 5, 7)

table = {}
for name, (degree, resonance) in cases.items():
    rows = {}
    for p in primes:
        norm_bad = degree % p == 0
        resonance_bad = resonance % p == 0
        assert not (norm_bad and not resonance_bad)
        if norm_bad:
            regime = "norm-and-resonance-bad"
        elif resonance_bad:
            regime = "resonance-only-bad"
        else:
            regime = "good"
        rows[p] = regime
    table[name] = rows

assert table["A4->C3"][2] == "norm-and-resonance-bad"
assert table["A4->C3"][3] == "resonance-only-bad"
assert table["A4->C3"][5] == "good"

print({"prime_regimes": table, "impossible_norm_only_cell": "empty", "checks": "pass"})
