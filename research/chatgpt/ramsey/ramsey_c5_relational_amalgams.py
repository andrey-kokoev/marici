"""Join two induced C5 views at any compatible two-role interface. Compare outputs only after generation. uv run --with igraph python <file>"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import igraph as ig

def canon(edges):
    g=ig.Graph(n=8,edges=list(edges));return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(g.canonical_permutation()).get_edgelist()))

def main():
    outputs=set();pairs=list(combinations(range(8),2));red=lambda i,j:(i-j)%5 in (1,4)
    for gap in (1,2): # C5 is transitive on ordered pairs of each color
        first=list(range(5));it=iter((5,6,7));second=[i if i in (0,gap) else next(it) for i in first];fixed={}
        for copy in (first,second):
            for i,j in combinations(first,2):
                e=tuple(sorted((copy[i],copy[j])));assert fixed.get(e,red(i,j))==red(i,j);fixed[e]=red(i,j)
        holes=[e for e in pairs if e not in fixed];assert len(holes)==9
        valid=Counter()
        for mask in range(1<<9):
            E={e for e,x in fixed.items() if x}|{e for i,e in enumerate(holes) if mask>>i&1}
            if any(all(e in E for e in combinations(t,2)) for t in combinations(range(8),3)):continue
            if any(all(e not in E for e in combinations(t,2)) for t in combinations(range(8),4)):continue
            valid[canon(E)]+=1
        outputs.update(valid);print('shared', 'red' if gap==1 else 'blue','valid fillings',sum(valid.values()),'classes',len(valid),'class multiplicities',sorted(valid.values()))
    ref=set()
    for line in Path(__file__).with_name('pauli-realization-catalogues').joinpath('r34_8.g6').read_bytes().splitlines():
        assert line[0]==71;bits=''.join(f'{x-63:06b}' for x in line[1:]);ref.add(canon((i,j) for i,j in pairs if bits[j*(j-1)//2+i]=='1'))
    print('output classes',len(outputs),'catalogue classes',len(ref),'matched',len(outputs&ref));assert outputs<=ref
if __name__=='__main__':main()
