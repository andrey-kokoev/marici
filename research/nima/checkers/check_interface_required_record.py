"""Derive the minimal exterior record for the existing interface readout.
Fixed 12-mode projector and the already marked AB/BA interface only.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_four_packet_record_feedback import mm,basis,rank,transpose
ROOT=Path(__file__).resolve().parents[1]

def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c):return tuple(tuple(c*x for x in row) for row in a)
def act(a,x):return tuple(sum(v*w for v,w in zip(row,x)) for row in a)
def main():
    rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
    selected=[i for i,r in enumerate(rows) if r['outer_arrow'] in ('AB','BA')]
    rest=[i for i in range(12) if i not in selected]
    assert len(selected)==2 and len(rest)==10
    M=tuple((F(1,12),)*12 for _ in range(12))
    q=tuple(basis(12)[i] for i in selected)
    B=tuple(tuple(M[i][j] for j in rest) for i in selected)
    assert rank(B)==1
    zero=(F(0),)*12;remote=list(zero);remote[rest[0]]=1
    assert act(q,zero)==act(q,remote)==(0,0)
    assert act(mm(q,M),zero)==(0,0) and act(mm(q,M),remote)==(F(1,12),)*2
    # Exact quotient preserving these interface observations for this operator:
    # (a,b,s), where s is the mean of the ten exterior coefficients.
    T=q+(tuple(F(i in rest,10) for i in range(12)),)
    U=tuple((F(1,12),F(1,12),F(10,12)) for _ in range(3))
    assert mm(T,M)==mm(U,T) and mm(U,U)==U
    assert rank(T)==3 and rank(U)==1
    W=((F(1),0,0),(0,F(1),0),(0,0,F(10)))
    assert mm(W,U)==mm(transpose(U),W)
    # Retain rather than erase the exterior contrasts omitted by this quotient.
    sample=tuple(F(i*i-3*i,7) for i in range(12));a,b,s=act(T,sample)
    residual={i:sample[i]-s for i in rest}
    assert sum(residual.values())==0
    rebuilt=tuple(a if i==selected[0] else b if i==selected[1] else s+residual[i] for i in range(12))
    assert rebuilt==sample
    assert sum(x*x for x in sample)==a*a+b*b+10*s*s+sum(x*x for x in residual.values())
    # Eliminate a stationary exterior response using the actual block D, not
    # an invented environment stiffness. This is not a physical energy law.
    A=tuple((F(1,12),)*2 for _ in range(2));D=tuple((F(1,12),)*10 for _ in range(10));C=transpose(B)
    inverse=add(basis(10),scale(D,6))
    assert mm(add(basis(10),scale(D,-1)),inverse)==basis(10)
    effective=add(A,mm(mm(B,inverse),C))
    assert effective==((F(1,2),F(1,2)),)*2
    assert act(effective,(1,-1))==(0,0)
    result=dict(schema='marici.nima.interface-required-record.v1',status='pass',
        boundary='Next interface readout does not factor through the present two interface coefficients.',
        explicit_counterexample='Zero state and a unit perturbation in one exterior block have identical interface input, but next interface outputs differ by (1/12,1/12).',
        exterior_to_interface_rank=1,
        minimal_linear_extension='Add one exterior mean s. Update (a,b,s) to (m,m,m), m=(a+b+10s)/12.',
        commuting_identity='T M = U T exactly',
        retention='The nine exterior contrast coordinates remain separate retained residuals; the three-variable observer is not a lossless replacement for the full state.',
        stationary_exterior_elimination={'exterior_uniform_eigenvalue':'5/6','effective_interface_matrix':[['1/2','1/2'],['1/2','1/2']]},
        disposition='The existing operation requires one extra relational record for this interface, not another spatial tetrahedron. Its closed response still annihilates the candidate antisymmetric electron mode.',
        scope='Minimal linear sufficient state for the selected interface under this fixed projector. No universal WG successor, native admission, particle or physical-energy law is claimed.')
    (ROOT/'results/interface-required-record.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
