"""Conditional preparation/coupling/interrogation using existing source maps.

An existing Cl(2,0) representation types record values as2x2 operators. Source
resource, provenance and identification with boundary A->B remain explicit.
No physical pulse, detector, clock or absolute normalization is selected here.
"""
from dataclasses import dataclass
from pathlib import Path
from fractions import Fraction
import sys

NIMA=Path(__file__).resolve().parents[2]/'nima/checkers'
if str(NIMA) not in sys.path: sys.path.insert(0,str(NIMA))
import check_four_packet_cycle as algebra
import check_four_packet_record_feedback as memory


@dataclass(frozen=True)
class ReferenceProtocol:
    state: memory.RetainedState
    preparation: tuple
    events: tuple = ()

    def advance(self):
        return ReferenceProtocol(self.state.advance(),self.preparation,
                                 self.events+('existing-conservative-exchange',))

    def interrogate(self, mode, readout_policy='normalized'):
        if mode == 'stored':
            bank=self.state.record
        elif mode == 'delayed':
            bank=memory.left_rotate(self.state.record)
        else:
            raise ValueError('Specify stored or delayed record port')
        if readout_policy == 'normalized':
            value=memory.readout(bank)
        elif readout_policy == 'raw-sewing':
            value=algebra.sew(bank)
        else:
            raise ValueError('Specify normalized or raw-sewing readout policy')
        return {'value':value,'operator':algebra.matrix(value),'mode':mode,
                'readout_policy':readout_policy,
                'depth':self.state.depth,'events':self.events,
                'preparation':self.preparation}

    def recover_initial(self):
        state=self.state
        while state.parent is not None:
            if memory.inverse_cycle(state.carrier,state.record)!=(state.parent.carrier,state.parent.record):
                raise ValueError('Retained parent fails source inverse')
            state=state.parent
        return state


def prepare(carrier, bank, provenance):
    if not provenance:
        raise ValueError('Explicit source-resource provenance required')
    carrier=algebra.vector(carrier)
    if len(bank)!=16:
        raise ValueError('Explicit sixteen-slot bank required')
    bank=tuple(Fraction(v) for v in bank)
    return ReferenceProtocol(memory.RetainedState(carrier,bank),tuple(provenance))


def inverse_operator(operator):
    a,b=operator[0];c,d=operator[1]
    det=a*d-b*c
    if det==0:
        raise ValueError('Record operator is singular; no strict inverse return')
    return ((d/det,-b/det),(-c/det,a/det))
