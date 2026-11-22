"""Extract small unsatisfiable row families before a branching refutation, then lift their guards into third-port cuts. Catalogue record 20, failed reopen position 1."""
from ramsey_capacity_transfer_78 import decode,D,json,inds,bits
# Proof by exhaustive branching on the smallest surviving obligation.
from time import perf_counter

def run():
    r=json.loads((D/'ramsey_missed_row_reopen_78.json').read_text())[0];H=decode((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[r['record']-1]);_,c,a,b=r['supports'];I=inds(H);M=[s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H))];T=[t for t in I if t.bit_count()>=4];slack={t:7-t.bit_count()-sum(not t&s for s in (a,b)) for t in T};assert min(slack.values())>=0
    def requirements(c):
        rows=[]
        for t,z in slack.items():
            rem=z-int(not t&c)
            if rem<0:return [0]
            if rem==0:rows.append(t)
        return rows
    start=perf_counter();rows=requirements(c);assert 0 not in rows;allowed={t:sum(1<<i for i,m in enumerate(M) if m&t) for t in rows};core=sorted(rows,key=lambda t:(-t.bit_count(),t));full=(1<<len(M))-1
    def satisfiable(ts):
        hit=full
        for t in ts:hit&=allowed[t]
        return bool(hit)
    assert not satisfiable(core)
    for t in list(core):
        rest=[u for u in core if u!=t]
        if not satisfiable(rest):core=rest
    def refute(live,chosen):
        un=[t for t in core if not t&chosen];assert un
        t=min(un,key=lambda t:(t&live).bit_count());return dict(row=t,branches={x:refute(live&~H[x],chosen|1<<x) for x in bits(t&live)})
    proof=refute((1<<len(H))-1,0);guard=0
    for t in core:
        if slack[t]==1:guard|=t
    assert not c&guard;learn_ms=1000*(perf_counter()-start);start=perf_counter();cut={s for s in I if not s&guard};filter_ms=1000*(perf_counter()-start);start=perf_counter();bad=set()
    masks={t:sum(1<<i for i,m in enumerate(M) if t&m) for t in T};masks[0]=0
    for s in I:
        hit=full
        for t in requirements(s):hit&=masks[t]
        if not hit:bad.add(s)
    enum_ms=1000*(perf_counter()-start);assert cut<=bad;return dict(record=r['record'],pair=[a,b],third=c,all=len(I),bad=len(bad),cut=len(cut),maximal=len(M),maximal_bad=len(bad.intersection(M)),maximal_cut=len(cut.intersection(M)),guard=list(bits(guard)),roots=[dict(row=t,guarded=slack[t]==1) for t in core],rounds=proof,learn_ms=learn_ms,filter_ms=filter_ms,enumerate_ms=enum_ms)
if __name__=='__main__':
    out=run();print({k:v for k,v in out.items() if k!='rounds'});(D/'ramsey_guarded_prefix_pilot.json').write_text(json.dumps(out)+'\n')
