#!/usr/bin/env python3
"""Rank-two primitive germs with source-derived intrinsic dlog transitions."""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_shared_facet_primitive_census import s,rational,parameters,source_key,dimension,cyclic_coarsenings,derivative
from check_three_composite_inverse_normals import normalize,target_jac,extract,setup_H,inverse_H,setup_A,inverse_A
from check_three_composite_boundary_residues import weights,physical
from check_paired_composite_corner_residues import gradient
PRIOR='research/benincasa/results/three_composite_normalizations.json'
CENSUS='research/benincasa/results/shared_facet_primitive_census.json'
INVERSES='research/benincasa/results/three_composite_inverse_normals.json'


def groups_for(embedding):
    groups=[tuple(g) for g in embedding['cell_key']['parallel_classes']]
    used={x for g in groups for x in g}
    groups += [(x,) for x in embedding['support'] if x not in used]
    return sorted(groups,key=min)


def covers(groups):
    out=[]
    for i,g in enumerate(groups):
        if len(g)>1:
            for label in g:out.append({'id':f'delete-{label}','type':'delete','label':label,'group':i})
    for i in range(len(groups)):out.append({'id':f'merge-{i}-{(i+1)%len(groups)}','type':'merge','edge':i})
    return out


def source_chart(groups,operation):
    # Keep a merger between the first two middle direction classes. Both
    # framing directions stay distinct, including when merging across the cut.
    cut=0 if operation['type']=='delete' else (operation['edge']-1)%len(groups)
    ordered=groups[cut:]+groups[:cut];labels=[x for g in ordered for x in g]
    deleted=operation.get('label');first=next(x for x in ordered[0] if x!=deleted);last=next(x for x in ordered[-1] if x!=deleted)
    gaps=list(s.symbols('g1:'+str(len(groups)-1)))
    scales={x:s.Symbol('l'+str(x)) for x in labels if x not in (first,last)}
    allcoords=gaps+list(scales.values());assert len(allcoords)==8
    radial=scales[deleted] if deleted is not None else gaps[0];t=s.Symbol('t')
    coordinates=[t]+[z for z in allcoords if z!=radial]
    C=s.zeros(2,8);cut_label=labels[0]
    for i,g in enumerate(ordered):
        vector=s.Matrix([1,0]) if i==0 else s.Matrix([0,1]) if i==len(ordered)-1 else s.Matrix([sum(gaps[i-1:]),1])
        for label in g:
            scale=scales.get(label,s.Integer(1));sign=-1 if label<cut_label else 1
            C[:,label-1]=sign*scale*vector
    C=C.subs(radial,t)
    return C,coordinates,{'cyclic_classes':[list(g) for g in ordered],'cut_label':cut_label,
        'first_anchor':first,'last_anchor':last,'radial_original_symbol':str(radial),
        'ordered_gaps':[str(z) for z in gaps],'scales':{str(x):str(z) for x,z in scales.items()},
        'coordinate_order':[str(z) for z in coordinates],'wrapped_sign':-1}


def radial_from_source(R,frame,operation):
    first,last=frame['first_anchor'],frame['last_anchor'];cut=frame['cut_label']
    def col(label):return (-1 if label<cut else 1)*R[:,label-1]
    W=s.Matrix.hstack(col(first),col(last));assert W.det()!=0
    B=(W.inv()*R).applyfunc(rational)
    def c(label):return (-1 if label<cut else 1)*B[:,label-1]
    if operation['type']=='delete':
        label=operation['label'];group=next(i for i,g in enumerate(frame['cyclic_classes']) if label in g)
        return rational(c(label)[0] if group==0 else c(label)[1])
    reps=[g[0] for g in frame['cyclic_classes']]
    return rational(c(reps[1])[0]/c(reps[1])[1]-c(reps[2])[0]/c(reps[2])[1])


def intrinsic_transition(C,coordinates,embedding,fixed):
    alpha,_,_=extract(C,embedding)
    # Exact source dlog transition circuit, never a fitted per-face scale.
    av=[rational(x.subs(fixed)) for x in alpha]
    ordinary=s.Matrix([[rational(s.diff(x,z).subs(fixed)) for z in coordinates] for x in alpha])
    logJ=s.diag(*[1/x for x in av])*ordinary*s.diag(*[fixed.get(z,z) for z in coordinates])
    det=rational(logJ.det(method='domain-ge'));t=coordinates[0]
    numerator,denominator=s.fraction(det);assert denominator.subs(t,0)!=0
    coefficient=rational(det.subs(t,0));assert coefficient!=0
    assert all(x.subs(t,1)>0 and x.subs(t,s.Rational(1,2))>0 for x in av)
    return alpha,det,coefficient


