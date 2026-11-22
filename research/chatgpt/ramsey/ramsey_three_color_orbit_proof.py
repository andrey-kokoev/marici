"""Symmetry-aware row kernels: test small orbit families exhaustively; optimize orbit count on the archived 17-core. Different objective from minimizing individual rows. Independent group enumeration via adjacency-preserving bijections."""
from ramsey_three_color_row_kernel import D,json,graph,inds,bits,combinations,Solver
from ramsey_global_five_basis import minimum

def autos(H):
    n=len(H);F=(1<<n)-1
    def rec(cs,p):
        if not cs:yield p;return
        i=min(cs,key=lambda j:cs[j].bit_count());
        for j in bits(cs[i]):
            rest={k:t&(H[j] if H[i]>>k&1 else F^(H[j]|1<<j)) for k,t in cs.items() if k!=i}
            if all(rest.values()):yield from rec(rest,{**p,i:j})
    return list(rec({i:sum(1<<j for j,h in enumerate(H) if h.bit_count()==H[i].bit_count()) for i in range(n)},{}))

def audit(H):
    n=len(H);group=autos(H);orbs={}
    for t in inds(H):
        if t.bit_count()!=5:continue
        orb={sum(1<<p[i] for i in bits(t)) for p in group};orbs[min(orb)]=sorted(orb)
    reps=sorted(orbs);C=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)];labels=[1+3*n+j for j in range(len(reps))]
    for t,a in zip(reps,labels):
        for u in orbs[t]:
            for ps in combinations(range(3),2):C.append([-a]+[1+3*i+k for i in bits(u) for k in ps])
    with Solver(name='g4',bootstrap_with=C) as sat:
        for k in range(1,(len(reps) if len(reps)<=13 else 3)+1):
            winners=[]
            for js in combinations(range(len(reps)),k):
                if not sat.solve(assumptions=[labels[j] for j in js]):winners.append(js)
            if winners:
                js=min(winners,key=lambda js:sum(len(orbs[reps[j]]) for j in js));return dict(group=len(group),classes=len(reps),kernel=[orbs[reps[j]] for j in js],minimum=k,winning_families=len(winners))
    return dict(group=len(group),classes=len(reps),minimum='>3')
if __name__=='__main__':
    z=[audit(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print([(r['group'],r['classes'],r['minimum'],[len(v) for v in r.get('kernel',[])]) for r in z]);(D/'ramsey_three_color_orbit_proof.json').write_text(json.dumps(z)+'\n')
