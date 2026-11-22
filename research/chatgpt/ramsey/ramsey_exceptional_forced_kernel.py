"""Singleton-hit closure on unique exceptional repairs. Distinguish mere compatibility with the partial support from iterated row-blocker compatibility (stronger control)."""
from collections import Counter
from ramsey_fork_audit_uniform import D,json,grow,inds,verify
from ramsey_final_miss_levels import bits

def trace(H,T,seed,prune,forbid=0):
    s=seed;F=(1<<len(H))-1;log=[]
    while True:
        un=[t for t in T if not t&s];live=(F^s)&~forbid
        for x in bits(s):live&=~H[x]
        while prune and un:
            rows=sorted({t&live for t in un},key=int.bit_count);blocked=sum(1<<x for x in bits(live) if any(not (t&~H[x]) for t in rows));
            if not blocked:break
            live&=~blocked
        rows=[t&live for t in un];
        if 0 in rows:return log+[dict(support=s,contradiction=True)]
        units={t for t in rows if t.bit_count()==1};log.append(dict(support=s,unhit=len(un),min_options=min(map(int.bit_count,rows),default=0),units=sorted(units)))
        if not units:return log
        s|=sum(units);assert all(not H[x]&s for x in bits(s))

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=inds(H);seed=(1<<10)|(1<<26);trip=Counter(tuple(r['kept']) for r in json.loads((D/'ramsey_two_port_repair_depth.json').read_text())['repairs']);lookup={tuple(r['triple']):r for r in json.loads((D/'ramsey_compulsory_kernel_test.json').read_text())['triples']};out=[];hist=Counter()
    for q,mult in trip.items():
        mins={s|seed for s in lookup[q]['minima'] if not any(H[x]&(s|seed) for x in bits(s|seed))};mins=sorted(s for s in mins if not any(s!=t and s&t==t for t in mins));assert mins;T=[t for t in I if t.bit_count()+sum(not s&t for s in q)==9];a,b=[trace(H,T,seed,p) for p in (False,True)];
        for l in (a,b):
            assert all(l[-1]['support']&s==l[-1]['support'] for s in mins)
            if not l[-1]['unhit']:assert mins==[l[-1]['support']];verify(grow(H,[*q,mins[0]]),10)
        hist[len(mins),not a[-1]['unhit'],not b[-1]['unhit']]+=1;out.append(dict(fixed=q,multiplicity=mult,minima=mins,plain=a,blockers=b,exclude_probe={x:trace(H,T,b[-1]['support'],True,1<<x)[-1].get('contradiction',False) for x in bits(mins[0]&~b[-1]['support'])} if len(mins)==1 else {}))
    return dict(hist={str(k):v for k,v in hist.items()},rows=out)
if __name__=='__main__':
    out=run();print(out['hist']);(D/'ramsey_exceptional_forced_kernel.json').write_text(json.dumps(out)+'\n')
