"""Independently sourced geometric action square and localized PN obstruction."""
from pathlib import Path
import json,hashlib,ast,contextlib,io
# Freshly reruns the exact native geometry/field audit (owner-local outputs).
# Keep one JSON summary on stdout for SCC; dependency evidence is hash-linked.
with contextlib.redirect_stdout(io.StringIO()):
    import check_field_rotation_rigidity as r
A,F,ONE,ZERO=r.A,r.F,r.ONE,r.ZERO
product,plus,scaled=r.product,r.plus,r.scaled
I={(i,i):ONE for i in range(36)}
adjoint=lambda x:{(j,i):v.flip(8) for (i,j),v in x.items()}
minus=lambda a,b:plus(a,scaled(A(-1),b))
# Evaluate only the existing primitive-edge declaration, without running the
# historical generator and its transitive checker/output side effects.
edgeSource=r.ROOT/'research/strominger/checkers/check_two_block_leaf_generation.py'
edgeTree=ast.parse(edgeSource.read_text(encoding='utf8'))
edgeExpr=next(n.value for n in edgeTree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='full_edges' for t in n.targets))
primitiveEdges=eval(compile(ast.Expression(edgeExpr),str(edgeSource),'eval'),{'__builtins__':{},'tuple':tuple,'range':range})
patchEdges={tuple('ABCD'.index(c) for c in edge) for edge in r.patches}
assert patchEdges==set(primitiveEdges) and len(primitiveEdges)==12
assert all(sum(label.startswith(edge+':') for label in r.labels)==3 for edge in r.patches)
B={};Binv={};constantFrame={};sourceCycle={}
reference=r.patches['AB']['surfaceTriangle'];Xref=r.geo.transpose(tuple(r.points[k] for k in reference))
for edge,patch in r.patches.items():
    X=r.geo.transpose(tuple(r.points[k] for k in patch['surfaceTriangle']));Y=r.geo.inv(X);indices=[r.labels.index(edge+':'+a) for a in 'xyz']
    for i in range(3):
        for j in range(3):
            for matrix,block in [(B,X),(Binv,Y),(constantFrame,Xref),(sourceCycle,r.geo.C)]:
                if block[i][j]:matrix[indices[i],indices[j]]=A(block[i][j])
