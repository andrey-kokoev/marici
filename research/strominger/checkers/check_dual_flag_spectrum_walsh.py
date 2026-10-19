"""Independent tracked verifier of the unchanged iteration1 mathematical source.
Uses a FULL invertible Walsh transform, not the generic quotient verifier.
"""
from collections import Counter
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/dual-flag-spectrum-v1.json'
NOTE=ROOT/'research/strominger/dual-flag-spectrum-walsh-v1.md'
MODEL=ROOT/'research/strominger/scc-models/dual-flag-spectrum-walsh-v1.json'
COMMON=HERE.with_name('check_dual_flag_spectrum.py')
OUT=ROOT/'research/strominger/results/dual-flag-spectrum-walsh'
spec=importlib.util.spec_from_file_location('flag_shared_pure_utilities',COMMON)
common=importlib.util.module_from_spec(spec);spec.loader.exec_module(common)
X=sp.Symbol('x')


def progress(message):print(message,file=sys.stderr,flush=True)


def run(report):
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    graph=json.loads((ROOT/f['source_graph']).read_text(encoding='utf-8'))
    prior=json.loads((ROOT/f['source_geometry']).read_text(encoding='utf-8'))
    check('prior_geometry_and_all_its_sources_current',prior['status']=='pass' and all(prior['checks'].values()) and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior['source_sha256'].items()))
    source=prior['regular_candidates']['16-cell']['geometry']
    tetra=source['tetrahedral_facets'];vertices=source['vertices']
    flags=[{'vertex':v,'tetrahedron':i,'tetrahedron_vertices':face} for i,face in enumerate(tetra) for v in face]
    expected=[]
    for i,j in combinations(range(64),2):
        a,b=flags[i],flags[j]
        if (a['tetrahedron']==b['tetrahedron'] and a['vertex']!=b['vertex']) or (a['vertex']==b['vertex'] and len(set(a['tetrahedron_vertices'])&set(b['tetrahedron_vertices']))==3):expected.append([i,j])
    check('original_flags_and_edges_exactly_rebuilt',graph['flags']==flags and graph['edges']==expected and len(expected)==192)
    H=6*sp.eye(64);adj=[set() for _ in flags]
    for i,j in expected:H[i,j]=H[j,i]=-1;adj[i].add(j);adj[j].add(i)
    axis_sign={}
    for i,v in enumerate(vertices):
        entries=[(axis,a,b) for axis,(a,b) in enumerate(v) if (a,b)!=(0,0)]
        check('axis_vertex_'+str(i),len(entries)==1 and entries[0][2]==0 and abs(entries[0][1])==4)
        axis_sign[i]=(entries[0][0],entries[0][1]//4)
    facet_signs=[]
    for face in tetra:
        signs=[0]*4
        for v in face:
            axis,sign=axis_sign[v];signs[axis]=sign
        facet_signs.append(signs)
    check('facets_are_all_16_distinct_sign_vectors',len({tuple(s) for s in facet_signs})==16)
    F=sp.zeros(64)
    for row,flag in enumerate(flags):
        axis,_=axis_sign[flag['vertex']];signs=facet_signs[flag['tetrahedron']]
        for mask in range(16):
            character=1
            for j in range(4):
                if mask>>j&1:character*=signs[j]
            F[row,4*mask+axis]=character
    check('full_Walsh_isometry_keeps_all64_modes',F.T*F==16*sp.eye(64))
    transformed=F.T*H*F/16
    blocks=[transformed[4*m:4*m+4,4*m:4*m+4] for m in range(16)]
    check('actual_full_operator_block_diagonalizes',transformed==sp.diag(*blocks))
    check('all_actual_blocks_match_source_incidence_formula',all(blocks[m]==(4+2*m.bit_count())*sp.eye(4)-2*sp.diag(*[(m>>i)&1 for i in range(4)])-sp.ones(4) for m in range(16)))
    progress('Full64-state Walsh similarity verified; computing small exact blocks.')
    canonical={};multiplicity=Counter();block_records=[]
    for count in range(5):
        block=blocks[(1<<count)-1]
        eigen=block.eigenvals();projectors=[];total=sp.zeros(4)
        for value,rank in eigen.items():
            P=sp.eye(4)
            for other in eigen:
                if other!=value:P=(P*(block-other*sp.eye(4))/(value-other)).applyfunc(sp.simplify)
            check(f'canonical_{count}_projector_{len(projectors)}',(P*P-P).applyfunc(sp.simplify)==sp.zeros(4) and P.T==P and (block*P-value*P).applyfunc(sp.simplify)==sp.zeros(4) and sp.simplify(sp.trace(P)-rank)==0)
            projectors.append({'eigenvalue':value,'rank':int(rank),'projector':P});total+=P
        check('canonical_'+str(count)+'_complete',total.applyfunc(sp.simplify)==sp.eye(4))
        canonical[count]={'operator':block,'projectors':projectors}
    full_poly=sp.Poly(1,X)
    for mask,block in enumerate(blocks):
        order=[i for i in range(4) if mask>>i&1]+[i for i in range(4) if not(mask>>i&1)]
        count=mask.bit_count()
        check('block_permutation_'+str(mask),block.extract(order,order)==canonical[count]['operator'])
        for record in canonical[count]['projectors']:multiplicity[sp.expand(record['eigenvalue'])]+=record['rank']
        full_poly*=block.charpoly(X).as_poly()
        block_records.append({'mask':mask,'operator':block,'axis_order_to_canonical':order,'canonical_weight':count})
    roots=sp.real_roots(full_poly.sqf_part())
    bands=[{'band':i+1,'eigenvalue':str(value),'scalar_rank':multiplicity[sp.expand(value)],'separately_spin_doubled_rank':2*multiplicity[sp.expand(value)]} for i,value in enumerate(roots)]
    check('all_source_spectral_dimensions_retained',sum(b['scalar_rank'] for b in bands)==64 and len(roots)==len(multiplicity))
    check('predicted_first_bands', [b['scalar_rank'] for b in bands[:3]]==f['predictions']['first_three_scalar_band_ranks'])
    power=[[int(i==j) for j in range(64)] for i in range(64)];moments=[]
    for degree in range(11):
        actual=sum(power[i][i] for i in range(64));moments.append(actual)
        predicted=sum(m*value**degree for value,m in multiplicity.items())
        check('full_source_moment_'+str(degree),sp.expand(predicted)==actual)
        if degree<10:
            power=[[6*power[i][j]-sum(power[k][j] for k in adj[i]) for j in range(64)] for i in range(64)]
    progress('All spectral blocks and independent full-graph moments verified; checking rational source interface.')
    B=sp.zeros(64,8)
    for i,flag in enumerate(flags):B[i,flag['vertex']]=1
    D=B.T/8;P=B*D;Q=sp.eye(64)-P
    check('canonical_source_lift_and_decoder',B.T*B==8*sp.eye(8) and D*B==sp.eye(8))
    Hv=6*sp.eye(8)
    for i,j in source['edges']:Hv[i,j]=Hv[j,i]=-1
    h=D*H*B
    check('first_compression_equals_half_original_vertex_operator',h==Hv/2)
    lookup={tuple(tuple(p) for p in v):i for i,v in enumerate(vertices)}
    antipodes=[lookup[tuple((-a,-b) for a,b in v)] for v in vertices]
    T=sp.zeros(8)
    for i,j in enumerate(antipodes):T[j,i]=1
    odd=(sp.eye(8)-T)/2;even=sp.eye(8)-odd
    K=Q*H*B;residual=D*H*H*B-h*h
    check('source_composition_residual_is_nonzero_rank4',residual==3*odd and odd*odd==odd and sp.trace(odd)==4)
    check('leakage_exact_Gram_certificate',K.T*K/8==3*odd and K*even==sp.zeros(64,8))
    representatives=[i for i,j in enumerate(antipodes) if i<j]
    K4=K[:,representatives]
    check('four_independent_memory_columns',K4.T*K4==12*sp.eye(4) and B.T*K4==sp.zeros(8,4))
    q=K4[:,0]
    check('forgotten_information_reappears_under_next_reader',D*q==sp.zeros(8,1) and D*H*q!=sp.zeros(8,1))
    encoder=D.col_join(Q);decoder=B.row_join(sp.eye(64))
    check('full_packet_reconstruction_proves_rank64',decoder*encoder==sp.eye(64))
    full_left=(B*D+Q)*H*(B*D+Q)*H;full_right=H*H
    check('retaining_residual_preserves_two_applications',full_left==full_right)
    W=B.row_join(K4);gram=sp.diag(*([8]*8+[12]*4));left_inverse=sp.diag(*([sp.Rational(1,8)]*8+[sp.Rational(1,12)]*4))*W.T
    check('closure_Gram_certificate_rank12',W.T*W==gram and left_inverse*W==sp.eye(12))
    A=left_inverse*H*W
    check('minimal_closure_intertwines_source_and_inherits_metric',H*W==W*A and A.T*gram==gram*A)
    check('closure_generated_by_original_preparations_and_one_application',H*B-B*h==K and K*even==sp.zeros(64,8) and H*K4==B*(3*odd[:,representatives])+3*K4)
    Pclosed=W*left_inverse;memory=Pclosed-P;unseen=sp.eye(64)-Pclosed
    check('orthogonal_8_plus4_plus52_decomposition',Pclosed.T==Pclosed and Pclosed*Pclosed==Pclosed and memory*memory==memory and sp.trace(P)==8 and sp.trace(memory)==4 and sp.trace(unseen)==52)
    check('52_other_modes_task_invisible_not_deleted',D*unseen==sp.zeros(8,64) and H*unseen==unseen*H and unseen!=sp.zeros(64))
    closure_poly=sp.factor(A.charpoly(X).as_expr())
    check('closure_spectrum_certified',sp.expand(closure_poly-X*(X-4)**3*(X**2-6*X+6)**4)==0)
    compiler=common.load('independent_flag_compiler',common.COMPILER)
    coarse=common.diagram('coarse_forgetting_composition',8,D*H*H*B,h*h)
    retained=common.diagram('retained_packet_composition',64,full_left,full_right)
    bad=compiler.compile_diagram(coarse);good=compiler.compile_diagram(retained)
    check('SCC_localizes_actual_failed_coarse_cell',not bad['passed'] and good['passed'])
    OUT.mkdir(parents=True,exist_ok=True)
    for name,d in [('coarse',coarse),('retained',retained)]:
        (OUT/(name+'-diagram.json')).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
    report.update({'classification':'raw_flags_split_and_vertex_forgetting_requires_four_memory_modes','iteration':1,
      'bands':bands,'scalar_band_ranks':[b['scalar_rank'] for b in bands],'separately_spin_doubled_band_ranks':[b['separately_spin_doubled_rank'] for b in bands],
      'full_state_Walsh':{'matrix':F,'scale_squared':16,'blocks':block_records,'canonical_projectors':canonical,'full_characteristic_polynomial':str(full_poly.as_expr()),'full_graph_moments':moments},
      'H':H,'incidence_lift_B':B,'reader_D':D,'source_projector':P,'instantaneous_discarded_projector':Q,'compressed_operator':h,'original_vertex_operator':Hv,
      'odd_vertex_projector':odd,'leakage_K':K,'composition_residual':residual,'composition_residual_rank':4,
      'reader_witness':{'flag_state':q,'coarse_now':D*q,'coarse_after_H':D*H*q},
      'full_packet':{'encoder':encoder,'decoder':decoder,'display_coordinates':72,'independent_rank':64},
      'minimal_closure':{'Krylov_ranks_certified':[8,12,12],'dimension':12,'inclusion':W,'left_inverse':left_inverse,'metric':gram,'operator':A,'characteristic_polynomial':str(closure_poly),'memory_projector':memory,'other_modes_projector':unseen,'other_full_source_modes':52},
      'compiled_cells':{'coarse':bad,'retained':good},
      'scope':'Same original64-mode source; source-specific12-mode closure is not a principal electron-shell capacity, physical gauge quotient or native P/N/E bridge. Spin/statistics remain external assumptions.',
      'execution_boundary':'Independent verifier and separate output. The original synchronous generic run returned no execution_ref or verified outcome; no conclusion about its termination is inferred.'})


def main():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    paths=[HERE,FIXTURE,NOTE,MODEL,COMMON,HERE.with_name('check_dual_flag_spectrum_walsh_scc.py'),ROOT/f['net'],ROOT/f['source_graph'],ROOT/f['source_geometry'],common.COMPILER]
    report={'schema':'marici.strominger.dual-flag-spectrum-walsh.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},'sympy_version':sp.__version__,'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:run(report);report['status']='pass'
    except Exception as error:report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(common.serial(report),indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),
          'scalar_bands':report.get('scalar_band_ranks'),'composition_defect_rank':report.get('composition_residual_rank'),
          'minimal_closure':report.get('minimal_closure',{}).get('dimension'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
