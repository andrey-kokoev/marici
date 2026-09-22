"""Exact convex-height and projection regressions on typed Boolean paths."""
from pathlib import Path
from itertools import permutations, product
from math import factorial
import importlib.util
import json

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('lift',HERE/'check_controlled_ideal_factorization_lift.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)


def le(a,b):return a & b==a


def main():
    vertices=range(16)
    # A scrambled injective code makes convex closure nontrivial.
    code={v:((5*v+3)%16)+1 for v in vertices}
    packets={}
    for H in range(1,17):
        seed={v for v in vertices if code[v]<=H}
        packet={v for a in seed for b in seed if le(a,b)
                for v in vertices if le(a,v) and le(v,b)}
        assert seed<=packet
        if H>1:assert packets[H-1]<=packet
        packets[H]=packet
    height={v:min(H for H in packets if v in packets[H]) for v in vertices}
    h=lambda a,b:max(height[a],height[b])
    triples=projections=0
    for a,b,c in product(vertices,repeat=3):
        if not (le(a,b) and le(b,c)):continue
        assert height[b]<=h(a,c)
        assert h(a,c)<=max(h(a,b),h(b,c))
        assert max(h(a,b),h(b,c))==h(a,c)
        assert h(a,c)<=h(a,b)*h(b,c)
        triples+=1
        for H,V in packets.items():
            assert (a in V and c in V)==(a in V and b in V and c in V)
            projections+=1
    paths=outputs=0
    for start,end in product(vertices,repeat=2):
        if not le(start,end):continue
        items=tuple(j for j in range(4) if ((end^start)>>j)&1)
        for word in permutations(items):
            for marks in product((0,1),repeat=len(word)):
                R=g.section(g.bar_column(start,{(word,marks):1}))
                for (newword,newmarks),coefficient in R.items():
                    state=start
                    assert len(newword)==len(word)
                    for j in newword:
                        nxt=state|(1<<j)
                        assert h(state,nxt)<=h(start,end)
                        state=nxt
                    assert state==end
                    assert sum(newmarks)==sum(marks)
                    outputs+=1
                paths+=1
    for n,m in product(range(12),repeat=2):
        assert factorial(n+m)<=2**(n+m)*factorial(n)*factorial(m)
    for H,V in packets.items():
        max_length=max((b^a).bit_count() for a in V for b in V if le(a,b))
        depth=max(1,max_length//2)
        assert 2*(depth+1)>max_length
    result={'passed':True,'convex_composition_triples':triples,
        'multiplicative_projection_checks':projections,'terminal_source_paths':paths,
        'terminal_output_height_checks':outputs,
        'scope':'Finite typed Boolean regressions. General bounds use local finiteness, convex closure and the existing Gamma-weighted source estimates; height is charged once per total corner.'}
    out=HERE.parent/'results/convex-source-height.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
