"""Lossless refinement comparisons through eight center-star sectors.
The native cells remain source objects; sector values are comparison coordinates.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import contextlib,io,json,subprocess,hashlib,copy
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
for name in ('check_fcc_toroidal_geometry.mjs','export_eight_sector_readers.mjs'):
    subprocess.run(['node',str(Path(__file__).with_name(name))],cwd=ROOT,check=True,capture_output=True,text=True)
geometry_path=BASE/'fcc-toroidal-geometry/verification.json';reader_path=BASE/'eight-sector-readers/verification.json'
geometry=json.loads(geometry_path.read_text());reader=json.loads(reader_path.read_text())
for receipt in (geometry,reader):
    for p,digest in receipt['sourceHashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest
log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_five_coefficient_field_binding as binding
    import check_field_rotation_rigidity as field
A,Z,O=binding.A,binding.ZERO,binding.ONE
cube=tuple(product((-1,1),repeat=3));add=lambda a,b:tuple(x+y for x,y in zip(a,b));sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
def mean(vs):return tuple(sum(v[i] for v in vs)/F(len(vs)) for i in range(len(vs[0])))
def fcc(v):return (v[1]+v[2],v[1]+v[3],v[2]+v[3])
def det(M):
    if len(M)==1:return M[0][0]
    return sum((-1)**j*v*det([row[:j]+row[j+1:] for row in M[1:]]) for j,v in enumerate(M[0]))
def volume(vertices):return abs(det([list(sub(v,vertices[0])) for v in vertices[1:]]))/6
def key(vs):return tuple(sorted(tuple(v) for v in vs))
def tr(M):return [list(row) for row in zip(*M)]
def mm(M,N):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*N)] for row in M]
def scaled(M,c):return [[c*x for x in row] for row in M]
I=[[F(i==j) for j in range(8)] for i in range(8)]
def rank(M):
    M=[list(map(F,row)) for row in M];r=0
    for col in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][col]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r];v=M[r][col];M[r]=[x/v for x in M[r]]
        for i in range(len(M)):
            if i!=r:
                v=M[i][col];M[i]=[a-v*b for a,b in zip(M[i],M[r])]
        r+=1
    return r
owner=geometry['sourceOctahedron'];vertices=[tuple(map(F,v)) for v in owner['vertices']];center=mean(vertices);physical_center=fcc(center)
faces={}
for face in owner['faces']:
    vs=[tuple(map(F,v)) for v in face]
    sigma=tuple(3*x for x in sub(mean([fcc(v) for v in vs]),physical_center));assert sigma in cube
    faces[sigma]=vs
assert len(faces)==8
stars={sigma:[center,*face] for sigma,face in faces.items()}
assert all(volume([fcc(v) for v in star])==F(1,6) for star in stars.values())
charts={};pairs={}
for axis in range(3):
    others=[i for i in range(3) if i!=axis];ps=[]
    for signs in product((-1,1),repeat=2):
        plus=[0]*3;plus[axis]=1
        for j,v in zip(others,signs):plus[j]=v
        minus=plus.copy();minus[axis]=-1;ps.append((cube.index(tuple(plus)),cube.index(tuple(minus))))
    pairs[str(axis)]=ps
# Antipodal pairs labelled by the source root tetrahedron, not an arbitrary
# cube ordering. Positive representative is minus the centered root vertex.
root=[tuple(map(F,v)) for v in geometry['classes']];root_center=mean(root)
reps=[tuple(-2*x for x in sub(v,root_center)) for v in root]
assert all(v in cube and v[0]*v[1]*v[2]==1 for v in reps)
pairs['antipodal']=[(cube.index(v),cube.index(tuple(-x for x in v))) for v in reps]
for name,ps in pairs.items():
    H=[[F(0)]*8 for _ in range(8)]
    for row,(a,b) in enumerate(ps):H[row][a]=H[row][b]=1;H[row+4][a]=1;H[row+4][b]=-1
    assert mm(H,tr(H))==scaled(I,2);charts[name]=H
# Geometry establishes that these pairings, rather than arbitrary partitions,
# are exactly the three source diagonal subdivisions.
component_rows={};native_axis=None
for choice in geometry['refinements']:
    axis_vector=sub(fcc(choice['axis'][1]),fcc(choice['axis'][0]));axis=next(i for i,x in enumerate(axis_vector) if x)
    mapping={}
    for component in choice['parts']:
        ckey=key(component);cset=set(ckey)
        assert set(map(tuple,choice['axis']))<=cset
        incident=[sigma for sigma,face in faces.items() if set(face)<=cset];assert len(incident)==2
        pair=frozenset(cube.index(v) for v in incident)
        row=next(i for i,p in enumerate(pairs[str(axis)]) if frozenset(p)==pair);mapping[ckey]=row
        # Center is the midpoint of the diagonal, hence lies in the component;
        # the other three vertices of each fine sector are component vertices.
        assert center==mean([tuple(map(F,v)) for v in choice['axis']])
        assert volume([fcc(tuple(map(F,v))) for v in component])==F(1,3)
        assert sum(volume([fcc(v) for v in stars[sigma]]) for sigma in incident)==F(1,3)
    component_rows[str(axis)]=mapping
    if {key(c) for c in choice['parts']}=={key(c) for c in owner['components']}:native_axis=str(axis)
assert native_axis is not None
T={(target,source):scaled(mm(charts[target],tr(charts[source])),F(1,2)) for target in charts for source in charts}
for M in T.values():assert mm(tr(M),M)==I
for a,b,c in product(charts,repeat=3):assert mm(T[c,b],T[b,a])==T[c,a]
# Average-only projection, common invisible mode, and explicit loss witness.
projectors={name:scaled(mm(tr(H[:4]),H[:4]),F(1,2)) for name,H in charts.items()}
for P in projectors.values():assert mm(P,P)==P and rank(P)==4
assert rank(mm(projectors['0'],projectors['1']))==2
assert rank(mm(mm(projectors['0'],projectors['1']),projectors['2']))==1
average_stack=[row for axis in ('0','1','2') for row in charts[axis][:4]]
assert rank(average_stack)==7
parity=[F(x*y*z) for x,y,z in cube]
assert all(sum(a*b for a,b in zip(row,parity))==0 for row in average_stack)
other=next(str(i) for i in range(3) if str(i)!=native_axis)
witness=[F(v[int(other)]) for v in cube]
column=lambda v:[[x] for x in v]
assert mm(projectors[native_axis],column(witness))==column(witness)
assert mm(projectors[other],column(witness))==column([F(0)]*8)
# The actual proper-root actions permute the sectors and the refinement index.
sector_actions={};symmetry_checks=0
for row in geometry['rootActions']:
    p=tuple(row['permutation'])
    def move(v):
        result=[F(0)]*4
        for i,x in enumerate(v):result[p[i]]=x
        return tuple(result)
    newcenter=mean([fcc(move(v)) for v in vertices]);perm=[]
    for sigma in cube:
        normal=tuple(3*x for x in sub(mean([fcc(move(v)) for v in faces[sigma]]),newcenter));perm.append(cube.index(normal))
    P=[[F(i==perm[j]) for j in range(8)] for i in range(8)];sector_actions[p]=P
    for axis in range(3):
        target=next(j for j in range(3) if len({cube[perm[i]][j]*cube[i][axis] for i in range(8)})==1)
        M=scaled(mm(mm(charts[str(target)],P),tr(charts[str(axis)])),F(1,2))
        assert all(M[i][j]==0 for i in range(8) for j in range(8) if (i<4)!=(j<4))
        assert all(sum(x!=0 for x in line)==1 for line in M);symmetry_checks+=1
    anti=scaled(mm(mm(charts['antipodal'],P),tr(charts['antipodal'])),F(1,2))
    expected=[[F((i<4)==(j<4) and i%4==p[j%4]) for j in range(8)] for i in range(8)]
    assert anti==expected;symmetry_checks+=1
for p,P in sector_actions.items():
    for q,Q in sector_actions.items():assert mm(P,Q)==sector_actions[tuple(p[q[i]] for i in range(4))]
# Affine torus actions are separate: translations move the octahedron center,
# while only rho acts on its relative sector normals. Keep the cover center
# and deck offset rather than replacing translations by root rotations.
def rho(v,k):
    for _ in range(k):v=(v[2],v[0],v[1])
    return tuple(v)
affine_actions={};affine_poses=[];affine_squares=0
for action in geometry['affineActions']:
    t=tuple(action['translation']);k=action['rotationPower']
    moved_center=add(rho(physical_center,k),t)
    perm=[]
    for sigma in cube:
        moved_face=[add(rho(fcc(v),k),t) for v in faces[sigma]]
        normal=tuple(3*x for x in sub(mean(moved_face),moved_center));perm.append(cube.index(normal))
    P=[[F(i==perm[j]) for j in range(8)] for i in range(8)];affine_actions[t,k]=P
    for source in charts:
        target=str((int(source)+k)%3) if source!='antipodal' else source
        Q=scaled(mm(mm(charts[target],P),tr(charts[source])),F(1,2))
        assert mm(Q,tr(Q))==I
        assert all(Q[i][j]==0 for i in range(8) for j in range(8) if (i<4)!=(j<4));affine_squares+=1
    affine_poses.append({'translation':t,'rotationPower':k,'center':moved_center,'relativeSectorPermutation':perm})
for (ta,ka),Pa in affine_actions.items():
    for (tb,kb),Pb in affine_actions.items():
        raw=add(ta,rho(tb,ka));tc=tuple(x%2 for x in raw);kc=(ka+kb)%3;deck=sub(raw,tc)
        assert mm(Pa,Pb)==affine_actions[tc,kc]
        assert add(rho(add(rho(physical_center,kb),tb),ka),ta)==add(add(rho(physical_center,kc),tc),deck)
# Actual N coefficient and field interfaces, retaining both known noncanonical
# seed choices. Phase-aware bindings are input data, not re-derived from shape.
Ametric=list(map(F,binding.sources['neutron']['source']['metric']))
assert Ametric==field.metric and len(Ametric)==36
reader_rows=[]
for rec in reader['readers']:
    ck=key([tuple(map(F,v.split(','))) for v in rec['cell']['vertices']]);reader_rows.append(component_rows[native_axis][ck])
assert sorted(reader_rows)==list(range(4))
provenance=copy.deepcopy({k:reader[k] for k in ('rootReader','readers','operations','witnesses')});provenance_digest=hashlib.sha256(json.dumps(provenance,sort_keys=True).encode()).hexdigest()
image=[0]*16;image[8]=1;imag=A(tuple(image))
root_coeff=tuple(A(i+1)+imag*A(2*i+1) for i in range(5))
def apply(M,v,n):
    result=[Z]*n
    for (i,j),x in M.items():
        if v[j]!=Z:result[i]=result[i]+x*v[j]
    return tuple(result)
def mix(M,rows):
    result=[]
    for row in M:
        out=[Z]*len(rows[0])
        for weight,v in zip(row,rows):
            if weight:
                for j,x in enumerate(v):
                    if x!=Z:out[j]=out[j]+A(weight)*x
        result.append(tuple(out))
    return result
norm5=lambda rows:sum((x.flip(8)*x for v in rows for x in v),Z)
def normfield(rows):return sum((x.flip(8)*A(Ametric[i])*x for row in rows for i,x in enumerate(row) if x!=Z),Z)
def decode_packet(packet):
    assert hashlib.sha256(json.dumps(packet['source_contexts'],sort_keys=True).encode()).hexdigest()==provenance_digest
    restored=mix(T[packet['source_chart'],packet['chart']],packet['values'])
    recovered=[]
    for rec,row in zip(packet['source_contexts']['readers'],packet['reader_rows']):
        B=binding.seeds[packet['binding_seed']]
        for _ in range(rec['packet']['origin']):B=binding.product(B,binding.Pi['neutron'])
        sharp={(j,i):x.flip(8)*A(Ametric[i]) for (i,j),x in B.items()}
        recovered.append(apply(sharp,restored[row],5))
    return restored,recovered,copy.deepcopy(packet['source_contexts'])
fixture_results=[];phase_folding_rejected=0;average_only_failures=0
for seed_index,seed in enumerate(binding.seeds):
    embeddings=[]
    for rec in reader['readers']:
        B=seed
        for _ in range(rec['packet']['origin']):B=binding.product(B,binding.Pi['neutron'])
        assert binding.gram(B,Ametric)==binding.I5;embeddings.append(B)
    assert embeddings[0]==embeddings[2] and provenance['readers'][0]['frame']!=provenance['readers'][2]['frame']
    for i in range(3):assert binding.product(embeddings[i+1],binding.Pi['neutron'])==embeddings[i]
    for mode in ('independent-records','coherent-native-NN-chain'):
        coeffs=[];fields=[None]*4
        for i,(rec,B,row) in enumerate(zip(reader['readers'],embeddings,reader_rows)):
            coeff=tuple(root_coeff[j] for j in rec['packet']['permutation']) if mode=='coherent-native-NN-chain' else tuple(A((i+1)*(j+2))+imag*A(i+2*j+1) for j in range(5))
            coeffs.append(coeff);fields[row]=apply(B,coeff,36)
        if mode=='coherent-native-NN-chain':assert all(v==fields[0] for v in fields)
        original=fields+[tuple([Z]*36) for _ in range(4)]
        assert normfield(original)==norm5(coeffs)
        for target in charts:
            packet={'chart':target,'source_chart':native_axis,'values':mix(T[target,native_axis],original),
                    'source_contexts':copy.deepcopy(provenance),'reader_rows':reader_rows[:],'binding_seed':seed_index}
            view=packet['values'];restored,recovered,contexts=decode_packet(packet)
            assert restored==original and contexts==provenance
            assert normfield(view)==normfield(original)
            assert recovered==coeffs
            if any(x!=Z for v in view[4:] for x in v):
                bad=copy.deepcopy(packet);bad['values'][4:]=[tuple([Z]*36) for _ in range(4)]
                assert decode_packet(bad)[1]!=coeffs;average_only_failures+=1
            bad=copy.deepcopy(packet)
            for rec in bad['source_contexts']['readers']:rec['packet']['origin']%=2
            try:decode_packet(bad)
            except AssertionError:phase_folding_rejected+=1
            else:raise AssertionError('Origin folding accepted')
            if mode=='coherent-native-NN-chain':assert all(x==Z for v in view[4:] for x in v)
            assert hashlib.sha256(json.dumps(provenance,sort_keys=True).encode()).hexdigest()==provenance_digest
            fixture_results.append({'seed':seed_index,'mode':mode,'target':target,'fiveCoefficientRecovery':True,'metricPreserved':True,
                                    'detailNonzero':any(x!=Z for v in view[4:] for x in v)})
assert any(f['detailNonzero'] for f in fixture_results if f['mode']=='independent-records')
assert phase_folding_rejected==16 and average_only_failures>0
# Full 36-coordinate N fields, including vectors outside the five-coordinate
# embedding, are preserved by chart changes. Uniform named field operations
# commute with them; this does not assert a new cross-cell native move.
dense=[tuple(A((i+2)*(j+1)%13)+imag*A((i+3*j)%11) for j in range(36)) for i in range(8)]
operator_checks=0
for target in charts:
    M=T[target,native_axis];moved=mix(M,dense);assert normfield(moved)==normfield(dense)
    for op in (field.Nop['L'],field.Nop['G'],field.cycleN):
        assert mix(M,[apply(op,v,36) for v in dense])==[apply(op,v,36) for v in moved];operator_checks+=1
# Native NN channel maps become partial maps between source-record summands.
# Their co-moving field action is identity, by E_(r+1) Pi_N = E_r above.
# Conjugate their slot support; do not pretend these partial maps are unitary
# evolution on the entire direct sum of records.
update_support=[]
for i in range(3):
    M=[[F(0)]*8 for _ in range(8)];M[reader_rows[i+1]][reader_rows[i]]=1
    for target in charts:
        transported=mm(mm(T[target,native_axis],M),T[native_axis,target])
        incoming=sorted({j%4 for row in transported for j,x in enumerate(row) if x})
        outgoing=sorted({j%4 for j,row in enumerate(transported) if any(row)})
        touched=sorted(set(incoming)|set(outgoing))
        assert mm(T[native_axis,target],mm(transported,T[target,native_axis]))==M
        update_support.append({'sourceOrigin':i,'targetOrigin':i+1,'chart':target,'inputPairs':incoming,'outputPairs':outgoing,'touchedPairs':touched})
assert max(len(row['touchedPairs']) for row in update_support if row['chart']!='antipodal')==4
# Retaining only averages fails even for an originally valid native coarse view.
assert sum(x*x for x in witness)==8
report={'schema':'marici.eight-sector-interface.v1','status':'pass',
 'nativeAxis':native_axis,'sectorSigns':cube,'nativeReaderRows':reader_rows,
 'starVolume':'1/6','coarseVolume':'1/3','eachNativeComponentIsTwoStarSectors':True,
 'chartConvention':'A_i = H_i / sqrt(2); first four rows averages, last four differences; mass-normalized coordinates',
 'pairings':pairs,'unnormalizedCharts':charts,'transitions':[{'source':src,'target':tgt,'matrix':M} for (tgt,src),M in T.items()],
 'invertibleChartTransitions':16,'compositionTriangles':64,'A4SectorProducts':144,'A4IndexedChartSquares':symmetry_checks,
 'affineIndexedChartSquares':affine_squares,'affineCompositionDeckSquares':144,'affinePoses':affine_poses,
 'averageOnlyPairRank':2,'averageOnlyTripleRank':1,'combinedThreeAverageRank':7,'invisibleParityMode':parity,
 'averageOnlyLossWitness':{'fineValues':witness,'sourceAxis':native_axis,'targetAxis':other,'initialSquaredNorm':8,'coarseTargetSquaredNorm':0},
 'readerBindings':{'seedsTested':2,'canonicalSeedSelected':False,'records':4,'origins':[rec['packet']['origin'] for rec in provenance['readers']],
                   'independentInputComplexDimension':20,'sectorFieldWorkspaceComplexDimension':288,'provenanceSHA256':provenance_digest,
                   'nativeNNChainAlsoTested':True,'uniformFieldOperatorChecks':operator_checks,'fixtures':fixture_results},
 'readerCoefficientRecovery':True,'absoluteOriginsRetained':True,'readOnlyComparisonInterfaceConstructed':True,
 'negativeControls':{'phaseFoldingRejected':phase_folding_rejected,'averageOnlyRecoveryFailures':average_only_failures},
 'nativeNNChannelMapsTransported':12,'nativeNNUpdateSupport':update_support,
 'allNNUpdatesRemainWithinTwoCoarsePairs':False,'nativeDiagonalNNMaximumTouchedPairs':4,
 'nativeRefinementChangingMoveAdmitted':False,'nativeGrammarChanged':False,
 'scope':'Lossless indexed comparison of prescribed coefficient/field records. The eight sectors are a common workspace, not new occupied primitives. Uniform field-operation covariance is not a cross-carrier PN or refinement-changing native constructor.',
 'prerequisiteReplay':log.getvalue()}
out=BASE/'eight-sector-interface';out.mkdir(parents=True,exist_ok=True)
paths=[Path(__file__),geometry_path,reader_path,BASE/'five-coefficient-field-binding/verification.json',BASE/'field-rotation-rigidity/verification.json',ROOT/'research/strominger/eight-sector-interface-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def serial(x):
    if isinstance(x,F):return str(x)
    raise TypeError(type(x))
(out/'verification.json').write_text(json.dumps(report,indent=2,default=serial)+'\n')
print(json.dumps({k:report[k] for k in ('status','nativeAxis','invertibleChartTransitions','compositionTriangles','A4IndexedChartSquares','combinedThreeAverageRank','readerCoefficientRecovery','absoluteOriginsRetained','nativeGrammarChanged')},indent=2))
