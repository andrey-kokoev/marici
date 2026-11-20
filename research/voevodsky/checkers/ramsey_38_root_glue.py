"""Try 1+4+22, first using the constructed (3,7) witness, then catalogue cores. No 27-vertex graph input. Maximal independent port neighborhoods suffice by monotonicity; repeats allowed."""
from pathlib import Path
from itertools import combinations
import json
H=Path(__file__).resolve().parents[1];cat=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6'
def solve(E):
 n=22;adj=[0]*n
 for i,j in E:adj[i]|=1<<j;adj[j]|=1<<i
 assert not any(adj[i]&adj[j] for i,j in E);sets=[]
 def visit(s,a):
    sets.append(s)
    while a:
        v=a&-a;a-=v;visit(s|v,a&~adj[v.bit_length()-1])
 visit(0,(1<<n)-1);assert max(map(int.bit_count,sets))<=6
 rows=[s for s in sets if all(s&(adj[i]|1<<i) for i in range(n))];dis={k:[] for k in (4,5,6)}
 for k,D in dis.items():
    faces=[s for s in sets if s.bit_count()==k];post=[sum(1<<j for j,t in enumerate(faces) if t>>i&1) for i in range(n)];U=(1<<len(faces))-1
    for s in rows:
        hit=0;a=s
        while a:
            v=a&-a;a-=v;hit|=post[v.bit_length()-1]
        D.append(U^hit)
 # Common unhit (8-t)-set among any t ports would make a minus eight-clique.
 B=[{j for j in range(i,len(rows)) if not dis[6][i]&dis[6][j]} for i in range(len(rows))];D=dis[5];F=dis[4]
 for i in range(len(rows)):
    for j in sorted(B[i]):
        rest=B[i]&B[j];ij=D[i]&D[j]
        for k in sorted(rest):
            if ij&D[k]:continue
            for l in sorted(rest&B[k]):
                if (ij | (D[i]&D[k]) | (D[j]&D[k])) & D[l] or F[i]&F[j]&F[k]&F[l]:continue
                choice=[rows[x] for x in (i,j,k,l)];links={(0,x) for x in range(1,5)}|{(a+5,b+5) for a,b in E}|{(z+1,v+5) for z,s in enumerate(choice) for v in range(n) if s>>v&1};assert not any(all(e in links for e in combinations(t,2)) for t in combinations(range(27),3));assert not any(all(e not in links for e in combinations(t,2)) for t in combinations(range(27),8));return dict(cross_plus=[[v+5 for v in range(n) if s>>v&1] for s in choice],plus_edges=sorted(links))
def inputs():
 yield 'previous_root_glue',json.loads((H/'results/ramsey_37_root_glue.json').read_text())['witness']['plus_edges']
 for idx,g in enumerate(cat.read_text().splitlines()):
    assert ord(g[0])-63==22;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);yield f'catalogue_{idx}',[(i,j) for j in range(22) for i in range(j) if bits[j*(j-1)//2+i]=='1']
if __name__=='__main__':
    tested=[];w=None
    for name,E in inputs():
        tested.append(name);w=solve(E)
        if w:break
    out=dict(tested=tested,witness=w);(H/'results/ramsey_38_root_glue.json').write_text(json.dumps(out,indent=2)+'\n');print(len(tested),tested[-1],None if not w else w['cross_plus'])
