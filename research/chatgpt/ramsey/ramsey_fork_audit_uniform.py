"""Calibration only. Frozen predictor: four ports fit iff the UNIFORM eight-set miss budget passes. Failure is a certificate, pass only a prediction. Use all eight one-port omissions and first legal single thinning per omission (lexicographic). No 39 schedule used. Predict batch before importing comparator."""
from verify_ramsey_pure_forks import grow,D,json,verify
from itertools import combinations

def inds(H):
    I=[0]
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    return I

def predict(H):
    I=inds(H);T=[s for s in I if s.bit_count()==8];assert max(map(int.bit_count,I))==8
    M=[s for s in I if all((s>>v)&1 or s&r for v,r in enumerate(H))];hits=[sum(1<<i for i,t in enumerate(T) if t>>v&1) for v in range(len(H))];best=0
    for s in M:
        z=0
        while s:b=s&-s;s-=b;z|=hits[b.bit_length()-1]
        best=max(best,z.bit_count())
    m=len(T)-best;return dict(eights=len(T),minimum_missed=m,margin=len(T)-4*m,predicted=len(T)>=4*m)

def run():
    src=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=src['stem_graphs'][-1];S=src['to35'];rows=[];cores=[]
    for skip in range(8):
        U=S[:skip]+S[skip+1:];A=grow(H,U);I=inds(A);assert max(map(int.bit_count,I))==8;extra=None
        for i,s in enumerate(U):
            for v in range(26):
                if s>>v&1 and not any(t.bit_count()==7 and not(t&(A[26+i]|A[v])) for t in I):
                    V=U[:];V[i]^=1<<v;extra=(i,v,grow(H,V));break
            if extra:break
        for i,v,G in [(None,None,A)]+([extra] if extra else []):cores.append(G);rows.append(dict(skip=skip,thin=[i,v],edges=sum(map(int.bit_count,G))//2,**predict(G)))
    from ramsey_ports_saturated_core import four
    for G,r in zip(cores,rows):
        a=four(G);r.update(actual=bool(a['supports']),supports=a['supports']);
        if a['supports']:verify(grow(G,a['supports']),10)
    return rows
if __name__=='__main__':
    out=run();print([(r['skip'],r['thin'],r['margin'],r['actual']) for r in out]);(D/'ramsey_fork_audit_uniform.json').write_text(json.dumps(out)+'\n')
