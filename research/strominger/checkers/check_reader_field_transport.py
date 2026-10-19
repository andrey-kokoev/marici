"""Exact P transport and N orientation-convention transport test."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
from assemble_metric_coefficient_protocol import A,ONE,ZERO,read_operator,product,sharp
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_belt_operator_inputs import mode,mean
from check_coupled_six_piece_belt import R as Quad,conj
BASE=ROOT/'research/strominger/results';files={s:BASE/f'common-three-carrier-protocol/{s}.json' for s in ['proton','neutron']};sources={s:json.loads(f.read_text()) for s,f in files.items()}
def ops(d):return {k:read_operator(d['operators'][k],36) for k in ['L','G','N']}
p=sources['proton'];P=ops(p);labels=p['source']['coordinates'];rename=dict(zip('ABCD','CDAB'));R=geo.rotation((2,3,0,1));U={}
for j,label in enumerate(labels):
    edge,axis=label.split(':');b='xyz'.index(axis);newEdge=''.join(rename[v] for v in edge)
    for a in range(3):
        if R[a][b]:U[labels.index(newEdge+':'+'xyz'[a]),j]=A(R[a][b])
I={(i,i):ONE for i in range(36)};assert product(U,U)==I;assert product(sharp(U,[F(1)]*36),U)==I
for key in P:assert product(P[key],U)==product(U,P[key])
# Independently derive the reflected mode convention from actual corner data.
belt=json.loads((ROOT/'research/voevodsky/results/four_six_center_cones.json').read_text());ambient=json.loads((ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json').read_text())['record'];points={k:tuple(map(F,v)) for k,v in belt['belt_scaled_coordinates'].items()}
for face in belt['belt_faces']:points['F_'+'_'.join(sorted(face))]=mean([points[k] for k in face])
mirror={k:(-v[0],v[1],v[2]) for k,v in points.items()}
def plane(t,ps):
    rr,ss=mode(t,ps);r,s=tuple(Quad(*x) for x in rr),tuple(Quad(*x) for x in ss)
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    aa,bb=dot(s,s),dot(r,s);assert aa.b==bb.b==0;a,b=aa.a,bb.a
    v=tuple(x-(b/a)*y for x,y in zip(r,s));be=dot(v,v);assert be.b==0
    return ((Quad(b),Quad(a)),(Quad(be.a),Quad())),(a,be.a)
for f,a,b in ambient['triangles']:
    old,ds=plane((f,a,b),points);new,dt=plane((f,b,a),mirror);assert ds==dt
    expected=tuple(tuple(sign*x for x in conj(z)) for sign,z in zip([-1,1],old));assert new==expected
n=sources['neutron'];N=ops(n);metric=list(map(F,n['source']['metric']));D={(i,i):A(-1 if i%2==0 else 1) for i in range(36)}
conjugate=lambda op:{k:v.flip(8) for k,v in op.items()}
# Reflect geometry and reverse ordered corners to restore outward orientation.
# r->O r, s->-O s; intrinsic axes ->(-O e1,O e2).
# Thus target numerator z' = D conjugate(z), metric unchanged.
reflected={k:product(product(D,conjugate(op)),D) for k,op in N.items()}
assert reflected['G']==N['G'];assert reflected['L']!=product(product(D,N['L']),D)
for key in N:assert product(reflected[key],D)==product(D,conjugate(N[key]))
assert product(sharp(D,metric),D)==I;assert product(D,conjugate(D))==I
left=product(reflected['L'],D);right=product(D,N['L']);key=next(k for k in set(left)|set(right) if left.get(k,ZERO)!=right.get(k,ZERO));witness={'targetSource':key,'outwardTargetL_times_D':left.get(key,ZERO).record(),'D_times_sourceL':right.get(key,ZERO).record()}
paths=[ROOT/'research/voevodsky/results/four_six_center_cones.json',ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json',ROOT/'research/voevodsky/checkers/check_belt_operator_inputs.py',Path(__file__).resolve(),*files.values(),BASE/'reader-field-transport/orientation.json',ROOT/'research/strominger/checkers/derive_neutron_belt_field_attachment.py']
result={'status':'reader-field-transport-tested-with-explicit-orientation-convention','proton':{'transport':'tetrahedral vertex rotation AB CD -> CD AB, acting on patch labels and vector components','nonzeroCoefficients':len(U),'metricUnitary':True,'fullLGNIntertwining':True,'squareIdentity':True},'neutron':{'nativeNNSpatialOrientation':'reversing in all sampled native NN edges','outwardPositiveCharacterConvention':{'targetOperators':'L_new = D conjugate(L_old) D; similarly G,N','D':'(-1,+1) on each intrinsic plane pair','spatialOnlyLinearDIntertwines':False,'failureWitness':witness,'antiunitaryTransport':'D times complex conjugation','metricAntiunitary':True,'fullLGNIntertwining':True,'twoSuchAbstractReflectionsSquareToIdentity':True},'orderedCornerTransportAlternative':'Carry ordered corners and plane axes with the marked cell isometry. In co-moving coordinates U=I and L/G/metric unchanged; outward orientation flips on each NN step. This is a different explicit field convention, not a derivation of the native five-coefficient law.'},'sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'scope':'Exact full 36-coordinate algebra. P same-body advance is a derived linear symmetry. N outward-reflection field convention requires antiunitary transport; ordered-corner convention permits linear co-moving transport with orientation tracking. No claim native five-slot NN permutation is antiunitary. Bridge from five-slot coefficients to 36 fields, global PNE sewing and loop coherence remain open. Absolute origin/history never reset.'}
out=BASE/'reader-field-transport/field-verification.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'protonFullTransport':True,'neutronOutwardLinearTransport':False,'neutronOutwardAntiunitaryTransport':True,'linearOrderedCornerAlternative':True}))
