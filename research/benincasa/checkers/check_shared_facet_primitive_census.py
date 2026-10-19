#!/usr/bin/env python3
"""Invariant rank-two primitive source-boundary census of the shared cell."""
import json
import sys
import itertools
import copy
from collections import Counter
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_facet_contracted_merger import s,rational,parameters,target_jac,derivative
from check_three_composite_boundary_residues import physical
PARENT=[(1,),(2,),(3,5),(6,7,8)]
PATHS={
    'prior':('research/benincasa/results/three_composite_normalizations.json','check_three_composite_normalizations.py'),
    'facet':('research/benincasa/results/shared_internal_composite_facet.json','check_shared_internal_composite_facet.py'),
    'zero':('research/benincasa/results/shared_internal_facet_boundaries.json','check_shared_internal_facet_boundaries.py'),
    'radial':('research/benincasa/results/shared_facet_correlated_radial.json','check_shared_facet_correlated_radial.py'),
    'mixed':('research/benincasa/results/shared_facet_mixed_radial.json','check_shared_facet_mixed_radial.py'),
    'shear':('research/benincasa/results/shared_facet_direction_merger.json','check_shared_facet_direction_merger.py'),
    'contracted':('research/benincasa/results/shared_facet_contracted_merger.json','check_shared_facet_contracted_merger.py')}


def key(groups):return tuple(sorted(tuple(sorted(g)) for g in groups if g))


def dimension(groups):return sum(len(g) for g in groups)+len(groups)-4


def cyclic_coarsenings(groups):
    n=len(groups)
    for k in range(2,n+1):
        for gaps in itertools.combinations(range(n),k):
            retained=set(gaps);start=(gaps[0]+1)%n;blocks=[];block=[]
            for step in range(n):
                j=(start+step)%n;block.extend(groups[j])
                if j in retained:blocks.append(tuple(block));block=[]
            assert not block and len(blocks)==k
            yield key(blocks)


def enumerate_closure():
    labels=sorted(x for g in PARENT for x in g);cells=set()
    for size in range(2,len(labels)+1):
        for subset in itertools.combinations(labels,size):
            allowed=set(subset);groups=[tuple(x for x in g if x in allowed) for g in PARENT];groups=[g for g in groups if g]
            if len(groups)<2:continue
            cells.update(cyclic_coarsenings(groups))
    parent=key(PARENT);assert parent in cells and dimension(parent)==7
    covers={g for g in cells if dimension(g)==6}
    expected={}
    for group in PARENT:
        if len(group)>1:
            for label in group:
                k=key([tuple(x for x in g if x!=label) for g in PARENT]);expected[f'delete-{label}']=k
    for i in range(len(PARENT)):
        j=(i+1)%len(PARENT);merged=tuple(PARENT[i]+PARENT[j])
        k=key([g for h,g in enumerate(PARENT) if h not in (i,j)]+[merged]);expected[f'merge-{i}-{j}']=k
    assert set(expected.values())==covers and len(covers)==9
    return cells,covers,expected


def source_key(C):
    support=[j for j in range(8) if any(rational(x)!=0 for x in C[:,j])];groups=[];unseen=set(support)
    while unseen:
        i=min(unseen);group={j for j in unseen if rational(C[:,[i,j]].det())==0}
        assert i in group
        # Parallelism of nonzero rank-two columns is an equivalence relation.
        assert all(rational(C[:,[j,k]].det())==0 for j,k in itertools.combinations(group,2))
        groups.append(tuple(j+1 for j in group));unseen-=group
    return key(groups)


def compact_matrix(receipt):
    C=s.Matrix([[s.sympify(x) for x in row] for row in receipt['source_witness']['shared_source_germ']])
    return C.subs(s.Symbol('t'),0)


