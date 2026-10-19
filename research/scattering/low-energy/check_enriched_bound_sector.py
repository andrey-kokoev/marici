"""Coupled point-sector counts and ambient projector gap for the enrichment."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_resonant_native_enrichment as enrichment

p=enrichment.p;ROOT=p.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/enriched-bound-sector.v1.json'
PROOF=HOME/'ENRICHED-BOUND-SECTOR.md'
RESULT=HOME/'results/enriched-bound-sector.v1.json'
F,mm,eye,scale,invert=p.F,p.mm,p.eye,p.scale,p.invert
transpose,decode,difference,zeros=p.transpose,p.decode,p.difference,p.zeros


def equal(A,B):assert A==B,'bound-sector support identity failed'
def energy(s):
    assert 0<s<=1,'upper-branch tail parameter required'
    return 2+s+1/s
def tail_factor(s):
    assert 0<s<1,'square-summable tail required'
    return s*s/(1-s*s)
def boundary_matrix(K,P,s):
    return difference(difference(scale(F(energy(s)),eye(len(K))),K),scale(F(1+s),P))

def sector(K,H,P,B,edge):
    G=mm(mm(transpose(B),H),B);L=mm(mm(invert(G),transpose(B)),H)
    A=mm(mm(L,K),B);C=mm(mm(L,P),B);M=mm(mm(L,edge),B);d=len(G)
    equal(mm(L,B),eye(d));equal(mm(K,B),mm(B,A));equal(mm(P,B),mm(B,C))
    assert p.inertia(G)==(d,0,0)
    equal(mm(G,M),transpose(mm(G,M)))
    counts=p.inertia(mm(G,M));assert counts[2]==0
    return {'dimension':d,'edge_inertia':list(counts),'point_dimension':counts[1],
            'B':B,'G':G,'L':L,'A':A,'C':C}

def audit_core(K,H):
    n=len(K);P=[[F(int(i==j and i<3)) for j in range(n)] for i in range(n)]
    assert p.inertia(H)==(n,0,0) and p.inertia(mm(H,K))==(n-1,0,1)
    equal(mm(H,K),transpose(mm(H,K)));equal(mm(P,P),P)
    equal(mm(H,P),transpose(mm(H,P)));assert p.inertia(mm(H,P))==(3,0,n-3)
    visible=p.cyclic(K,[[F(int(i==j)) for i in range(n)] for j in range(3)])
    assert len(visible[0])==n
    edge=boundary_matrix(K,P,Q(1));counts=p.inertia(mm(H,edge));assert counts[2]==0
    sym=p.cyclic(K,[[F(int(i==0)) for i in range(n)],[F(int(i in (1,2))) for i in range(n)]])
    anti=p.cyclic(K,[[F(int(i==1)-int(i==2)) for i in range(n)]])
    S=sector(K,H,P,sym,edge);A=sector(K,H,P,anti,edge)
    assert S['dimension']==5 and A['dimension']==n-5
    equal(mm(mm(transpose(sym),H),anti),zeros(5,n-5))
    assert p.rank(mm(P,sym))==2 and p.rank(mm(P,anti))==1
    assert counts[1]==S['point_dimension']+A['point_dimension']
    # Bind the monotone formula and the signed infinite-tail recurrence exactly.
    a,b=Q(1,3),Q(1,2)
    secant=difference(boundary_matrix(K,P,a),boundary_matrix(K,P,b))
    expected=scale(F(b-a),p.add(scale(F(1/(a*b)-1),eye(n)),P))
    equal(secant,expected);assert p.inertia(mm(H,secant))==(n,0,0)
    for s in (a,b):assert (energy(s)-2)*(-s)+s*s+1==0
    return {'dimension':n,'P':P,'edge':edge,'edge_inertia':list(counts),'point_dimension':counts[1],
            'visible_cyclic_dimension':n,'symmetric':S,'antisymmetric':A}

def validate_contract(c):
    assert c['schema']=='marici.scattering.enriched-bound-sector.v1'
    assert ROOT/c['enrichment_certificate']==enrichment.RESULT
    assert c['native_point_dimension']==5 and c['enriched_point_dimension']==3
    assert c['symmetric_point_dimensions']==[2,2] and c['antisymmetric_point_dimensions']==[3,1]
    assert c['bound_projection_operator_norm_gap']==1
    for key in ('named_antisymmetric_retained_weights_evaluated','same_finite_time_state_error_lower_bound_claimed',
                'native_bound_counts_inherited','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=enrichment.build();assert parent==json.loads(enrichment.RESULT.read_text(encoding='utf-8')),'stale enrichment input'
    src=json.loads(p.base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    Kr=decode(parent['reduced_core']);Hr=decode(parent['full_metric'])
    E=decode(parent['embedding']);L=decode(parent['metric_adjoint'])
    equal(mm(L,E),eye(9));equal(L,mm(mm(invert(Hr),transpose(E)),H))
    equal(mm(mm(transpose(E),H),E),Hr)
    native=audit_core(K,H);reduced=audit_core(Kr,Hr)
    assert native['edge_inertia']==[6,5,0] and reduced['edge_inertia']==[6,3,0]
    assert native['symmetric']['edge_inertia']==reduced['symmetric']['edge_inertia']==[3,2,0]
    assert native['antisymmetric']['edge_inertia']==[3,3,0]
    assert reduced['antisymmetric']['edge_inertia']==[3,1,0]
    S=native['symmetric'];Sr=mm(L,S['B'])
    equal(mm(E,Sr),S['B']);equal(mm(Kr,Sr),mm(Sr,S['A']))
    equal(mm(reduced['P'],Sr),mm(Sr,S['C']))
    equal(mm(mm(transpose(Sr),Hr),Sr),S['G'])
    HP=[row[:3] for row in H[:3]]
    Vn=[[F(int(i==j)) for j in range(3)] for i in range(11)]
    Vr=[[F(int(i==j)) for j in range(3)] for i in range(9)]
    Vnsharp=mm(mm(invert(HP),transpose(Vn)),H)
    Vrsharp=mm(mm(invert(HP),transpose(Vr)),Hr)
    equal(mm(E,Vr),Vn);equal(mm(Vnsharp,E),Vrsharp)
    equal(mm(Vn,Vnsharp),native['P']);equal(mm(Vr,Vrsharp),reduced['P'])
    equal(mm(Vnsharp,Vn),eye(3));equal(mm(Vrsharp,Vr),eye(3))
    vs=[[F()],[F(1)],[F(1)]];va=[[F()],[F(1)],[F(-1)]]
    for port,sign in ((1,F(1)),(2,F(-1))):
        v=[[F(int(i==port))] for i in range(3)]
        equal(scale(F(Q(1,2)),p.add(vs,scale(sign,va))),v)
        norm=p.mm(p.mm(transpose(v),HP),v)[0][0]
        assert p.mm(p.mm(transpose(vs),HP),vs)[0][0]==2*norm
        assert p.mm(p.mm(transpose(va),HP),va)[0][0]==2*norm
    equal(mm(mm(transpose(vs),HP),va),[[F()]])
    controls=[]
    for name in ('inherit-five-native-modes','drop-contact-shift','wrong-tail-sign','normalize-core-only',
                 'promote-gap-to-finite-time-error','admit-physical-outcomes'):
        try:
            if name=='inherit-five-native-modes':assert reduced['point_dimension']==native['point_dimension']
            elif name=='drop-contact-shift':equal(native['edge'],difference(scale(F(4),eye(11)),K))
            elif name=='wrong-tail-sign':
                s=Q(1,2);assert (energy(s)-2)*s+s*s+1==0
            elif name=='normalize-core-only':assert tail_factor(Q(1,2))==0
            else:
                bad=copy.deepcopy(c)
                bad['same_finite_time_state_error_lower_bound_claimed' if name=='promote-gap-to-finite-time-error' else 'physical_outcomes_admitted']=True
                validate_contract(bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile bound-sector control accepted: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((enrichment.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_enriched_bound_sector.py'))
    def payload(data):
        return {'core_dimension':data['dimension'],'visible_cyclic_dimension':data['visible_cyclic_dimension'],
                'upper_edge_inertia':data['edge_inertia'],'point_dimension':data['point_dimension'],
                'upper_edge_matrix':p.base.encoded(data['edge']),
                'symmetric':{key:data['symmetric'][key] for key in ('dimension','edge_inertia','point_dimension')},
                'antisymmetric':{key:data['antisymmetric'][key] for key in ('dimension','edge_inertia','point_dimension')}}
    return {'schema':'marici.scattering.enriched-bound-sector-receipt.v1','status':'pass',
        'scope_verdict':'enriched_conditional_point_sector_differs_from_native',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'native':payload(native),'enriched':payload(reduced),
        'all_point_modes_above_band':True,'no_embedded_or_edge_point_modes_by_cyclicity':True,
        'monotone_decaying_lead_schur_support_verified':True,
        'ambient_lifted_bound_projection_norm_gap':1,'native_point_subspace_nullity_lower_bound':2,
        'symmetric_point_projection_intertwining':True,'symmetric_preparation_bound_weights_exactly_preserved':True,
        'single_carrier_weight_difference_formula':'(w_anti_native-w_anti_9)/2',
        'single_carrier_symmetric_antisymmetric_normalized_weights':['1/2','1/2'],
        'full_tail_norm_factor':'s^2/(1-s^2)','tail_factor_at_s_one_half':'1/3',
        'named_antisymmetric_retained_weights_evaluated':False,
        'same_finite_time_state_error_lower_bound_claimed':False,'native_bound_counts_inherited':False,
        'new_singular_continuous_or_full_central_release_completeness_claimed':False,
        'analytic_argument_machine_formalized':False,'physical_preparation_or_detector_binding_claimed':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale enriched bound-sector certificate'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':r['status'],'native_point_dimension':r['native']['point_dimension'],
        'enriched_point_dimension':r['enriched']['point_dimension'],
        'ambient_lifted_bound_projection_norm_gap':r['ambient_lifted_bound_projection_norm_gap'],
        'named_antisymmetric_retained_weights_evaluated':False,'hostile_controls_refused':r['hostile_controls_refused']}))


if __name__=='__main__':main()
