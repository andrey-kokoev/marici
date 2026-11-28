"""Contacts with old representatives as signatures for constructing new role neighborhoods."""
from ramsey_seven_role_coexist import roots_and_lines,pairings,decode,D
from itertools import combinations,product
from collections import Counter,defaultdict
import json

def audit():
    roots,lines=roots_and_lines();hist=defaultdict(Counter);samples={};total=0
    for idx,v in roots:
        a=decode(lines[idx-1].decode());ns=[i for i in range(27) if a[v]>>i&1];outside=defaultdict(list)
        for i in set(range(27))-{v}-set(ns):outside[tuple(sorted(j for j in ns if a[i]>>j&1))].append(i)
        for six in combinations(ns,6):
            for pairs in pairings(list(six)):
                bits=list(product(range(2),repeat=3));ls=[outside[tuple(sorted(q))] for q in product(*pairs)];present=[j for j,s in enumerate(ls) if s];
                if len(present)!=7:continue
                assert all(len(ls[j])==1 for j in present);total+=1;miss=next(j for j in range(8) if j not in present);faces={p[b]:sum(1<<j for j in range(8) if bits[j][k]==b) for k,p in enumerate(pairs) for b in (0,1)};want={''.join(s):sum(1<<j for j in present if all(x=='*' or int(x)==y for x,y in zip(s,bits[j]))) for s in product('01*',repeat=3) if s.count('*')<=1};target=Counter(want.values());rest=set(range(27))-set(six)
                for own in (False,True):
                    mode='self_bit' if own else 'old_red';obs=[sum(1<<j for j in present if a[i]>>ls[j][0]&1 or (own and i==ls[j][0])) for i in range(27)];assert all(obs[i]==mask&~(1<<miss) for i,mask in faces.items());available=Counter(obs[i] for i in rest);hits=sum((available&target).values());hist[mode][hits]+=1
                    known=[i for i,mask in faces.items() if mask>>miss&1];assert len(known)==3
                    samples.setdefault(mode,dict(record=idx,root=v,missing_bits=bits[miss],column_pairs=pairs,faces_for_missing_port=known,unchanged_corner_or_edge_columns=hits,deficits={str(mask):n for mask,n in (target-available).items()}))
    assert total==161;out=dict(frames=total,corner_edge_match_histograms=hist,examples=samples);print(out);(D.parent/'ramsey_seven_contact_lift.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
