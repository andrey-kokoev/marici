"""Regression controls for the written all-refinement Berry theorem.
Numerical convergence samples are not promoted to the universal proof.
"""
import cmath
import hashlib
import json
import math
from pathlib import Path
from check_oscillator_family_promotion import promotion_api

ROOT=Path(__file__).resolve().parents[3]
PROOF='research/strominger/canonical-berry-refinement-proof-v1.md'
API=promotion_api()
Row=API['Row']


def inner(u,v): return sum(a.conjugate()*b for a,b in zip(u,v))
def projector(v): return tuple(tuple(a*b.conjugate() for b in v) for a in v)
def multiply(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def cyclic_trace(matrices):
    product=((1+0j,0j),(0j,1+0j))
    for matrix in matrices: product=multiply(product,matrix)
    return product[0][0]+product[1][1]
def phase(z):
    if abs(z)<1e-14: raise ValueError('Zero or numerically unresolved overlap product')
    return z/abs(z)


def main():
    checks=0
    reports=[]
    for p in (.2,.5,.73):
        omega=2*math.pi
        # Exact horizontal-frame second-derivative norm for this latitude.
        M=omega**2*math.sqrt((1-p)*p**4+p*(1-p)**4)
        target=cmath.exp(2j*math.pi*p)
        for N in (16,32,64,128):
            times=[(j/N)**1.3 for j in range(N+1)]
            frames=[(complex(math.sqrt(1-p)),math.sqrt(p)*cmath.exp(2j*math.pi*t)) for t in times[:-1]]
            matrices=[projector(v) for v in frames]
            raw=cyclic_trace(matrices)
            overlap=1+0j # independent scalar overlap product
            for i,v in enumerate(frames): overlap*=inner(v,frames[(i+1)%N])
            assert abs(raw-overlap)<1e-12
            got=phase(raw)
            mesh=max(b-a for a,b in zip(times,times[1:]))
            assert M*mesh**2/2<1
            error=abs(got-target)
            assert error<=M*mesh+1e-12
            rephased=[tuple(cmath.exp(1j*(.31*t+.2*math.sin(4*math.pi*t)))*z for z in v)
                      for t,v in zip(times,frames)]
            assert abs(phase(cyclic_trace([projector(v) for v in rephased]))-got)<1e-12
            assert abs(phase(cyclic_trace(list(reversed(matrices))))-got.conjugate())<1e-12
            if p==.2: assert abs(got-got.conjugate())>1
            checks+=5
            # Actual retained data: entries AND ordered parameter samples.
            rows=tuple(Row(('projector',j,a,b),('sample',j),('entry',a,b),matrices[j][a][b])
                       for j in range(N) for a in range(2) for b in range(2))
            rows+=tuple(Row(('time',j),('sample',j),('parameter',),t) for j,t in enumerate(times))
            for policy in ('inherited','common'):
                first=API['incoming_promotion'](rows,1,policy)
                second=API['incoming_promotion'](first,2,policy)
                for view in (second,API['unindex'](API['indexed'](second,'source')),
                             API['unindex'](API['indexed'](second,'target'))):
                    leaves=API['leaves'](view)
                    assert leaves==rows
                    values={r.label:r.value for r in leaves}
                    assert [values[('time',j)] for j in range(N+1)]==times
                    recovered=[tuple(tuple(values[('projector',j,a,b)] for b in range(2)) for a in range(2))
                               for j in range(N)]
                    assert cyclic_trace(recovered)==raw
                    checks+=3
            reports.append({'latitude_occupation':p,'partition_size':N,'mesh':mesh,
                            'phase_error':error,'proved_bound':M*mesh})
    # Pole-crossing frame is horizontal but not periodic: endpoint factor -1.
    for N in (8,17,64):
        frames=[(complex(math.cos(math.pi*j/N)),complex(math.sin(math.pi*j/N))) for j in range(N)]
        got=phase(cyclic_trace([projector(v) for v in frames]))
        assert abs(got+1)<1e-12 and abs(got-1)>1
        checks+=2
    # Exactly orthogonal coarse neighbors: normalization is legitimately absent.
    zero=cyclic_trace([((1,0),(0,0)),((0,0),(0,1))])
    assert zero==0
    try: phase(zero)
    except ValueError: checks+=1
    else: raise AssertionError('Coarse zero product accepted')
    paths=[PROOF,'research/strominger/berry-connection-domain-cut-v1.md',
           'research/strominger/retained-domain-representation-theorem-v1.md',
           'research/nima/checkers/check_rung_transport_diagram.py',
           'research/strominger/checkers/check_oscillator_family_promotion.py',
           str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','claim':'refining-canonical-berry-cuts',
            'outcome_semantics':'proof-attempt-outcomes-v1','intent':'prove','outcome':'++',
            'proof_kind':'written all-refinement ODE/Taylor proof plus numerical and retained-record regression controls',
            'kernel_verified_analytic_theorem':False,'regression_checks':checks,
            'all_refinement_proof':PROOF,'error_bound':'M*mesh(pi), M=sup norm(horizontal_frame_second_derivative)',
            'numerical_controls':reports,'endpoint_transition_hostile_rejected':True,
            'coarse_zero_overlap_refused':True,'retained_products_both_policies':True,
            'scope':'Canonical rank-one C2 loop readout convergence; no arbitrary connection, infinite-tower convergence or universal physical coverage.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/canonical-berry-refinement/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('numerical_controls','sha256')},indent=2))


if __name__=='__main__': main()
