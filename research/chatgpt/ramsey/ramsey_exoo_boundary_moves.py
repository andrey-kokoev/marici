"""Exact move graph and commuting Boolean faces on the input-derived exceptional star."""
from itertools import combinations
from pathlib import Path
from collections import Counter,deque
from exoo39_symbolic_relations import edges
import json
D=Path(__file__).parent;E=edges();H=[sum(1<<j for j in range(39) if tuple(sorted((i,j))) in E) for i in range(39)];A=H[22];mask=A|1<<22;V=[i for i in range(39) if not mask>>i&1];defect=sum(1<<i for i in range(39) if A>>i&1 and H[i].bit_count()<9);center,=[i for i in V if H[i]&A==defect];I=[0]
for i,h in enumerate(H):
    if i!=center:I.extend([s|1<<i for s in I if not s&h]);
T=[s for s in I if s.bit_count()==9];assert max(s.bit_count() for s in I)==9;B={s for s in I if s&mask==defect and all(s&t for t in T)};old=json.loads((D/'ramsey_exoo_chart22_words.json').read_text());F=old['probes'];assert {''.join(str(s>>v&1) for v in F) for s in B}==set(old['words']) and len(B)==len(old['words']);nb={s:{s^1<<v for v in V if s^1<<v in B} for s in B};ex={s:{t for t in B if t.bit_count()==s.bit_count() and (s^t).bit_count()==2} for s in B};
def distances(s,N):
    d={s:0};q=deque([s]);
    while q:
        u=q.popleft()
        for t in N[u]-d.keys():d[t]=d[u]+1;q.append(t)
    return d

def comps(N):
    todo=set(N);out=[]
    while todo:
        d=distances(min(todo),N);todo-=d.keys();out.append(sorted(d))
    return out
cs=comps(nb);ds=Counter();gap=Counter();worst=None;diam=0
for s in B:
    for t,d in distances(s,nb).items():
        if s>=t:continue
        diam=max(d,diam);g=d-(s^t).bit_count();gap[g]+=1
        if worst is None or g>worst[0]:worst=(g,s,t,d)
# Convexity in subset inclusion: bottom hits the nines; top is independent. Every intermediate subset is legal. Thus comparable pairs count each occupied axis-aligned face exactly once.
faces=Counter((s^t).bit_count() for s in B for t in B if s&t==s);deg=Counter(map(len,nb.values()));swap=comps(ex);sm=H[center];word=lambda s:''.join(str(s>>v&1) for v in F);moves=lambda s:sorted((s^t).bit_length()-1 for t in nb[s]);holes=next(((s,a,b) for s in sorted(B) for a,b in combinations(moves(s),2) if s^(1<<a)^(1<<b) not in B),None);r=dict(center=center,sites=len(B),component_sizes=list(map(len,cs)),degrees=deg,edges=sum(map(len,nb.values()))//2,diameter=diam,graph_minus_hamming=gap,largest_detour=dict(source=word(worst[1]),target=word(worst[2]),length=worst[3]),faces=faces,missing_square=[word(holes[0]),*holes[1:]] if holes else None,seed_moves=moves(sm),exchange_components=[(c[0].bit_count(),len(c)) for c in swap]);# Every used cube bit defines an intrinsic distance cut at any edge flipping it. Distinct cuts force distinct axes in any isometric cube embedding.
used=sorted({v for s in B for v in moves(s)});cuts={min(tuple(sorted(s for s in B if s>>v&1)),tuple(sorted(s for s in B if not s>>v&1))) for v in used};assert gap.keys()=={0} and len(cuts)==len(used)==14;r.update(isometric_dimension=len(cuts),missing_square_old_red_edge=tuple(sorted(holes[1:])) in E);print(r);(D/'ramsey_exoo_boundary_moves.json').write_text(json.dumps(r,indent=2)+'\n')
