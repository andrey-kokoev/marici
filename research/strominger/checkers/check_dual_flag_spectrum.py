"""Iteration1: exact frozen flag spectrum and canonical forgetting interface.
Run via uv run --with sympy python. No physical occupation rule is supplied.
"""
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/dual-flag-spectrum-v1.json'
PACKET=ROOT/'research/strominger/dual-tetrahedral-branching-iteration-01.md'
MODEL=ROOT/'research/strominger/scc-models/dual-flag-spectrum-v1.json'
COMPILER=ROOT/'research/aspect/scc/categorical_compiler.py'
OUT=ROOT/'research/strominger/results/dual-flag-spectrum'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def serial(value):
    if isinstance(value,sp.MatrixBase):return [[str(x) for x in row] for row in value.tolist()]
    if isinstance(value,sp.Basic):return str(value)
    if isinstance(value,dict):return {key:serial(v) for key,v in value.items()}
    if isinstance(value,(list,tuple)):return [serial(v) for v in value]
    return value


def digest(value):
    return sha256(json.dumps(serial(value),sort_keys=True).encode()).hexdigest()


def diagram(name,dimension,left,right):
    obj=f'Q{dimension}'
    return {'id':name,'objects':[{'id':obj}],
      'arrows':[{'id':side,'source':obj,'target':obj,'map_token':digest(m),'evaluated_map':serial(m)} for side,m in [('left',left),('right',right)]],
      'cells':[{'id':name,'kind':'evaluated_source_composition_comparison','routes':[['left'],['right']],'threshold':'exact_zero'}],
      'obstructions':[],'claims':[], 'scope':'Owner-calculated exact source matrices; no physical-time or higher-native-cell assertion'}


