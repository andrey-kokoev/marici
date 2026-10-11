"""Conditional preparation of relative alignment by an existing source flip.

Initial J and the decision to act on one reference are explicit inputs. The
opposition is computed by conjugation, not assigned as a desired scalar sign.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,J,matrix
from check_four_packet_record_feedback import mm,transpose
ROOT=Path(__file__).resolve().parents[1]
I=matrix(UNIT);X=matrix(E2);j=matrix(J)


def mul(*args):
    out=I
    for a in args:out=mm(out,a)
    return out


def conj(g,a):return mul(g,a,transpose(g))
def readout(a,b):return tuple(tuple(v/2 for v in row) for row in mul(b,transpose(a)))
def tr(a):return a[0][0]+a[1][1]
def norm(a):return sum(x*x for row in a for x in row)


@dataclass(frozen=True)
class Preparation:
    a: tuple
    b: tuple
    history: tuple=()
    parent: 'Preparation | None'=None

    def flip(self,side):
        assert side in ('A','B')
        return Preparation(conj(X,self.a) if side=='A' else self.a,
                           conj(X,self.b) if side=='B' else self.b,
                           self.history+(side,),self)


def main():
    # Source truth tables already proved from actual retained edge witnesses.
    proof=ROOT/'agda/TetrahedralEdgeReadout.agda'
    receipt=json.loads((ROOT/'results/agda-TetrahedralEdgeReadout.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['inputs_stable_during_check']
    assert receipt['source_sha256']==hashlib.sha256(proof.read_bytes()).hexdigest()
    assert mul(X,X)==I
    seed=Preparation(j,j)
    first=seed.flip('A');returned=first.flip('A')
    assert (first.a,first.b)!=(seed.a,seed.b)
    assert (returned.a,returned.b)==(seed.a,seed.b)
    assert returned.history!=seed.history and returned.parent is first
    assert conj(X,first.a)==seed.a and first.parent is seed
    assert [tr(readout(p.a,p.b)) for p in (seed,first,returned)]==[F(1),F(-1),F(1)]
    assert all(norm(p.a)+norm(p.b)==4 for p in (seed,first,returned))
    # Complete finite parity family: absolute sign choices are not the signal.
    for a_bit,b_bit in product((0,1),repeat=2):
        p=seed
        if a_bit:p=p.flip('A')
        if b_bit:p=p.flip('B')
        assert tr(readout(p.a,p.b))==(-1)**(a_bit+b_bit)
        for g in (I,X):
            transported=readout(conj(g,p.a),conj(g,p.b))
            assert transported==conj(g,readout(p.a,p.b))
            assert tr(transported)==tr(readout(p.a,p.b))
    both=seed.flip('A').flip('B')
    assert both.a==both.b and tr(readout(both.a,both.b))==1
    result=dict(schema='marici.nima.reference-alignment-preparation.v1',status='pass',
        source_operation='Boolean flip from the existing tetrahedral edge transport contract; counting-basis matrix X',
        protocol='Prepare (J,J); conjugate exactly one reference by X; retain operation side, parent and history.',
        trace_sequence=['1','-1','1'],full_history_retained=True,inverse_by_same_flip=True,
        reference_frobenius_budget='4 throughout (not calibrated energy)',
        relative_parity='trace((1/2) B A^-1)=(-1)^(number of single-reference flips)',
        disposition='Given an initial retained J and a chosen one-reference intervention, the existing flip constructs opposed relative alignment and its inverse without inserting a target minus sign. Simultaneous frame conjugation leaves the relative signal unchanged.',
        limits='Explicit new preparation protocol using an existing operation, not a previously source-selected physical coupling. It does not derive J, choose the acted-on reference, supply autonomous timing, identify the seed seam with these reference matrices, or prove joint feedback budget conservation. Not an extraction of Agda execution.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'agda/TetrahedralEdgeReadout.agda','agda/GradedBoundaryCoherence.agda',
            'checkers/check_four_packet_cycle.py','checkers/check_reference_alignment_preparation.py')})
    (ROOT/'results/reference-alignment-preparation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
