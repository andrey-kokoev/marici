"""Bounded representation test of the existing relational anomaly-inflow packet.
Anomaly matching and its admissibility assumptions are supplied physics, not derived.
"""
from pathlib import Path
from itertools import product, permutations
import copy
import hashlib
import json
import sympy as s
from check_oscillator_retained_cone import API, Row, build, triangle_decode
from check_oscillator_fcc_representation import encode, decode

ROOT=Path(__file__).resolve().parents[3]
FIELDS=('level','normal','flavor_sign','symmetry_preserved','gap_open')


def source(k,eta,J,symmetry=True,gap=True):
    values=(k,eta,J,int(symmetry),int(gap))
    # Canonical field table: these are record ports, not spatial/physical edges.
    return tuple(Row(('field',name),('packet',),('field_port',name),s.Integer(value)) for name,value in sorted(zip(FIELDS,values)))


def present(raw,policy):
    return API['incoming_promotion'](API['incoming_promotion'](raw,1,policy),2,policy)


def read(packet):
    leaves=API['leaves'](packet)
    if len(leaves)!=len(FIELDS) or {r.label for r in leaves}!={('field',x) for x in FIELDS}:
        raise ValueError('Incomplete domain record')
    values={r.label[1]:int(r.value) for r in leaves}
    if values['normal'] not in (-1,1) or values['flavor_sign'] not in (-1,1):
        raise ValueError('Invalid orientation')
    if any(values[x] not in (0,1) for x in ('symmetry_preserved','gap_open')):
        raise ValueError('Invalid admission flag')
    current=values['level']*values['normal']*values['flavor_sign']
    return values, -current, current


def require_matching(packet,k_ir):
    values,_,_=read(packet)
    # A supplied matching contract is being validated, not computed from a UV QFT.
    if not values['symmetry_preserved'] or not values['gap_open']:
        raise ValueError('Outside declared matching regime')
    if values['level']!=k_ir:
        raise ValueError('Matching contract violated')
    return k_ir


def main():
    results={}
    for policy in ('inherited','common'):
        checked=0
        for k,eta,J in product((-3,0,3),(-1,1),(-1,1)):
            raw=source(k,eta,J)
            p=present(raw,policy)
            vertices=build(p)
            for chart in permutations(range(4)):
                decorated=copy.deepcopy(encode(vertices,chart))
                recovered=decode(decorated)
                triangle=copy.deepcopy(recovered[1:])
                restored=triangle_decode(triangle)
                assert API['leaves'](restored)==raw
                values,energy,current=read(restored)
                assert (energy,current)==(-k*eta*J,k*eta*J)
                assert require_matching(restored,k)==k
                checked+=1
        pplus=present(source(3,1,1),policy)
        pminus=present(source(3,-1,-1),policy)
        assert pplus!=pminus
        assert read(pplus)[2]==read(pminus)[2]==3
        assert read(pplus)[0]['flavor_sign']!=read(pminus)[0]['flavor_sign']
        # The whole four-state source is retained; selecting a reference is explicit.
        states=[(eta,J) for eta,J in product((-1,1),repeat=2)]
        energies={state:read(present(source(3,*state),policy))[1] for state in states}
        minima=[state for state in states if energies[state]==min(energies.values())]
        assert set(minima)=={(-1,-1),(1,1)}
        assert [state for state in minima if state[0]==1]==[(1,1)]
        assert {read(present(source(0,*state),policy))[1] for state in states}=={0}
        # Mirror transport acts on retained fields; encode/decode does not fix a frame.
        for eta,J in states:
            original=present(source(3,eta,J),policy)
            mirror=present(source(3,-eta,-J),policy)
            for p in (original,mirror):
                assert triangle_decode(decode(encode(build(p),(2,0,3,1)))[1:])==p
            assert read(original)[2]==read(mirror)[2]
        # Missing orientation is not reconstructible from the equal scalar current.
        erased=tuple(r for r in source(3,1,1) if r.label!=('field','normal'))
        try:
            read(present(erased,policy))
        except ValueError:
            pass
        else:
            raise AssertionError('Orientation erasure accepted')
        rejected=0
        for p,kir in ((pplus,4),(present(source(3,1,1,symmetry=False),policy),3),(present(source(3,1,1,gap=False),policy),3)):
            try:
                require_matching(p,kir)
            except ValueError:
                rejected+=1
            else:
                raise AssertionError('Invalid matching contract accepted')
        assert rejected==3
        # Existing vectorlike-pair arithmetic, not a derivation of QFT decoupling.
        assert 3+1-1==3
        results[policy]={'decorated_charts_checked':checked,'source_states_per_level':4,
                         'levels_tested':[-3,0,3],'mirror_pair_retained':True,
                         'reference_selection_explicit':True,'matching_contract_rejections':rejected,
                         'scalar_current_not_faithful':True,'missing_orientation_rejected':True}
    sources=['research/flavor/flavor-anomaly-inflow-relational-orientation-audit.md',
             'research/flavor/checkers/wp807_anomaly_inflow_relational_orientation_audit.py',
             'research/strominger/checkers/check_oscillator_fcc_representation.py',
             'research/strominger/checkers/check_oscillator_retained_cone.py',
             'research/strominger/checkers/check_oscillator_family_promotion.py',
             str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','scope':'Finite relational-inflow source packet represented through two family promotions, retained cone and decorated FCC cell.',
            'policies':results,'anomaly_matching_derived':False,
            'boundary':'Quantized level, response formula and matching hypotheses are supplied. No UV/IR QFT, full anomaly polynomial, spatial boundary geometry or calibrated detector derived.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/anomaly-domain-cut/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
