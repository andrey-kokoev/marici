"""PySAT pilot: fix two ports, jointly encode third and fourth. Learn absence-only cores, verify coverage independently with fourth-support enumeration."""
from ramsey_capacity_transfer_78 import decode,D,json,inds,bits
from pysat.solvers import Solver
from time import perf_counter
from itertools import combinations

def run():
    p=json.loads((D/'ramsey_guarded_prefix_pilot.json').read_text());H=decode((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[p['record']-1]);n=len(H);a,b=p['pair'];old=p['third'];I=inds(H);M=[s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H))];start=perf_counter();clauses=[[-(i+off+1),-(j+off+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for off in (0,n)];rows=[]
    for t in I:
        z=7-t.bit_count()-int(not a&t)-int(not b&t);assert z>=0
        if z>=2:continue
        rows.append((z,t));x=[i+1 for i in bits(t)];y=[i+n+1 for i in bits(t)];clauses.extend([x,y] if z==0 else [x+y])
    def mask(lits):return sum(1<<(-l-1) for l in lits)
    with Solver(name='g4',bootstrap_with=clauses) as sat:
        assumes=[-i-1 for i in p['guard']];assert not sat.solve(assumptions=assumes);raw=sat.get_core();core=list(raw)
        for l in raw:
            tmp=[x for x in core if x!=l]
            if not sat.solve(assumptions=tmp):core=tmp
        pilot_ms=1000*(perf_counter()-start);allmin=[]
        for k in range(len(core)+1):
            for sub in combinations(assumes,k):
                if not sat.solve(assumptions=list(sub)):allmin.append(mask(sub))
            if allmin:break
    start=perf_counter();full=(1<<len(M))-1;mr=[(z,t,sum(1<<i for i,m in enumerate(M) if m&t)) for z,t in rows];good=[]
    for s in I:
        legal=full
        for z,t,w in mr:
            if not z and not s&t:legal=0;break
            if not z or not s&t:legal&=w
            if not legal:break
        if legal:good.append(s)
    enum_ms=1000*(perf_counter()-start);out=[]
    for g in sorted(set(allmin+[mask(core),mask(raw)])):
        assert not old&g and all(s&g for s in good);out.append(dict(guard=list(bits(g)),independent=sum(not s&g for s in I),maximal=sum(not s&g for s in M)))
    return dict(clauses=len(clauses),good=good,raw=list(bits(mask(raw))),shrunk=list(bits(mask(core))),minimum=[list(bits(g)) for g in allmin],coverage=out,pilot_ms=pilot_ms,enum_ms=enum_ms)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_sat_prefix_pilot.json').write_text(json.dumps(out)+'\n')
