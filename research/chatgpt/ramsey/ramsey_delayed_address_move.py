"""Exhibit a surviving path and test every last move up to isomorphism of its prefix.
Uses the external complete catalogue of 191 (3,7;22) graphs for the upper bound.
"""
from pathlib import Path
from ramsey_37_pair_rotation_rule import build
from pauli_realization_audit import triangle_free, decode_graph6


def moves(rows):
    safe=[0]
    for i,row in enumerate(rows):safe += [p|(1<<i) for p in safe if not p&row]
    assert triangle_free(rows) and all(p.bit_count()<7 for p in safe)
    six=[p for p in safe if p.bit_count()==6]
    legal=[p for p in safe if all(p&s for s in six)]
    return len(safe),len(six),legal

if __name__=='__main__':
    g=build()
    for n in range(23):
        mask=(1<<n)-1
        safe,six,legal=moves([r&mask for r in g[:n]])
        if n<22:assert g[n]&mask in legal
        else:assert not legal
        if n>=19:print('prefix',n,'triangle-safe',safe,'six-sets',six,'legal next moves',len(legal))
    cat=Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6'
    lines=cat.read_text().splitlines();assert len(lines)==191 and len(set(lines))==191
    total=0
    for line in lines:
        rows=decode_graph6(line);assert len(rows)==22
        safe,_,legal=moves(rows);assert not legal;total+=safe
    print('catalogue records',len(lines),'triangle-safe last moves',total,'surviving moves',0)