def check_face(row,operation,cache):
    embedding=row['superfunction_runs'][0]['matches'][0];groups=groups_for(embedding)
    C,coordinates,frame=source_chart(groups,operation);t=coordinates[0];C0=C.subs(t,0)
    key=source_key(C0);assert dimension(key)==7
    # Named positive gap/scale fixture, held constant for both external Z.
    fixed=dict(zip(coordinates[1:],[s.Integer(x) for x in [2,3,5,7,11,13,17]]))
    alpha,logdet,coefficient=intrinsic_transition(C,coordinates,embedding,fixed)
    # Actual intrinsic source reconstruction at a positive top point.
    a,original,_=parameters(row['target_runs'][0]);positive=dict(zip(a,[x.subs(fixed).subs(t,1) for x in alpha]))
    Cp=C0.subs(fixed);assert Cp.rank()==2 and all(Cp[:,list(p)].det()>=0 for p in itertools.combinations(range(8),2))
    top=C.subs(fixed).subs(t,1)
    pivot_source=next(p for p in itertools.combinations(range(8),2) if Cp[:,list(p)].det()>0)
    assert normalize(top,list(pivot_source))==normalize(original.subs(positive),list(pivot_source))
    ds=[derivative(Cp,C0.diff(z).subs(fixed),list(pivot_source)) for z in coordinates[1:]]
    sourcecoords=[(i,j) for i in range(2) for j in range(8) if j not in pivot_source]
    assert s.Matrix([[d[i,j] for d in ds] for i,j in sourcecoords]).rank()==7
    minors={(i,j):s.factor(C[:,[i,j]].det()) for i,j in itertools.combinations(range(8),2)}
    runs=[]
    for shift in (0,1):
        Z,W=cache[shift];Y=Cp*Z;N=normalize(Y,[0,1])
        J,coords=target_jac(Y,[C.diff(z).subs(t,0).subs(fixed)*Z for z in coordinates],[0,1])
        F=J[:,1:]*s.diag(*[fixed[z] for z in coordinates[1:]]);rank=F.rank()
        polynomials={q:s.factor(sum(minors[i,j]*weight for i,j,weight in ws)) for q,ws in W.items()}
        vanished=[q for q,p in polynomials.items() if p.subs(t,0)==0]
        candidates=[q for q in vanished if polynomials[q]!=0 and s.diff(polynomials[q],t).subs(t,0).subs(fixed)!=0]
        run={'positive_Z_moment_shift':shift,'source_tangent_rank':7,'target_tangent_rank':rank,'full_target_germ_rank':J.rank(),
            'source_log_transition_function':str(logdet),'source_boundary_coefficient':str(coefficient),
            'vanishing_brackets':[list(q) for q in vanished],'physical_brackets':[list(q) for q in vanished if physical(q)]}
        if rank<7:
            run.update({'disposition':'primitive_source_facet_target_contracted','ordinary_target_residue':None,'actual_normal':None})
            runs.append(run);continue
        assert rank==7 and J.det()!=0
        selected=next(I for I in itertools.combinations(range(8),7) if F[list(I),:].det()!=0)
        det=s.factor(F[list(selected),:].det());prod=s.prod(fixed[z] for z in coordinates[1:])
        if candidates:
            quad=next((q for q in candidates if physical(q)),candidates[0]);g=gradient(N,Z,quad,coords)
            normal={'type':'actual_normalized_target_bracket','bracket':list(quad),'physical':physical(quad),
                'raw_symbolic_source_pullback':str(polynomials[quad])}
        else:
            data=setup_H(Z,embedding) if embedding['seed']=='H' else setup_A(Z,embedding)
            def b(target):
                R,_=inverse_H(target,data) if embedding['seed']=='H' else inverse_A(target,data)
                return radial_from_source(R,frame,operation)
            assert b(N)==0
            Nt=normalize(C.subs(fixed)*Z,[0,1]).applyfunc(rational);assert rational(b(Nt)-t)==0
            h=s.Symbol('h');values=[]
            for i,j in coords:
                E=s.zeros(2,6);E[i,j]=1;values.append(rational(s.diff(b(N+h*E),h).subs(h,0)))
            g=s.Matrix(1,8,values)
            normal={'type':'actual_source_fiber_inverse_gap_normal','physical':False,
                'rule':'Reconstruct source through pinned A/H circuit; fix this cyclic frame by first/last anchors; subtract slopes of middle classes1_and2.',
                'arc_identity':'b(target_source_arc(t))=t identically'}
        normals=g*J;assert normals[0]!=0 and all(normals[j]==0 for j in range(1,8))
        D=s.Matrix.vstack(normals,J[list(selected),:]);assert D.det()!=0
        source=s.factor(coefficient/det);target=s.factor(coefficient*normals[0]/(prod*D.det()));assert source==target and -source!=target
        run.update({'disposition':'physical_primitive_local_residue' if normal.get('physical') else 'nonphysical_or_nonlinear_primitive_local_residue',
            'actual_normal':normal,'selected_target_coordinate_indices':list(selected),'boundary_log_jacobian':str(det),
            'normal_source_slope':str(normals[0]),'source_residue_then_pushforward':str(source),
            'top_pushforward_then_actual_target_residue':str(target),'orientation_failure_residual':str(-source-target)})
        runs.append(run)
    assert [(r['target_tangent_rank'],r['disposition']) for r in runs[:1]]==[(r['target_tangent_rank'],r['disposition']) for r in runs[1:]]
    return {'operation':operation,'frame':frame,'source_chart_matrix':[[str(x) for x in rr] for rr in C.tolist()],
        'source_boundary_class_key':[list(g) for g in key],
        'intrinsic_alpha_transition':[str(x) for x in alpha],'source_log_transition_rule':'det(diag(1/alpha)*d(alpha)/d(ordered_gap_scale_coordinates)*diag(ordered_gap_scale_coordinates))',
        'positive_source_fixture':{str(z):str(x) for z,x in fixed.items()},'runs':runs}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());census=json.loads((ROOT/CENSUS).read_text());inv=json.loads((ROOT/INVERSES).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
        (census,'research/benincasa/checkers/check_shared_facet_primitive_census.py'),
        (inv,'research/benincasa/checkers/check_three_composite_inverse_normals.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    cache={}
    for shift in (0,1):
        Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)]);cache[shift]=(Z,weights(Z))
    rows=[]
    for row in prior['rows']:
        embedding=row['superfunction_runs'][0]['matches'][0];groups=groups_for(embedding);assert dimension(tuple(groups))==8
        faces=[check_face(row,operation,cache) for operation in covers(groups)]
        keys=[tuple(tuple(g) for g in f['source_boundary_class_key']) for f in faces];assert len(keys)==len(set(keys))
        summary={'primitive_source_facets':len(faces),'physical_rank7_faces':sum(f['runs'][0]['disposition']=='physical_primitive_local_residue' for f in faces),
            'nonphysical_bracket_faces':sum((f['runs'][0].get('actual_normal') or {}).get('type')=='actual_normalized_target_bracket' and not f['runs'][0]['actual_normal']['physical'] for f in faces),
            'nonlinear_inverse_faces':sum((f['runs'][0].get('actual_normal') or {}).get('type')=='actual_source_fiber_inverse_gap_normal' for f in faces),
            'contracted_faces':sum(f['runs'][0]['target_tangent_rank']<7 for f in faces)}
        rows.append({'history_index':row['history_index'],'root':row['root'],'parent_cyclic_classes':[list(g) for g in groups],
            'parent_source_dimension':8,'faces':faces,'summary':summary})
    assert [r['summary']['primitive_source_facets'] for r in rows]==[9,10,9]
    assert [r['summary']['physical_rank7_faces'] for r in rows]==[5,6,5]
    checks={'twenty_eight_invariant_primitive_source_germs':True,'positive_cyclic_frames_and_symbolic_dimension7_source_keys':True,
        'derived_intrinsic_A_H_log_transition_circuits_and_exact_radial_coefficients':True,
        'twenty_eight_positive_intrinsic_source_reconstructions':True,'fifty_six_source_and_target_rank_screens':True,
        'physical_rank7_counts_5_6_5_recovered_without_fitting':True,'all_admitted_actual_normal_residue_squares_equal_orientation_hostiles_nonzero':True,
        'nonlinear_inverse_arc_controls_and_primitive_contractions_retained':True}
    paths=[PRIOR,CENSUS,INVERSES,'research/benincasa/checkers/check_three_composite_normalizations.py',
        'research/benincasa/checkers/check_shared_facet_primitive_census.py',
        'research/benincasa/checkers/check_three_composite_inverse_normals.py',
        'research/benincasa/checkers/check_three_composite_boundary_residues.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.three-composite-primitive-atlas.v1','rows':rows,'checks':checks,'passed':True,
        'disposition':'three_intrinsic_rank2_primitive_source_censuses_with_oriented_local_5_6_5_physical_provenance',
        'claim_boundary':'Complete primitive rank2 positive source-stratum census for these three matched intrinsic cells; explicit cyclic germs and source-derived log transitions. Target ranks/normals/residue squares at two fixed external Z and named positive source fixtures. Not recovered historical BCFW chain, global positive covering/orientation anchor, supercomponent extraction or weighted nine-sector map.',
        'next_action':'Find equal invariant source boundary keys across these three primitive censuses. Compare the actual common internal facets in identical source and target coordinates, derive boundary log transitions and test oriented paired cancellations; do not pair equal physical bracket labels with different source keys.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/three_composite_primitive_atlas.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'summaries':[{'history_index':r['history_index'],**r['summary']} for r in rows],'checks':checks},indent=2))


if __name__=='__main__':main()
