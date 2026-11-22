"""Exact lower bounds on exceptional-port drops by separate row clearance, then by fixed-point vertex blocking. No minimal kernels used to estimate costs; compare afterward with known optimum."""
from itertools import combinations
from collections import Counter
from ramsey_fork_audit_uniform import grow,inds,D,json
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=[s for s in inds(H) if 6<=s.bit_count()<=8];joint=(1<<10)|(1<<26);cache={};out=[]
    for r in json.loads((D/'ramsey_exceptional_port_drop.json').read_text())['rows']:
        q=tuple(r['fixed']);s=r['old'];
        if q not in cache:cache[q]=[t for t in I if t.bit_count()+sum(not a&t for a in q)==9]
        T=cache[q];soft=None;prop=None;example=None
        for k in range(1+s.bit_count()-2):
            for ds in combinations(bits(s&~joint),k):
                retained=s^sum(1<<v for v in ds);ban=0
                for v in bits(retained):ban|=H[v]
                opts={t&~ban for t in T if not t&retained};
                if 0 in opts:continue
                if soft is None:soft=k
                initial=opts
                while opts and 0 not in opts:
                    ban2=sum(1<<v for v in bits(union(opts)) if any(not(t&~H[v]) for t in opts));
                    if not ban2:break
                    opts={t&~ban2 for t in opts}
                if 0 not in opts:prop=k;break
                if example is None:
                    clash=next(((a,b) for a in sorted(initial) for b in sorted(initial) if all(not(b&~H[v]) for v in bits(a))),None);example=dict(drops=ds,clash=clash)
            if prop is not None:break
        actual=len(r['dropped']);assert soft<=prop<=actual;cleared=[];extendible=[]
        for ds in combinations(bits(s&~joint),soft):
            retained=s^sum(1<<v for v in ds);ban=0
            for v in bits(retained):ban|=H[v]
            if any(not(t&retained) and not(t&~ban) for t in T):continue
            cleared.append(ds)
            if any(not(m['kernel']&ban) for m in r['kernel_blockers']):extendible.append(ds)
        out.append(dict(fixed=q,old=s,clear=soft,pruned=prop,actual=actual,witness=example,cleared=cleared,extendible=extendible))
    return out

def union(opts):
    a=0
    for t in opts:a|=t
    return a
if __name__=='__main__':
    out=run();print(Counter((r['clear'],r['pruned'],r['actual']) for r in out));print(next((r for r in out if r['clear']<r['actual'] and r['witness'] and r['witness']['clash']),None));(D/'ramsey_local_clearance_cost.json').write_text(json.dumps(out)+'\n')
