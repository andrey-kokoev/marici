"""Explore every surviving incidence option of the builder's smallest outstanding clause, recursively; separately test off-policy live choices at the root. Independent SAT truth for extendibility, never used to accept a move."""
from ramsey_square_unit_builder import build,D,json,graph,inds,bits,gzip,Counter
from pysat.solvers import Solver
from functools import lru_cache

def audit(on,live,cs,ban,close,witness):
    C=[[i+1 for i in bits(s)] for s in cs]+[[-i-1,-j-1] for i in bits(live|on) for j in bits(ban[i]&(live|on)) if j>i];seen=set();cnt=Counter();ex={};depth=0
    @lru_cache(None)
    def probe(o,l):
        while True:
            z=close(o,l)
            if z is None:return None
            o,l,p,_=z
            if p is None:return o,l,0
            yes=no=0
            for i in bits(l&~o):
                if close(o,l^(1<<i)) is None:yes|=1<<i
                if close(o|1<<i,l&~ban[i]) is None:no|=1<<i
            if not yes|no:return o,l,p
            for i in bits(yes):l&=~ban[i]
            o|=yes;l&=~no
    with Solver(name='g4',bootstrap_with=C) as sat:
        def visit(state,path):
            nonlocal depth
            o,l,p=state
            if state in seen:return
            seen.add(state);depth=max(depth,len(path));
            if not p:witness(o);cnt['terminal']+=1;return
            # Fix all propagated exclusions including those at the entry state.
            neg=[-(j+1) for j in bits(((1<<len(ban))-1)&~l)];pos=[j+1 for j in bits(o)];
            for i in bits((l&~o) if not path else p):
                tag='chosen_row' if p>>i&1 else 'other_root';z=probe(o|1<<i,l&~ban[i]);ok=sat.solve(assumptions=neg+pos+[i+1]);assert not ok or z is not None;label='repairable' if ok else 'escape' if z is not None else 'rejected';cnt[tag+'_'+label]+=1
                if label=='escape':ex.setdefault(tag,dict(path=path,choice=i,chosen_options=list(bits(p))))
                if tag=='chosen_row' and z is not None and ok:visit(z,path+[i])
        visit(probe(on,live),[])
    return dict(counts=cnt,states=len(seen),max_depth=depth,examples=ex)

def run():
    src=json.loads((D/'ramsey_square_unit_builder.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();out=[];last=None
    for r in src:
        if not r['ok'] or r.get('probe')!='open':continue
        p,W=r['record'],r['seed'];
        if p!=last:H=graph(ls[p-1]);T=[s for s in inds(H) if s.bit_count()>=5];last=p
        z=build(H,T,W,audit)['residual'];out.append(dict(record=p,seed=W,**z))
    return out
if __name__=='__main__':
    z=run();print(sum((r['counts'] for r in z),Counter()),sum(r['states'] for r in z),max(r['max_depth'] for r in z));print(next((r for r in z if r['examples']),None));(D/'ramsey_square_choice_audit.json').write_text(json.dumps(z)+'\n')
