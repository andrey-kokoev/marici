#!/usr/bin/env python3
"""All 24 selected composite coordinate faces: target ranks and local residues.

An isolated coordinate screen is not the recovered invariant boundary atlas.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as s
from check_composite_root_normalization import normalize,target_jac

PRIOR='research/benincasa/results/three_composite_normalizations.json'
FIRST='research/benincasa/results/composite_boundary_residue_square.json'
QUADS=list(itertools.combinations(range(1,9),4))


def physical(quad):
    q=set(quad)
    return any({i,i%8+1,j,j%8+1}==q and len({i,i%8+1,j,j%8+1})==4
               for i in range(1,9) for j in range(i+1,9))


def weights(Z):
    return {q:[(i,j,s.Matrix.vstack(Z[i,:],Z[j,:],*[Z[k-1,:] for k in q]).det())
        for i,j in itertools.combinations(range(8),2) if i+1 not in q and j+1 not in q] for q in QUADS}


def scan(sample,W):
    a=s.symbols('a1:9');C=s.Matrix([[s.sympify(v) for v in row] for row in sample['source_chart_matrix']])
    Z=s.Matrix([[s.Integer(j+sample['positive_Z_moment_shift'])**k for k in range(6)] for j in range(1,9)])
    vals={v:s.Integer(sample['source_parameters'][str(v)]) for v in a}
    minors={(i,j):s.factor(C[:,[i,j]].det()) for i,j in itertools.combinations(range(8),2)}
    ps={q:s.factor(sum(minors[i,j]*k for i,j,k in W[q])) for q in QUADS}
    Ysym=C*Z;pivot=s.factor(Ysym[:,[0,1]].det());rows=[]
    for e,z in enumerate(a):
        v=vals|{z:s.Integer(0)};Y=Ysym.subs(v);assert pivot.subs(v)!=0
        N=normalize(Y,[0,1]);free=[j for j in range(8) if j!=e]
        J,coords=target_jac(Y,[C.diff(x).subs(v)*Z for x in a],[0,1])
        Jfree=J[:,free]*s.diag(*[vals[a[j]] for j in free]);rank=Jfree.rank()
        full_rank=J.rank()
        vanished=[q for q in QUADS if ps[q].subs(z,0)==0]
        phys=[q for q in vanished if physical(q)]
        source_minors=[value.subs(v) for value in minors.values()]
        assert all(value>=0 for value in source_minors)
        disposition=('contracted_rank_below_seven' if rank<7 else
                     'physical_divisor_local_branch' if phys else 'rank_seven_nonphysical_or_nonlinear_image')
        residue=None
        if rank==7:
            candidates=[q for q in vanished if ps[q]!=0 and s.diff(ps[q],z).subs(v)!=0]
            if candidates:
                quad=next((q for q in candidates if physical(q)),candidates[0]);p=ps[quad]
                slope=s.factor(s.diff(p,z).subs(v)/pivot.subs(v))
                assert slope!=0
                selected=next(I for I in itertools.combinations(range(8),7) if Jfree[list(I),:].det()!=0)
                det=s.factor(Jfree[list(selected),:].det())
                gradient=[]
                for i,j in coords:
                    E=s.zeros(2,6);E[i,j]=1
                    gradient.append(s.factor(s.Matrix.vstack(E[0,:],N[1,:],*[Z[k-1,:] for k in quad]).det()+
                        s.Matrix.vstack(N[0,:],E[1,:],*[Z[k-1,:] for k in quad]).det()))
                normals=s.Matrix(1,8,gradient)*J
                assert normals[0,e]==slope and all(normals[0,j]==0 for j in free)
                full=s.Matrix.vstack(normals,J[list(selected),:]);detfull=s.factor(full.det());assert detfull!=0
                sign=(-1)**e
                routeA=s.factor(sign/det)
                routeB=s.factor(slope/(s.prod(vals[a[j]] for j in free)*detfull))
                assert routeA==routeB and -routeA!=routeB
                residue={'target_bracket':list(quad),'physical':physical(quad),'symbolic_raw_bracket':str(p),
                    'normalized_target_normal':'raw bracket / det((CZ)[:,columns1,2])',
                    'normal_slope':str(slope),'source_residue_sign':sign,
                    'selected_target_coordinate_indices':list(selected),
                    'selected_target_coordinates':[[coords[i][0]+1,coords[i][1]+1] for i in selected],
                    'boundary_log_jacobian':str(det),'full_ordinary_normal_jacobian':str(detfull),
                    'source_residue_then_pushforward':str(routeA),'top_pushforward_then_target_residue':str(routeB),
                    'orientation_failure_residual':str(-routeA-routeB)}
        if rank<7:residue_status='no_rank7_divisorial_pushforward_in_this_chart'
        elif residue is None:residue_status='missing_regular_bracket_normal; nonlinear_or_singular_normal_not_constructed'
        else:residue_status='constructed_local_oriented_differential_square'
        rows.append({'alpha':e+1,'target_tangent_rank':rank,'ordinary_target_full_rank':full_rank,'source_residue_sign':(-1)**e,
            'source_boundary_parameters':{str(x):str(w) for x,w in v.items()},
            'identically_vanishing_four_brackets':[list(q) for q in vanished],
            'physical_adjacent_pair_brackets':[list(q) for q in phys],
            'disposition':disposition,'residue_status':residue_status,'local_residue_square':residue})
    return {'positive_Z_moment_shift':sample['positive_Z_moment_shift'],'faces':rows}


def verify_receipt(path,checker):
    r=json.loads((ROOT/path).read_text())
    for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert sha256((ROOT/checker).read_bytes()).hexdigest()==r['checker_sha256']
    return r


def main():
    prior=verify_receipt(PRIOR,'research/benincasa/checkers/check_three_composite_normalizations.py')
    first=verify_receipt(FIRST,'research/benincasa/checkers/check_composite_boundary_residue_square.py')
    cache={shift:weights(s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])) for shift in (0,1)}
    rows=[]
    for row in prior['rows']:
        runs=[scan(sample,cache[sample['positive_Z_moment_shift']]) for sample in row['target_runs']]
        signatures=lambda run:[(f['alpha'],f['target_tangent_rank'],f['identically_vanishing_four_brackets'],f['residue_status']) for f in run['faces']]
        assert signatures(runs[0])==signatures(runs[1])
        summary={kind:sum(f['disposition']==kind for f in runs[0]['faces']) for kind in
            ['physical_divisor_local_branch','rank_seven_nonphysical_or_nonlinear_image','contracted_rank_below_seven']}
        summary['local_residue_squares']=sum(f['local_residue_square'] is not None for f in runs[0]['faces'])
        summary['rank7_without_bracket_normal']=sum(f['target_tangent_rank']==7 and f['local_residue_square'] is None for f in runs[0]['faces'])
        assert all(f['ordinary_target_full_rank']==8 for run in runs for f in run['faces']
                   if f['target_tangent_rank']==7 and f['local_residue_square'] is None)
        if row['history_index']==5:
            for run,old in zip(runs,first['runs']):
                face=run['faces'][1]['local_residue_square']
                assert face['source_residue_then_pushforward']==old['source_residue_then_pushforward']
                assert face['top_pushforward_then_target_residue']==old['top_pushforward_then_target_residue']
        rows.append({'history_index':row['history_index'],'root':row['root'],'seed':row['seed'],'summary_per_fixture':summary,'runs':runs})
    total={key:sum(r['summary_per_fixture'][key] for r in rows) for key in rows[0]['summary_per_fixture']}
    assert sum(total[k] for k in ['physical_divisor_local_branch','rank_seven_nonphysical_or_nonlinear_image','contracted_rank_below_seven'])==24
    checks={'48_coordinate_face_evaluations':True,'two_fixture_rank_and_bracket_signatures_agree':True,
        'all_constructed_local_residue_routes_equal':True,'all_orientation_failure_controls_nonzero':True,
        'source_boundary_positivity_checked':True,'first_history5_residue_receipt_preserved':True,
        'contracted_and_missing_normal_dispositions_retained':True,
        'three_missing_bracket_normals_have_full_rank_eight_at_both_samples':True}
    paths=[PRIOR,FIRST,'research/benincasa/checkers/check_three_composite_normalizations.py',
        'research/benincasa/checkers/check_composite_boundary_residue_square.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.three-composite-boundary-residues.v1','rows':rows,
        'totals_per_fixture':total,'checks':checks,'passed':True,
        'disposition':'selected_composite_coordinate_boundary_screen_and_bracket_normal_residue_squares_constructed',
        'claim_boundary':'Twenty-four selected chart faces tested at two positive Z/source fixtures; symbolic bracket restrictions in source coordinates for those Z. No invariant atlas completeness, global target degree, cross-history normalization/cancellation, BCFW orientation anchor or supercomponent boundary map.',
        'next_action':'Construct an inverse-branch target normal for the alpha4=0 image of one composite: full ordinary differential rank is eight while the boundary rank is seven, but no four-bracket defines it. Verify an actual local inverse/germ, not a fitted linear tangent plane. Alternatively compare shared composite source facets on a common target chart. Neither task supplies the complete 5/6/5 atlas.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/three_composite_boundary_residues.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'summary':[{k:r[k] for k in ('history_index','root','summary_per_fixture')} for r in rows],
        'totals_per_fixture':total,'checks':checks},indent=2))


if __name__=='__main__':main()
