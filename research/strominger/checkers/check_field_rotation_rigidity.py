"""Exact geometric symmetry and patch-local rigidity of native P/N fields."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research/nima/checkers'),str(ROOT/'research/voevodsky/checkers')]
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,product,sharp,plus,scaled
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results'
def lift(z):return A(tuple(F(z[0]) if i==0 else F(z[1]) if i==10 else F(0) for i in range(16)))
def conj(op):return {k:v.flip(8) for k,v in op.items()}
def commute(U,X,anti=False):return product(U,conj(X) if anti else X)==product(X,U)
def native(species):
    d=json.loads((BASE/f'common-three-carrier-protocol/{species}.json').read_text());return d,{k:read_operator(d['operators'][k],36) for k in ['L','G','N']}
p,Pop=native('proton');labels=p['source']['coordinates'];records=json.loads((BASE/'tetrahedral-field-attachment/verification.json').read_text())['gridGeometry'];patches={rec['outerArrow']:rec for rec in records};points=dict(geo.POINTS);cycleP={};P_eigen_gram=[];expectedPL={}
coeff=(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA))
for edge,rec in patches.items():
    f,a,b=rec['surfaceTriangle'];points[f]=geo.mean([points[k] for k in f[2:]]);X=geo.transpose(tuple(points[k] for k in [f,a,b]));cyc=geo.mm(geo.mm(X,geo.C),geo.inv(X))
    for i in range(3):
        for j in range(3):
            if cyc[i][j]:cycleP[labels.index(edge+':'+'xyz'[i]),labels.index(edge+':'+'xyz'[j])]=A(cyc[i][j])
    v=list(map(lift,geo.zmv(X,coeff)));norm=sum((a.flip(8)*a for a in v),ZERO)
    for i in range(3):
        for j in range(3):
            entry=v[i]*v[j].flip(8)/norm
            if entry!=ZERO:expectedPL[labels.index(edge+':'+'xyz'[i]),labels.index(edge+':'+'xyz'[j])]=entry
    vectors=[list(map(A,geo.mv(X,(F(1),)*3))),v,[z.flip(8) for z in v]];gram=[[sum((a.flip(8)*b for a,b in zip(x,y)),ZERO) for y in vectors] for x in vectors];assert all(gram[i][j]!=ZERO for i in range(3) for j in range(3));P_eigen_gram.append([[z.record() for z in row] for row in gram])
assert expectedPL==Pop['L']
def permutation_order(p):
    current=list(range(len(p)));order=0
    while True:
        current=[current[j] for j in p];order+=1
        if current==list(range(len(p))):return order
        assert order<=720
trace=lambda op:sum((v for (i,j),v in op.items() if i==j),ZERO)
# Verify the transport factorization used to derive the continuous stabilizer.
expectedPG={}
for ea,ra in patches.items():
    R=tuple(tuple(map(F,row)) for row in ra['rotation'])
    for eb,rb in patches.items():
        S=tuple(tuple(map(F,row)) for row in rb['rotation']);block=geo.mm(R,geo.transpose(S))
        for i in range(3):
            for j in range(3):
                if block[i][j]:expectedPG[labels.index(ea+':'+'xyz'[i]),labels.index(eb+':'+'xyz'[j])]=A(block[i][j]/12)
assert expectedPG==Pop['G']
cyclePinv=product(cycleP,cycleP);Prows=[];Pthird=[]
for g in permutations(range(4)):
    rot=geo.rotation(g);parity=1 if geo.det(rot)==1 else -1;U={}
    for j,label in enumerate(labels):
        edge,axis=label.split(':');new=''.join('ABCD'[g['ABCD'.index(v)]] for v in edge)
        if parity==-1:new=new[::-1]
        for i in range(3):
            if rot[i]['xyz'.index(axis)]:U[labels.index(new+':'+'xyz'[i]),j]=A(rot[i]['xyz'.index(axis)])
    assert product(sharp(U,[F(1)]*36),U)=={(i,i):ONE for i in range(36)}
    linear={k:commute(U,X) for k,X in Pop.items()};anti={k:commute(U,X,True) for k,X in Pop.items()};forward=commute(U,cycleP);reversedCycle=product(U,cycleP)==product(cyclePinv,U)
    assert all(linear.values())==(parity==1);assert (all(anti.values()) if parity==-1 else True);assert forward==(parity==1);assert reversedCycle==(parity==-1)
    orderG=permutation_order(g)
    if parity==1 and orderG==3:Pthird.append(U)
    rolesPreserved=all((i in [0,2])==(g[i] in [0,2]) for i in range(4))
    Prows.append({'vertices':g,'orientation':parity,'order':orderG,'CMRolePartitionPreserved':rolesPreserved,'linearProjectors':linear,'antiunitaryProjectors':anti,'forwardCycle':forward,'inverseCycle':reversedCycle})
# N belt isometries: enumerate actual six-vertex metric symmetries, not S6.
n,Nop=native('neutron');metric=list(map(F,n['source']['metric']));belt=json.loads((NATIVE/'four_six_center_cones.json').read_text());ambient=json.loads((NATIVE/'coupled_six_piece_belt_store.json').read_text())['record'];store=json.loads((NATIVE/'belt_three_by_twelve_store.json').read_text());names=[k for k in belt['belt_scaled_coordinates'] if k!='O'];coords={k:tuple(map(F,belt['belt_scaled_coordinates'][k])) for k in names};faces={frozenset(f) for f in belt['belt_faces']};triangles=list(map(tuple,ambient['triangles']));order=store['triangle_order'];positions={t:i for i,t in enumerate(order)};triangleIndex={t:i for i,t in enumerate(triangles)}
def dist(a,b):return sum(w*(x-y)**2 for w,x,y in zip([3,1,1],coords[a],coords[b]))
pairs=list(combinations(names,2));distances={tuple(sorted(p)):dist(*p) for p in pairs};basis=geo.transpose(tuple(coords[k] for k in names[:3]));basisDet=geo.det(basis);assert basisDet
zcol=json.loads((BASE/'baryon-tensor-grid/verification.json').read_text())['carriers']['neutron']['sourceReturnColumn'];z=[A(tuple(F(v.get(str(i),0)) for i in range(16))) for v in zcol];cycleN={};N_nonorthogonal=[]
C2=((F(-1,2),F(1,2)),(F(-3,2),F(-1,2)))
for t in range(18):
    zz=z[2*t:2*t+2];recordsZ=[x.record() for x in zz];X=[[F(r.get('0',0)),F(r.get('10',0))] for r in recordsZ];det=X[0][0]*X[1][1]-X[0][1]*X[1][0];assert det
    inv=[[X[1][1]/det,-X[0][1]/det],[-X[1][0]/det,X[0][0]/det]];mm=lambda a,b:[[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)];cyc=mm(mm(X,C2),inv)
    for i in range(2):
        for j in range(2):
            if cyc[i][j]:cycleN[2*t+i,2*t+j]=A(cyc[i][j])
    overlap=sum((A(metric[2*t+i])*zz[i].flip(8)*zz[i].flip(8) for i in range(2)),ZERO);assert overlap!=ZERO;N_nonorthogonal.append(overlap.record())
assert all(x!=ZERO for x in z)
expectedNG={(12*a+i,12*b+i):A(F(1,3)) for a in range(3) for b in range(3) for i in range(12)};assert expectedNG==Nop['G']
expectedNL={}
for sector in range(3):
    indices=list(range(12*sector,12*sector+12));norm=sum((A(metric[i])*z[i].flip(8)*z[i] for i in indices),ZERO)
    for i in indices:
        for j in indices:expectedNL[i,j]=z[i]*z[j].flip(8)*A(metric[j])/norm
assert expectedNL==Nop['L']
cycleNinv=product(cycleN,cycleN);Nrows=[];Nthird=[]
readerMap=json.loads((BASE/'neutron-reader-field-interface/verification.json').read_text())['charts'][0]['vertexMap'];readerRoles={k:('M' if v in ['b','v'] else 'C') for k,v in readerMap.items()}
for permuted in permutations(names):
    rename=dict(zip(names,permuted))
    if any(distances[tuple(sorted((rename[a],rename[b])))]!=d for (a,b),d in distances.items()):continue
    if {frozenset(rename[k] for k in f) for f in faces}!=faces:continue
    orient=geo.det(geo.transpose(tuple(coords[rename[k]] for k in names[:3])))/basisDet;assert orient in [1,-1];U={};tp=[]
    for t,(f,a,b) in enumerate(triangles):
        nf='F_'+'_'.join(sorted(rename[k] for k in f[2:].split('_')));na,nb=rename[a],rename[b]
        if orient==-1:na,nb=nb,na
        nt=triangleIndex[nf,na,nb];tp.append(nt)
        for axis in range(2):U[2*positions[nt]+axis,2*positions[t]+axis]=A(-1 if orient==-1 and axis==0 else 1)
    assert product(sharp(U,metric),U)=={(i,i):ONE for i in range(36)}
    linear={k:commute(U,X) for k,X in Nop.items()};anti={k:commute(U,X,True) for k,X in Nop.items()};forward=commute(U,cycleN);inverse=product(U,cycleN)==product(cycleNinv,U)
    sectorSets={frozenset(order[6*s:6*s+6]) for s in range(3)};preservesSectors={frozenset(tp[t] for t in sector) for sector in sectorSets}==sectorSets
    orderG=permutation_order([names.index(rename[k]) for k in names])
    if orient==1 and orderG==3:Nthird.append(U)
    rolesPreserved=all(rename[k] in readerRoles and readerRoles[rename[k]]==role for k,role in readerRoles.items())
    Nrows.append({'vertices':rename,'orientation':int(orient),'order':orderG,'fixedReaderCMPartitionPreserved':rolesPreserved,'sectorGroupingPreserved':preservesSectors,'linearProjectors':linear,'antiunitaryProjectors':anti,'forwardCycle':forward,'inverseCycle':inverse})
# Record geometric counts without silently interpreting them as move availability.
counts=lambda rows:{'metricAndFaceIsometries':len(rows),'properGeometric':sum(r['orientation']==1 for r in rows),'linearFullProjectorSymmetries':sum(all(r['linearProjectors'].values()) for r in rows),'improperAntiunitaryProjectorSymmetries':sum(r['orientation']==-1 and all(r['antiunitaryProjectors'].values()) for r in rows),'linearProjectorsAndForwardCycle':sum(all(r['linearProjectors'].values()) and r['forwardCycle'] for r in rows)}
assert len(Pthird)==8 and len(Nthird)==2
for U in Pthird:assert trace(product(Pop['G'],U))==A(3)
for U in Nthird:assert trace(product(Nop['L'],U))==ZERO
# Explicit patch-local unitary hostiles: preserve metric and L/G, but break
# the actual cyclic operation, witnessing that the last constraint matters.
I={(i,i):ONE for i in range(36)};UP=plus(I,scaled(A(-2),Pop['L']));assert product(sharp(UP,[F(1)]*36),UP)==I;assert all(commute(UP,x) for x in Pop.values());assert not commute(UP,cycleP)
QN={}
for patch in range(18):
    indices=[2*patch,2*patch+1];norm=sum((A(metric[i])*z[i].flip(8)*z[i] for i in indices),ZERO)
    for i in indices:
        for j in indices:QN[i,j]=z[i]*z[j].flip(8)*A(metric[j])/norm
UN=plus(I,scaled(A(-2),QN));assert product(sharp(UN,metric),UN)==I;assert all(commute(UN,x) for x in Nop.values());assert not commute(UN,cycleN)
assert counts(Prows)=={'metricAndFaceIsometries':24,'properGeometric':12,'linearFullProjectorSymmetries':12,'improperAntiunitaryProjectorSymmetries':12,'linearProjectorsAndForwardCycle':12}
assert counts(Nrows)=={'metricAndFaceIsometries':12,'properGeometric':6,'linearFullProjectorSymmetries':6,'improperAntiunitaryProjectorSymmetries':0,'linearProjectorsAndForwardCycle':6}
joint={}
for name,ops in [('proton',Pop),('neutron',Nop)]:
    assert product(ops['L'],ops['G'])==ops['N']
    q=trace(ops['N']);dims=[q,trace(ops['L'])-q,trace(ops['G'])-q,A(36)-trace(ops['L'])-trace(ops['G'])+q];dimensions=[int(v.c[0]) for v in dims];assert sorted(dimensions)==[1,2,11,22];joint[name]={'jointSectorDimensions':dimensions,'projectorOnlyUnitaryGroupRealDimension':sum(x*x for x in dimensions)}
result={'status':'geometric-and-cyclic-field-rigidity-measured','projectorOnlySymmetries':joint,'patchLocalHostiles':{'metricAndProjectorPreservingButCycleBreaking':{'proton':True,'neutron':True}},'geometricPNRotationObstruction':{'sourceGeometricC3TraceOnAlignmentImage':3,'targetGeometricC3TraceOnLocalImage':0,'sourceC3ActionsChecked':len(Pthird),'targetC3ActionsChecked':len(Nthird),'conclusion':'No invertible PN map can simultaneously exchange G_P with L_N and identify these geometric C3 actions: restricted traces would have to agree. The algebraic PN candidate must transport that P symmetry to a different, internal N action, or relax the projection-role exchange.'},'proton':{'counts':counts(Prows),'isometries':Prows,'cyclicEigenbasisGramMatrices':P_eigen_gram},'neutron':{'counts':counts(Nrows),'isometries':Nrows,'cyclicConjugateEigenvectorOverlaps':N_nonorthogonal},'continuousPatchLocalAnalysis':{'P_projectors_and_fixed_patch_support':'U(1) x U(2): G forces a single co-moving unitary V; L requires [V,P0]=0. Real dimension 5.','P_with_tangent_normal_splitting':'U(1)^3: selected complex line, its tangent orthogonal line, and real-normal complex line.','P_with_ordered_cyclic_operator':'Only common U(1): three simple cyclic eigenvectors have a connected nonzero metric-overlap graph. Unitary commuting eigenphases must coincide.','N_projectors_and_fixed_patch_support':'U(1)^7: G ties the three copies of each of six reference patches; L ties all six selected-line phases. Six independent orthogonal-line phases remain.','N_with_ordered_cyclic_operator':'Only common U(1): every positive/negative cyclic eigenpair has nonzero metric overlap; the orthogonal-line freedom collapses, and L ties patch phases.'},'scope':'Geometric isometries and internal basis stabilizers of the supplied native decorated fields. Preserving actual forward cyclic operations is stronger than preserving projector ranges. Antiunitary orientation reversal and inverse-cycle duality are not native forward operations. Lie-group parameter counts are not geometric/configuration dimensions. Native C/M markings, outside contexts and actual reachable window paths impose further constraints. No production/viewer changes.'}
files=[Path(geo.__file__).resolve(),Path(sys.modules['assemble_metric_coefficient_protocol'].__file__).resolve(),Path(__file__).resolve(),ROOT/'research/strominger/field-rotation-rigidity-protocol-v1.md',BASE/'common-three-carrier-protocol/proton.json',BASE/'common-three-carrier-protocol/neutron.json',BASE/'tetrahedral-field-attachment/verification.json',BASE/'baryon-tensor-grid/verification.json',BASE/'neutron-reader-field-interface/verification.json',NATIVE/'four_six_center_cones.json',NATIVE/'coupled_six_piece_belt_store.json',NATIVE/'belt_three_by_twelve_store.json'];result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};out=BASE/'field-rotation-rigidity';out.mkdir(exist_ok=True);(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'P':result['proton']['counts'],'N':result['neutron']['counts']}))
