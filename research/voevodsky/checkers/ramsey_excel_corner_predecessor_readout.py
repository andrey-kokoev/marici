"""Do predecessor contact probes fill the four addresses? Direct build, no supplied supports."""
from ramsey_retention_slice import decode,check,CAT,D
from itertools import combinations
from collections import Counter
import json

def squares(a):
    # Both diagonals red, sides blue and recolorable. Start with unordered red edges.
    es=[(i,j) for i,j in combinations(range(len(a)),2) if a[i]>>j&1]
    for (i,h),(j,l) in combinations(es,2):
        c=(i,j,h,l)
        if len(set(c))==4 and all(not(a[x]>>y&1 or a[x]&a[y]) for x,y in zip(c,c[1:]+c[:1])):yield c

def run():
    res=[]
    for k,n in [(6,17),(7,22)]:
        stats=Counter();mult=Counter();example=None
        for row,line in enumerate((CAT/f'r3{k}_{n}.g6').read_text().splitlines(),1):
            a=decode(line)
            for c in squares(a):
                stats['squares']+=1;cls=[[] for _ in c];outside=[]
                for v in set(range(n))-set(c):
                    contacts=[i for i,x in enumerate(c) if a[v]>>x&1];assert len(contacts)<=1
                    if not contacts:outside.append(v);continue
                    cls[contacts[0]].append(v)
                mult[tuple(sorted(map(len,cls)))+(len(outside),)]+=1
                # Two overlapping side probes encode single contact; 00 is also returned by no contact.
                stats['ambiguous_00_squares']+=bool(outside and cls[0]);assert [(int(i in (1,2)),int(i in (2,3))) for i in range(4)]==[(0,0),(1,0),(1,1),(0,1)]
                winners=[]
                from itertools import permutations
                for perm in permutations(range(4)):
                    G=a.copy()+[0]*5
                    for t,h in enumerate(perm):
                        for x in (c[t],c[(t+1)%4],*cls[h],n+4):G[n+t]|=1<<x;G[x]|=1<<(n+t)
                    if check(G,(1<<(n+5))-1,3,k+1):winners.append(perm)
                stats['bijections_tested']+=24;stats['legal_bijections']+=len(winners);stats['exactly_two_cyclic']+=set(winners)=={tuple((t+h)%4 for t in range(4)) for h in (2,3)}
                if example is None:example=dict(record=row,square=c,classes=cls,no_contact=outside,legal_assignments=winners)
        print(k,stats,mult,example);res.append(dict(k=k,counts=stats,sizes=[dict(four_sizes_and_no_contact=p,squares=f) for p,f in sorted(mult.items())],example=example))
    dest=D.parent/'ramsey_excel_corner_predecessor_readout.json';text=json.dumps(res,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
