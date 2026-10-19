#!/usr/bin/env python3
"""Seven coordinate boundaries of the actual shared internal positive facet."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_internal_composite_facet import s,rational,normalize,target_jac,parameters,sign,gradient
from check_three_composite_inverse_normals import setup_A,inverse_A,extract
from check_three_composite_boundary_residues import weights,physical
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FACET='research/benincasa/results/shared_internal_composite_facet.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'
INTERNAL=(1,2,3,5)


def run(rows,old):
    shift=old['positive_Z_moment_shift'];Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
    a,A,values=parameters(rows[8]['target_runs'][shift]);_,H,_=parameters(rows[9]['target_runs'][shift])
    F=A.subs(a[0],0);values[a[0]]=0
    assert F==H.subs({a[0]:a[1],a[1]:0},simultaneous=True)
    W=weights(Z);minors={(i,j):s.factor(F[:,[i,j]].det()) for i,j in itertools.combinations(range(8),2)}
    polynomials={q:s.factor(sum(minors[i,j]*w for i,j,w in ws)) for q,ws in W.items()}
    assert polynomials[INTERNAL]==0
    emb=rows[8]['superfunction_runs'][0]['matches'][0];inverse_data=setup_A(Z,emb)
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)];faces=[]
    for e in range(1,8):
        va=values|{a[e]:0};vh=va|{a[0]:va[a[1]],a[1]:0}
        assert A.subs(va)==H.subs(vh)
        N=normalize(A.subs(va)*Z,[0,1]);pivot=s.factor((F*Z)[:,[0,1]].det());assert pivot.subs(va)!=0
        chart_data=[]
        for history,C,v,internal,outer in [(8,A,va,0,e),(9,H,vh,1,0 if e==1 else e)]:
            parity,free=sign([internal,outer]);J,actual=target_jac(C.subs(v)*Z,[C.diff(z).subs(v)*Z for z in a],[0,1]);assert actual==coords
            facetfree=[j for j in range(8) if j!=internal]
            tangent=J[:,free]*s.diag(*[v[a[j]] for j in free])
            assert all(C.subs(v)[:,list(pair)].det()>=0 for pair in itertools.combinations(range(8),2))
            chart_data.append((history,C,v,internal,outer,parity,free,facetfree,J,tangent))
        assert chart_data[0][9]==chart_data[1][9] and chart_data[0][5]==-chart_data[1][5]
        rank=chart_data[0][9].rank();vanished=[q for q,p in polynomials.items() if p.subs(a[e],0)==0]
        candidates=[q for q in vanished if polynomials[q]!=0 and s.diff(polynomials[q],a[e]).subs(va)!=0]
        base={'A_deleted_alphas':[1,e+1],'H_deleted_alphas':[2,1 if e==1 else e+1],
            'target_tangent_rank':rank,'facet_ordinary_ranks':[d[8][:,d[7]].rank() for d in chart_data],
            'full_target_ranks':[d[8].rank() for d in chart_data],
            'source_deletion_parities':[d[5] for d in chart_data],
            'identically_vanishing_brackets_on_corner':[list(q) for q in vanished],
            'regular_second_bracket_candidates':[list(q) for q in candidates],
            'source_matrix_and_ordered_tangent_identity':True,'symbolic_source_paired_residues':'opposite identical six-dlog forms'}
        if rank<6:
            base.update({'disposition':'contracted_rank_below_six','target_residue_status':'no_ordinary_rank6_divisorial_pushforward_in_this_coordinate_branch',
                'paired_target_density_sum':None,'second_normal':None})
            faces.append(base);continue
        assert rank==6
        if candidates:
            quad=next((q for q in candidates if physical(q)),candidates[0])
            g2=gradient(N,Z,quad,coords)
            second={'type':'actual_normalized_target_bracket','bracket':list(quad),'physical':physical(quad),
                'raw_source_facet_pullback':str(polynomials[quad]),
                'source_facet_transverse_slope':str(s.factor(s.diff(polynomials[quad],a[e]).subs(va)/pivot.subs(va)))}
        else:
            # A alpha4 has a genuine nonlinear target normal from the already
            # pinned rational inverse circuit. Here specialize it to alpha1=0.
            assert e==3
            def b(Y):
                R,loc=inverse_A(Y,inverse_data);pars,gauge,_=extract(R,emb)
                assert all(q!=0 for q in loc+gauge)
                return pars[e]
            assert b(N)==0
            t=s.symbols('t');arc=va|{a[e]:t};Na=normalize(A.subs(arc)*Z,[0,1])
            assert rational(b(Na)-t)==0
            h=s.symbols('h');g=[]
            for i,j in coords:
                E=s.zeros(2,6);E[i,j]=1;g.append(rational(s.diff(b(N+h*E),h).subs(h,0)))
            g2=s.Matrix(1,8,g)
            second={'type':'actual_rational_inverse_source_alpha4_normal','inverse_receipt':INVERSES,
                'source_facet_arc_identity':'b(target(alpha4=t,alpha1=0))=t identically',
                'no_four_bracket_second_normal':True}
        g1=gradient(N,Z,INTERNAL,coords)
        if e==5:
            # Keep the previous corner's chosen six-coordinate frame exactly.
            corner=json.loads((ROOT/'research/benincasa/results/paired_composite_corner_residues.json').read_text())
            selected=corner['runs'][shift]['selected_common_target_coordinate_indices']
        else:selected=next(I for I in itertools.combinations(range(8),6) if chart_data[0][9][list(I),:].det()!=0)
        routes=[];densities=[]
        for history,C,v,internal,outer,parity,free,facetfree,J,tangent in chart_data:
            det=s.factor(tangent[list(selected),:].det());source=s.factor(parity/det)
            normal2=g2*J;assert normal2[outer]!=0 and all(normal2[j]==0 for j in free)
            prod=s.prod(v[a[j]] for j in free)
            D7=s.Matrix.vstack(normal2[:,facetfree],J[list(selected),facetfree]);det7=s.factor(D7.det());assert det7!=0
            middle=s.factor((-1)**internal*normal2[outer]/(prod*det7));assert middle==source
            B=s.Matrix.vstack(g1*J,normal2);minor=B[:,[internal,outer]]
            full=s.Matrix.vstack(B,J[list(selected),:])
            if J.det()!=0 and minor.det()!=0 and full.det()!=0:
                top=s.factor(minor.det()/(prod*full.det()));assert top==source
                top_status='constructed_regular_two_normal_route'
            else:top=None;top_status='undefined_regular_top_route_at_this_full_rank_or_normal_localization'
            densities.append(source);routes.append({'history_index':history,'source_deletion_sign':parity,
                'boundary_log_jacobian':str(det),'second_normal_source_slope':str(normal2[outer]),
                'iterated_source_residue_then_pushforward':str(source),'facet_pushforward_then_second_target_residue':str(middle),
                'top_pushforward_then_two_target_residues':None if top is None else str(top),'top_route_status':top_status})
        assert sum(densities)==0;hostile=s.factor(-densities[0]+densities[1]);assert hostile!=0
        if e==5:
            prior_routes={r['history_index']:r for r in old['boundary_naturality_routes']}
            for route in routes:assert route['iterated_source_residue_then_pushforward']==prior_routes[route['history_index']]['source_corner_then_pushforward']
        base.update({'disposition':'rank6_local_paired_iterated_residue_constructed','second_normal':second,
            'selected_common_target_coordinate_indices':list(selected),'routes':routes,'paired_target_density_sum':'0',
            'orientation_reversal_residual':str(hostile),'alpha6_predecessor_preserved':e==5})
        faces.append(base)
    summary={'rank6_paired_corners':sum(f['target_tangent_rank']==6 for f in faces),
        'contracted_corners':sum(f['target_tangent_rank']<6 for f in faces),
        'bracket_second_normals':sum((f.get('second_normal') or {}).get('type')=='actual_normalized_target_bracket' for f in faces),
        'nonlinear_inverse_second_normals':sum((f.get('second_normal') or {}).get('type')=='actual_rational_inverse_source_alpha4_normal' for f in faces),
        'undefined_regular_top_routes':sum(r['top_route_status'].startswith('undefined') for f in faces for r in f.get('routes',[]))}
    return {'positive_Z_moment_shift':shift,'faces':faces,'summary':summary}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());facet=json.loads((ROOT/FACET).read_text());inverses=json.loads((ROOT/INVERSES).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (facet,'research/benincasa/checkers/check_shared_internal_composite_facet.py'),
        (inverses,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows={r['history_index']:r for r in prior['rows']};runs=[run(rows,old) for old in facet['runs']]
    signature=lambda r:[(f['A_deleted_alphas'],f['target_tangent_rank'],f['disposition'],f['second_normal'] and f['second_normal']['type']) for f in r['faces']]
    assert signature(runs[0])==signature(runs[1])
    checks={'fourteen_coordinate_corner_screens':True,'two_fixture_disposition_signatures_agree':True,
        'actual_source_matrix_ordered_transition_and_positivity_controls':True,
        'all_admitted_facet_second_residue_routes_agree_and_paired_sums_zero':True,
        'actual_bracket_and_rational_inverse_normals_not_tangent_planes':True,
        'contracted_and_undefined_top_routes_retained':True,'orientation_hostiles_nonzero':True,'alpha6_corner_receipt_preserved':True}
    paths=[PRIOR,FACET,INVERSES,'research/benincasa/results/paired_composite_corner_residues.json',
        'research/benincasa/checkers/check_shared_internal_composite_facet.py',
        'research/benincasa/checkers/check_paired_composite_corner_residues.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_three_composite_boundary_residues.py']
    out={'schema':'marici.benincasa.shared-internal-facet-boundaries.v1','histories':[8,9],'runs':runs,'checks':checks,'passed':True,
        'disposition':'seven_coordinate_boundaries_classified_with_actual_normals_and_admitted_unweighted_paired_residues',
        'claim_boundary':'Seven zero-coordinate boundaries of one actual shared positive internal facet at two fixed Z. Contracted images and unavailable regular top routes are not completed six-form squares. No full compactified boundary atlas, weighted map, global chain orientation or covered A3-stratum theorem.',
        'next_action':'Screen the seven one-parameter infinity boundaries of this shared facet via alpha_j=1/t and a finite target pivot at t=0; classify limiting ranks, source orientation and actual inverse-normal availability. Do not call the seven zero-coordinate faces the complete invariant boundary atlas.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/shared_internal_facet_boundaries.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'summaries':[r['summary'] for r in runs]},indent=2))


if __name__=='__main__':main()
