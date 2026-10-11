"""Common retained composition tree with geometric and four-momentum readouts.

Matter provenance weights, not masses. Binding is a certified redistribution,
not an associator. Physics inputs remain supplied. Rational c=1 units.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json
from check_hydrogen_mass_readout import HydrogenInput, generate

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Payload:
    weight: int
    moment: tuple
    energy: F
    px: F

    def __add__(self,other):
        return Payload(self.weight+other.weight,tuple(a+b for a,b in zip(self.moment,other.moment)),
                       self.energy+other.energy,self.px+other.px)

    def center(self):
        return None if self.weight==0 else tuple(x/self.weight for x in self.moment)

    def mass_squared(self):return self.energy*self.energy-self.px*self.px


@dataclass(frozen=True)
class Leaf:
    name: str
    payload: Payload
    parents: tuple = ()


@dataclass(frozen=True)
class Join:
    left: object
    right: object


def readout(tree):
    return tree.payload if isinstance(tree,Leaf) else readout(tree.left)+readout(tree.right)


def bracketings(a,b,c,d):
    return [Join(Join(Join(a,b),c),d),Join(Join(a,Join(b,c)),d),
            Join(a,Join(Join(b,c),d)),Join(a,Join(b,Join(c,d))),Join(Join(a,b),Join(c,d))]


def main():
    inp=json.loads((ROOT/'results/proton-hydrogen-helium-structure.json').read_text())['inputs']
    me=F(inp['electron_rest_energy_eV']);mp=F(inp['proton_me'])*me;B=F(inp['hydrogen_binding_eV'])
    source=HydrogenInput(mp,me,B);physical=generate(source)
    p=Leaf('proton',Payload(1,(F(1),F(0),F(0),F(0)),mp,F(0)))
    e=Leaf('electron',Payload(1,(F(0),F(1),F(0),F(0)),me,F(0)))
    old=Join(p,e)
    # Hydrogen inherits matter provenance. Photon has no original matter
    # occurrence, but retains the source references and NONZERO four-momentum.
    h=Leaf('hydrogen',Payload(2,(F(1),F(1),F(0),F(0)),physical.atom.energy,physical.atom.px),(p,e))
    photon=Leaf('photon',Payload(0,(F(0),)*4,physical.photon.energy,physical.photon.px),(p,e))
    bound=Join(h,photon)
    assert readout(old)==readout(bound)
    assert physical.valid()
    assert h.parents==(p,e) and photon.parents==(p,e)
    assert photon.payload.center() is None and photon.payload.energy>0
    assert photon.payload.mass_squared()==0
    assert h.payload.mass_squared()==physical.atom_rest_eV**2
    assert readout(bound).mass_squared()==(mp+me)**2
    # Auxiliary independent spectators test compositional contexts. Their
    # numbers are fixtures, not claimed new particles or measured systems.
    x=Leaf('spectator-X',Payload(1,(F(0),F(0),F(1),F(0)),F(7),F(0)))
    y=Leaf('spectator-Y',Payload(1,(F(0),F(0),F(0),F(1)),F(11),F(0)))
    initial=bracketings(p,e,x,y)
    final=bracketings(h,photon,x,y)
    assert all(readout(t)==readout(initial[0]) for t in initial+final)
    # Two routes to the same terminal tree: bind in left branch then reassociate,
    # or reassociate then bind. Retained route records are not identified.
    route1=('bind-pair','regroup-to-balanced')
    route2=('regroup-to-balanced','bind-pair')
    endpoint1=Join(bound,Join(x,y))
    endpoint2=Join(Join(h,photon),Join(x,y))
    assert endpoint1==endpoint2 and route1!=route2
    assert readout(endpoint1)==readout(initial[0])
    # Deliberately dropping the zero-matter-weight complement passes the
    # geometric projection but FAILS the four-momentum projection.
    geo=lambda v:(v.weight,v.moment)
    assert geo(readout(old))==geo(h.payload)
    assert (h.payload.energy,h.payload.px)!=(readout(old).energy,readout(old).px)
    # No factorization of the ATOM mass through its geometric representative:
    # same parent and geometry, different supplied binding -> different mass.
    rival=generate(HydrogenInput(mp,me,B/2))
    rival_h=Payload(h.payload.weight,h.payload.moment,rival.atom.energy,rival.atom.px)
    assert geo(rival_h)==geo(h.payload)
    assert rival_h.mass_squared()!=h.payload.mass_squared()
    result=dict(schema='marici.nima.joint-hydrogen-readouts.v1',status='pass',
                obligation='common retained source with aggregation associativity and binding-in-context readout compatibility',
                packet='typed constituent tree + source links + geometric (matter weight,moment) + four-momentum + separate binding certificate',
                count_semantics='weights count original marked matter occurrences, not every output record; hydrogen 2, photon 0',
                photon_semantics='zero matter provenance weight, no matter centroid, nonzero null four-momentum; must remain retained',
                hydrogen_geometric_center=list(map(str,h.payload.center())),
                source_and_bound_total_equal=True,source_bracketings=5,target_bracketings=5,
                two_routes=[route1,route2],common_endpoint='((hydrogen,photon),(spectator-X,spectator-Y))',
                controls=['dropping photon preserves geometric readout but violates four-momentum',
                          'same hydrogen geometry and parents permit different masses under different supplied binding'],
                disposition='The two readouts coexist and respect the same regrouping; a separately certified binding step is compatible with composition contexts. Physical mass does not factor through the geometric representative alone.',
                residual='Geometric coordinate here is matter provenance, not spatial center of mass. Masses, binding and radiative channel remain supplied. No WG derivation of the interaction or photon amplitude; no identification of physical binding with an associator.')
    (ROOT/'results/joint-hydrogen-readouts.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