assert product(B,Binv)==I and product(Binv,B)==I
K=product(adjoint(B),B)
assert product(adjoint(constantFrame),constantFrame)==K
assert product(B,sourceCycle)==product(r.cycleP,B)
sourceActions={};targetActions={};squares=[]
# SCC compares map tokens, not matrices. Tokens below hash exact, independently
# evaluated composite matrices; the numerical proof remains this checker.
diagram={'id':'rotation-realization-square-v1','objects':[{'id':'corner_coefficients'},{'id':'spatial_fields'}],'arrows':[{'id':'B','source':'corner_coefficients','target':'spatial_fields'}],'cells':[],'obstructions':[{'id':'PN-geometric-C3','description':'Any role-exchanging unitary has rank-two rotation residual on the alignment sector; not an unspecified filler','evidence':'research/strominger/results/rotation-realization-square/verification.json'}],'claims':[{'id':'coordinate_square','requires':['actual_corner_realization','independent_rotation_actions','exact_squares']},{'id':'field_is_rung12','requires':['field_to_T9_input_adapter','operation_preserving_binding']},{'id':'whole_spacetime_at_rung4','requires':['rung4_event_readout','Lorentzian_metric_and_causal_structure','source_time_map']}],'available_witnesses':['actual_corner_realization','independent_rotation_actions','exact_squares','field_to_primitive_arrow_support'],'higher_coherence':[{'id':'field_to_numbered_tower','degree':2,'state':'unsupported'}],'normalization':'Composite map tokens are SHA256 of exact sorted sparse matrices evaluated in the cited checker, not arbitrary equality labels.'}
def token(op):return hashlib.sha256(json.dumps([[i,j,v.record()] for (i,j),v in sorted(op.items())],sort_keys=True).encode()).hexdigest()
for row in r.Prows:
    if row['orientation']!=1:continue
    g=tuple(row['vertices']);rotation=r.geo.rotation(g);V={};U={}
    for j,label in enumerate(r.labels):
        edge,axis=label.split(':');new=''.join('ABCD'[g['ABCD'.index(c)]] for c in edge)
        V[r.labels.index(new+':'+axis),j]=ONE
        for i in range(3):
            if rotation[i]['xyz'.index(axis)]:U[r.labels.index(new+':'+'xyz'[i]),j]=A(rotation[i]['xyz'.index(axis)])
    assert product(U,B)==product(B,V)
    assert product(adjoint(U),U)==I
    assert product(product(adjoint(V),K),V)==K
    assert all(r.commute(U,x) for x in r.Pop.values())
    assert r.commute(U,r.cycleP)
    omittedRotation=minus(product(V,B),product(B,V))
    erasedFrames=minus(product(U,constantFrame),product(constantFrame,V))
    if row['order']!=1:assert omittedRotation and erasedFrames
    suffix=''.join(map(str,g));vs='V_'+suffix;us='U_'+suffix
    diagram['arrows'].extend([{'id':vs,'source':'corner_coefficients','target':'corner_coefficients','map_token':token(V)},{'id':us,'source':'spatial_fields','target':'spatial_fields','map_token':token(U)}])
    left='rotate_then_realize_'+suffix;right='realize_then_rotate_'+suffix
    for name,composite,factors in [(left,product(B,V),[vs,'B']),(right,product(U,B),['B',us])]:diagram['arrows'].append({'id':name,'source':'corner_coefficients','target':'spatial_fields','map_token':token(composite),'evaluated_from':factors})
    diagram['cells'].append({'id':'square_'+suffix,'kind':'exact-composite-comparison','routes':[[left],[right]]})
    assert {(g[a],g[b]) for a,b in primitiveEdges}==patchEdges
    sourceActions[g]=V;targetActions[g]=U
    squares.append({'vertexPermutation':g,'order':row['order'],'exactNaturality':True,'metricCompatible':True,'CMPartitionPreserved':row['CMRolePartitionPreserved'],'wrongVectorActionResidualEntries':len(omittedRotation),'constantFrameResidualEntries':len(erasedFrames)})
compositions=0
for g,V in sourceActions.items():
    for h,W in sourceActions.items():
        gh=tuple(g[h[i]] for i in range(4))
        assert product(V,W)==sourceActions[gh]
        assert product(targetActions[g],targetActions[h])==targetActions[gh]
        compositions+=1
# No PN map is manufactured: derive a necessary residual for ANY unitary S
# satisfying S Gp=Ln S and S Lp=Gn S using the independent target rotation.
for Up in r.Pthird:assert product(Up,r.Pop['G'])==r.Pop['G']
localizations=[]
for Un in r.Nthird:
    average=scaled(A(F(1,3)),plus(plus(I,Un),product(Un,Un)))
    fixedLocal=product(average,r.Nop['L'])
    assert fixedLocal==r.Nop['N']
    relative=minus(r.Nop['L'],r.Nop['N'])
    assert product(relative,relative)==relative and r.sharp(relative,r.metric)==relative
    assert r.trace(relative)==A(2)
    D=product(minus(Un,I),r.Nop['L'])
    squared=product(r.sharp(D,r.metric),D)
    assert squared==scaled(A(3),relative)
    assert product(r.Nop['N'],D)=={}
    assert product(D,r.Nop['N'])=={}
    localizations.append({'fixedLocalRank':1,'relativeLocalRank':2,'squaredResidual':'D^sharp D = 3 (L_N - N_N)','returnReadoutResidualZero':True,'nonzeroResidualEntries':len(D)})
