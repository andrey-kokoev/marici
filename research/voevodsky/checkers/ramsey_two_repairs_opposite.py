"""Opposite-axis formula; compare exact labeled outputs with the independent quartet census."""
from itertools import combinations,permutations,product
from collections import Counter
from hashlib import sha256
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D
import json


def run():
    totals=Counter();keys=set();examples={};profiles=Counter()
    for sq,_,cycles in charts():
        U=set().union(*sq);f,=set.intersection(*map(set,sq));mov=U-{f};W=set(range(1,11))-U
        for cyc in cycles:
            for x,z in combinations(sorted(mov),2):
                if any({x,z}<=set(r) for r in sq):continue
                u,v=x-1,z+1;edge=(u,v);Y=mov-{x,z}
                if not {u,v}<=W or edge in cyc or any(abs(y-i)==1 for y in Y for i in edge):continue
                K=W-{u,v};ab,=[p for p in combinations(sorted(K),2) if p in cyc];h,=K-set(ab);kinds=Counter()
                for same_axis in (True,False):
                    for k,l in product(ab,repeat=2):
                        a,=set(ab)-{k};b,=set(ab)-{l}
                        if same_axis and k==l:continue
                        if not same_axis and (min(abs(f-u),abs(f-v))==1 or (k!=l and (tuple(sorted((u,l))) not in cyc or tuple(sorted((v,k))) not in cyc))):continue
                        for y,w in permutations(sorted(Y)):
                            if abs(a-y)==1 or abs(b-w)==1:continue
                            for X,Z in ([(x,z),(z,x)] if same_axis else [(x,z)]):
                                rs=tuple(sorted(tuple(sorted(r)) for r in [(X,h,k),(X if same_axis else Z,h,l),(Z,y,a),(Z if same_axis else X,w,b)]));key=(sq,tuple(sorted(cyc)),rs)
                                if key in keys:continue
                                keys.add(key);tag='same axis site' if same_axis else 'opposite, equal pair' if k==l else 'opposite, different pairs';totals[tag]+=1;kinds[tag]+=1;examples.setdefault(tag,dict(square=sq,cycle=sorted(cyc),missed=edge,rows=rs))
                profiles[bool(kinds['opposite, equal pair']+kinds['opposite, different pairs'])]+=1
    digest=sha256(json.dumps(sorted(keys),separators=(',',':')).encode()).hexdigest();ref=json.loads((D/'ramsey_four_port_repair_shared.json').read_text());assert digest==ref['positive_digest'];out=dict(by_type=totals,edges_by_opposite=profiles,examples=examples,digest=digest);print(out);(D/'ramsey_two_repairs_opposite.json').write_text(json.dumps(out,indent=2)+'\n')
    return keys
if __name__=='__main__':run()
