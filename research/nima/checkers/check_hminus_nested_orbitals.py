"""Nested-role H-minus Coulomb benchmark with exchange-symmetric spatial state.

Unnormalized Chandrasekhar trial exp(-a*r1-b*r2)+exp(-b*r1-a*r2),
spin singlet. Standard fixed-nucleus Hamiltonian is supplied, not WG-derived.
Exact rational integrals, fixed ratio grid and analytical scale minimization.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def terms(a,b,Z=F(1)):
    # Factors pi and pi^2 are canceled consistently from all integrals.
    na=1/a**3;nb=1/b**3;s=8/(a+b)**3
    norm=na*nb+s*s  # Common factor 2 in symmetric state cancels.
    kinetic=((a*a+b*b)*na*nb/2+a*b*s*s)/norm
    attraction=(-Z*(a+b)*na*nb-8*Z*s/(a+b)**2)/norm
    direct=(a*a+3*a*b+b*b)/(a*a*b*b*(a+b)**3)
    exchange=20/(a+b)**5
    # Independent radial integration: split at r1=r2, integrate the outer
    # radial variable, and evaluate factorial moments of the inner one.
    def radial(A,B):
        return 16*(6/(A*(A+B)**4)+2/(A*A*(A+B)**3)
                   +6/(B*(A+B)**4)+2/(B*B*(A+B)**3))
    assert direct==radial(2*a,2*b)
    assert exchange==radial(a+b,a+b)
    repulsion=(direct+exchange)/norm
    return kinetic,attraction,repulsion,s*s/(na*nb)


def energy(a,b):return sum(terms(a,b)[:3])


def main():
    rows=[]
    for j in range(1,1001):
        ratio=F(j,1000)
        T,Vn,Vee,_=terms(F(1),ratio)
        V=Vn+Vee
        assert T>0 and V<0 and Vee>0
        scale=-V/(2*T)
        E=-V*V/(4*T)
        assert energy(scale,scale*ratio)==E
        assert energy(scale,scale*ratio)==energy(scale*ratio,scale)
        rows.append((E,ratio,scale,scale*ratio))
    E,ratio,a,b=min(rows)
    threshold=F(-1,2)  # Exact hydrogen ground state + free electron in this model.
    assert E<threshold
    equal=rows[-1][0]
    assert equal==-F(121,256) and equal>threshold
    T,Vn,Vee,overlap2=terms(a,b)
    assert 2*T+Vn+Vee==0  # Scale stationary virial balance.
    assert 0<overlap2<1 and a>b>0
    # Normalized symmetric spatial state: both numbered-electron marginals
    # contain the SAME compact, diffuse and cross terms. Exchange has no
    # effect on energy despite different role exponents.
    rho_coefficients=(1/(2*(1+overlap2)),)*2
    assert rho_coefficients[0]==rho_coefficients[1]
    # Parent hydrogen exponent is 1. Retaining it does not freeze the final
    # compact orbital; benchmark also checks the explicitly frozen-parent trial.
    frozen=min((energy(F(1),F(j,1000)),F(j,1000)) for j in range(1,1001))
    assert E<frozen[0]<threshold
    # Removing electron repulsion overbinds; role exchange cannot cancel it.
    assert T+Vn<E and Vee>0
    # Coincident exponent limit reproduces single-exponent helium/hydrogen forms.
    for zeta in (F(1),F(27,16),F(11,16)):
        tt,vn,ve,_=terms(zeta,zeta)
        assert tt==zeta*zeta and vn==-2*zeta and ve==F(5,8)*zeta
    inputs=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    hydrogen=F(inputs['hydrogen_binding_eV']);unit=2*hydrogen
    affinity=(threshold-E)*unit
    parent=dict(core='proton Z=1',first_electron_exponent='1',energy_hartree='-1/2')
    result=dict(schema='marici.nima.hminus-nested-orbitals.v1',status='pass',
                obligation='conditional physical realization of distinct orbital roles with exchange symmetry and retained parent',
                parent_record=parent,
                output=dict(compact_exponent=str(a),diffuse_exponent=str(b),ratio=str(ratio),
                            compact_decimal=float(a),diffuse_decimal=float(b),
                            spatial_state='exp(-a*r1-b*r2)+exp(-b*r1-a*r2)',spin='antisymmetric singlet'),
                selection='ratio=j/1000, j=1..1000 frozen before readout; positive overall scale optimized analytically',
                energy_hartree=str(E),energy_decimal=float(E),threshold_hartree=str(threshold),
                equal_exponent_energy_hartree=str(equal),equal_exponent_disposition='trial above threshold: does not demonstrate binding, not proof of nonbinding',
                frozen_parent_energy_hartree=str(frozen[0]),
                hydrogen_calibrated_unit_eV=str(unit),
                predicted_second_attachment_binding_eV=str(affinity),affinity_decimal_eV=float(affinity),
                total_electronic_binding_eV=str(-E*unit),total_binding_decimal_eV=float(-E*unit),
                squared_orbital_overlap=str(overlap2),virial_residual=str(2*T+Vn+Vee),
                disposition='Distinct compact/diffuse orbital roles yield a trial below H+free-electron threshold while preserving fermion exchange; original hydrogen source is retained, not frozen.',
                residual='Supplied Coulomb Hamiltonian and orbital ansatz; finite ratio grid; fixed nucleus/nonrelativistic model and hydrogen-based unit calibration. No measured affinity used or precision comparison claimed; no native WG selection of this Hamiltonian or nesting law.')
    (ROOT/'results/hminus-nested-orbitals.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
