# /// script
# dependencies = ["sympy"]
# ///
"""Shared geometric seed decoded from the full twelve-arrow retained state."""
import importlib.util
import json
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from source_arrow_hamiltonian import construct
DEF='research/conjecture_net/contracts/shared-quadrilateral-geometric-seed.v1.json'
NOTE='research/voevodsky/shared-quadrilateral-geometric-seed-v1.md'
OUT='research/voevodsky/results/shared-quadrilateral-geometric-seed-v1.json'

def require(ok,msg):
    if not ok:raise ValueError(msg)
def main():
    cfg=json.loads((ROOT/DEF).read_text())
    prior=json.loads((ROOT/'research/strominger/results/source-arrow-hamiltonian-descent.json').read_text())
    bridge=json.loads((ROOT/'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json').read_text())
    source,C,edges=construct(tuple('ABCD'),prior['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    order=cfg['boundary_order'];rho={a:order[(i+1)%4] for i,a in enumerate(order)}
    require(rho==prior['vertex_permutation'],'boundary rotation mismatches native source')
    diagonals=[tuple(d) for d in cfg['diagonals']]
    require({frozenset(d) for d in diagonals}=={frozenset((order[0],order[2])),frozenset((order[1],order[3]))},'not quadrilateral diagonals')
    K=S.Matrix(bridge['projection_then_attachment']);E=S.zeros(12,4)
    for i in range(4):E[i,i]=1
    section=E*K[:,:4].inv();N=S.eye(12)-section*K
    def encode(v):
        x=S.zeros(12,1)
        for w,(u,z) in zip(v,diagonals):
            x[edges.index(u+z)]+=w/2;x[edges.index(z+u)]+=w/2
        return x
    def decode(x):
        v=S.Matrix([x[edges.index(u+z)]+x[edges.index(z+u)] for u,z in diagonals])
        require(v in (S.Matrix([1,0]),S.Matrix([0,1])) and encode(v)==x,'outside geometric seed image')
        return v
    G=S.zeros(2)
    for j,(u,z) in enumerate(diagonals):
        moved=frozenset((rho[u],rho[z]));i=next(i for i,d in enumerate(diagonals) if frozenset(d)==moved);G[i,j]=1
    checks=[]
    for j in range(2):
        v=S.eye(2)[:,j];x=encode(v)
        for step in range(4):
            require(C**step*x==encode(G**step*v),'native geometric square')
            require(decode(section*K*C**step*x+N*C**step*x)==G**step*v,'retained reconstruction')
            checks.append(f'seed={j}/rotation={step}')
    x0=encode(S.Matrix([1,0]));x1=encode(S.Matrix([0,1]))
    require(K*x0==K*x1 and N*x0!=N*x1,'coarse hostile missing')
    try:decode(S.zeros(12,1))
    except ValueError:checks.append('non-seed decoder rejected')
    else:raise AssertionError('zero accepted as triangulation')
    # Bind the decoded seed to the actual finite-packet access implementation.
    path=ROOT/'research/voevodsky/checkers/check_retained_history_source_access.py'
    spec=importlib.util.spec_from_file_location('access',path);access=importlib.util.module_from_spec(spec);spec.loader.exec_module(access)
    test=[(S.Integer(1),S.Integer(0),S.Integer(0),S.Integer(1)),(S.Integer(2),S.Integer(0),S.Integer(0),S.Integer(1))]
    for j in range(2):
        v=decode(section*K*encode(S.eye(2)[:,j])+N*encode(S.eye(2)[:,j]))
        seed=tuple(int(a) for a in v)
        s=dict(h=S.Rational(1,3),j=j,D=2,history=[],mode='packet',seeds={'T':seed},terms=[(seed,S.Integer(1),'T',())])
        require(S.simplify(access.query(s,test)-S.exp(-S.pi*test[j][0]/9))==0,'decoded seed query')
        moved=access.update(s,'perm',[1,0]);require(moved['j']==1-j and moved['terms'][0][0]==tuple(G*v),'mark/archive binding')
        heat=access.update(s,'heat',S.Rational(1,2));require(heat['seeds']==s['seeds'] and heat['terms'][0][2]=='T','seed provenance after heat')
        checks.append(f'seed={j}/packet-access')
    paths=[DEF,NOTE,'research/strominger/results/source-arrow-hamiltonian-descent.json',
           'research/strominger/checkers/source_arrow_hamiltonian.py',
           'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json',
           'research/voevodsky/checkers/check_retained_history_source_access.py',
           'research/conjecture_net/contracts/retained-history-source-access.v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.shared-quadrilateral-geometric-seed-validation.v1',passed=True,checks=checks,
                distinct_geometries_equal_K_readout=True,geometric_distinction_recovered_from_N=True,
                native_geometric_square=True,packet_query_binding=True,
                geometric_rotation_is_channel_Fourier=False,full_operation_source_binding=False,common_source_node_closed=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
