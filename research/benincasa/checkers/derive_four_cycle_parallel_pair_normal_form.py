"""Derive the compactified local normal form of complementary C4 denominators."""
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-ofpt-packet.json"
OUT = ROOT / "research/benincasa/results/four-cycle-parallel-pair-normal-form.json"


def sites(label):
    if not label.startswith("g_"):
        return None
    return frozenset(int(x) for x in label.removeprefix("g_"))


def edge_normal(site_set):
    zero = {x - 1 for x in site_set}
    return tuple(
        int((i in zero) != (((i + 1) % 4) in zero))
        for i in range(4)
    )


def x_vector(site_set):
    return tuple(int(i in site_set) for i in range(1, 5))


def primitive_up_to_sign(v):
    for x in v:
        if x:
            return tuple(v) if x > 0 else tuple(-y for y in v)
    raise AssertionError("zero letter")


packet = json.loads(SOURCE.read_text())
terms = packet["four_cycle"]["terms"]
common = ["g_1", "g_2", "g_3", "g_4"]

pair_occurrences = Counter()
ordered_pivots = Counter()
identities = []

for term_id, extra in enumerate(terms):
    labels = common + extra
    groups = defaultdict(list)
    for label in labels:
        s = sites(label)
        if s is not None:
            groups[edge_normal(s)].append(label)
    for labels_at_normal in groups.values():
        if len(labels_at_normal) != 2:
            continue
        left, right = sorted(labels_at_normal)
        sl, sr = sites(left), sites(right)
        assert sl.isdisjoint(sr) and sl | sr == frozenset({1, 2, 3, 4})
        pair = tuple(sorted(("".join(map(str, sorted(sl))), "".join(map(str, sorted(sr))))))
        pair_occurrences["|".join(pair)] += 1

        xl, xr = x_vector(sl), x_vector(sr)
        delta_lr = tuple(b - a for a, b in zip(xl, xr))
        delta_rl = tuple(-x for x in delta_lr)
        ordered_pivots[str(primitive_up_to_sign(delta_lr))] += 2

        # Homogenized forms are Q_l=L+s X_l and Q_r=L+s X_r.
        # On Q_l=0, L=-s X_l, hence Q_r=s(X_r-X_l), and conversely.
        identities.append({
            "term": term_id,
            "labels": [left, right],
            "common_infinity_normal": list(edge_normal(sl)),
            "on_left_residue": {"partner": right, "restriction": f"s*({delta_lr})"},
            "on_right_residue": {"partner": left, "restriction": f"s*({delta_rl})"},
        })

assert len(identities) == 36
assert sum(pair_occurrences.values()) == 36
assert sum(ordered_pivots.values()) == 72
assert set(pair_occurrences) == {"1|234", "134|2", "124|3", "123|4", "12|34", "14|23"}

result = {
    "schema": "marici.benincasa.four_cycle_parallel_pair_normal_form.v1",
    "duplicate_pair_occurrences": 36,
    "ordered_parallel_residue_pivots": 72,
    "complement_partition_census": dict(sorted(pair_occurrences.items())),
    "signed_energy_letter_count_up_to_sign": len(ordered_pivots),
    "signed_energy_letters_up_to_sign": dict(sorted(ordered_pivots.items())),
    "local_identity": "Q_T|_{Q_S=0}=s*(X_T-X_S), for T=S^c",
    "generic_coefficient_type": "infinity Cartier/Tate factor times rank-one Kummer letter (X_T-X_S)^(-1)",
    "enhanced_support": "X_T-X_S=0, equivalently 2 X_S-E=0",
    "new_carrier_datum": False,
    "identities": identities,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "pair_census": result["complement_partition_census"],
    "letters": result["signed_energy_letters_up_to_sign"],
}))
