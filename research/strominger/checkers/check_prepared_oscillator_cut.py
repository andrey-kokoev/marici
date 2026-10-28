"""Versioned preparation-bearing source adapter and exact regression tests."""
from dataclasses import replace
from pathlib import Path
import hashlib
import json
import sympy as s
from check_oscillator_family_promotion import promotion_api
from check_oscillator_fibration_cut import transfer

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/strominger/contracts/prepared-oscillator-cut.v2.json'
API=promotion_api()
Row=API['Row']
PORTS=((0,2),(1,2),(2,3),(0,3))
OCCUPATION=('occupation',1)
STATE_PORT=('bath-state',1)


def nonnegative(value):
    value=s.sympify(value)
    if value.is_real is not True or value.is_nonnegative is not True:
        raise ValueError('Occupation must be provably real and nonnegative')
    return value


def source(g,h,delta,n):
    g,h,delta=map(s.sympify,(g,h,delta))
    if g.is_positive is not True or h.is_positive is not True or delta.is_real is not True:
        raise ValueError('Expected positive real couplings and real detuning')
    n=nonnegative(n)
    chi=1/((g*g+h*h)/2-s.I*delta)
    coefficients=(g*chi,h*chi,-g,s.Integer(1))
    rows=tuple(Row(('leaf',i),(a,),(b,),v) for i,((a,b),v) in enumerate(zip(PORTS,coefficients)))
    return rows+(Row(OCCUPATION,STATE_PORT,STATE_PORT,n),)


def typed_records(raw):
    # No model or preparation argument: all state data come from this cut.
    records=API['leaves'](raw)
    expected={('leaf',i) for i in range(4)}|{OCCUPATION}
    if len(records)!=5 or {r.label for r in records}!=expected:
        raise ValueError('Missing, duplicate or unknown source role')
    by_label={r.label:r for r in records}
    for i,(a,b) in enumerate(PORTS):
        row=by_label[('leaf',i)]
        if row.source!=(a,) or row.target!=(b,) or row.mass!=1:
            raise ValueError('Invalid transfer role')
    occupation=by_label[OCCUPATION]
    if occupation.source!=STATE_PORT or occupation.target!=STATE_PORT or occupation.mass!=1:
        raise ValueError('Invalid preparation role')
    nonnegative(occupation.value)
    return by_label


def recover_source(raw):
    """Recover the four declared inputs and validate source-family membership.

    Validates recovered leaves, not consistency of all promotion summaries.
    Unknown symbolic admissibility is rejected rather than assumed.
    """
    records=typed_records(raw)
    a,b,c,d=(s.sympify(records[('leaf',i)].value) for i in range(4))
    g=s.simplify(-c)
    if g.is_positive is not True:
        raise ValueError('Invalid recovered external coupling')
    chi=s.simplify(a/g)
    if chi.is_zero is not False:
        raise ValueError('Susceptibility must be provably nonzero')
    h=s.simplify(b/chi)
    delta=s.simplify(s.I*(1/chi-(g*g+h*h)/2))
    n=nonnegative(records[OCCUPATION].value)
    rebuilt=source(g,h,delta,n) # checks parameter admissibility
    if any(s.simplify(records[r.label].value-r.value)!=0 for r in rebuilt):
        raise ValueError('Coefficients do not belong to the declared source family')
    return g,h,delta,n


def readout(raw):
    _,_,_,n=recover_source(raw)
    by_label=typed_records(raw)
    edges=tuple((by_label[('leaf',i)].value,a,b) for i,(a,b) in enumerate(PORTS))
    rr,qq=transfer(edges,0,3),transfer(edges,1,3)
    weight=s.simplify(qq*s.conjugate(qq))
    return {'r':rr,'q':qq,'occupation':n,
            'commutator':s.simplify(rr*s.conjugate(rr)+weight),
            'added_occupation':s.simplify(weight*n)}


def stages(rows,policy):
    first=API['incoming_promotion'](rows,1,policy)
    return rows,first,API['incoming_promotion'](first,2,policy)


def replace_occupation(rows,value):
    # Poison only the actual retained preparation; no original source fallback.
    return tuple(replace(r,members=replace_occupation(r.members,value)) if r.members
                 else replace(r,value=value) if r.label==OCCUPATION else r for r in rows)


