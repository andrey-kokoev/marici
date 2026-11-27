"""Six width-seven midpoints: compare literal path attachments and inherited swaps in a common frame."""
from itertools import combinations,permutations
import json
from pathlib import Path

def unit(i):return tuple(int(h==i) for h in range(4))
def grow(x,j):return tuple(n+(h==j) for h,n in enumerate(x))
def reds(x):return (1+x[0],3+sum(x[:2]),5+sum(x[:3]))
def moves(x):return {(i,j) for i in range(4) for j in range(4) if abs(i-j)==1 and x[i]}
def step(x,i,j):return tuple(n-(k==i)+(k==j) for k,n in enumerate(x))
def graph_probe(r,h):
    # Same final path colors; probe 9 red to 8 and h only (all other pairs blue).
    E={tuple(sorted(e)) for e in [*((v,v+1) for v in range(1,7)),*((v,8) for v in r),(8,9),(h,9)]}
    return not any(all(e in E for e in combinations(s,2)) for s in combinations(range(1,10),3)) and not any(all(e not in E for e in combinations(s,2)) for s in combinations(range(1,10),7))

def run():
    out=[]
    for i,j in combinations(range(4),2):
        x=grow(unit(i),j);assert x==grow(unit(j),i);probes=[];inherited=[]
        for old,new in [(i,j),(j,i)]:
            p=unit(old);child=grow(p,new);probes.append([h for h in range(1,8) if graph_probe(reds(child),h)])
            # A child swap lifts across the SAME growth map iff it acts on a legal parent row.
            m={e for e in moves(child) if e in moves(p) and step(child,*e)==grow(step(p,*e),new)};inherited.append(m)
        a,b=inherited;assert probes[0]==probes[1] and not a&b and a|b==moves(x)
        # Change frame, carrying the path, row and directed move labels, not just the row.
        for f in permutations(range(4)):
            edges={(f[u],f[v]) for u,v in moves((1,1,1,1))};occupied={f[i],f[j]};both={e for e in edges if e[0] in occupied};assert both=={(f[u],f[v]) for u,v in a|b}
        out.append(dict(gaps=[i,j],row=reds(x),legal_final_probes=probes[0],via_i_then_j=sorted(a),via_j_then_i=sorted(b)))
    print([(q['row'],len(q['via_i_then_j']),len(q['via_j_then_i'])) for q in out]);dest=Path(__file__).resolve().parents[1]/'results/ramsey_gap_midpoint_transport.json';s=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
