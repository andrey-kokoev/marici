"""Use immediate witnessed swaps as table contact. No use of graph labels or fitted subset."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json,sys
D=Path(__file__).resolve().parents[1]/'results';P=D/'ramsey_excel_swap_contact_protocol.json';R=D/'ramsey_excel_swap_contact_transfer.json'
rule=dict(source='Use every distinct separated triple of the new width once, including rows outside all two-swap placements. Contact = one witnessed adjacent RB/BR swap to a corner of a terminal-reaching square. Do not count the four focal rows as exterior.',comparison='Test exclusivity, whether all four contact classes are nonempty, and whether their four sizes match any predecessor contact profile up to permutation. Compare zero-contact counts separately. Surplus zero rows allowed for the positive-class test, but no repetition, removal or merging of positive rows. Count two-swap path cycles independently of graph data.')
def run():
    assert json.loads(P.read_text())==rule;graph=json.loads((D/'ramsey_excel_corner_predecessor_readout.json').read_text());out=[]
    for w in (7,8):
        U={frozenset(c) for c in combinations(range(1,w+1),3) if min(c[1]-c[0],c[2]-c[1])>=2};adj={r:{s for s in U if len(r^s)==2 and max(r^s)-min(r^s)==1} for r in U};faces=set()
        for r,N in adj.items():
            for s,t in combinations(N,2):
                if (r^s)&(r^t):continue
                v=r^s^t;F=frozenset([r,s,t,v]);
                if v in adj[s]&adj[t] and any(w in x for x in F):faces.add(F)
        hist=Counter();cases=[];gprofiles=[tuple(e['four_sizes_and_no_contact']) for e in graph[w-7]['sizes']];stats=Counter()
        for f in sorted(faces,key=lambda f:sorted(sorted(r) for r in f)):
            c=sorted(f,key=sorted);hits=[frozenset(i for i,r in enumerate(c) if r in adj[v]) for v in U-f];multiple=sum(len(h)>1 for h in hits);sizes=sorted(hits.count({j}) for j in range(4));none=hits.count(frozenset());hist[tuple(sizes+[none])]+=1;stats['exclusive']+=not multiple;stats['all_four']+=all(sizes);stats['positive_profile_match']+=not multiple and any(list(p[:4])==sizes for p in gprofiles);cases.append(dict(corners=list(map(sorted,c)),multiple=multiple,sizes=sizes,no_contact=none))
        print(w,hist,stats);out.append(dict(width=w,rows=len(U),stats=stats,cases=cases))
    text=json.dumps(out,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        s=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==s;P.write_text(s)
    else:run()
