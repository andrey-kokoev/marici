"""Independent SAT replay + deletion shrinking of failed-literal certificates. uv run --with python-sat python ..."""
from ramsey_request_scale import *
from pysat.solvers import Solver

def main():
 data=json.loads((D/'ramsey_blind_forcing.json').read_text());p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);red=[[-i-1,-j-1] for i,a in enumerate(A) for j in range(i) if a>>j&1];out=[]
 for b in data:
    prs={}
    for v,rows in b['proofs'].items():
        with Solver(name='g4',bootstrap_with=red+[[-int(v)-1]]) as sl:
            for j,r in enumerate(rows):sl.add_clause([-35-j]+[i+1 for i in range(34) if r>>i&1]);
            cs=list(range(35,35+len(rows)));assert not sl.solve(assumptions=cs);cs=sorted(sl.get_core())
            for j in list(cs):
                t=[k for k in cs if k!=j]
                if not sl.solve(assumptions=t):cs=t
            assert not sl.solve(assumptions=cs) and all(sl.solve(assumptions=[k for k in cs if k!=j]) for j in cs);prs[v]=[rows[k-35] for k in cs]
    out.append(dict(case=b['case'],proofs=prs))
 (D/'ramsey_blind_shrunk.json').write_text(json.dumps(out));l=[len(p) for a in out for p in a['proofs'].values()];print('shrunk',min(l),statistics.median(l),max(l));a=next(a for a in out if a['case']==51);print('51',[(v,len(p)) for v,p in a['proofs'].items()]);
if __name__=='__main__':main()
