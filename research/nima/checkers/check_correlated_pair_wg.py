"""Executable pair-state WG adapter and exact benchmark readout comparison.

The Python adapter mirrors, but is not extracted from, CorrelatedPairWitness.
Its generator and Coulomb readout are supplied; neither is claimed emergent.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from pathlib import Path
from contextlib import redirect_stdout
import io
import json
import check_helium_correlated_variational as benchmark
from check_helium_correlated_variational import ONE, add, scale, mul, integral

ROOT=Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Parameters:
    nuclear_charge: int
    zeta: F
    b: F


@dataclass(frozen=True)
class Independent:
    parameters: Parameters
    roles: tuple = ('electron-1', 'electron-2')


@dataclass(frozen=True)
class Correlated:
    parent: Independent
    rule: str = 'multiply-by-1+b*zeta*r12'


@dataclass(frozen=True)
class Witness:
    source: Independent
    target: Correlated

    def valid(self):
        return self.target.parent == self.source and self.target.rule == 'multiply-by-1+b*zeta*r12'


def generate(source):
    if source.parameters.zeta <= 0 or source.parameters.b < 0:
        raise ValueError('outside the frozen variational domain')
    target=Correlated(source)
    witness=Witness(source,target)
    assert witness.valid()
    return target,witness


def readout(packet):
    # Only compiled pair-state data supplies the polynomial, its derivative
    # and retained source parameters. No result or reference mass is read here.
    p=packet.parent.parameters
    x={(1,0,0):F(1)};y={(0,1,0):F(1)};z={(0,0,1):F(1)}
    r1=scale(add(x,y),F(1,2));r2=scale(add(x,z),F(1,2));u=scale(add(y,z),F(1,2))
    measure=mul(r1,r2,u)
    factor=add(ONE,scale(u,p.b));derivative=p.b
    square=mul(factor,factor)
    cos_weight=scale(add(mul(r2,add(mul(r1,r1),scale(mul(r2,r2),-1),mul(u,u))),
                         mul(r1,add(mul(r2,r2),scale(mul(r1,r1),-1),mul(u,u)))),F(1,2))
    potential=add(scale(mul(r2,u),-p.nuclear_charge),
                  scale(mul(r1,u),-p.nuclear_charge),mul(r1,r2))
    norm=integral(mul(measure,square))
    kinetic=integral(add(mul(measure,square),scale(measure,derivative**2),
                         scale(mul(cos_weight,factor),-derivative)))/norm
    v=integral(mul(potential,square))/norm
    energy=p.zeta**2*kinetic+p.zeta*v
    # Swapping electrons exchanges perimetric y,z; spatial factor is invariant.
    assert {(i,k,j):c for (i,j,k),c in factor.items()}==factor
    return energy,factor,norm


def main():
    with redirect_stdout(io.StringIO()): benchmark.main()
    expected=json.loads((ROOT/'results/helium-correlated-variational.json').read_text())
    source=Independent(Parameters(2,F(expected['selected']['zeta']),F(expected['selected']['b'])))
    target,witness=generate(source)
    energy,factor,norm=readout(target)
    assert energy==F(expected['selected']['energy'])
    assert target.parent is source and witness.source is source
    assert norm>0
    # Retained construction history distinguishes generated state from parent;
    # removing the pair relation is detectable by the physical readout.
    history=(witness,)
    assert len(history)==1 and history[0].target is target
    erased_source=replace(source,parameters=replace(source.parameters,b=F(0)))
    erased,erased_witness=generate(erased_source)
    erased_energy,_,_=readout(erased)
    assert erased_witness.valid() and erased_energy!=energy
    assert not Witness(source,erased).valid()
    # Changing parameters while claiming the old parent fails the adapter
    # certificate; it is not a new equivalence created by endpoint similarity.
    altered=Correlated(replace(source,parameters=replace(source.parameters,b=F(1))))
    assert not Witness(source,altered).valid()
    swapped=Correlated(replace(source,roles=source.roles[::-1]))
    swapped_energy,_,_=readout(swapped)
    assert swapped_energy==energy and swapped.parent.roles!=source.roles
    # Grid-selected parameters are supplied; no optimization occurs in WG.
    result=dict(schema='marici.nima.correlated-pair-wg.v1',status='pass',
                state={'nuclear_charge':2,'zeta':str(source.parameters.zeta),'b':str(source.parameters.b),
                       'roles':source.roles,'rule':target.rule,'retained_steps':len(history)},
                compiled_scaled_pair_polynomial={str(k):str(v) for k,v in factor.items()},
                energy_hartree=str(energy),binding_decimal_eV=expected['binding_decimal_eV'],
                erased_pair_energy_same_zeta=str(erased_energy),
                tests=['exact benchmark energy recovered','source and witness retained','electron exchange preserves spatial readout',
                       'pair erasure changes energy','false parent and parameter-substitution certificates rejected'],
                formal_boundary='Agda generic adapter checked separately; Python is a corresponding implementation, not verified extraction or a formal real-integral proof.',
                physical_boundary='Supplied variational parameters, pair kernel, spin-singlet interpretation and Coulomb Hamiltonian. WG packages/certifies the declared construction, not the physical selection of those inputs.')
    (ROOT/'results/correlated-pair-wg.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