def measure(C,values,shift):
    variables=sorted(C.free_symbols,key=str);assert len(variables)==6
    assert all(z in values for z in variables)
    Cp=C.subs(values);assert Cp.rank()==2 and all(Cp[:,list(p)].det()>=0 for p in itertools.combinations(range(8),2))
    sourcepivot=next(p for p in itertools.combinations(range(8),2) if Cp[:,list(p)].det()>0)
    sourcecoords=[(i,j) for i in range(2) for j in range(8) if j not in sourcepivot]
    ds=[derivative(Cp,C.diff(z).subs(values),list(sourcepivot)) for z in variables]
    sourceJ=s.Matrix([[d[i,j] for d in ds] for i,j in sourcecoords]);assert sourceJ.rank()==6
    Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    J,_=target_jac(Cp*Z,[C.diff(z).subs(values)*Z for z in variables],[0,1])
    return {'positive_Z_moment_shift':shift,'source_tangent_rank':sourceJ.rank(),'target_tangent_rank':J.rank(),
        'source_pivot':[j+1 for j in sourcepivot]}


def coverage_valid(covers,rows):
    keys=[tuple(tuple(g) for g in r['cyclic_class_key']) for r in rows]
    if len(keys)!=len(set(keys)) or set(keys)!=covers:return False
    for r in rows:
        if r['source_dimension']!=6:return False
        for run in r['runs']:
            if run['target_tangent_rank']==6:
                if run['paired_target_density_sum']!='0':return False
            elif run['target_tangent_rank']==5:
                if run['paired_target_density_sum'] is not None:return False
            else:return False
    return True


