"""Positive symmetric pair factors with equal coincidence data, unequal energies.

This tests supplied-factor admissibility in the adapter, not native reachability
from an unchanged seed family. Coulomb physics remains an external readout.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_helium_correlated_variational import ONE, add, scale, mul, integral

ROOT=Path(__file__).resolve().parents[1]


def main():
    prior=json.loads((ROOT/'results/helium-correlated-variational.json').read_text())
    b=F(prior['selected']['b']);zeta=F(prior['selected']['zeta'])
    x={(1,0,0):F(1)};y={(0,1,0):F(1)};z={(0,0,1):F(1)}
    r1=scale(add(x,y),F(1,2));r2=scale(add(x,z),F(1,2));u=scale(add(y,z),F(1,2))
    measure=mul(r1,r2,u)
    cross=scale(add(mul(r2,add(mul(r1,r1),scale(mul(r2,r2),-1),mul(u,u))),
                    mul(r1,add(mul(r2,r2),scale(mul(r1,r1),-1),mul(u,u)))),F(1,2))
    potential=add(scale(mul(r2,u),-2),scale(mul(r1,u),-2),mul(r1,r2))
    swap=lambda p:{(i,k,j):v for (i,j,k),v in p.items()}
    rows=[];factors=[]
    for c in (F(0),b*b/2,b*b):
        # Dimensionless distance u=zeta*r12. All factors have F(0)=1,
        # F'(0)=b, positive coefficients, and are square integrable with envelope.
        factor=add(ONE,scale(u,b),scale(mul(u,u),c))
        derivative=add(scale(ONE,b),scale(u,2*c))
        assert swap(factor)==factor and swap(swap(factor))==factor
        assert factor[(0,0,0)]==1
        assert all(v>0 for v in factor.values())
        factors.append(factor)
        norm=integral(mul(measure,factor,factor))
        kinetic=integral(add(mul(measure,factor,factor),mul(measure,derivative,derivative),
                             scale(mul(cross,factor,derivative),-1)))/norm
        v=integral(mul(potential,factor,factor))/norm
        energy=zeta*zeta*kinetic+zeta*v
        rows.append(dict(c=str(c),factor='1+b*u+c*u^2',norm=str(norm),energy=str(energy)))
    assert rows[0]['energy']==prior['selected']['energy']
    assert len({r['energy'] for r in rows})==3
    # Multiplication composition commutes for every tested pair, but history
    # order is retained separately; no arbitrary state equality is inferred.
    for f in factors:
        for g in factors:
            assert mul(f,g)==mul(g,f)
            assert swap(mul(f,g))==mul(swap(f),swap(g))
    # An asymmetric factor violates the required spatial exchange law.
    wrong=add(ONE,scale(r1,b))
    assert swap(wrong)!=wrong
    result=dict(schema='marici.nima.pair-factor-selection.v1',status='pass',
                obligation='supplied-factor symmetry and composition audit, not native seed reachability',
                common_parameters={'b':str(b),'zeta':str(zeta)},factors=rows,
                common_constraints=['exchange symmetry','positive radial factor','F(0)=1','same scaled first derivative b at coincidence',
                                    'normalizable with fixed exponential envelope','multiplication composition and exchange compatibility'],
                asymmetric_control='rejected',
                disposition='Three distinct energy readouts satisfy the same tested adapter constraints. Those constraints do not select the correlation kernel.',
                residual='No general no-go for additional native laws; inspected native comparison rules consume supplied equivalences and witnesses. A native physical pair law has not been supplied.')
    (ROOT/'results/pair-factor-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
