"""Transport the residual deck-odd H2 classes under the labelled C4 action."""
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-residual-cyclic-transport.json"


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def shift_label(label):
    if label.startswith("G_minus_e"):
        i, j = map(int, re.findall(r"\d", label))
        return f"G_minus_e{i % 4 + 1}{j % 4 + 1}"
    if label.startswith("g_"):
        shifted = sorted(int(x) % 4 + 1 for x in re.findall(r"\d", label))
        return "g_" + "".join(map(str, shifted))
    raise ValueError(label)


def canon_group(group):
    return tuple(sorted(group))


def shift_group(group):
    return canon_group(shift_label(x) for x in group)


def permutation_sign(values):
    inversions = sum(values[i] > values[j] for i in range(len(values))
                     for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def columns(matrix):
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))] if matrix and matrix[0] else []


source = json.loads(SOURCE.read_text())
terms = {x["term_index"]: x for x in source["term_packets"]}
active = {i: x for i, x in terms.items() if x["deck_minus"]["H2"] == 1}


def mark_set(term):
    groups = set()
    for edge in term["deck_minus"]["C1_basis"]:
        groups.update(canon_group(x) for x in edge)
    for triple in term["deck_minus"]["C2_basis"]:
        groups.update(canon_group(x) for x in triple)
    return frozenset(groups)


by_marks = {mark_set(term): index for index, term in terms.items()}


def representative(term):
    basis = [tuple(canon_group(g) for g in triple)
             for triple in term["deck_minus"]["C2_basis"]]
    vector = [0] * len(basis)
    rep = term["deck_minus"]["representatives"][0]
    for item in rep:
        triple = tuple(canon_group(g) for g in item["triple"])
        vector[basis.index(triple)] = item["coefficient"]
    return vector


transitions = []
for source_index, source_term in sorted(active.items()):
    target_key = frozenset(shift_group(g) for g in mark_set(source_term))
    target_index = by_marks[target_key]
    assert target_index in active
    target_term = active[target_index]
    source_basis = [tuple(canon_group(g) for g in triple)
                    for triple in source_term["deck_minus"]["C2_basis"]]
    target_basis = [tuple(canon_group(g) for g in triple)
                    for triple in target_term["deck_minus"]["C2_basis"]]
    target_marks = sorted(mark_set(target_term))
    target_position = {g: i for i, g in enumerate(target_marks)}
    transported = [0] * len(target_basis)
    for coefficient, triple in zip(representative(source_term), source_basis):
        if not coefficient:
            continue
        mapped = [shift_group(g) for g in triple]
        positions = [target_position[g] for g in mapped]
        sign = permutation_sign(positions)
        ordered = tuple(g for _, g in sorted(zip(positions, mapped)))
        transported[target_basis.index(ordered)] += sign * coefficient
    target_rep = representative(target_term)
    image = columns(target_term["deck_minus"]["d1"])
    base_rank = rank(image)
    scalar = next((s for s in (-1, 1)
                   if rank(image + [[a - s * b for a, b in zip(transported, target_rep)]])
                   == base_rank), None)
    assert scalar is not None
    d2 = target_term["deck_minus"]["d2"]
    assert all(sum(row[j] * transported[j] for j in range(len(transported))) == 0
               for row in d2)
    transitions.append({"source_term": source_index, "target_term": target_index,
                        "cohomology_scalar": scalar,
                        "transported_representative": transported})

orbits = []
seen = set()
by_source = {x["source_term"]: x for x in transitions}
for start in sorted(active):
    if start in seen:
        continue
    orbit, scalars, current = [], [], start
    while current not in orbit:
        orbit.append(current)
        seen.add(current)
        step = by_source[current]
        scalars.append(step["cohomology_scalar"])
        current = step["target_term"]
    assert current == start and len(orbit) == 4
    product = 1
    for scalar in scalars:
        product *= scalar
    assert product == 1
    orbits.append({"terms": orbit, "transition_scalars": scalars,
                   "cyclic_product": product})

packet = {
    "schema": "marici.benincasa.four_site_qg_residual_cyclic_transport.v1",
    "residual_dimension": len(active),
    "orbits": orbits,
    "transitions": transitions,
    "conclusion": "The residual deck-odd H2 is two free labelled C4 orbits; every transported representative agrees modulo the exact pair boundary and each four-step product is +1.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"orbits": orbits}))
