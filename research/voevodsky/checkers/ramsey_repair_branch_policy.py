"""Unknown pentagon; assume the installed link belongs to some minimum two-link completion."""
from collections import Counter,defaultdict
from itertools import permutations,combinations
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts,path
from ramsey_two_row_branch import can
from ramsey_square_repair_counts import ways
from ramsey_inherited_swap_selector import D
import json


def predict(sq,base):
    U=set().union(*sq);W=sorted(set(range(1,11))-U);f,=set.intersection(*map(set,sq));mov=U-{f};S,B=sorted(map(set,base),key=lambda r:len(r&U));x,=S&U;a,=B-U;edge=tuple(sorted(set(W)-S-B));u,v=edge;z=u+1+v-1-x;y,=(B&U)-{z};w,=mov-{x,z,y};fz=v if x<z else u;clear=all(abs(i-f)!=1 for i in edge);make=lambda s,d:tuple(sorted((tuple(sorted(s)),tuple(sorted(d)))));family=0;support=Counter();states={}
    for h,k in permutations(S-U):
        ab=tuple(sorted((a,k)));side=tuple(sorted((k,fz)))
        for side_red in (False,True):
            n=ways(W,{ab}|({side} if side_red else set()),{edge}|(set() if side_red else {side}));opts=[]
            if abs(k-w)!=1:
                opts.append(make((x,h,a),(z,w,k)))
                if clear and side_red:opts.append(make((z,h,a),(x,w,k)))
            if clear and abs(w-a)!=1:opts.append(make((z,h,k),(x,w,a)))
            if opts and n:
                end=tuple(sorted((a,k)));fu=u+v-fz
                cycle=tuple(sorted([end,tuple(sorted((h,u))),tuple(sorted((h,v))),tuple(sorted((k,fz if side_red else fu))),tuple(sorted((a,fu if side_red else fz)))]));assert n==1;states[cycle]=set(opts)
                family+=n
                for p in opts:support[p]+=n
    return family,{p:n for p,n in support.items() if n},states


def audit():
    ref=defaultdict(lambda:defaultdict(set));counts=Counter();records=[];triads=[]
    for sq,c,rs in run():
        ok=[p for p in combinations(rs,2) if set(p[0]).isdisjoint(p[1]) and all(set(r)&set(p[0]+p[1]) for r in sq)];es,=[(p,q) for p,q in combinations(ok,2) if set(p).isdisjoint(q)]
        for p,q in permutations(es):ref[sq,p][c].add(q)
    for (sq,base),verified in sorted(ref.items()):
        n,expected,by=predict(sq,base);assert by==verified
        freq=Counter(p for opts in by.values() for p in opts);assert n==len(by) and expected==dict(freq)
        if n<2:continue
        common=[p for p,v in freq.items() if v==n];branches=[];one_test=set()
        for c,opts in by.items():
            for p in sorted(opts):
                if freq[p]==n:continue
                for r in p:
                    # Third port blue to both installed ports in the intended minimum matching.
                    assert can(sq,c,base,True,r,())
                    neg=[other for other in by if not can(sq,other,base,True,r,())];pos=set(by)-set(neg)
                    if neg and all(p in by[other] for other in pos):
                        branches.append(dict(probe=r,partner=p,yes=len(pos),no=len(neg)))
                        for fallback in set.intersection(*(by[other] for other in neg)):
                            assert r not in fallback
                            one_test.add((r,p,fallback,len(pos),len(neg)))
        if n==3:
            U=set().union(*sq);fixed,=set.intersection(*map(set,sq));s,d=sorted(map(set,base),key=lambda r:len(r&U));x,=s&U;a,=d-U;z,=[i for i in d&U if abs(i-x)==1];w,=(U-{fixed})-(s|d);b,c=sorted(s-U)
            def completion(i,j):return tuple(sorted((tuple(sorted((x,a,i))),tuple(sorted((z,w,j))))))
            assert min(abs(w-i) for i in (b,c))>1
            for i,j in ((b,c),(c,b)):
                direct=(tuple(sorted((x,a,i))),completion(i,j),completion(j,i));assert any(t[:3]==direct for t in one_test)
            triads.append(dict(square=sq,installed=base,plans=[dict(probe=r,accept=p,reject=f,yes=yes,no=no) for r,p,f,yes,no in sorted(one_test)]))
        counts[n,bool(common),bool(branches)]+=1;records.append(dict(square=sq,installed=base,cycles=n,common=common,branches=sorted({(tuple(t['probe']),t['partner'],t['yes'],t['no']) for t in branches})))
    print(counts);print(next((r for r in records if r['branches'] and r['common']),None));out=dict(three_cycle_single_test_plans=triads,by_size_common_permanent={str(k):v for k,v in counts.items()},records=records);(D/'ramsey_repair_branch_policy.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
