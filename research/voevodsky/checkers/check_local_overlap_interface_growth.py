"""Independent overlap experiment: support-union rewrite versus singleton probes.

This is our synthetic labelled-contact calculus. It uses no Nima objects.
"""
from itertools import combinations
from pathlib import Path
import json

def states(labels):
    return [frozenset(xs) for k in range(len(labels)+1) for xs in combinations(labels,k)]

def local_add(s,label):return s|{label}
def join(a,b):return a|b
def overlap(a,context):return len(a & context)

def signature(s,labels):return tuple(overlap(s,frozenset((label,))) for label in labels)

sizes=[]
for n in range(9):
    labels=tuple(range(n));ss=states(labels)
    assert len(ss)==2**n
    # Every pair of states has distinct future singleton-overlap answers.
    assert len({signature(s,labels) for s in ss})==len(ss)
    for a in ss:
        for x in labels:
            assert local_add(a,x)==join(a,frozenset((x,)))
        for b in ss:
            assert overlap(join(a,b),frozenset(labels))==len(a|b)
    sizes.append({'labels':n,'minimal_states':len(ss)})

# Fixed two-label interface can collapse all histories to four supports.
assert len(states((0,1)))==4
# Cardinality alone loses continuation information even at two labels.
a=frozenset((0,));b=frozenset((1,))
assert len(a)==len(b) and overlap(a,frozenset((0,)))!=overlap(b,frozenset((0,)))
report={'passed':True,'local_update':'SUPPORT(S)--CONTACT(label) -> SUPPORT(S union {label})','join':'set union; finite-label support congruence','fixed_two_labels':'four sufficient and singleton-distinct states','growing_labels':'2^n singleton-distinct states for n possible labels','sizes':sizes,'qualification':'Labels are parameters; a finite agent alphabet requires explicit label encoding. This is a synthetic overlap calculus, not Nima E/E_B or a complete port-level interaction net.'}
out=Path(__file__).resolve().parents[1]/'results/local-overlap-interface-growth.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
