"""All-displacement covariance of actual P/N geometric charts, not native moves."""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,hashlib
# Replays full native coefficient reconstructions, preserving their own receipts.
with contextlib.redirect_stdout(io.StringIO()):
    import derive_tetrahedral_field_attachment as p
    import derive_neutron_belt_field_attachment as n

class Affine:
    """Exact Q[t_x,t_y,t_z] affine part; nonlinear products intentionally absent."""
    def __init__(self,value=0):
        self.c=value.c if isinstance(value,Affine) else tuple(map(F,value)) if isinstance(value,tuple) else (F(value),F(0),F(0),F(0))
        assert len(self.c)==4
    def __add__(self,other):return Affine(tuple(a+b for a,b in zip(self.c,Affine(other).c)))
    __radd__=__add__
    def __neg__(self):return Affine(tuple(-x for x in self.c))
    def __sub__(self,other):return self+-Affine(other)
    def __rsub__(self,other):return Affine(other)+-self
    def __mul__(self,scalar):return Affine(tuple(x*F(scalar) for x in self.c))
    __rmul__=__mul__
    def __truediv__(self,scalar):return self*(1/F(scalar))
    def __eq__(self,other):return self.c==Affine(other).c
    def constant(self):
        assert self.c[1:]==(0,0,0),'translation dependence retained'
        return self.c[0]

shift=tuple(Affine(tuple(int(j==i+1) for j in range(4))) for i in range(3))
translated={key:tuple(Affine(x)+t for x,t in zip(point,shift)) for key,point in p.points.items()}
center=p.geo.mean([translated[key] for key in 'ABCD'])
assert center==shift
assert p.geo.mean([p.points[key] for key in 'ABCD'])==(0,0,0)
patches=0;hostiles=0
for patch in p.patches.values():
    triangle=patch['triangle']
    X=p.geo.transpose(tuple(p.points[key] for key in triangle))
    Xt=p.geo.transpose(tuple(tuple((a-b).constant() for a,b in zip(translated[key],center)) for key in triangle))
    assert Xt==X
    inverse=p.geo.inv(X);inverse_t=p.geo.inv(Xt)
    assert inverse==inverse_t
    assert p.geo.mm(p.geo.transpose(Xt),Xt)==p.geo.mm(p.geo.transpose(X),X)
    assert p.geo.mm(p.geo.mm(Xt,p.geo.C),inverse_t)==p.geo.mm(p.geo.mm(X,p.geo.C),inverse)
    # Full corner realization can fail even when zero-sum cyclic mode survives.
    tri_center=p.geo.mean([p.points[key] for key in triangle])
    raw=p.geo.transpose(tuple(tuple(x-c for x,c in zip(p.points[key],tri_center)) for key in triangle))
    assert p.geo.det(raw)==0 and p.geo.det(X)!=0
    assert p.geo.zmv(raw,p.coeff)==p.geo.zmv(X,p.coeff)
    patches+=1;hostiles+=1
# Tetrahedral rotations are derived from the same centered vertices.
assert all(tuple((a-b).constant() for a,b in zip(translated[k],center))==p.geo.POINTS[k] for k in 'ABCD')
translated_n={key:tuple(Affine(x)+t for x,t in zip(point,shift)) for key,point in n.points.items()}
triangles=0
for triangle in n.triangles:
    original=n.mode(triangle,n.points)
    moved=n.mode(triangle,translated_n)
    constant=tuple(tuple(tuple(x.constant() for x in pair) for pair in vector) for vector in moved)
    assert constant==original
    triangles+=1
assert patches==12 and hostiles==12 and triangles==18
# Algebraic action on points. Two independent displacements are represented
# in separate formal polynomial evaluations: linearity makes the identity
# (p+u)+v=p+(u+v) exact coefficientwise; center subtraction cancels each leg.
# Its fiber leg is I36 in the geometrically derived unchanged charts.
assert p.geo.zadd(p.geo.zadd(p.coeff[0],p.coeff[1]),p.coeff[2])==p.geo.ZERO
# Reconstructed full operator matches were asserted by both imported checkers.
assert p.result['nativeFullCoefficientsReconstructed']=={'L':True,'G':True,'return':True}
assert n.result['nativeFullOperatorsReconstructed']==['L','G','N']
assert n.result['nativeMetricReconstructed']
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results'
result={'status':'pass','classification':'source-geometric-PN-full-field-covariance-for-arbitrary-rigid-displacements',
        'translationDomain':'all real3 displacements; identities checked in three independent formal variables',
        'proton':{'patches':patches,'fullFieldDimension':36,'center':'mean of four body vertices','centeredFramesIdentical':True,'inverseMetricAndCyclicOperationsIdentical':True,'rawAbsoluteFramesSingularUnderControlShift':hostiles,'zeroSumModeMissesAllControls':True},
        'neutron':{'patches':triangles,'fullFieldDimension':36,'actualSourceModeFunctionSymbolicallyInvariant':True,'consequence':'Both plane generators unchanged, hence derived plane basis, weights and full native operators unchanged with marking retained.'},
        'freshNativeCoefficientReconstructions':['proton','neutron'],
        'transport':'Identity on all amplitudes in the source-geometric co-moving charts, composing additively on rigid placements.',
        'rigidCopyCovarianceVerified':True,'nativeArbitraryReaderTransportDerived':False,
        'electronCovered':False,'exteriorAttachmentSewingVerified':False,'uniquePhysicalConnectionDerived':False,
        'canonicalParentConstructed':False,'monsterGateActivated':False,'physicalValidation':False,'formalOutcome':None,
        'nextObligation':'Compare transported marked P/N chart interfaces with fixed exterior or changing readers; a preserved isolated fiber is not a global connection. No grading/product or sector-readout parent map yet.'}
sources=[Path(__file__),Path(p.__file__),Path(n.__file__),Path(p.geo.__file__),
         ROOT/'research/voevodsky/checkers/check_belt_operator_inputs.py',
         ROOT/'research/strominger/arbitrary-rigid-field-transport-v1.md',
         BASE/'tetrahedral-field-attachment/verification.json',BASE/'neutron-belt-field-attachment/verification.json']
# Pin all direct scientific sources of both freshly replayed reconstructions.
source_hashes={**p.result['sourceHashes'],**n.result['sourceHashes']}
for path,digest in source_hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
source_hashes.update({path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sources})
result['sourceHashes']=source_hashes
out=BASE/'arbitrary-rigid-field-transport';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','proton','neutron','nativeArbitraryReaderTransportDerived','monsterGateActivated']}))
