"""Same retained hydrogen parent, different supplied two-electron targets.

This is a representation-level discriminator, not native target reachability.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json
from check_hminus_nested_orbitals import energy

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class HydrogenParent:
    nuclear_charge: int = 1
    orbital_exponent: F = F(1)
    energy: F = F(-1,2)


@dataclass(frozen=True)
class Attachment:
    parent: HydrogenParent
    compact: F
    diffuse: F


def main():
    parent=HydrogenParent()
    previous=json.loads((ROOT/'results/hminus-nested-orbitals.json').read_text())
    a=F(previous['output']['compact_exponent']);b=F(previous['output']['diffuse_exponent'])
    frozen_E,frozen_b=min((energy(F(1),F(j,1000)),F(j,1000)) for j in range(1,1001))
    targets=[('equal_orbitals',Attachment(parent,F(11,16),F(11,16))),
             ('freeze_compact_orbital',Attachment(parent,F(1),frozen_b)),
             ('relax_both_roles',Attachment(parent,a,b))]
    unit=F(previous['hydrogen_calibrated_unit_eV'])
    rows=[]
    for name,target in targets:
        assert target.parent is parent
        E=energy(target.compact,target.diffuse)
        assert E==energy(target.diffuse,target.compact)
        rows.append(dict(target=name,compact=str(target.compact),diffuse=str(target.diffuse),
                         energy=str(E),energy_decimal=float(E),
                         below_H_plus_e_threshold=E<parent.energy,
                         signed_attachment_binding_eV=str((parent.energy-E)*unit),
                         signed_binding_decimal_eV=float((parent.energy-E)*unit)))
    assert len({r['energy'] for r in rows})==3
    assert [r['below_H_plus_e_threshold'] for r in rows]==[False,True,True]
    assert energy(a,b)<frozen_E<parent.energy
    # Parent recovery succeeds even when the current compact orbital changed.
    assert targets[-1][1].parent.orbital_exponent!=targets[-1][1].compact
    result=dict(schema='marici.nima.retained-parent-selection.v1',status='pass',
                obligation='source retention versus additional active-state constraints',
                common_parent={'Z':1,'orbital_exponent':'1','energy_hartree':'-1/2'},
                targets=rows,
                conclusion='Identical retained parent and exchange symmetry allow different target energies and threshold results. Freezing the compact orbital is an additional condition, not a consequence of recovering the parent.',
                residual='Actual native packaging theorem is separate from native reachability. Supplied Coulomb target family; no native second-attachment selection law has been derived.')
    (ROOT/'results/retained-parent-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
