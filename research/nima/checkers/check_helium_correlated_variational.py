"""Exact rational correlated helium variational trial in perimetric coordinates.

Hamiltonian is standard fixed-nucleus Coulomb input, not WG-derived.
Select b on a frozen 0..1 rational grid, optimize scale analytically;
only then compare with rounded reference data. No exact ground-state claim.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
ONE={(0,0,0):F(1)}


def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}


def scale(p,c):return {k:v*c for k,v in p.items() if v*c}


def mul(*polys):
    out=ONE
    for p in polys:
        new={}
        for k,v in out.items():
            for l,w in p.items():
                key=tuple(a+b for a,b in zip(k,l))
                new[key]=new.get(key,F(0))+v*w
        out=new
    return out


def integral(p):
    # Integral over x,y,z >=0 against exp(-2x-y-z). The common angular
    # factor and perimetric Jacobian cancel from Rayleigh quotients.
    return sum((v*F(factorial(i)*factorial(j)*factorial(k),2**(i+1))
                for (i,j,k),v in p.items()),F(0))


def main():
    x={(1,0,0):F(1)};y={(0,1,0):F(1)};z={(0,0,1):F(1)}
    r1=scale(add(x,y),F(1,2));r2=scale(add(x,z),F(1,2));u=scale(add(y,z),F(1,2))
    measure=mul(r1,r2,u)
    r1sq=mul(r1,r1);r2sq=mul(r2,r2);usq=mul(u,u)
    # measure * (rhat1 dot grad1 u + rhat2 dot grad2 u)
    cross_term=scale(add(mul(r2,add(r1sq,scale(r2sq,-1),usq)),
                         mul(r1,add(r2sq,scale(r1sq,-1),usq))),F(1,2))
    # measure * [-Z/r1-Z/r2+1/u], Z=2.
    potential=add(scale(mul(r2,u),-2),scale(mul(r1,u),-2),mul(r1,r2))
    # psi=exp[-zeta(r1+r2)]*(1+b*zeta*r12).
    # Scaling gives E=zeta^2*T(b)+zeta*V(b).
    rows=[]
    for j in range(1001):
        b=F(j,1000)
        factor=add(ONE,scale(u,b));square=mul(factor,factor)
        norm=integral(mul(measure,square))
        kinetic=integral(add(mul(measure,square),scale(measure,b*b),
                             scale(mul(cross_term,factor),-b)))/norm
        potential_mean=integral(mul(potential,square))/norm
        assert norm>0 and kinetic>0 and potential_mean<0
        zeta=-potential_mean/(2*kinetic)
        energy=-potential_mean**2/(4*kinetic)
        assert 2*zeta*kinetic+potential_mean==0
        rows.append(dict(b=b,zeta=zeta,energy=energy,T=kinetic,V=potential_mean))
    assert rows[0]['T']==1 and rows[0]['V']==-F(27,8)
    assert rows[0]['zeta']==F(27,16) and rows[0]['energy']==-F(729,256)
    best=min(rows,key=lambda r:r['energy'])
    assert best['energy']<rows[0]['energy']
    assert 0<best['b']<1
    # Exact scale-minimum identity, including nonoptimal positive scales.
    for s in (F(1),F(2),best['zeta']+F(1,10)):
        assert best['T']*s*s+best['V']*s-best['energy']==best['T']*(s-best['zeta'])**2
    # Input observations enter only after trial selection.
    inp=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    unit=2*F(inp['hydrogen_binding_eV']);reference=F(inp['helium_electronic_binding_eV'])
    binding=-best['energy']*unit
    gain=(rows[0]['energy']-best['energy'])*unit
    result=dict(schema='marici.nima.helium-correlated-variational.v1',status='pass',
                ansatz='exp[-zeta(r1+r2)]*(1+b*zeta*r12), with normalized spin singlet',
                integration='exact factorial moments over nonnegative perimetric x,y,z; analytic Coulomb and gradient kinetic forms',
                selection='minimum over frozen b=j/1000, j=0..1000; scale zeta optimized analytically for each b',
                selected={k:str(v) for k,v in best.items()},
                calibrated_energy_unit_eV=str(unit),binding_eV=str(binding),
                binding_decimal_eV=float(binding),reference_eV=str(reference),
                prediction_minus_reference_eV=str(binding-reference),
                error_decimal_eV=float(binding-reference),
                correlation_improvement_eV=str(gain),improvement_decimal_eV=float(gain),
                residual='Restricted variational family and rational grid, not exact ground state. Fixed nucleus, nonrelativistic Coulomb Hamiltonian supplied externally; hydrogen calibration and rounded references retained. Not a WG-derived interaction or nuclear/isotope calculation.')
    (ROOT/'results/helium-correlated-variational.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
