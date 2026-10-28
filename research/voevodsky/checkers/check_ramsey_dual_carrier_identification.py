"""Conditional full44 carrier identification using the actual checked N-port map."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize,rational
pins={}
def load(path):
 raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def zeros(n,k):return [[R() for _ in range(k)] for _ in range(n)]
def main():
 cert=load('research/voevodsky/results/ramsey-complete-reversed-reference-v1.json')
 fieldtest=load('research/voevodsky/results/ramsey-reversed-certificate-fields-v1.json')
 port=load('research/voevodsky/results/ramsey-based-port-readout-v1.json')
 five=load('research/strominger/results/full-five-channel-candidate/verification.json')
 pn=load('research/strominger/results/global-PN-transport/verification.json')
 ne=load('research/strominger/results/neutron-contrast-electron-transport/verification.json')
 native=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
 for report in [cert,fieldtest,port,five,pn,ne]:
  for path,digest in report.get('source_sha256',report.get('sourceHashes',{})).items():
   assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
   pins[path]=digest
 m=list(map(F,native['source']['metric']));metrics=[[F(1)]*44,m+[F(1)]*8,m+[F(1)]*8]
 B=[restore(five['protonFiveEmbedding'])+zeros(8,5),restore(five['neutronFiveEmbedding'])+zeros(8,5),restore(five['postNEJointEmbedding'])]
 PN=restore(pn['matrix']);PNinv=sharp(PN,m)
 K=restore(ne['contrastFrame']);J=restore(ne['electronFrame'])
 Ksharp=sharp(K,m);Jsharp=adj(J)
 def exchange(X):
  left,right=X[:36],X[36:];u,v=mm(Ksharp,left),mm(Jsharp,right)
  return add(left,mm(K,add(v,u,-1)))+add(right,mm(J,add(u,v,-1)))
 def frame(i,X,inverse=False):
  if i==0:return X
  if inverse:
   if i==2:X=exchange(X)
   return mm(PNinv,X[:36])+X[36:]
  X=mm(PN,X[:36])+X[36:]
  return exchange(X) if i==2 else X
 Q=perm(cert['basisMap']);P=perm([3,1,2,0,4]);E=perm([0,4,2,3,1]);words=[identity(5),P,mm(E,P)]
 H=mm(Q,words[2]);assert H==perm([1,0,2,4,3]) and mm(H,H)==identity(5)
 B0=B[0];B0s=adj(B0)
 assert mm(B0s,B0)==identity(5)
 # Use the actual previously constructed36-coordinate N port map, not a
 # newly fitted extension of H on the remaining39 dimensions.
 U=restore(port['fullFieldMap'])
 Us=[[U[j][i].conj()*(m[j]/m[i]) for j in range(36)] for i in range(36)]
 assert mm(Us,U)==identity(36) and mm(U,U)==identity(36)
 def portlift(X):return mm(U,X[:36])+X[36:]
 def G(X):return frame(1,portlift(frame(1,X)),inverse=True)
 assert G(B0)==mm(B0,H)
 assert H==adj(H)
 # G=F1^-1 (U direct-sum I8) F1 is metric-unitary and involutive.
 # D_i=F_(2-i) G F_i^-1, with adjacent F1/F1^-1 cancelled below.
 def D(i,X):
  if i==0:return exchange(portlift(frame(1,X)))
  if i==1:return portlift(X)
  return frame(1,portlift(exchange(X)),inverse=True)
 for i in range(3):
  assert frame(i,B0)==mm(B[i],words[i])
  # Forced coefficient identity makes every canonical species binding match.
  assert mm(words[2-i],mm(H,adj(words[i])))==Q
  assert D(i,B[i])==mm(B[2-i],Q)
 # Exact metric adjoint square on full44 inputs, computed via inverse images
 # of the five target binding columns rather than expanding dense44 products.
 for i in range(3):
  inverse_target=D(2-i,B[2-i])
  assert sharp(inverse_target,metrics[i])==mm(Q,sharp(B[i],metrics[i]))
 # All-field inverse and edge coherence follow by cancellation of F_i^-1 F_i
 # and G^2=I. Check representative dense inputs independently.
 probe=[[R((j*7)%19-9)] for j in range(44)]
 for i in range(3):assert D(2-i,D(i,probe))==probe
 # Frame indices go 2->1->0 under reversal; mapped indices go0->1->2.
 def old_reverse(edge,X):return exchange(X) if edge==1 else mm(PNinv,X[:36])+X[36:]
 def new_forward(edge,X):return mm(PN,X[:36])+X[36:] if edge==1 else exchange(X)
 for edge,(source,target) in enumerate([(1,0),(2,1)]):
  assert D(target,old_reverse(edge,probe))==new_forward(edge,D(source,probe))
 # Explicitly identify the dual E raw8 carrier inside the enlarged old root.
 e8=zeros(36,8)+identity(8)
 raw_preimage=D(2,e8) # D_2 is inverse to old-P -> canonical dual-E map D_0
 assert mm(adj(raw_preimage),raw_preimage)==identity(8)
 return_preimage=D(2,zeros(36,2)+J)
 assert mm(adj(return_preimage),return_preimage)==identity(2)
 assert return_preimage[36:]==zeros(8,2)
 # The return comes from PN-pulled-back N contrast, not the old P return.
 p_contrast=mm(PNinv,K)+zeros(8,2)
 assert mm(return_preimage,adj(return_preimage))==mm(p_contrast,adj(p_contrast))
 # The other six raw E directions were already present in the retained E8
 # complement, not fabricated by relabelling a36-dimensional native P field.
 PE=mm(J,adj(J));expected_lower=add(identity(8),PE,-1)
 assert raw_preimage[36:]==expected_lower
 assert mm(expected_lower,expected_lower)==expected_lower
 assert rational(sum((expected_lower[i][i] for i in range(8)),R()))==6
 upperGram=mm(adj(raw_preimage[:36]),raw_preimage[:36])
 assert upperGram==PE
 # Prepared dual E finally has its saved rank2 E plus rank3 baryon split.
 identified=D(0,B[0]);assert identified==mm(B[2],Q)
 gE=mm(adj(identified[36:]),identified[36:]);gN=mm(sharp(identified[:36],m),identified[:36])
 assert add(gE,gN)==identity(5)
 assert rational(sum((gE[i][i] for i in range(5)),R()))==2
 assert rational(sum((gN[i][i] for i in range(5)),R()))==3
 # Controls: identity root alignment fails the Q binding; deleting the
 # original E-complement loses six raw target directions.
 assert frame(2,B0)!=mm(B[2],Q)
 assert upperGram!=identity(8)
 geometry_ineligible=sum(row['dual']['bodies'][-1]['geometry']!='proton' for row in cert['rows'])
 assert geometry_ineligible==16
 for module in list(sys.modules.values()):
  filename=getattr(module,'__file__',None)
  if filename:
   path=Path(filename).resolve()
   if path.is_file() and path.is_relative_to(ROOT/'research'):
    pins[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
 result={'schema':'marici.ramsey-dual-carrier-identification.v1','node':'T-seam-based-port-readout-binding','checkerStatus':'passed',
  'scientificStatus':'conditional_canonical_joint44_dual_carrier_identification_passes',
  'rootCoefficientAlignment':[1,0,2,4,3],
  'rootFieldExtension':'G=F1^-1 (U_N direct-sum I8) F1, using the previously checked full N port map; no independently fitted39-dimensional complement',
  'middleCarrierMapIsActualPriorPortMap':True,
  'carrierMaps':'D_i=F_(2-i) G F_i^-1, F_0=I,F_1=PN,F_2=NE_exchange PN',
  'allCanonicalBindingSquares':True,'allFull44ReadoutSquares':True,
  'fullFieldInverseAndEdgeCoherence':'Algebraic frame cancellation using the prior metric-isometric field frames and G^2=I; dense exact probe regressions also pass.',
  'dualElectronPreparedRanks':{'E':2,'retainedBaryon':3},
  'dualElectronRaw8Preimage':serialize(raw_preimage),
  'dualElectronReturnPreimage':serialize(return_preimage),
  'returnIdentification':'PN-pulled-back neutron contrast rank2, not old P return rank1',
  'rawEightDecomposition':{'oldBaryonContrast':2,'retainedOldElectronComplement':6},
  'geometryCasesOutsideUnchangedForwardPGuard':geometry_ineligible,
  'negativeControls':['identity root alignment fails Q square','erasing old E complement destroys raw8 recovery'],
  'scope':'Conditional construction within the already chosen joint44 candidate and five-column seed. Root H is forced by coefficient conventions; its full-field action is inherited from the actual prior N port map, extended by identity on the existing E8 block. The prior seed/port conventions remain conditional. Uses retained extra field directions. No primitive native P/E law equivalence, new forward rule, or spatial isometry is claimed. Source geometry is untouched;16 reversed P bodies remain outside the unchanged forward regular-P guard.',
  'netOutcomeChanged':False,'source_sha256':pins}
 (ROOT/'research/voevodsky/results/ramsey-dual-carrier-identification-v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','allCanonicalBindingSquares','allFull44ReadoutSquares','dualElectronPreparedRanks','rawEightDecomposition','geometryCasesOutsideUnchangedForwardPGuard']}))
if __name__=='__main__':main()
