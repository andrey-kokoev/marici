"""Extend Nima's exact recoil/radiation readout to deuterium bookkeeping.

Primitive masses are retained rounded reference inputs. Binding controls are
illustrative inputs, not measured or source-derived nuclear/atomic energies.
One effective photon channel is a kinematic test, not a capture-rate model.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'nima/checkers'))
from check_hydrogen_mass_readout import FourMomentum, HydrogenInput, generate

BASE=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class DeuteriumInput:
    proton: F
    neutron: F
    electron: F
    nuclear_binding: F
    electronic_binding: F


def readout(source):
    if source.nuclear_binding<0 or source.electronic_binding<0:raise ValueError('negative binding input')
    deuteron=source.proton+source.neutron-source.nuclear_binding
    if deuteron<=0:raise ValueError('nonpositive deuteron mass')
    atom=deuteron+source.electron-source.electronic_binding
    if atom<=0:raise ValueError('nonpositive atom mass')
    # Reuse the exact one-photon threshold algebra, retaining the complete
    # source tuple separately from its temporary two-summand presentation.
    out=generate(HydrogenInput(source.proton+source.neutron,source.electron,
                              source.nuclear_binding+source.electronic_binding,3))
    assert out.atom_rest_eV==atom and out.valid()
    incoming=FourMomentum(source.proton+source.neutron+source.electron,F(0))
    assert out.atom+out.photon==incoming
    return source,deuteron,out


def main():
    path=BASE.parent/'nima/results/proton-hydrogen-helium-structure.json'
    raw=path.read_bytes();data=json.loads(raw)
    inputs=data['inputs'];me=F(inputs['electron_rest_energy_eV'])
    mp=F(inputs['proton_me'])*me;mn=F(inputs['neutron_me'])*me
    controls=[]
    # Nuclear energies are deliberately round controls, not an imported
    # deuteron observation. Electronic input is the old hydrogen test value.
    for BN,BA in ((F(0),F(0)),(F(1000000),F(0)),(F(2200000),F(inputs['hydrogen_binding_eV']))):
        source=DeuteriumInput(mp,mn,me,BN,BA)
        retained,deuteron,out=readout(source)
        assert retained is source
        assert out.atom_rest_eV/me==F(inputs['proton_me'])+F(inputs['neutron_me'])+1-(BN+BA)/me
        total=mp+mn+me;recoil=out.atom.energy-out.atom_rest_eV
        assert recoil==(BN+BA)**2/(2*total)
        assert out.photon.energy+recoil==BN+BA
        assert (out.atom+out.photon).invariant_squared()==total*total
        # Incorrectly placing all binding in radiation with no recoil fails.
        if BN+BA>0:
            bad=FourMomentum(out.atom_rest_eV,F(0))+FourMomentum(BN+BA,BN+BA)
            assert bad!=FourMomentum(total,F(0))
        controls.append({'nuclear_binding_eV':str(BN),'electronic_binding_eV':str(BA),
                         'deuteron_rest_energy_eV':str(deuteron),'atom_mass_me':str(out.atom_rest_eV/me),
                         'atom_mass_me_decimal':float(out.atom_rest_eV/me),
                         'radiation_energy_eV':str(out.photon.energy),'recoil_energy_eV':str(recoil),
                         'full_source_retained':True,'mass_shell_and_conservation':True})
    assert len({row['atom_mass_me'] for row in controls})==3
    report={'verification_passed':True,
            'reused_constructor':'research/nima/checkers/check_hydrogen_mass_readout.py: generate and FourMomentum',
            'mass_law':'M_deuteron=mp+mn-B_nuc; M_atom=M_deuteron+me-B_elec, c=1',
            'complete_source_fields':['mp','mn','me','B_nuc','B_elec'],
            'channel':'One effective photon at three-constituent incoming rest threshold; not a two-stage nuclear/atomic capture process.',
            'binding_controls_status':'Illustrative supplied values; 2.2 MeV is not an observed deuteron binding input, and the hydrogen electronic binding is a readout test only.',
            'reference_input_status':data['input_status'],
            'controls':controls,
            'closed_mass_me':str(F(inputs['proton_me'])+F(inputs['neutron_me'])+1),
            'binding_derived':False,'source_sha256':sha256(raw).hexdigest()}
    (BASE/'results/deuterium_mass_readout.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
