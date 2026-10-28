"""Collision test of the frozen complete intrinsic coefficient cut.
No ThreeWitnessRetainedCone or geometry wrapper is imported or constructed.
"""
from pathlib import Path
from dataclasses import dataclass
import hashlib
import json
import sympy as s
from check_oscillator_family_promotion import promotion_api
from check_oscillator_fibration_cut import transfer

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/strominger/contracts/intrinsic-cut-oscillator-falsifier.v1.json'
API=promotion_api()
Row=API['Row']


@dataclass(frozen=True)
class Prepared:
    g: object
    h: object
    delta: object
    occupation: object


def coefficient_rows(model):
    # Exactly the existing preparation of the four transfer-coefficient records.
    # Occupation is deliberately NOT inserted after seeing the hostile.
    chi=1/((model.g**2+model.h**2)/2-s.I*model.delta)
    return tuple(Row(('leaf',i),(a,),(b,),v) for i,(v,a,b) in enumerate(((model.g*chi,0,2),(model.h*chi,1,2),(-model.g,2,3),(s.Integer(1),0,3))))


def expose(model,policy):
    raw=coefficient_rows(model)
    first=API['incoming_promotion'](raw,1,policy)
    second=API['incoming_promotion'](first,2,policy)
    return second,API['indexed'](second,'source'),API['indexed'](second,'target')


def coefficient_read(cut):
    rows=API['leaves'](cut[0])
    coefficients=tuple((r.value,r.source[0],r.target[0]) for r in rows)
    return transfer(coefficients,0,3),transfer(coefficients,1,3)


def main():
    frozen=(ROOT/CONTRACT).read_bytes()
    vacuum=Prepared(s.Integer(1),s.Integer(2),s.Integer(0),s.Integer(0))
    thermal=Prepared(s.Integer(1),s.Integer(2),s.Integer(0),s.Rational(3,2))
    assert vacuum!=thermal
    results={}
    for policy in ('inherited','common'):
        left,right=expose(vacuum,policy),expose(thermal,policy)
        assert left==right # includes the ENTIRE retained member trees
        assert API['unindex'](left[1])==API['unindex'](left[2])==left[0]
        assert API['indexed'](API['unindex'](left[1]),'target')==left[2]
        assert API['leaves'](left[0])==coefficient_rows(vacuum)
        assert API['leaves'](right[0])==coefficient_rows(thermal)
        rr,qq=coefficient_read(left)
        assert rr==s.Rational(3,5) and qq==-s.Rational(4,5)
        weight=s.simplify(qq*s.conjugate(qq))
        assert weight==s.Rational(16,25)
        added_vac=s.simplify(weight*vacuum.occupation)
        added_thermal=s.simplify(weight*thermal.occupation)
        assert added_vac==0 and added_thermal==s.Rational(24,25)
        assert added_vac!=added_thermal
        changed=Prepared(s.Integer(1),s.Integer(3),s.Integer(0),s.Integer(0))
        assert expose(changed,policy)!=left
        assert coefficient_read(expose(changed,policy))!=(rr,qq)
        # Same source maps and exact shared rows suffice; not merely isomorphic
        # shapes, identical means, or equality of a chosen scalar observation.
        results[policy]={'complete_cut_equal':True,'source_member_trees_equal':True,
                         'intrinsic_presentation_triangle_commutes':True,
                         'r':str(rr),'q':str(qq),'bath_transfer_weight':str(weight),
                         'added_occupation_vacuum':str(added_vac),
                         'added_occupation_thermal':str(added_thermal),
                         'changed_coupling_is_detected':True}
    n=s.symbols('n',nonnegative=True,real=True)
    assert s.diff(s.Rational(16,25)*n,n)==s.Rational(16,25)
    assert (ROOT/CONTRACT).read_bytes()==frozen
    sources=[CONTRACT,'research/aspect/markov-oscillator-loss-noise-identity.md',
             'research/aspect/checkers/markov_oscillator_loss_noise_identity.py',
             'research/nima/checkers/check_rung_transport_diagram.py',
             'research/strominger/checkers/check_oscillator_family_promotion.py',
             str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','scientific_disposition':'frozen_cut_not_faithful_on_prepared_thermal_models',
            'policies':results,
            'obstruction':'The cut is independent of n while required added occupation is 16*n/25. Hence no function of this cut alone equals that observation for every admitted n.',
            'surviving_scope':'Intrinsic presentation triangle and coefficient-domain recovery survive. No counterexample to existence of another WG cut retaining bath occupation is claimed.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/intrinsic-cut-oscillator-falsifier/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
