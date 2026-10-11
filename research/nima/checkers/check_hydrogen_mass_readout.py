"""Witnessed hydrogen mass readout with an explicit recoil/radiation complement.

Uses supplied rounded masses and binding. Not a WG derivation of these inputs,
not an allowed-channel/rate proof. Four-momenta use c=1 and eV units.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class FourMomentum:
    energy: F
    px: F

    def __add__(self,other):return FourMomentum(self.energy+other.energy,self.px+other.px)
    def invariant_squared(self):return self.energy**2-self.px**2


@dataclass(frozen=True)
class HydrogenInput:
    proton_rest_eV: F
    electron_rest_eV: F
    binding_eV: F
    occurrence_weight: int = 2


@dataclass(frozen=True)
class HydrogenOutput:
    parent: HydrogenInput
    atom_rest_eV: F
    atom: FourMomentum
    photon: FourMomentum

    def valid(self):
        source=FourMomentum(self.parent.proton_rest_eV+self.parent.electron_rest_eV,F(0))
        return (self.atom+self.photon==source and
                self.atom.invariant_squared()==self.atom_rest_eV**2 and
                self.photon.invariant_squared()==0 and
                self.atom_rest_eV==source.energy-self.parent.binding_eV)


def generate(source):
    total=source.proton_rest_eV+source.electron_rest_eV
    B=source.binding_eV
    if not (0 <= B < total):raise ValueError('binding outside declared domain')
    atom_mass=total-B
    photon=B-B*B/(2*total)
    target=HydrogenOutput(source,atom_mass,FourMomentum(total-photon,-photon),FourMomentum(photon,photon))
    assert target.valid()
    return target


def main():
    data=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    electron=F(data['electron_rest_energy_eV']);ratio=F(data['proton_me']);B=F(data['hydrogen_binding_eV'])
    source=HydrogenInput(ratio*electron,electron,B)
    out=generate(source)
    assert out.parent is source
    mass_ratio=out.atom_rest_eV/electron
    assert mass_ratio==ratio+1-B/electron
    recoil=out.atom.energy-out.atom_rest_eV
    assert recoil==B*B/(2*(source.proton_rest_eV+electron))
    assert out.photon.energy+recoil==B
    closed=out.atom+out.photon
    assert closed.invariant_squared()==(source.proton_rest_eV+electron)**2
    # A photon has zero rest mass but positive energy; dropping it because of
    # that zero would violate total four-momentum conservation.
    assert out.photon.invariant_squared()==0 and out.photon.energy>0
    assert out.atom!=closed
    # Sum of subsystem rest masses is not closed-system invariant mass.
    assert out.atom_rest_eV < closed.energy
    # Fixed grouping and constituent count do not select binding.
    controls=[]
    for trial_B in (F(0),B/2,B):
        trial=generate(HydrogenInput(ratio*electron,electron,trial_B))
        assert trial.valid() and trial.parent.occurrence_weight==2
        controls.append(dict(binding_eV=str(trial_B),atom_rest_eV=str(trial.atom_rest_eV)))
    assert len({r['atom_rest_eV'] for r in controls})==3
    # A falsely certified atom with all binding put into a photon but no
    # recoil cannot satisfy the invariant mass and momentum constraints.
    bad=HydrogenOutput(source,out.atom_rest_eV,FourMomentum(out.atom_rest_eV,F(0)),FourMomentum(B,B))
    assert not bad.valid()
    result=dict(schema='marici.nima.hydrogen-mass-readout.v1',status='pass',
                obligation='conditional mass-valued readout of retained composite and complementary record',
                retained_source={'proton_mass_me':str(ratio),'electron_rest_eV':str(electron),'binding_eV':str(B)},
                occurrence_weight=2,hydrogen_mass_me=str(mass_ratio),hydrogen_mass_me_decimal=float(mass_ratio),
                hydrogen_rest_energy_eV=str(out.atom_rest_eV),photon_energy_eV=str(out.photon.energy),
                recoil_energy_eV=str(recoil),photon_decimal_eV=float(out.photon.energy),recoil_decimal_eV=float(recoil),
                closed_system_mass_me=str(ratio+1),
                readout='Subsystem mass from invariant four-momentum, not aggregation count; composition adds four-momenta before taking invariant mass.',
                same_count_different_mass_controls=controls,
                disposition='Explicit source-retaining hydrogen readout with exact mass-shell and conservation certificate. Correct photon inclusion distinguishes atom mass from closed-system mass.',
                residual='Primitive masses and binding are supplied rounded inputs. No native WG mass-selection law, Coulomb derivation, photon amplitude or precision mass prediction is supplied.')
    (ROOT/'results/hydrogen-mass-readout.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
