#!/usr/bin/env python3
"""Conditional period-current preflight; never substitutes for physical source selection."""
import copy
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/benincasa/contracts/history6-current-contour-admission.v1.json'
LATTICE='research/benincasa/results/history6_current_projective_lattice.json'
TRANSPORT='research/benincasa/results/history6_current_gl3_transport.json'
CORNER='research/benincasa/results/history6_quotient_boundary.json'
FLAGS='research/benincasa/results/history6_current_ordered_lifts.json'


def main():
    contract=json.loads((ROOT/CONTRACT).read_text());receipts={p:json.loads((ROOT/p).read_text()) for p in (LATTICE,TRANSPORT,CORNER,FLAGS)}
    for p,receipt in receipts.items():
        assert receipt['passed']
        for source,h in receipt['source_sha256'].items():assert sha256((ROOT/source).read_bytes()).hexdigest()==h,source
    assert receipts[TRANSPORT]['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_gl3_transport.py').read_bytes()).hexdigest()
    lattice=receipts[LATTICE];P=s.Matrix(lattice['split_period_matrix']);forget=s.Matrix([lattice['canonical_forgetful_map']])
    assert s.ones(1,2)*P==forget
    corner=receipts[CORNER]['source_corner_extraction']
    assert contract['owning_regular_corner_word']==corner['deleted_order']
    conditional=contract['conditional_append_b3'];word=conditional['deletion_word']
    matched=next(flag for flag in lattice['all_six_source_flags'] if flag['word']==word)
    raw=next(flag for flag in receipts[FLAGS]['ordered_flags'] if flag['deletion_word']==word)
    assert conditional['fixed_oriented_cycle_coordinates']==matched['cycle_basis_coordinates']
    assert conditional['projective_split_periods']==matched['split_periods']
    assert conditional['raw_source_eight_form_deletion_parity']==raw['source_eight_form_deletion_parity']
    before=contract['before_contour'];after=contract['after_contour']
    assert before['graded_degree']==before['fiber_form_degree']-before['external_codimension']==-1
    assert after['graded_degree']==after['fiber_form_degree']-after['external_codimension']==-3
    assert after['graded_degree']==before['graded_degree']-2
    assert contract['fermionic_degree']==8 and contract['Berezin_normalization']==2880
    # A mechanical preflight can validate conditional data; it does not
    # verify a physical selection. That gate remains explicitly null.
    selection=contract['physical_selection']
    missing=[key for key,value in selection.items() if value is None and key!='endpoint_branch_regularization_if_using_real_relative_chain']
    assert selection['status']=='not_admitted' and len(missing)==6
    def preflight(candidate):
        defects=[];coords=candidate.get('cycle_coordinates')
        if not isinstance(coords,list) or len(coords)!=4 or any(type(q) is not int for q in coords):
            return {'conditional_pass':False,'physical_admitted':False,'defects':['four_integral_cycle_coordinates_required'],'missing_physical_data':missing}
        c=s.Matrix(coords)
        if (forget*c)[0]!=contract['canonical_source_class']:defects.append('canonical_source_class_changed')
        claim=candidate.get('conditional_word')
        if claim is not None:
            flags=[flag for flag in lattice['all_six_source_flags'] if flag['word']==claim]
            if not flags or flags[0]['cycle_basis_coordinates']!=coords:defects.append('conditional_word_full_cycle_mismatch')
        if candidate.get('graded_degree')!=-3 or candidate.get('external_codimension')!=3 or candidate.get('ordinary_superfunction',False):
            defects.append('period_current_codomain_or_grade_changed')
        if candidate.get('physical_selection_asserted',False):defects.append('physical_selection_unsubstantiated_by_owning_source')
        return {'conditional_pass':not defects,'physical_admitted':False,'defects':defects,
            'projective_period_pair':[int(q) for q in P*c],
            'external_E7_period_pair_over_A3_delta3':[int(q) for q in -P*c],
            'canonical_class':int((forget*c)[0]),'missing_physical_data':missing}
    candidate={'cycle_coordinates':conditional['fixed_oriented_cycle_coordinates'],
        'conditional_word':word,'graded_degree':-3,'external_codimension':3,'ordinary_superfunction':False}
    good=preflight(candidate);assert good['conditional_pass'] and not good['physical_admitted']
    tests=[]
    bad=copy.deepcopy(candidate);bad['cycle_coordinates']=[0,1,0,0]
    # Another actual source flag has identical split periods but differs by
    # RD_double, invisible to both splits. It is not the claimed word.
    assert P*s.Matrix(bad['cycle_coordinates'])==P*s.Matrix(candidate['cycle_coordinates'])
    tests.append(('invisible_class_removed_but_same_word_claimed',bad,'conditional_word_full_cycle_mismatch'))
    bad=copy.deepcopy(candidate);bad['cycle_coordinates']=[0,0,1,0];bad['conditional_word']=None
    assert P*s.Matrix(bad['cycle_coordinates'])==s.zeros(2,1)
    tests.append(('nonzero_simultaneous_zero_cycle_fitted',bad,'canonical_source_class_changed'))
    bad=copy.deepcopy(candidate);bad['graded_degree']=-1
    tests.append(('fiber_integration_degree_not_lowered',bad,'period_current_codomain_or_grade_changed'))
    bad=copy.deepcopy(candidate);bad['ordinary_superfunction']=True;bad['external_codimension']=0
    tests.append(('singular_support_discarded',bad,'period_current_codomain_or_grade_changed'))
    bad=copy.deepcopy(candidate);bad['physical_selection_asserted']=True
    tests.append(('conditional_completion_promoted_by_boolean',bad,'physical_selection_unsubstantiated_by_owning_source'))
    bad=copy.deepcopy(candidate);bad['cycle_coordinates']=[0,1,s.Rational(1,2),0]
    # Materialized test input uses a JSON-safe string; still fails integrality.
    bad['cycle_coordinates'][2]='1/2'
    tests.append(('fractional_lift_without_integral_cycle',bad,'four_integral_cycle_coordinates_required'))
    hostile=[]
    for name,bad,expected in tests:
        result=preflight(bad);assert not result['conditional_pass'] and expected in result['defects'] and not result['physical_admitted']
        hostile.append({'id':name,'candidate':bad,'result':result})
    # Evaluate all actual conditional flags, without claiming any is selected.
    all_flags=[]
    for flag in lattice['all_six_source_flags']:
        item={'cycle_coordinates':flag['cycle_basis_coordinates'],'conditional_word':flag['word'],
            'graded_degree':-3,'external_codimension':3,'ordinary_superfunction':False}
        outcome=preflight(item);assert outcome['conditional_pass'] and not outcome['physical_admitted']
        all_flags.append({'word':flag['word'],'full_cycle_coordinates':flag['cycle_basis_coordinates'],'result':outcome})
    # Current periods know only P*c, while the contract retains c itself.
    # Zero periods always imply source class0, even for nonzero H2 cycles.
    kernel=s.Matrix(lattice['simultaneous_split_period_kernel_basis_columns'])
    assert P*kernel==s.zeros(2,2) and forget*kernel==s.zeros(1,2)
    paths=[CONTRACT,LATTICE,TRANSPORT,CORNER,FLAGS,'research/benincasa/checkers/check_history6_current_gl3_transport.py']
    out={'schema':'marici.benincasa.history6-current-contour-admission.v1','history_index':6,
        'conditional_completed_corner':{'candidate':candidate,'result':good},
        'all_conditional_flags':all_flags,'rejected_hostiles':hostile,
        'period_current_type':'Fiber2 integrated to fiber0; external codim3 remains, grade_minus3, fermionicdegree8 with normalization2880; no ordinary superfunction.',
        'simultaneous_zero_shortcut':'Nonzero simultaneous-zero H2 classes exist, but all map to canonical source class0. They cannot replace a lift of the fixed class1.',
        'missing_physical_data':missing,'physical_admitted':False,
        'passed':True,'claim_boundary':'Conditional contour/current preflight and exact source-word/full-cycle/grade controls; not physical admission. Null owning-source/external/gluing data remain required rather than fabricated.',
        'next_action':contract['next_action'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_contour_admission.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'conditional_append_b3_cycle':candidate['cycle_coordinates'],
        'conditional_period_current_pair':good['external_E7_period_pair_over_A3_delta3'],
        'grade_after_contour':-3,'hostiles_rejected':len(hostile),'conditional_flags':len(all_flags),
        'physical_admitted':False,'missing_physical_data':missing},indent=2))

if __name__=='__main__':main()