result={'status':'coordinate-realization-square-verified-PN-relative-sector-obstruction-retained','activeObligations':['attachment transport','route/coherencer compatibility'],'source':'12 ordered triangle corner-coefficient triples, with metric B*B','target':'native P 12 spatial patch-vector triples, with identity metric','adapter':'B has actual ordered triangle corner coordinates as its columns; block inverse checked exactly','classification':'invertible coordinate realization, not a nontrivial filler extension, state generation, or rung assignment','squares':squares,'compositionComparisons':compositions,'hostilesRejected':{'omitVectorRotation':11,'erasePatchFramesWithUnchangedMetric':11},'PNlocalizations':localizations,'forgetfulLift':{'coarseCategory':'Positive-metric spaces with two named commuting orthogonal projectors; target N has its L/G roles exchanged','decoratedCategory':'The same data plus the independently supplied geometric C3 action; morphisms must intertwine it','coarseIsomorphismsExist':'Equal joint-sector dimensions (1,11,2,22) after target role exchange give metric-unitary sectorwise isomorphisms','equivariantLiftFiber':'empty for every coarse isomorphism, by the three-dimensional restricted-character obstruction','classification':'Obstruction to restoring named geometric action after forgetting it; not a proved Postnikov k-invariant or numbered rung'}, 'universalConditionalConsequence':'For any metric-unitary S exchanging L/G and any tested source/target geometric order-three rotations, E=(U_N S-S U_P)G_P obeys E^sharp E=3(G_P-N_P). Hence rank(E)=2, and the target return readout N_N E vanishes. This is an exact consequence of the native identities, not a fitted conversion or an added coherence filler.','primitiveSupportBinding':{'source':'existing full_edges declaration in check_two_block_leaf_generation.py','primitiveArrows':len(primitiveEdges),'PVectorComponentsPerArrow':3,'endpointAndRotationEquivariant':True,'informationForgotten':'All field amplitudes, metric/corner decorations and operator data are absent from bare Primitive records. This support map is not a full field-preserving T9 adapter.'},'towerAssignment':None,'missingNumberedTransportAdapter':['Map source-decorated field configurations to the pinned T9 record domain with endpoints and actual admitted comparisons','Specify preparation, masses, reference and readout without fitting the desired outcome','Preserve the independently declared operation actions, or explicitly change the proposed realization structure'],'scope':'All 12 proper symmetries of this fixed tetrahedron and both N geometric order-three actions. No new native reader move, T9 source adapter, physical time, 4D spacetime identification, Postnikov identification or production/viewer change.'}
files=[r.ROOT/'research/aspect/scc/categorical_compiler.py',edgeSource,Path(__file__),Path(r.__file__),r.ROOT/'research/strominger/rotation-realization-square-protocol-v1.md',r.BASE/'field-rotation-rigidity/verification.json'];result['sourceHashes']={p.resolve().relative_to(r.ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
contract=r.ROOT/'research/strominger/contracts/rotation-realization-square-v1.json';contract.write_text(json.dumps(diagram,indent=2)+'\n',encoding='utf8')
out=r.BASE/'rotation-realization-square';out.mkdir(exist_ok=True)
r.sys.path.append(str(r.ROOT/'research/aspect/scc'))
from categorical_compiler import compile_diagram
compilation=compile_diagram(diagram)
assert compilation['passed'] and len(compilation['cells'])==12
assert compilation['inverse_design']['field_is_rung12']['status']=='missing_witnesses'
assert compilation['higher_coherence'][0]['state']=='unsupported'
(out/'categorical-verification.json').write_text(json.dumps(compilation,indent=2)+'\n',encoding='utf8')
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({'status':result['status'],'geometricSquares':len(squares),'compositionComparisons':compositions,'hostilesRejected':result['hostilesRejected'],'PNrelativeObstructionRank':2,'returnReadoutHidesObstruction':True}))