def run(report):
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    graph=json.loads((ROOT/f['source_graph']).read_text(encoding='utf-8'))
    prior=json.loads((ROOT/f['source_geometry']).read_text(encoding='utf-8'))
    check('prior_geometry_receipt_passed',prior['status']=='pass' and all(prior['checks'].values()))
    check('all_transitive_geometry_source_pins_current',all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior['source_sha256'].items()))
    source=prior['regular_candidates']['16-cell']['geometry']
    tetra=source['tetrahedral_facets']
    flags=[{'vertex':v,'tetrahedron':i,'tetrahedron_vertices':face} for i,face in enumerate(tetra) for v in face]
    check('all_original_flag_labels_reconstructed_without_coercion',graph['flags']==flags and len(flags)==64)
    expected=[]
    for i,j in combinations(range(64),2):
        a,b=flags[i],flags[j]
        if (a['tetrahedron']==b['tetrahedron'] and a['vertex']!=b['vertex']) or (a['vertex']==b['vertex'] and len(set(a['tetrahedron_vertices'])&set(b['tetrahedron_vertices']))==3):expected.append([i,j])
    check('original_192_edges_and_operator_unchanged',graph['edges']==expected and len(expected)==192 and graph['operator']=='degree6 I - adjacency')
    adjacency=[set() for _ in flags]
    H=sp.eye(64)*6
    for i,j in graph['edges']:adjacency[i].add(j);adjacency[j].add(i);H[i,j]=H[j,i]=-1
    helper=load('flag_exact_spectral_source',ROOT/f['spectral_constructor'])
    spectrum=helper.spectrum('source_flag',adjacency,check)
    scalar=[b['scalar_rank'] for b in spectrum['bands']]
    doubled=[b['spin_resolved_capacity'] for b in spectrum['bands']]
    check('predicted_first_three_band_ranks',scalar[:3]==f['predictions']['first_three_scalar_band_ranks'] and doubled[:3]==f['predictions']['first_three_separately_spin_doubled_ranks'])
    check('raw_64_labels_not_one_retained_spectral_band',sum(scalar)==64 and len(scalar)>1 and max(scalar)<64)
    B=sp.zeros(64,8)
    for i,flag in enumerate(flags):B[i,flag['vertex']]=1
    D=B.T/8;P=B*D;Q=sp.eye(64)-P
    check('canonical_incidence_lift_retains_every_vertex',B.T*B==8*sp.eye(8) and D*B==sp.eye(8))
    check('forgetting_plus_residual_is_full_exact_packet',P+Q==sp.eye(64) and P*P==P and Q*Q==Q and D*Q==sp.zeros(8,64))
    Hv=6*sp.eye(8)
    for i,j in source['edges']:Hv[i,j]=Hv[j,i]=-1
    h=D*H*B
    check('first_compression_is_half_original_vertex_operator',h==Hv/2)
    vertices=source['vertices'];lookup={tuple(tuple(p) for p in v):i for i,v in enumerate(vertices)}
    antipode=sp.zeros(8)
    for i,v in enumerate(vertices):antipode[lookup[tuple((-a,-b) for a,b in v)],i]=1
    odd=(sp.eye(8)-antipode)/2;even=(sp.eye(8)+antipode)/2
    K=Q*H*B
    residual=D*H*H*B-h*h
    check('genuine_composition_defect_has_rank_four',residual==3*odd and residual.rank()==f['predictions']['leakage_rank'])
    check('leakage_gram_and_even_sector_exact',K.T*K/8==3*odd and K.rank()==4 and K*even==sp.zeros(64,8))
    witness_column=next(j for j in range(8) if K[:,j]!=sp.zeros(64,1))
    q=K[:,witness_column]
    check('discarded_flag_information_is_detectable_by_next_source_reader',D*q==sp.zeros(8,1) and D*H*q!=sp.zeros(8,1))
    encoder=D.col_join(Q);decoder=B.row_join(sp.eye(64))
    check('retained_packet_has_full_rank_not_new_independent_degrees',decoder*encoder==sp.eye(64) and encoder.rank()==64)
    full_left=decoder*encoder*H*decoder*encoder*H
    full_right=H*H
    check('full_retained_packet_preserves_two_applications',full_left==full_right)
    C1=B.row_join(H*B);C2=C1.row_join(H*H*B)
    ranks=[B.rank(),C1.rank(),C2.rank()]
    check('Krylov_closure_ranks_are_8_12_12',ranks==[8,12,12])
    W=sp.Matrix.hstack(*C1.columnspace());gram=W.T*W;left_inverse=gram.inv()*W.T
    closed=left_inverse*H*W;Pclosed=W*left_inverse
    check('explicit_minimal_closure_intertwiner',W.cols==f['predictions']['minimal_vertex_initiated_invariant_closure_dimension'] and left_inverse*W==sp.eye(12) and H*W==W*closed)
    check('closure_inherits_the_source_metric',closed.T*gram==gram*closed and Pclosed.T==Pclosed and Pclosed*Pclosed==Pclosed)
    check('closure_is_minimal_and_reducing_for_the_fixed_task',Pclosed*B==B and H*Pclosed==Pclosed*H and C1.rank()==W.cols)
    memory=Pclosed-P;unused=sp.eye(64)-Pclosed
    check('eight_source_four_memory_fiftytwo_other_modes_preserved',memory*memory==memory and memory.rank()==4 and unused.rank()==52 and P+memory+unused==sp.eye(64))
    check('other52_modes_are_task_invisible_not_declared_physical_gauge',D*unused==sp.zeros(8,64) and H*unused==unused*H and unused!=sp.zeros(64))
    check('minimal_closure_spectrum_certified',sp.factor(closed.charpoly(helper.X).as_expr())==sp.expand(helper.X*(helper.X-4)**3*(helper.X**2-6*helper.X+6)**4).factor())
    compiler=load('flag_composition_scc',COMPILER)
    coarse=diagram('coarse_forgetting_composition',8,D*H*H*B,h*h)
    retained=diagram('retained_packet_composition',64,full_left,full_right)
    bad=compiler.compile_diagram(coarse);good=compiler.compile_diagram(retained)
    check('SCC_assigns_failed_cell_to_coarse_compression',not bad['passed'] and all(not c['passed'] for c in bad['cells']))
    check('SCC_accepts_full_retained_comparison',good['passed'])
    OUT.mkdir(parents=True,exist_ok=True)
    for name,d in [('coarse',coarse),('retained',retained)]:
        (OUT/(name+'-diagram.json')).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
    report.update({'classification':'flag_bands_split_raw_count_and_canonical_vertex_forgetting_fails_composition','iteration':1,
      'spectrum':spectrum,'scalar_band_ranks':scalar,'separately_spin_doubled_band_ranks':doubled,
      'H':H,'incidence_lift_B':B,'reader_D':D,'initial_projector':P,'instantaneous_residual_projector':Q,
      'original_vertex_operator':Hv,'compressed_operator':h,'antipodal_vertex_action':antipode,'odd_vertex_projector':odd,
      'leakage_K':K,'composition_residual':residual,'composition_residual_rank':4,
      'lost_information_witness':{'flag_vector':q,'reader_now':D*q,'reader_after_H':D*H*q},
      'full_packet':{'encoder':encoder,'decoder':decoder,'display_coordinates':72,'independent_rank':64},
      'minimal_closure':{'Krylov_ranks':ranks,'dimension':12,'inclusion_W':W,'left_inverse':left_inverse,'metric':gram,'operator':closed,'projector':Pclosed,
        'characteristic_polynomial':str(sp.factor(closed.charpoly(helper.X).as_expr())),'source_dimension':8,'additional_memory_dimension':4,'other_full_flag_modes':52,'memory_projector':memory,'task_invisible_projector':unused},
      'compiled_cells':{'coarse':bad,'retained':good},
      'scientific_disposition':'The declared raw64 count is not one spectral capacity. A canonical source map exists, but forgetting tetrahedron labels does not preserve the enabled H-composition task. A12-dimensional minimal task carrier is constructed without changing H; all64 original modes remain available.',
      'physical_boundary':'No spin, electron principal grading, native P/N/E attachment, physical occupation or stability derived.12/24 here are not a reindexed principal-shell result.',
      'enabled_successor':'Compare the same incidence-derived flag operator and canonical forgetting closure across cross-polytope dimensions2..6, with d distinct from spectral grade.'})


def main():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    paths=[HERE,FIXTURE,PACKET,MODEL,HERE.with_name('check_dual_flag_spectrum_scc.py'),ROOT/f['net'],ROOT/f['source_graph'],ROOT/f['source_geometry'],ROOT/f['spectral_constructor'],COMPILER]
    report={'schema':'marici.strominger.dual-flag-spectrum.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},'sympy_version':sp.__version__,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:run(report);report['status']='pass'
    except Exception as error:report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),
          'scalar_bands':report.get('scalar_band_ranks'),'composition_defect_rank':report.get('composition_residual_rank'),
          'minimal_closure':report.get('minimal_closure',{}).get('dimension'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
