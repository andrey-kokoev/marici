"""Exact native endpoint compression vs retained-stage sufficiency and archive cost."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
import json
from check_rank_one_return_packets import LineInterface
from assemble_metric_coefficient_protocol import (ROOT,A,ZERO,ONE,read_operator,product,plus,scaled,encode,integer_trace)
CONTRACT=ROOT/'research/strominger/contracts/packet-stage-cost-comparison.v1.json'
def digest(p):return sha256(p.read_bytes()).hexdigest()
def act(M,v,out_size):
    out=[ZERO]*out_size
    for (i,j),a in M.items():out[i]+=a*v[j]
    return tuple(out)
def subtract(a,b):return plus(a,scaled(-ONE,b))
def source_electron_factors():
    store=json.loads((ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json').read_text(encoding='utf-8'))
    def coefficient(z):
        c=[F(0)]*16
        for a,mask in zip([v for pair in z for v in pair],(0,2,8,10)):c[mask]=F(a)
        return A(tuple(c))
    K={(2*f+i,j):coefficient(p[i][j]) for f,p in enumerate(store['face_projectors']) for i in range(2) for j in range(2) if coefficient(p[i][j])!=ZERO}
    D={(j,i):x.flip(8)/A(2) for (i,j),x in K.items()}
    return K,D

def main():
    prior_path=ROOT/'research/strominger/results/baryon-coefficient-spin-binding-v1.json'
    prior=json.loads(prior_path.read_text(encoding='utf-8'));assert prior['status']=='pass'
    pins=dict(prior['source_sha256']);pins[prior_path.relative_to(ROOT).as_posix()]=digest(prior_path)
    for p in (CONTRACT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale source'
    contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
    checks={};rows={}
    for name in ('proton','neutron','electron'):
        p=ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json'
        source=json.loads(p.read_text(encoding='utf-8'));dim=len(source['source']['metric'])
        ops={s:read_operator(source['operators'][s],dim) for s in 'LGN'}
        if name=='electron':K,D=source_electron_factors();r=2
        else:
            line=LineInterface(p);r=1
            K={(i,0):x for i,x in enumerate(line.column) if x!=ZERO}
            D={(0,j):x for j,x in enumerate(line.row) if x!=ZERO}
        assert product(D,K)=={(i,i):ONE for i in range(r)}
        assert product(K,D)==ops['N']
        assert product(ops['N'],product(ops['G'],ops['L']))==ops['N']
        n=contract['candidate_accounting']['native_return_n'][name]
        assert n==2*r-1 # normalized full complex return fiber, phase retained
        candidate=[n**3*2**(n-1),n**3*2**(2*n-2),n**4*2**(2*n-2)]
        native=[len(ops[s]) for s in 'LGN'];factors=len(K)+len(D)
        assert native==source['measures']['stage_transfer_supports']
        assert factors==(32 if name=='electron' else 72)
        # Stronger than testing Lx != Nx on an arbitrary column: build a pair
        # with IDENTICAL compressed latent and endpoint but DIFFERENT L-reader.
        Q=subtract(ops['L'],ops['N']);assert Q and product(Q,Q)==Q
        assert not product(D,Q) and not product(ops['N'],Q)
        j=min(j for i,j in Q)
        x=tuple(Q.get((i,j),ZERO) for i in range(dim));assert any(a!=ZERO for a in x)
        assert act(D,x,r)==(ZERO,)*r
        assert act(ops['N'],x,dim)==(ZERO,)*dim
        assert act(ops['L'],x,dim)==x
        reader=next(i for i,a in enumerate(x) if a!=ZERO)
        # On the OLD return image, all retained stages remain identity, so the
        # broad raw-input counterexample does not invalidate image extraction.
        for s in 'LGN':assert product(ops[s],K)==K
        cold_native=sum(native);cold_combined=cold_native+factors
        assert cold_combined>cold_native>factors and candidate!=native
        rows[name]={'source_packet':p.relative_to(ROOT).as_posix(),'source_packet_sha256':digest(p),
          'native_stage_supports':native,'native_total':cold_native,'raw_dimension':dim,'return_rank':r,
          'encoder':encode(K),'decoder':encode(D),'factor_supports':[len(K),len(D)],
          'endpoint_factor_total':factors,'cold_complete_native_archive_plus_factor_total':cold_combined,
          'warm_additional_factor_occurrences':factors,'full_archive_occurrences_shared_globally':cold_native,
          'strict_candidate_stage_bijection':False,'candidate_n':n,'candidate_group_counts':candidate,
          'hostile':{'input_raw_coefficients':[a.record() for a in x],'input_origin':f'(L-N)e_{j}',
                     'compressed_latent':'zero, equal to zero input','endpoint':'zero, equal to zero input',
                     'L_reader_coordinate':reader,'L_reader_value':x[reader].record(),'zero_input_L_reader':{},
                     'L_minus_N_rank':integer_trace(Q)}}
        checks[name+'_all_input_factor_endpoint_matches_native_protocol']=True
        checks[name+'_same_latent_distinct_retained_L_readers']=True
        checks[name+'_archive_aware_cost_and_candidate_stage_mismatch']=True
    # Retain explicit small-basis noninvariance as a distinct previously sourced
    # boundary, not an unrun new universal minimality claim.
    assert rows['proton']['native_total']==rows['neutron']['native_total']==1836
    assert rows['electron']['native_total']==144
    assert [rows[n]['cold_complete_native_archive_plus_factor_total'] for n in ('proton','neutron','electron')]==[1908,1908,176]
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    checks['frozen_scope_cost_policy_and_native_sources_unchanged']=True
    report={'schema':'marici.packet-stage-cost-comparison.v1','status':'pass','checks':checks,'carriers':rows,
      'resolution':'Constructed source-fixed mathematical comparison. Endpoint factorizations are smaller; retained-stage latent sufficiency and literal J(n)-to-native-stage occurrence identification fail at this scope.',
      'scope':'Specified materialized coefficient tables and frozen endpoint/stage tasks, not universal minimum, source-constructor derivation cost or physical resource valuation.',
      'sharing':'Cold complete archives and warm shared-library incremental tables are separate ledgers.',
      'source_sha256':pins,'native_producers_executed':False,'formal_proof_recompiled':False,'physical_mass_or_cost_claim':False}
    (ROOT/'research/strominger/results/packet-stage-cost-comparison-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'checks':checks,'counts':{n:{k:r[k] for k in ('native_total','endpoint_factor_total','cold_complete_native_archive_plus_factor_total','candidate_n','candidate_group_counts')} for n,r in rows.items()},'resolution':report['resolution']},indent=2))
if __name__=='__main__':main()
