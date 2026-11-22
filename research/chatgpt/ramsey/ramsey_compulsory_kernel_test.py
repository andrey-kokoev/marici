"""Census exact minimal repairs of every distinct triple of the failed 404. Start with all valid maximal-support completions, then test EVERY subset of their fourth supports against tight rows, so nonmaximal repairs are included."""
from itertools import combinations
from collections import Counter,defaultdict
from functools import lru_cache
from ramsey_final_miss_levels import levels,bits,D,json
from ramsey_fork_audit_uniform import inds,grow,verify

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);valid=defaultdict(set);trip=set()
    def collect(S,tag,obs):
        if tag not in ('valid','fails_four'):return
        for i in range(4):
            q=tuple(sorted(S[:i]+S[i+1:]));
            if tag=='valid':valid[q].add(S[i])
            else:trip.add(q)
    levels(H,on_classified=collect);I=inds(H);Ts={k:[s for s in I if s.bit_count()==k] for k in (6,7,8)};hit={k:[sum(1<<j for j,s in enumerate(T) if s>>v&1) for v in range(34)] for k,T in Ts.items()};
    @lru_cache(None)
    def miss(k,s):
        h=0
        for v in bits(s):h|=hit[k][v]
        return ((1<<len(Ts[k]))-1)^h
    reports=[];hist=Counter();witness=None
    for q in sorted(trip):
        opts=valid.get(q,());mins=[]
        if opts:
            tight={}
            for k in Ts:
                a,b,c=[miss(k,s) for s in q];tight[k]=a&b&c if k==6 else (a&b)|(a&c)|(b&c) if k==7 else a|b|c
            seen=set()
            for m in opts:
                s=m
                while s:
                    seen.add(s);s=(s-1)&m
            legal={s for s in seen if all(not(miss(k,s)&z) for k,z in tight.items())};mins=sorted(s for s in legal if all((s^(1<<v)) not in legal for v in bits(s)));assert mins
            if len(mins)>1 and witness is None:
                x,y=mins[:2];diff=[]
                for i,j in [(x,y),(y,x)]:
                    diff.append(next((T for k in Ts for n in bits(tight[k]) if (T:=Ts[k][n])&i and not T&(i&j)),None));verify(grow(H,[*q,i]),10)
                witness=dict(fixed=q,repairs=[x,y],rows_missed_by_intersection=diff)
        hist[len(mins)]+=1;reports.append(dict(triple=q,minima=mins,maximal_count=len(opts)))
    return dict(total=len(trip),hist=hist,witness=witness,triples=reports)
if __name__=='__main__':
    out=run();print(out['total'],out['hist'],out['witness']);(D/'ramsey_compulsory_kernel_test.json').write_text(json.dumps(out)+'\n')