def main():
    receipts={}
    for name,(path,checker) in PATHS.items():
        receipt=json.loads((ROOT/path).read_text());receipts[name]=receipt
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        checkpath='research/benincasa/checkers/'+checker;assert receipt['checker_sha256']==sha256((ROOT/checkpath).read_bytes()).hexdigest()
    cells,covers,expected=enumerate_closure()
    rows_by_history={r['history_index']:r for r in receipts['prior']['rows']}
    a,A,_=parameters(rows_by_history[8]['target_runs'][0]);F=A.subs(a[0],0);assert source_key(F)==key(PARENT)
    # Evidence selection specifies source operations, not desired density values.
    mapping=[('delete-5','zero',1),('merge-3-0','zero',2),('merge-0-1','zero',3),('delete-7','zero',4),('delete-8','zero',5),
             ('delete-3','radial',None),('delete-6','mixed',None),('merge-1-2','shear',None),('merge-2-3','contracted',None)]
    rows=[]
    for identifier,receipt_name,outer in mapping:
        receipt=receipts[receipt_name];C=F.subs(a[outer],0) if outer is not None else compact_matrix(receipt)
        signature=source_key(C);assert signature==expected[identifier] and dimension(signature)==6
        runs=[];normal=None
        for shift in (0,1):
            if outer is not None:
                _,_,values=parameters(rows_by_history[8]['target_runs'][shift]);values=values|{a[0]:0,a[outer]:0}
                priorface=next(f for f in receipt['runs'][shift]['faces'] if f['A_deleted_alphas']==[1,outer+1])
                paired=priorface['paired_target_density_sum'];normal=priorface['second_normal']
            else:
                priorrun=receipt['runs'][shift]
                valuefield={'radial':'radial_parameters','mixed':'mixed_parameters','shear':'boundary_parameters','contracted':'boundary_parameters'}[receipt_name]
                values={s.Symbol(z):s.Rational(x) for z,x in priorrun[valuefield].items()};paired=priorrun['paired_target_density_sum']
                normal={'type':'actual_normalized_target_bracket','bracket':priorrun['physical_second_normal'],'physical':True} if receipt_name!='contracted' else None
            measured=measure(C,values,shift)
            expected_rank=5 if receipt_name=='contracted' else 6;assert measured['target_tangent_rank']==expected_rank
            if outer is not None:assert measured['target_tangent_rank']==priorface['target_tangent_rank']
            measured.update({'paired_target_density_sum':paired,'ordinary_six_form_status':'unavailable_contracted' if paired is None else 'admitted_three_route_local_cancellation'})
            runs.append(measured)
        rows.append({'id':identifier,'cyclic_class_key':[list(g) for g in signature],'source_dimension':dimension(signature),
            'symbolic_source_boundary_matrix':[[str(x) for x in rr] for rr in C.tolist()],
            'precursor_receipt':PATHS[receipt_name][0],'precursor_selector':{'A_second_zero_alpha':None if outer is None else outer+1},
            'source_operation':'delete_nonsingleton_member' if identifier.startswith('delete') else 'merge_adjacent_cyclic_directions',
            'actual_second_normal':normal,'runs':runs})
    assert coverage_valid(covers,rows)
    lower=[]
    for outer,label in [(6,1),(7,2)]:
        C=F.subs(a[outer],0);signature=source_key(C);assert dimension(signature)==5 and signature not in covers
        lower.append({'finite_coordinate_zero':outer+1,'deleted_singleton_label':label,'class_key':[list(g) for g in signature],
            'source_dimension':5,'primitive_codimension1_facet':False})
    # Deliberate structural/scientific coverage errors must fail the scoped validator.
    assert not coverage_valid(covers,rows[:-1])
    assert not coverage_valid(covers,rows+[rows[0]])
    assert not coverage_valid(covers,[r for r in rows if r['precursor_receipt']==PATHS['zero'][0]])
    falsezero=copy.deepcopy(rows);next(r for r in falsezero if r['id']=='merge-2-3')['runs'][0]['paired_target_density_sum']='0'
    assert not coverage_valid(covers,falsezero)
    smaller=copy.deepcopy(rows);smaller[0]['cyclic_class_key']=lower[0]['class_key'];smaller[0]['source_dimension']=5
    assert not coverage_valid(covers,smaller)
    physical_count=sum((r['actual_second_normal'] or {}).get('physical',False) for r in rows)
    assert physical_count==6
    checks={'exhaustive_rank2_support_and_cyclic_gap_closure_enumeration':True,'nine_primitive_source_facets':True,
        'nine_symbolic_matroid_keys_match_pinned_source_germs':True,'eighteen_fresh_source_rank6_and_target_rank_controls':True,
        'eight_regular_facets_attach_sixteen_paired_zero_sums':True,'contracted_primitive_merger_retained_with_unavailable_target_density':True,
        'singleton_coordinate_deletions_excluded_as_codimension2':True,'missing_duplicate_coordinate_only_falsezero_and_lowerdim_hostiles_rejected':True}
    paths=[p for p,c in PATHS.values()]+['research/benincasa/checkers/'+c for p,c in PATHS.values()]+['research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.shared-facet-primitive-census.v1','parent':{'support':[1,2,3,5,6,7,8],
        'cyclic_classes':[list(g) for g in PARENT],'dimension_formula':'m+r-4','dimension':7},
        'closure_cell_count':len(cells),'closure_dimension_histogram':dict(sorted(Counter(dimension(g) for g in cells).items())),
        'primitive_boundary_rows':rows,'excluded_lower_coordinate_images':lower,
        'summary':{'primitive_source_facets':9,'nonsingleton_member_deletions':5,'adjacent_direction_mergers':4,
            'regular_rank6_target_images':8,'contracted_rank5_target_images':1,'physical_second_normals':physical_count,
            'nonphysical_bracket_second_normals':1,'nonlinear_inverse_second_normals':1,'fixed_Z_paired_density_sums_zero':16},
        'coverage_argument':'A rank2 positive cell has m positive column magnitudes and r cyclic RP1 directions modulo GL2, dimension m+r-4. Closure removes active members and coalesces cyclic consecutive directions. Codimension1 loses exactly one member from a nonsingleton class or one cyclic direction gap. Singleton deletion loses two dimensions; combined removals/nonadjacent coalescences lose at least two. Exhaustive support-subset/cyclic-gap enumeration yields the same nine covers.',
        'checks':checks,'passed':True,'disposition':'bounded_invariant_primitive_source_boundary_census_attached_to_eight_local_cancellations_and_one_contraction',
        'claim_boundary':'Complete primitive rank2 positive-cell stratum census for this one shared internal source cell. Target ranks and normalized unweighted density comparisons are local at two fixed Z; this is not the complete three-composite 5/6/5 physical facet atlas, global covering/orientation, component extraction or weighted nine-image theorem.',
        'next_action':'Apply the invariant member-deletion/adjacent-merger census to the original history5,8,9 top cells. Construct positive gap-and-column-scale source germs with a nonsingular cyclic cut and derive their logarithmic transitions to the frozen intrinsic A/H orientations before target-rank/physical-normal classification. This addresses the missing three-composite primitive provenance without importing the shared-cell census as full atlas completeness.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_facet_primitive_census.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'closure_cells':len(cells),'summary':out['summary'],'checks':checks},indent=2))


if __name__=='__main__':main()
