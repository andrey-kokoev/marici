from ramsey_pentagon_selector import V,path,charts,ind,combinations,Counter,Path,json
from functools import reduce
from hashlib import sha256


def run():
    hist=Counter();squares=Counter();examples={};D=Path(__file__).resolve().parents[1]/'results'
    for sq,qs,cycles in charts():
        U=set().union(*sq);moving=U-set.intersection(*map(set,sq));probes={tuple(sorted((*e,z))):e for e in qs for z in moving if ind({*e,z})};marks=[(s,t) for s,t in combinations(sorted(probes),2) if sum(abs(a-b) for a,b in zip(s,t))==1];universal=set(range(len(cycles)));winners=set();univ_live=set(universal);live=0
        mask=lambda vs:sum(1<<(i-1) for i in vs);F=1023;caps=[]
        for cyc in cycles:
            edges=list(map(mask,path|cyc));cap=[0]*1024
            for v in range(1,1024):
                bit=v&-v;nb=reduce(int.__or__,(e for e in edges if e&bit),bit);cap[v]=max(cap[v^bit],1+cap[v&~nb])
            caps.append(cap)
        for s,t in marks:
            yes=set();alone=set();kind='same' if probes[s]==probes[t] else 'different';assert len(set(s)&set(t))==2 # probe-probe edge must be blue
            both=mask(s)|mask(t);allowed=[mask(r) for r in sq if set(s)&set(r) and set(t)&set(r)];tests=[(5-n,F&~(both|reduce(int.__or__,p,0))) for n in range(len(allowed)+1) for p in combinations(allowed,n)]
            for i,c in enumerate(cycles):
                if {probes[s],probes[t]}&c:continue
                alone.add(i)
                if all(caps[i][m]<threshold for threshold,m in tests):yes.add(i)
            hist[kind,len(alone),len(yes)]+=1;universal&=yes
            if yes:live+=1;univ_live&=yes
            if len(yes)==1:winners.update(yes)
            if len(cycles)>1 and len(yes)==1 and (kind not in examples or len(alone)>len(examples[kind]['alone'])):examples[kind]=dict(square=sq,rows=(s,t),outside_pairs=(probes[s],probes[t]),alone=list(sorted(cycles[i]) for i in sorted(alone)),joint=sorted(cycles[next(iter(yes))]),cycle_count=len(cycles))
        if len(cycles)>1:
            squares['ambiguous_at_start']+=1;squares['marks',bool(marks)]+=1;squares['common',len(universal)]+=1;squares['has_live_pair',bool(live)]+=1;squares['common_among_live',len(univ_live) if live else 'none_live']+=1;squares['uniquely_reachable']+=len(winners)
    enc=lambda d:{str(k):v for k,v in d.items()};result=dict(hist=enc(hist),squares=enc(squares),examples=examples,protocol_sha=sha256((D/'ramsey_pentagon_swap_selector_protocol.md').read_bytes()).hexdigest());print(result);(D/'ramsey_pentagon_swap_selector.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run()
