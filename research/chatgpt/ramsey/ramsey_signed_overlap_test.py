"""Reverse-test the signed common-row rule on every reflected catalogue frame.
Run: uv run --with networkx -- python research/chatgpt/ramsey/ramsey_signed_overlap_test.py
Mask bits 1,2 mean parallel,crossed. A shared row forbids the XOR of
its two incidence phases, because that column edge would close a triangle.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import networkx as nx


def test():
    path = Path(__file__).with_name('pauli-realization-catalogues') / 'r37_22.g6'
    totals = Counter(); best = None; best_data = None; center_min = 21
    for record, line in enumerate(path.read_bytes().splitlines(), 1):
        g = nx.from_graph6_bytes(line); hit = False
        for p in nx.isomorphism.GraphMatcher(g, g).isomorphisms_iter():
            if not all(v != p[v] and p[p[v]] == v for v in g): continue
            hit = True; totals['reflections'] += 1
            pairs = [(v,p[v]) for v in g if v < p[v]]
            m = [[int(g.has_edge(i,j)) + 2*int(g.has_edge(i,jp)) for j,jp in pairs] for i,ip in pairs]
            for rows in combinations(range(11),3):
                rest = sorted(set(range(11))-set(rows)); info = {}
                for a,b in combinations(rest,2):
                    forbidden = 0
                    for r in rows:
                        for x,y in ((0,0),(1,0),(0,1),(1,1)):
                            if m[r][a] & (1<<x) and m[r][b] & (1<<y): forbidden |= 1<<(x^y)
                    assert not forbidden & m[a][b]
                    # No overlap means no predicted edge, not both phases.
                    pred = 3^forbidden if forbidden else 0
                    info[a,b] = pred,m[a][b]
                for center in rest:
                    cols=[v for v in rest if v != center]
                    errors=[(a,b,s,t) for (a,b),(s,t) in info.items() if center not in (a,b) and s!=t]
                    cost=len(errors); totals['frames']+=1; totals['exact']+=not cost
                    # Variant: allow the distinguished center as a fourth witness.
                    center_errors=0
                    for a,b in combinations(cols,2):
                        shared=any(m[r][a] and m[r][b] for r in rows)
                        forbid=(3^info[a,b][0]) if shared else 0
                        for x,y in ((0,0),(0,1),(1,0),(1,1)):
                            if m[center][a] & (1<<x) and m[center][b] & (1<<y): forbid |= 1<<(x^y)
                        center_errors+=((3^forbid if forbid else 0)!=m[a][b])
                    center_min=min(center_min,center_errors); totals['center_variant_exact']+=not center_errors
                    # Prefer more genuinely predicted connections among tied frames.
                    score=(cost,-sum(bool(s) and s==t for k,(s,t) in info.items() if center not in k))
                    if best is None or score<best:
                        best=score; best_data=dict(record=record,pairs=pairs,rows=rows,columns=cols,center=center,
                                incidences=[[m[r][c] for c in cols] for r in rows],exceptions=errors,
                                correct_nonempty=-score[1])
        totals['records_with_reflection']+=hit
    print(dict(totals)); print('best:',best_data); print('minimum errors with center witness:',center_min)

if __name__=='__main__': test()
