"""Paired first-witness timings, counterbalanced repeats and two fixed ordering policies. Time includes SAT bootstrap/model extraction, excludes identical CNF/candidate generation and independent verification."""
from ramsey_sat_prefix_pilot import *
from ramsey_fork_audit_uniform import grow,verify
from statistics import median
from random import Random

def first(C,order,n,learn):
    start=perf_counter();cuts=[];calls=0
    with Solver(name='g4',bootstrap_with=C) as sat:
        for i,(s,A) in enumerate(order):
            if learn and any(not s&g for g in cuts):continue
            calls+=1
            if sat.solve(assumptions=A):
                w=sum(1<<(j-n-1) for j in sat.get_model() if n<j<=2*n);break
            if learn:
                g=sum(1<<(-j-1) for j in sat.get_core());cuts=[h for h in cuts if g&h!=g]+[g]
        else:raise AssertionError('no attachment')
    return (perf_counter()-start)*1e6,calls,i,s,w

def run():
    keys=json.loads((D/'ramsey_small_obligation_holdout.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for num,r in enumerate(keys):
        idx=r['record'];a,b=r['pair'];
        if idx!=last:
            H=decode(lines[idx-1]);I=inds(H);n=len(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));base=[(s,[-i-1 for i in range(n) if not s>>i&1]) for s in M];last=idx
        C=[[-(i+off+1),-(j+off+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for off in (0,n)]
        for t in I:
            z=7-t.bit_count()-int(not a&t)-int(not b&t);assert z>=0
            if z>=2:continue
            x=[i+1 for i in bits(t)];y=[i+n+1 for i in bits(t)];C.extend([x,y] if z==0 else [x+y])
        for shuffled in (False,True):
            order=list(base)
            if shuffled:Random(83219+num).shuffle(order)
            times=[[],[]];ws=set();calls={}
            for rep in range(4):
                for m in ((0,1) if (num+rep)%2==0 else (1,0)):
                    us,c,i,s,w=first(C,order,n,m);times[m].append(us);ws.add((s,w));calls[m]=c
            assert len({s for s,w in ws})==1
            for s,w in ws:verify(grow(H,[a,b,s,w]),8)
            out.append(dict(record=idx,pair=[a,b],shuffled=shuffled,times=times,calls=list(map(calls.get,(0,1))),position=i+1,witness=list(sorted(ws))))
    return out
if __name__=='__main__':
    out=run();(D/'ramsey_time_first_attachment.json').write_text(json.dumps(out)+'\n');
    for sh in (False,True):
        z=[r for r in out if r['shuffled']==sh];d=[median(r['times'][0])-median(r['times'][1]) for r in z];print(sh,[median(median(r['times'][i]) for r in z) for i in (0,1)],median(d),sum(v>0 for v in d),[sum(r['calls'][i] for r in z) for i in (0,1)])
