"""Retain nested witness roles and test electron-label transport.

A marked syntax and explicit two-mode fermion realization are supplied models,
not a derivation of physical electrons from WG. No helium/H-minus fit is made.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Core:
    name: str
    charge: int


@dataclass(frozen=True)
class Witnessed:
    parent: object
    electron: str


def relabel(term, names):
    if isinstance(term, Core): return term
    return Witnessed(relabel(term.parent, names), names[term.electron])


def labels(term):
    if isinstance(term,Core): return []
    return labels(term.parent)+[term.electron]


def depth(term):
    return 0 if isinstance(term,Core) else 1+depth(term.parent)


def main():
    proton=Core('proton',1)
    first=Witnessed(proton,'e1')
    nested=Witnessed(first,'e2')
    exchange={'e1':'e2','e2':'e1'}
    swapped=relabel(nested,exchange)
    assert nested.parent is first and first.parent is proton
    assert nested!=swapped and depth(nested)==depth(swapped)==2
    assert labels(nested)==['e1','e2'] and labels(swapped)==['e2','e1']
    assert relabel(swapped,exchange)==nested
    assert swapped.parent.electron=='e2' and swapped.electron=='e1'
    # Equivariance of the constructor is stronger than mere equal endpoints.
    assert relabel(Witnessed(first,'e2'),exchange)==Witnessed(relabel(first,exchange),'e1')
    # Charge accounting distinguishes the target from helium.
    assert proton.charge-len(labels(nested))==-1
    # A deliberately partial relabel leaves duplicate electron identities;
    # it fails retained occurrence uniqueness and is not a full transport.
    bad=Witnessed(first,'e1')
    assert len(set(labels(bad)))!=depth(bad)

    # Two orthonormal spatial modes a,b and a spin singlet. Different modes
    # need not make numbered electrons distinguishable. This is a supplied
    # two-mode illustration, not a computed H-minus ground state.
    # Basis aa,ab,ba,bb; spatial |a,b>+|b,a> times antisymmetric spin.
    psi=(F(0),F(1),F(1),F(0))
    swapped_psi=(psi[0],psi[2],psi[1],psi[3])
    assert swapped_psi==psi
    spin=(F(0),F(1),F(-1),F(0))
    permutation=(0,2,1,3)
    full=tuple(a*b for a in psi for b in spin)
    exchanged_full=tuple(psi[permutation[i]]*spin[permutation[j]]
                         for i in range(4) for j in range(4))
    assert exchanged_full==tuple(-x for x in full)
    norm=sum(x*x for x in psi)
    density=[[x*y/norm for y in psi] for x in psi]
    swapped_density=[[x*y/norm for y in swapped_psi] for x in swapped_psi]
    assert density==swapped_density
    rho1=[[sum(psi[2*i+k]*psi[2*j+k] for k in range(2))/norm for j in range(2)] for i in range(2)]
    rho2=[[sum(psi[2*k+i]*psi[2*k+j] for k in range(2))/norm for j in range(2)] for i in range(2)]
    assert rho1==rho2==[[F(1,2),F(0)],[F(0),F(1,2)]]
    # Naively assigning different intrinsic energies to numbered particles
    # fails permutation invariance. Same one-body law on both particles
    # allows different occupied-mode energies without that violation.
    role_label_energy=(F(4),F(8),F(5),F(9)) # h1=(1,2), h2=(3,7)
    assert role_label_energy[1]!=role_label_energy[2]
    physical_mode_energy=(F(2),F(4),F(4),F(6)) # h=(1,3) on each electron
    assert physical_mode_energy[1]==physical_mode_energy[2]
    expectation=sum(psi[i]**2*physical_mode_energy[i] for i in range(4))/norm
    assert expectation==4
    # Sequential addition energies may differ even for a fully symmetric
    # occupation law E(n)=epsilon*n+U*n(n-1)/2. U is declared, not derived.
    epsilon=F(2);interaction=F(3)
    energy=lambda n:epsilon*n+interaction*n*(n-1)/2
    increments=[energy(1)-energy(0),energy(2)-energy(1)]
    assert increments==[F(2),F(5)]
    assert sum(increments)==energy(2)
    result=dict(schema='marici.nima.nested-electron-roles.v1',status='pass',
                obligation='attachment transport and physical-readout descent under full electron relabeling',
                retained_construction='Witnessed(Witnessed(proton,e1),e2)',
                exchanged_construction='Witnessed(Witnessed(proton,e2),e1)',
                net_charge=-1,physical_target='proton plus two electrons: H-minus composition, not helium',
                hierarchy='inner/outer roles retained; exchange transports labels at both levels and squares to identity',
                fermion_fixture='two orthogonal spatial modes with symmetric spatial pair and antisymmetric spin singlet; not a computed H-minus ground state',
                normalized_one_particle_density=[[str(x) for x in row] for row in rho1],
                observable_result='Different occupied roles/modes coexist with identical numbered-particle marginals and exchange-invariant density.',
                sequential_addition_example={'epsilon':str(epsilon),'U':str(interaction),'increments':list(map(str,increments))},
                controls=['partial relabel duplicates a retained occurrence','particle-number-specific energy breaks exchange invariance'],
                residual='The nested constructor is supplied; no native rule deriving it, physical role/record coupling, H-minus binding calculation, or kernel selection is established.')
    (ROOT/'results/nested-electron-roles.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
