"""Same candidate order, fresh incremental Glucose instance per strategy/pair. No completion oracle in learner. Time classifying ALL maximal thirds, not first-solution search."""
from ramsey_sat_prefix_pilot import *
from collections import Counter

def batch():
    records=json.loads((D/'ramsey_missed_row_reopen_78.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();keys=sorted({(r['record'],*sorted(pair)) for r in records for pair in combinations(r['supports'],2)});out=[];cache={}
    for idx,a,b in keys:
        if idx not in cache:
            H=decode(lines[idx-1]);I=inds(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));cache[idx]=(H,I,M)
        H,I,M=cache[idx];n=len(H);rows=[(7-t.bit_count()-int(not a&t)-int(not b&t),t) for t in I];assert min(z for z,t in rows)>=0;rows=[(z,t) for z,t in rows if z<2];C=[[-(i+off+1),-(j+off+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for off in (0,n)]
        for z,t in rows:
            x=[i+1 for i in bits(t)];y=[i+n+1 for i in bits(t)];C.extend([x,y] if z==0 else [x+y])
        ans={};rec=dict(record=idx,pair=[a,b],candidates=len(M));
        for mode in ('direct','raw','shrink'):
            start=perf_counter();calls=skips=extra=0;cuts=[];good=[]
            with Solver(name='g4',bootstrap_with=C) as sat:
                for m in M:
                    if any(not m&g for g in cuts):skips+=1;continue
                    calls+=1
                    if sat.solve(assumptions=[-v-1 for v in range(n) if not m>>v&1]):good.append(m);continue
                    if mode=='direct':continue
                    core=sat.get_core() or []
                    if mode=='shrink':
                        for l in list(core):
                            tmp=[i for i in core if i!=l];extra+=1
                            if not sat.solve(assumptions=tmp):core=tmp
                    g=sum(1<<(-l-1) for l in core);cuts=[h for h in cuts if g&h!=g]+[g]
            rec[mode]=dict(ms=1000*(perf_counter()-start),calls=calls,skips=skips,extra=extra,rules=len(cuts));ans[mode]=good
        st=perf_counter();F=(1<<len(M))-1;mr=[(z,t,sum(1<<i for i,m in enumerate(M) if m&t)) for z,t in rows];truth=[]
        for s in M:
            hit=F
            for z,t,w in mr:
                if not z and not s&t:hit=0;break
                if not z or not s&t:hit&=w
                if not hit:break
            if hit:truth.append(s)
        rec.update(oracle_ms=1000*(perf_counter()-st),good=len(truth));assert all(v==truth for v in ans.values());out.append(rec)
    return out
if __name__=='__main__':
    out=batch();print(len(out),len(set(r['record'] for r in out)),sum(bool(r['good']) for r in out),sum(r['good'] for r in out),sum(r['oracle_ms'] for r in out));
    for m in ('direct','raw','shrink'):print(m,{k:round(sum(r[m][k] for r in out),2) for k in out[0][m]});
    (D/'ramsey_sat_learning_batch.json').write_text(json.dumps(out)+'\n')