def must_reject(rows):
    try:
        readout(rows)
    except ValueError:
        return
    raise AssertionError('Invalid preparation silently accepted')


def main():
    g,h=s.symbols('g h',positive=True,real=True)
    d=s.symbols('delta',real=True)
    n=s.symbols('n',nonnegative=True,real=True)
    symbolic=source(g,h,d,n)
    expected=readout(symbolic)
    chi=1/((g*g+h*h)/2-s.I*d)
    assert s.simplify(expected['added_occupation']-g*g*h*h*chi*s.conjugate(chi)*n)==0
    assert expected['commutator']==1
    reports={}
    for policy in ('inherited','common'):
        levels=stages(symbolic,policy)
        for rows in levels:
            assert API['leaves'](rows)==symbolic
            by_from,by_to=(API['indexed'](rows,field) for field in ('source','target'))
            assert API['indexed'](API['unindex'](by_from),'target')==by_to
            for presentation in (rows,API['unindex'](by_from),API['unindex'](by_to)):
                assert readout(presentation)==expected
                assert recover_source(presentation)==(g,h,d,n)
                rebuilt=source(*recover_source(presentation))
                assert rebuilt==symbolic
        # Equal response/noise magnitudes at opposite detuning must not
        # collapse the retained phase-sensitive source or its reconstruction.
        plus=stages(source(1,2,3,1),policy)[-1]
        minus=stages(source(1,2,-3,1),policy)[-1]
        assert readout(plus)['added_occupation']==readout(minus)['added_occupation']
        assert plus!=minus
        assert recover_source(plus)==(1,2,3,1)
        assert recover_source(minus)==(1,2,-3,1)
        for label,value in ((('leaf',3),2),(('leaf',0),0),(('leaf',2),1),(('leaf',1),s.I)):
            bad=tuple(replace(r,value=s.sympify(value)) if r.label==label else r
                      for r in source(1,2,0,1))
            must_reject(stages(bad,policy)[-1])
        vacuum=stages(source(1,2,0,0),policy)[-1]
        thermal=stages(source(1,2,0,s.Rational(3,2)),policy)[-1]
        assert vacuum!=thermal
        for field in ('source','target'):
            assert API['indexed'](vacuum,field)!=API['indexed'](thermal,field)
        assert readout(vacuum)['added_occupation']==0
        assert readout(thermal)['added_occupation']==s.Rational(24,25)
        changed=replace_occupation(thermal,s.Integer(2))
        assert readout(changed)['added_occupation']==s.Rational(32,25)
        assert readout(changed)['r']==readout(thermal)['r']
        # Stale summary values cannot hide a modified nested preparation.
        assert tuple(r.value for r in changed)==tuple(r.value for r in thermal)
        must_reject(replace_occupation(thermal,s.Integer(-1)))
        missing=tuple(r for r in source(1,2,0,1) if r.label!=OCCUPATION)
        must_reject(stages(missing,policy)[-1])
        duplicate=source(1,2,0,1)+(source(1,2,0,1)[-1],)
        must_reject(stages(duplicate,policy)[-1])
        malformed=source(1,2,0,1)[:-1]+(replace(source(1,2,0,1)[-1],target=(1,)),)
        must_reject(stages(malformed,policy)[-1])
        reports[policy]={'record_counts':[len(x) for x in levels],
                         'all_three_presentations_at_all_three_depths':True,
                         'declared_inputs_recovered_symbolically':True,
                         'source_reencode_roundtrip':True,
                         'opposite_detuning_same_noise_distinguished':True,
                         'malformed_coefficient_controls_rejected':4,
                         'vacuum_thermal_cut_collision_removed':True,
                         'added_occupations':['0','24/25'],
                         'nested_preparation_change_readout':'32/25',
                         'rejects':['missing occupation','duplicate occupation','negative occupation','wrong preparation port']}
    paths=[CONTRACT,'research/nima/checkers/check_rung_transport_diagram.py',
           'research/aspect/markov-oscillator-loss-noise-identity.md',
           'research/strominger/checkers/check_oscillator_family_promotion.py',
           'research/strominger/checkers/check_oscillator_fibration_cut.py',
           str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','contract':CONTRACT,'policies':reports,
            'general_symbolic_added_occupation':str(expected['added_occupation']),
            'scope':'Executable source-schema adapter plus supplied analytic law; not native WG derivation or universal domain determination.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/prepared-oscillator-cut/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
