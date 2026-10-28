"""Finite full-field descent on every interface of the reversed retained assembly."""
from pathlib import Path
from fractions import Fraction as F
from collections import deque
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,adj,identity,serialize
pins={}
def load(path):
 raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def sharp(a,m):return [[x*m[j] for j,x in enumerate(row)] for row in adj(a)]
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def main():
 assembly=load('research/voevodsky/results/ramsey-reversed-assembly-v1.json')
 old=load('research/strominger/results/joint-field-assembly-sewing.json')
 carrier=load('research/voevodsky/results/ramsey-dual-carrier-identification-v1.json')
 port=load('research/voevodsky/results/ramsey-based-port-readout-v1.json')
 native=load('research/strominger/results/common-three-carrier-protocol/neutron.json')
 for report in [assembly,old,carrier,port]:
  for path,digest in report.get('source_sha256',report.get('sourceHashes',{})).items():
   assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
   pins[path]=digest
 forward,dual=assembly['forward'],assembly['dual'];packets={p['id']:p for p in forward['packets']}
 species=lambda i:packets[i]['frame']['species']
 swap={'proton':'electron','neutron':'neutron','electron':'proton'}
 inverse={'PN':'inverse-PN','inverse-PN':'PN','NE':'NE','P-reader':'P-reader','U':'U'}
 def inv(word):return tuple(inverse[x] for x in reversed(word))
 def normal(word):
  stack=[]
  for x in word:
   if stack and stack[-1]==inverse[x]:stack.pop()
   else:stack.append(x)
  return tuple(stack)
 generators={name:restore(matrix) for name,matrix in old['generatorMatrices'].items()}
 U=restore(port['fullFieldMap']);generators['U']=[row+[R() for _ in range(8)] for row in U]+[[R() for _ in range(36)]+row for row in identity(8)]
 def apply(word,X):
  for x in normal(word):X=mm(generators[x],X)
  return X
 def edgeword(e):
  if e['kind']=='reader-phase-advance':return ('P-reader',) if species(e['source'])=='proton' else ()
  if e['kind']=='NN-phase-advance':return ()
  return (e['kind'],)
 D={'proton':('PN','U','NE'),'neutron':('U',),'electron':('NE','U','inverse-PN')}
 m=list(map(F,native['source']['metric']));metrics={'proton':[F(1)]*44,'neutron':m+[F(1)]*8,'electron':m+[F(1)]*8}
 # Fresh parity solution from ALL retained edges, not only chosen histories.
 parity={forward['entries'][0]:0};q=deque(parity)
 while q:
  a=q.popleft()
  for e in forward['edges']:
   if e['source']!=a:continue
   b=e['target'];bit=parity[a]^int(edgeword(e)==('P-reader',))
   if b in parity:assert parity[b]==bit
   else:parity[b]=bit;q.append(b)
 assert len(parity)==14
 def frame(i):
  word=('P-reader',) if parity[i] else ()
  if species(i)!='proton':word+=('PN',)
  if species(i)=='electron':word+=('NE',)
  return word
 frames={i:normal(frame(i)+D[species(i)]) for i in packets}
 oldbindings={p['packet']:p for p in old['packetBindings']}
 assert set(oldbindings)==set(packets)
 root=forward['entries'][0];B0=restore(oldbindings[root]['binding']);Q=perm([4,3,2,1,0])
 physical={word:apply(word,B0) for word in set(frames.values())}
 bindings={};readouts={}
 for i,p in packets.items():
  oldp=oldbindings[i];assert oldp['nativePermutation']==p['permutation'] and oldp['frameParity']==parity[i]
  bindings[i]=mm(mm(physical[frames[i]],adj(perm(p['permutation']))),Q)
  readouts[i]=sharp(bindings[i],metrics[swap[species(i)]])
  assert mm(readouts[i],bindings[i])==identity(5)
 edges=[];types={}
 for e,de in zip(forward['edges'],dual['edges']):
  a,b=de['source'],de['target']
  word=normal(inv(D[species(a)])+inv(edgeword(e))+D[species(b)])
  assert normal(frames[a]+word)==frames[b]
  assert normal(frames[b]+inv(word))==frames[a]
  key=(word,frames[a],frames[b])
  if key not in types:
   assert apply(word,physical[frames[a]])==physical[frames[b]]
   types[key]=True
  pi=perm(de['permutation']);Pa=perm(packets[a]['permutation']);Pb=perm(packets[b]['permutation'])
  assert mm(pi,mm(Q,Pa))==mm(Q,Pb)
  # Inverse field transport of the target binding, from the verified frame
  # relation, supplies the adjoint equality on every44-dimensional input.
  inverse_target_binding=mm(mm(physical[frames[a]],adj(Pb)),Q)
  assert sharp(inverse_target_binding,metrics[swap[species(a)]])==mm(pi,readouts[a])
  edges.append({'originalKind':e['kind'],'source':a,'target':b,'dualSourceSpecies':swap[species(a)],
    'dualTargetSpecies':swap[species(b)],'transportFactorWord':word,'full44ReadoutSquare':True})
 # All pair/triple chart comparisons compose by exact full-field cancellation.
 pair=lambda a,b:inv(frames[a])+frames[b]
 triples=0
 for a in packets:
  for b in packets:
   for c in packets:
    assert normal(pair(a,b)+pair(b,c))==normal(pair(a,c));triples+=1
 # Same geometric chart/origin histories must not have their bindings erased.
 pairs=[(a,b) for a in packets for b in packets if a<b and packets[a]['chart']==packets[b]['chart'] and packets[a]['origin']==packets[b]['origin'] and packets[a]['permutation']!=packets[b]['permutation']]
 equal_field_pairs=[(a,b) for a,b in pairs if frames[a]==frames[b]]
 assert equal_field_pairs and all(bindings[a]!=bindings[b] for a,b in equal_field_pairs)
 ereaders=[e for e in edges if e['originalKind']=='reader-phase-advance' and e['dualSourceSpecies']=='electron']
 assert ereaders and all(e['transportFactorWord'] for e in ereaders)
 # Do not replace the induced E-reader by identity, or identify histories.
 assert any(apply(e['transportFactorWord'],physical[frames[e['source']]])!=physical[frames[e['source']]] for e in ereaders)
 for path in ['research/voevodsky/checkers/check_ramsey_reversed_assembly_fields.py','research/strominger/checkers/exact_multiradical.py']:
  pins[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 result={'schema':'marici.ramsey-reversed-assembly-fields.v1','checkerStatus':'passed','node':'admitted-reversal-overlap-coherence',
  'scientificStatus':'finite_negative_direction_assembly_field_descent_passes',
  'packets':14,'interfaces':18,'fieldFrameTypes':len(physical),'independentlyCheckedTransitionTypes':len(types),
  'fullFieldComparisonTriangles':triples,'allPacketFiveCoefficientRecovery':True,
  'retainedDifferentBindingHistoryPairs':equal_field_pairs,'interfacesChecked':edges,
  'inducedElectronReaderInterfaces':ereaders,
  'negativeControls':['dropping transported E-reader to identity fails','erasing coefficient histories identifies different bindings'],
  'scope':'Finite exact connection comparison under the explicit negative-direction pullback policy. Every retained interface and all14^3 comparison triangles are checked. Full-field reasoning uses the prior metric-isometric generators and exact factor cancellation, with fresh five-column transition regressions. Induced E-reader words are transported comparisons, not new forward native operations. No arbitrary-assembly theorem, unique source selection or graph admission.',
  'netOutcomeChanged':False,'source_sha256':pins}
 (ROOT/'research/voevodsky/results/ramsey-reversed-assembly-fields-v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','packets','interfaces','fieldFrameTypes','independentlyCheckedTransitionTypes','fullFieldComparisonTriangles','allPacketFiveCoefficientRecovery']}))
if __name__=='__main__':main()
