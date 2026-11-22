"""Freeze the five archived rooted row signatures. Test held-out degree-four roots separately, pooled, and under predeclared coordinate projections; distinguish transfer by recognizing informative rows from vacuous inclusion of every row."""
from ramsey_inverse_five_motifs import D,json,graph,bits,inds,combinations,Counter
from pysat.solvers import Solver

def testgraph(H,signatures):
    n=len(H);T=[s for s in inds(H) if s.bit_count()==5];roots=[v for v,h in enumerate(H) if h.bit_count()==4];base=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)];labels=[1+3*n+j for j in range(len(T))];
    for a,t in zip(labels,T):
        for pair in combinations(range(3),2):base.append([-a]+[1+3*i+k for i in bits(t) for k in pair]);
    sig=lambda t,v:(t>>v&1,(H[v]&t).bit_count(),max((h&t).bit_count() for h in H),sum((h&t).bit_count()==3 for h in H));S={v:[sig(t,v) for t in T] for v in roots};out={}
    with Solver(name='g4',bootstrap_with=base) as sat:
        def check(sel):
            ok=sat.solve(assumptions=[labels[i] for i in sel]);model=set(sat.get_model()) if ok else set();colour=[sum(1<<i for i in range(n) if 1+3*i+k in model) for k in range(3)] if ok else None
            if ok:assert all(sum(bool(T[i]&s) for s in colour)>=2 for i in sel)
            return dict(rows=len(sel),forces=not ok,escape=colour)
        for mask in range(1,16):
            pr=lambda s:tuple(s[i] for i in range(4) if mask>>i&1);K={pr(s) for s in signatures};sels=[{i for i,s in enumerate(S[v]) if pr(s) in K} for v in roots];out[str(mask)]=dict(byroot=[check(sel) for sel in sels],pooled=check(set.union(*sels)))
        # Literal verbal descriptions of the five orbits: omit the final coordinate for the first four signatures only.
        sels=[{i for i,s in enumerate(S[v]) if s in signatures or s[:3] in {t[:3] for t in signatures[:-1]}} for v in roots];out['verbal']=dict(byroot=[check(sel) for sel in sels],pooled=check(set.union(*sels)))
    return dict(roots=roots,rows=len(T),tests=out)
if __name__=='__main__':
    sig=[tuple(r['signature']) for r in json.loads((D/'ramsey_orbit_escape_anatomy.json').read_text())];z=[testgraph(graph(l),sig) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print('core exact verbal pooled');
    for r in z:print(r['roots'],[(a['rows'],a['forces']) for a in r['tests']['15']['byroot']],sum(a['forces'] for a in r['tests']['verbal']['byroot']),r['tests']['15']['pooled']['forces']);
    for k in z[0]['tests']:
        rs=[a for r in z for a in r['tests'][k]['byroot']];print(k,sum(a['forces'] for a in rs),sum(a['rows'] for a in rs));
    (D/'ramsey_root_signature_transfer.json').write_text(json.dumps(z)+'\n')
