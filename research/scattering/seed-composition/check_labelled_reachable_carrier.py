"""Exact labelled closure exposes reachable endpoint-kernel directions."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, transpose, rank, encode
from check_segmented_copy_transport import audit as transport_audit
from check_event_branch_metric import audit as metric_audit
from check_controller_reflection import zero, permutation_matrix, parity

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/labelled-reachable-carrier.v1.json'


def closure(seed,matrices):
    vectors=transpose(seed);histories=[{'seed_column':i,'labels':[]} for i in range(len(vectors))]
    dimensions=[len(vectors)]
    for _ in range(19):
        old=list(zip(vectors,histories));before=len(vectors)
        for label,T in matrices:
            for v,h in old:
                image=[row[0] for row in mm(T,[[x] for x in v])]
                if rank(vectors+[image])>len(vectors):
                    vectors.append(image)
                    histories.append({'seed_column':h['seed_column'],'labels':h['labels']+[label]})
        dimensions.append(len(vectors))
        if len(vectors)==before:break
    else:raise AssertionError('Finite-dimensional closure failed to stabilize')
    B=transpose(vectors)
    assert all(rank(vectors+transpose(mm(T,B)))==len(vectors) for _,T in matrices)
    return B,histories,dimensions


def coordinates(B,v):
    # Full-column-rank basis: solve B*c=v by exact augmented elimination.
    n=len(B[0]);rows=[list(row)+[value] for row,value in zip(B,v)];pivot_rows=[];r=0
    for col in range(n):
        pivot=next(i for i in range(r,len(rows)) if rows[i][col])
        rows[r],rows[pivot]=rows[pivot],rows[r]
        factor=rows[r][col];rows[r]=[x/factor for x in rows[r]]
        for i in range(len(rows)):
            if i!=r:
                factor=rows[i][col];rows[i]=[a-factor*b for a,b in zip(rows[i],rows[r])]
        pivot_rows.append(r);r+=1
    assert all(not any(row[:n]) and not row[n] for row in rows[r:])
    out=[rows[pivot_rows[j]][n] for j in range(n)]
    assert mm(B,[[x] for x in out])==[[x] for x in v]
    return out


def audit():
    previous=metric_audit();transport=transport_audit()
    E=transport['matrices']['synchronized_mode_frame']+[[F(0),F(0)] for _ in range(6)]
    long=transport['segmented_automaton']['length_two_macro_ids']
    pairs=[i//6 for i in range(12)]+[e//6 for e in long]
    finishes=[i not in long for i in range(12)]+[True]*6
    labels=[tuple(branch['label']) for branch in previous['branch_rank_gate']['branches']]
    mats={label:zero(18) for label in labels}
    for a,b,p in transport['segmented_automaton']['transition_labels']:mats[pairs[a],p,finishes[a]][b][a]+=1
    B,histories,dims=closure(E,list(mats.items()))
    P=transport['matrices']['micro_P'];A,ag_histories,ag_dims=closure(E,[('aggregate',P)])
    assert dims==[2,13,14,14] and ag_dims==[2,3,4,5,6,6]
    assert rank(transpose(B)+transpose(A))==14
    boundary_perm=[9,10,11,6,7,8,3,4,5,0,1,2]
    cp=boundary_perm+[12+long.index(boundary_perm[e]) for e in long]
    J=permutation_matrix(cp);even,odd=parity(J)
    assert [rank(mm(even,B)),rank(mm(odd,B))]==[7,7]
    assert mm(J,A)==[[-v for v in row] for row in A]
    V=[row for label in labels for row in mats[label]]
    VB=mm(V,B);assert rank(VB)==12
    residuals=[[F(i==a)-F(i==b) for i in range(18)] for a,b in [(1,14),(10,16)]]
    kernel_records=[]
    for v in residuals:
        c=coordinates(B,v)
        assert all(mm(T,[[x] for x in v])==zero(18,1) for T in mats.values())
        assert rank(transpose(A)+[v])==7  # absent from aggregate closure
        kernel_records.append({'controller_vector':v,'coordinates_in_labelled_basis':c})
    assert rank(residuals)==2 and 14-rank(VB)==2
    assert rank(mm(V+residuals,B))==14
    # Repeatability equation with any positive G on the labelled carrier fails:
    # c!=0 but every labelled image is zero, forcing c^t G c=0.
    assert all(any(record['coordinates_in_labelled_basis']) for record in kernel_records)

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_labelled_reachable_carrier.py']
    return {
        'schema':'marici.scattering.labelled-reachable-carrier.v1',
        'status':'labelled_closure_rank_fourteen_contains_two_lost_history_directions_positive_completeness_impossible_without_residual_outputs',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'labelled_closure':{'dimensions_by_round':dims,'dimension':14,'even_odd_dimensions':[7,7],
                            'basis_columns':B,'basis_generation_histories':histories,
                            'invariant_under_every_label':True,
                            'minimality':'basis generated from seed images; final invariance proves smallest common invariant carrier'},
        'aggregate_closure':{'dimensions_by_round':ag_dims,'dimension':6,'entirely_odd':True,
                             'basis_columns':A,'basis_generation_histories':ag_histories,
                             'contained_in_labelled_closure':True,'contains_endpoint_kernel_witnesses':False},
        'reachable_kernel':{'labelled_output_rank_on_carrier':12,'kernel_dimension':2,'witnesses':kernel_records,
                             'rank_with_two_retained_difference_outputs':14},
        'positive_metric_gate':{'repeatable_unweighted_labelled_completeness_possible':False,
                                'equation':'sum_l A_l^t G A_l = G on the common labelled carrier',
                                'proof':'Both nonzero reachable kernel vectors have zero images under every label. Completeness forces their positive input norm to vanish.',
                                'even_separate_positive_branch_output_metrics_evade_kernel':False,
                                'scope':'unchanged endpoint-labelled maps with no residual/history output; not all enlarged channels or modified controls'},
        'boundary':{'all_lossless_retained_extensions_excluded':False,'metric_on_enlarged_output_derived':False,
                    'physical_instrument_or_preparation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Construct a predecessor-preserving event-arc lift on the reachable carrier, with a positive fiber-weighted output metric and exact decoder; compare its history retention and normalization with the endpoint summary, without declaring a physical instrument.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale reachable-carrier receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: labelled closure has dimension 14 (7 even + 7 odd), versus aggregate odd closure dimension 6.')
    print('PASS: two reachable kernel directions obstruct any positive labelled completeness without retained residual outputs.')
    print('Boundary: predecessor-preserving extensions remain possible; no physical instrument or preparation admitted.')


if __name__=='__main__':main()
