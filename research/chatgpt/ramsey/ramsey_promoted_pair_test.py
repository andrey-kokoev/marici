"""Reverse-test route closure on the reflected r37 catalogue. uv run --with networkx -- python <file>"""
from collections import Counter,defaultdict
from itertools import combinations,permutations
from pathlib import Path
import networkx as nx


def main():
    path=Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6'
    results=defaultdict(set); signed=defaultdict(dict); frames=0
    for record,line in enumerate(path.read_bytes().splitlines(),1):
        g=nx.from_graph6_bytes(line)
        for p in nx.isomorphism.GraphMatcher(g,g).isomorphisms_iter():
            if not all(v!=p[v] and p[p[v]]==v for v in g):continue
            pairs=[(v,p[v]) for v in g if v<p[v]]
            m=[[int(g.has_edge(i,j))+2*int(g.has_edge(i,jp)) for j,jp in pairs] for i,ip in pairs]
            for rowset in combinations(range(11),3):
                rest=set(range(11))-set(rowset)
                for rows in permutations(rowset):
                    vals={j:tuple(m[r][j] for r in rows) for j in rest}
                    masks={j:sum((1<<r) for r,v in enumerate(vals[j]) if v) for j in rest}
                    for z in rest:
                        cols=sorted(rest-{z},key=lambda j:(masks[j],j))
                        if [masks[j] for j in cols]!=[1,2,4,5,6,7,7] or any(3 in vals[j] for j in cols):continue
                        frames+=1;d,e=cols[-2:]; bits=[int(m[r][d]!=m[r][e]) for r in rows];minor=next(('ABC'[i] for i in range(3) if bits.count(bits[i])==1),'none')
                        degree=g.degree[pairs[z][0]]; profile=(tuple(m[r][z].bit_count() for r in rows),tuple(sorted([m[z][d].bit_count(),m[z][e].bit_count()])),m[z][z]!=0,degree)
                        results[minor].add(profile)
                        # Gauge-invariant key for ALL marked routes: switch row/col labels
                        # to lexicographically minimize incidence bits (incl. duplicate order).
                        keys=[]
                        for flips in range(8):
                            colbits=[]
                            for j in cols:
                                a=masks[j];b=sum(1<<i for i,s in enumerate(vals[j]) if s==2)^(flips&a)
                                colbits.append((a,min(b,b^a)))
                            keys.append(tuple(sorted(colbits)))
                        key=min(keys);signed[key].setdefault(profile,(record,rows,cols,z))
    print('labeled frames',frames,'profiles by exceptional row:');
    for k,v in sorted(results.items()):print(k,len(v),sorted(v))
    print('distinct signed seeds',len(signed),'profile counts',Counter(map(len,signed.values())))
    for key,ex in signed.items():
        for a,b in combinations(ex,2):
            if a[-1]!=b[-1] or a[-2]!=b[-2]:
                print('same signed seed',key,'different centers',a,ex[a],b,ex[b]);return

if __name__=='__main__':main()
