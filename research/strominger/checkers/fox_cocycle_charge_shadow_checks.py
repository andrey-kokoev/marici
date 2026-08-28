#!/usr/bin/env python3
"""Falsify scalar-charge sufficiency using exact free-group Fox calculus."""

from __future__ import annotations

import json


def reduce_word(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def wmul(left, right):
    return reduce_word(left + right)


def gr_add(*polys):
    out = {}
    for poly in polys:
        for word, coefficient in poly.items():
            out[word] = out.get(word, 0) + coefficient
            if out[word] == 0:
                del out[word]
    return out


def gr_scale(poly, scalar):
    return {word: scalar * coefficient for word, coefficient in poly.items() if scalar * coefficient}


def gr_mul(left, right):
    out = {}
    for lw, lc in left.items():
        for rw, rc in right.items():
            word = wmul(lw, rw)
            out[word] = out.get(word, 0) + lc * rc
            if out[word] == 0:
                del out[word]
    return out


def monomial(word, coefficient=1):
    word = reduce_word(word)
    return {} if coefficient == 0 else {word: coefficient}


def fox(word, generator):
    prefix = ()
    out = {}
    for letter in word:
        if letter == generator:
            out = gr_add(out, monomial(prefix))
        elif letter == -generator:
            out = gr_add(out, monomial(wmul(prefix, (letter,)), -1))
        prefix = wmul(prefix, (letter,))
    return out


def augmentation(poly):
    return sum(poly.values())


def abelianization(word):
    return tuple(sum(1 if letter == g else -1 if letter == -g else 0 for letter in word) for g in (1, 2))


def fundamental_identity(word):
    lhs = {}
    for generator in (1, 2):
        generator_minus_one = gr_add(monomial((generator,)), monomial((), -1))
        lhs = gr_add(lhs, gr_mul(fox(word, generator), generator_minus_one))
    rhs = gr_add(monomial(word), monomial((), -1))
    return lhs == rhs


def encoded(poly):
    return [
        {"word": list(word), "coefficient": coefficient}
        for word, coefficient in sorted(poly.items(), key=lambda item: (len(item[0]), item[0]))
    ]


commutator = (1, 2, -1, -2)
words = {
    "atomic_letter": (1,),
    "commutator_decorated": reduce_word((1,) + commutator),
    "left_decorated": reduce_word(commutator + (1,)),
}
records = {}
for name, word in words.items():
    dx = fox(word, 1)
    dy = fox(word, 2)
    records[name] = {
        "word": list(word),
        "abelian_charge": list(abelianization(word)),
        "fox_x": encoded(dx),
        "fox_y": encoded(dy),
        "fox_augmentation": [augmentation(dx), augmentation(dy)],
        "fundamental_identity": fundamental_identity(word),
    }

base = records["atomic_letter"]
right = records["commutator_decorated"]
left = records["left_decorated"]
same_charge = base["abelian_charge"] == right["abelian_charge"] == left["abelian_charge"]
different_fox = (
    (base["fox_x"], base["fox_y"]) != (right["fox_x"], right["fox_y"])
    and (base["fox_x"], base["fox_y"]) != (left["fox_x"], left["fox_y"])
    and (right["fox_x"], right["fox_y"]) != (left["fox_x"], left["fox_y"])
)

gates = {
    "all_words_have_identical_abelian_charge": same_charge,
    "all_words_have_distinct_fox_cocycles": different_fox,
    "fox_augmentation_recovers_charge": all(r["fox_augmentation"] == r["abelian_charge"] for r in records.values()),
    "fox_fundamental_identity_holds": all(r["fundamental_identity"] for r in records.values()),
    "scalar_response_aliases_the_hostile_pair": same_charge,
    "cocycle_separates_what_scalar_charge_aliases": same_charge and different_fox,
}
payload = {
    "schema": "marici.strominger.fox_cocycle_charge_shadow_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "integer_charge_is_the_augmentation_shadow_of_the_fox_cocycle",
    "records": records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The scalar additive charge is exact only on the restricted pure-power "
        "grammar. In the full free-group grammar, three words with charge (1,0) "
        "have distinct Fox cocycles. Augmentation maps each cocycle back to the "
        "same charge. The source-complete compositional datum is therefore the "
        "crossed Fox cocycle; integer charge is its abelian shadow."
    ),
}
print(json.dumps(payload, indent=2))
