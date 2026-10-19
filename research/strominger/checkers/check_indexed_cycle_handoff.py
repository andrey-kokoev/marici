"""Exhaust indexed-sector completions; separately test actual native returns.
No physical sector, particle, spin or clock is inferred from a finite automaton.
"""
from fractions import Fraction as F
from itertools import product as cartesian
from hashlib import sha256
from pathlib import Path
import json
import sys

from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,read_operator,product,integer_trace,encode
from check_port_incidence_conjectures import factor,identity,transpose

CONTRACT=ROOT/'research/strominger/contracts/indexed-cycle-handoff.v1.json'
OUT=ROOT/'research/strominger/results/indexed-cycle-handoff-v1.json'
PRIOR=ROOT/'research/strominger/results/port-incidence-conjectures-v1.json'
BITS=(0,1);STATES=tuple(cartesian(BITS,repeat=2))
FUNCTIONS=tuple(cartesian(BITS,repeat=2))
FLIP=(1,0);SAME=(0,1)
OBS={'proton':(1,0,1),'neutron':(0,1,0),'electron':(0,1,1)}


def digest(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dense_product(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def dense_transpose(a):return list(map(list,zip(*a)))
def from_dense(a):return {(i,j):A(F(x)) for i,row in enumerate(a) for j,x in enumerate(row) if x}
def kron(a,b,rows_b,cols_b):return {(i*rows_b+k,j*cols_b+l):x*y for (i,j),x in a.items() for (k,l),y in b.items()}
def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def recurrence(handoffs,state):
    sector,mode=state
    return handoffs[mode][FLIP[sector]],mode


def finite_checks():
    shared_crossings=[a for a in FUNCTIONS if all(a[s]==middle for s,middle,end in OBS.values())]
    assert shared_crossings==[FLIP]
    context_free=[h for h in FUNCTIONS if all(h[middle]==end for s,middle,end in OBS.values())]
    assert context_free==[]
    assert OBS['neutron'][1]==OBS['electron'][1] and OBS['neutron'][2]!=OBS['electron'][2]
    models=[]
    for h0,h1,p_mode in cartesian(FUNCTIONS,FUNCTIONS,BITS):
        modes={'proton':p_mode,'neutron':0,'electron':1};hs=(h0,h1)
        if not all(hs[modes[name]][middle]==end for name,(s,middle,end) in OBS.items()):continue
        models.append({'handoffs':hs,'modes':modes,
            'cycle_map':[recurrence(hs,state) for state in STATES],
            'each_handoff_bijective':all(len(set(h))==2 for h in hs)})
    assert len(models)==4
    reversible=[m for m in models if m['each_handoff_bijective']]
    assert len(reversible)==1
    chosen=reversible[0]
    assert chosen['handoffs']==(FLIP,SAME) and chosen['modes']=={'proton':0,'neutron':0,'electron':1}
    for s,b in STATES:assert recurrence(chosen['handoffs'],(s,b))==(s^b,b)
    fixed=[state for state in STATES if recurrence(chosen['handoffs'],state)==state]
    assert fixed==[(0,0),(1,0)]
    orbit=[(0,1)]
    for _ in range(2):orbit.append(recurrence(chosen['handoffs'],orbit[-1]))
    assert orbit==[(0,1),(1,1),(0,1)]
    for model in models:
        trace=[(0,1)]
        for _ in range(3):trace.append(recurrence(model['handoffs'],trace[-1]))
        model['electron_cycle_entry_trace']=trace
        if not model['each_handoff_bijective']:
            assert model['handoffs'][1]==(1,1) and trace==[(0,1),(1,1),(1,1),(1,1)]
    equivariant=[h for h in FUNCTIONS if all(h[FLIP[s]]==FLIP[h[s]] for s in BITS)]
    assert equivariant==[SAME,FLIP]
    assert set(equivariant)=={h for h in FUNCTIONS if len(set(h))==2}
    def dual(state):return state[0]^1,state[1]
    assert dual((1,0))==(0,0) and dual((0,1))==(1,1)
    assert all(recurrence(chosen['handoffs'],dual(s))==dual(recurrence(chosen['handoffs'],s)) for s in STATES)
    p_half=[1,0]*3;n_half=[0,1]*3
    assert p_half[1:]+p_half[:1]==n_half and p_half!=n_half
    # A globally reversible finite circuit can have constant-C coarse handoff:
    # after crossing, swap the sector with a fresh register initialized to C.
    def circuit(initial):
        state=list(initial);trace=[]
        for memory in range(1,len(state)):
            state[0]^=1
            middle=state[0]
            state[0],state[memory]=state[memory],state[0]
            trace.append((middle,state[0]))
        return tuple(state),trace
    worlds=tuple(cartesian(BITS,repeat=4))
    assert len({circuit(w)[0] for w in worlds})==len(worlds)==16
    environment_output,environment_trace=circuit((0,1,1,1))
    assert environment_trace==[(1,1),(0,1),(0,1)]
    assert environment_trace[0]==OBS['electron'][1:] and environment_trace[1][1]!=0
    X=[[F(0),F(1)],[F(1),F(0)]]
    J=[[F(0),F(-1)],[F(1),F(0)]]
    I=[[F(1),F(0)],[F(0),F(1)]]
    assert dense_product(dense_transpose(X),X)==I==dense_product(dense_transpose(J),J)
    assert [[abs(x) for x in row] for row in X]==[[abs(x) for x in row] for row in J]
    assert dense_product(X,X)==I
    assert dense_product(J,J)==[[-x for x in row] for row in I]
    assert dense_product(X,[[F(1)],[F(1)]])==[[F(1)],[F(1)]]
    assert dense_product(X,[[F(1)],[F(-1)]])==[[F(-1)],[F(1)]]
    return {'sector_encoding':{'M':0,'C':1},'observations':OBS,
        'shared_crossing':FLIP,'context_free_handoff_count':0,
        'minimum_handoff_contexts':2,'labelled_completions_examined':32,
        'fitting_completions':models,'reversible_completion_count':1,
        'minimal_reversible_recurrence':'F(s,b)=(s XOR b,b)',
        'minimal_state_order':STATES,'fixed_points':fixed,'electron_two_cycle':orbit,
        'global_reversible_environment_countermodel':{'fresh_memory_initialization':[1,1,1],
            'initial_sector':0,'half_step_then_handoff_trace':environment_trace,
            'final_full_state':environment_output,'full_circuit_state_count':16},
        'same_sector_permutation_unitary_lifts':{'X':X,'X_squared':I,'J':J,'J_squared':[[-x for x in row] for row in I]},
        'physical_spin_or_time_selected':False}


def native_checks():
    previous=read(PRIOR)
    assert previous['status']=='pass' and all(previous['checks'].values())
    pins=dict(previous['source_sha256'])
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale native comparison'
    pins[PRIOR.relative_to(ROOT).as_posix()]=digest(PRIOR)
    X=from_dense([[0,1],[1,0]]);I2=identity(2)
    rows={};all_assignment_choices=set()
    for name in OBS:
        path=ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json'
        source=read(path);pins[path.relative_to(ROOT).as_posix()]=digest(path)
        n=len(source['source']['metric']);metric=tuple(map(F,source['source']['metric']))
        ops={stage:read_operator(source['operators'][stage],n) for stage in 'LGN'}
        N=ops['N']
        assert product(N,N)==N and N
        f=factor(N,n,metric);K,D,H=f['K'],f['D'],f['gram'];r=f['rank']
        assert r=={'proton':1,'neutron':1,'electron':2}[name]
        for stage in 'LGN':assert product(ops[stage],K)==K
        assert product(N,product(N,K))==K
        witness={(i,0):x for (i,j),x in K.items() if j==0}
        assert witness and all(product(ops[stage],witness)==witness for stage in 'LGN')
        # Thus a raw-state-only reader has the same input at differently labelled
        # stages; it cannot recover the proposed changing sector without context.
        desired={'proton':[1,0,1],'neutron':[0,1,0],'electron':[0,1,1]}[name]
        assert len(set(desired))==2
        stage_ranks=[integer_trace(ops[stage]) for stage in 'LGN']
        assert stage_ranks[0]!=stage_ranks[1]
        # Explicit supplied tag register. All equations are restricted to the
        # encoded native return image, not arbitrary raw states.
        KT=kron(I2,K,n,r);DT=kron(I2,D,r,n)
        assert product(DT,KT)==identity(2*r)
        raw_metric={(i,i):A(metric[i%n]) for i in range(2*n)}
        tag_gram=kron(I2,H,r,r)
        assert product(transpose(KT,True),product(raw_metric,KT))==tag_gram
        crossing=kron(X,N,n,n);logical_crossing=kron(X,identity(r),r,r)
        assert product(crossing,KT)==product(KT,logical_crossing)
        mode_results=[]
        for mode,h in ((0,X),(1,I2)):
            handoff=kron(h,N,n,n);logical_handoff=kron(h,identity(r),r,r)
            assert product(handoff,KT)==product(KT,logical_handoff)
            cycle=product(handoff,product(crossing,KT))
            logical_cycle=product(logical_handoff,logical_crossing)
            assert cycle==product(KT,logical_cycle)
            assert product(transpose(logical_cycle,True),product(tag_gram,logical_cycle))==tag_gram
            assert product(DT,cycle)==logical_cycle
            assert product(handoff,product(crossing,cycle))==KT
            mode_results.append({'mode':mode,'logical_cycle':encode(logical_cycle)})
            all_assignment_choices.add((name,mode))
        # Forgetting the tag merges two distinct encoded preparations.
        mcopy={(i,0):x for (i,j),x in witness.items()}
        ccopy={(i+n,0):x for (i,j),x in witness.items()}
        assert mcopy!=ccopy
        forget={(i,k):x for (i,j),x in N.items() for k in (j,n+j)}
        assert product(forget,mcopy)==product(forget,ccopy)==witness
        rows[name]={'source':path.relative_to(ROOT).as_posix(),'raw_coordinates':n,
            'native_stage_image_ranks':stage_ranks,'active_return_rank':r,
            'native_cycle_idempotent':True,'native_active_payload_period':1,
            'active_encoder':encode(K),'active_decoder':encode(D),'active_metric':encode(H),
            'unchanged_raw_state_different_proposed_stage_labels':{'witness':encode(witness),'labels':desired},
            'supplied_tag_extension':{'raw_coordinates':2*n,'active_rank':2*r,
                'both_handoff_modes_compatible':mode_results,'native_mode_selection':False,
                'full_raw_recovery_claimed':False,'forgetting_tag_merges_distinct_preparations':True}}
    assert len(all_assignment_choices)==6
    # Each source accepts either supplied mode: all eight species assignments
    # are compatible with the unchanged payload equations, not only the proposal.
    assignments=list(cartesian(BITS,repeat=3))
    assert len(assignments)==8 and all(all((name,mode) in all_assignment_choices for name,mode in zip(OBS,a)) for a in assignments)
    return rows,pins,assignments


def main():
    contract=read(CONTRACT)
    assert contract['proposed_paths']=={'proton':['C_i','M_i','C_(i+1)'],
        'neutron':['M_i','C_i','M_(i+1)'],'electron':['M_i','C_i','C_(i+1)']}
    finite=finite_checks();native,pins,assignments=native_checks()
    checks={name:True for name in (
        'indexed_copy_notation_and_marked_half_step_roles',
        'shared_within_cycle_crossing_uniquely_fixed_by_observations',
        'context_free_handoff_impossible_and_two_contexts_necessary',
        'all_thirty_two_contextual_completions_exhausted_four_fit',
        'unique_minimal_bijective_completion_is_controlled_sector_flip',
        'sector_symmetry_and_bijectivity_equivalent_at_two_state_scope',
        'two_fixed_points_and_conditional_electron_two_cycle',
        'irreversible_loading_countermodels_refute_unconditional_two_cycle',
        'globally_reversible_memory_countermodel_refutes_coarse_reversibility_inference',
        'sector_duality_and_cycle_mark_erasure_distinguished',
        'same_sector_permutation_has_unitary_lifts_with_opposite_two_cycle_signs',
        'actual_native_returns_are_nonzero_idempotents_of_ranks_one_one_two',
        'all_native_stages_fix_active_payload_not_an_electron_swap',
        'unchanged_raw_state_cannot_supply_changing_sector_reader_without_context',
        'unequal_full_stage_image_dimensions_obstruct_literal_reversible_exchange',
        'supplied_tag_encoders_preserve_actual_induced_metrics_and_recovery',
        'tag_forgetting_loses_preparation_and_all_eight_mode_assignments_fit',
        'physical_sector_species_spin_and_clock_promotions_not_admitted')}
    for p in (CONTRACT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':pins[p.relative_to(ROOT).as_posix()]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.indexed-cycle-handoff-check.v1','status':'pass','checks':checks,
        'finite_completion':finite,'native_source_checks':native,
        'compatible_supplied_mode_assignments':assignments,
        'conditional_reversible_recurrence_constructed':True,
        'electron_two_cycle_follows_from_paths_alone':False,
        'source_native_sector_handoff_constructed':False,
        'explicit_tag_extension_constructed':True,'tag_extension_selects_species_assignment':False,
        'physical_particle_assignment_verified':False,'physical_spin_or_time_derived':False,
        'formal_proof_recompiled':False,'source_sha256':pins}
    OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'fitting_contextual_completions':4,
        'minimal_reversible_completions':1,'fixed_points':2,'electron_sector_period_if_minimal_reversible':2,
        'electron_two_cycle_unconditional':False,'native_payload_periods':[1,1,1],
        'compatible_tag_mode_assignments':8,'physical_assignment_verified':False},indent=2))


if __name__=='__main__':main()
