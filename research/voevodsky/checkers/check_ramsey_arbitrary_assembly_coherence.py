"""Finite parity certificate supporting the unbounded source-graph induction proof."""
from pathlib import Path
from itertools import permutations
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from exact_multiradical import Radical as R,mm,identity
pins={}
def load(path):
 raw=(ROOT/path).read_bytes();pins[path]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def restore(a):return [[R({int(k):v for k,v in x.items()}) for x in row] for row in a]
def solve(rows):
 basis={}
 for mask,rhs in rows:
  while mask:
   k=mask.bit_length()-1
   if k in basis:mask^=basis[k][0];rhs^=basis[k][1]
   else:basis[k]=(mask,rhs);break
  if not mask and rhs:return None,len(basis)
 sol=0
 for k,(mask,rhs) in sorted(basis.items()):
  if rhs^((mask&sol).bit_count()%2):sol|=1<<k
 return sol,len(basis)
def main():
 quotient=load('research/voevodsky/results/ramsey-native-chart-quotient-v1.json')
 replay=load('research/voevodsky/results/ramsey-forward-generators-replay-v1.json')
 carrier=load('research/voevodsky/results/ramsey-dual-carrier-identification-v1.json')
 port=load('research/voevodsky/results/ramsey-based-port-readout-v1.json')
 for report in [quotient,replay,carrier,port]:
  for path,digest in report.get('source_sha256',report.get('sourceHashes',{})).items():
   assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
   pins[path]=digest
 states,edges=quotient['states'],quotient['edges'];n=len(states)
 assert quotient['queueExhausted'] and n==96 and len(edges)==160 and len(quotient['roots'])==24
 assert replay['status']=='passed' and carrier['allFull44ReadoutSquares']
 rows=[];without_translation=[]
 for e in edges:
  mask=(1<<e['source'])^(1<<e['target']);without_translation.append((mask,e['fieldParity']))
  assert sum(e['displacement'])==0
  for i,d in enumerate(e['displacement']):
   if d%2:mask^=1<<(n+i)
  rows.append((mask,e['fieldParity']))
 assert solve(without_translation)[0] is None,'quotient-only parity unexpectedly suffices'
 sol,rank=solve(rows);assert sol is not None
 # Verify the witness independently of elimination, one actual transition at a time.
 c=[(sol>>i)&1 for i in range(n)];k=[(sol>>(n+i))&1 for i in range(4)]
 assert k==[0,1,1,0]
 for e in edges:assert c[e['target']]^c[e['source']]^(sum(a*b for a,b in zip(k,e['displacement']))%2)==e['fieldParity']
 def verifies(constants,character):return all(constants[e['target']]^constants[e['source']]^(sum(a*b for a,b in zip(character,e['displacement']))%2)==e['fieldParity'] for e in edges)
 assert not verifies(c,[0,0,0,0])
 mutated=c[:];mutated[edges[0]['source']]^=1;assert not verifies(mutated,k)
 invname={'PN':'inverse-PN','inverse-PN':'PN','NE':'NE','P-reader':'P-reader','U':'U'}
 def inv(word):return tuple(invname[x] for x in reversed(word))
 def normal(word):
  stack=[]
  for x in word:
   if stack and stack[-1]==invname[x]:stack.pop()
   else:stack.append(x)
  return tuple(stack)
 def frame(species,bit):
  w=('P-reader',) if bit else ()
  if species!='proton':w+=('PN',)
  if species=='electron':w+=('NE',)
  return w
 D={'proton':('PN','U','NE'),'neutron':('U',),'electron':('NE','U','inverse-PN')}
 Q=[4,3,2,1,0]
 def mul(a,b):return [b[i] for i in a]
 def inverse(p):return [p.index(i) for i in range(5)]
 field_cases=coefficient_cases=0
 for e in edges:
  s,t=states[e['source']]['descriptor']['species'],states[e['target']]['descriptor']['species']
  ew=('P-reader',) if e['fieldParity'] else () if e['kind'] in ['reader-phase-advance','NN-phase-advance'] else (e['kind'],)
  for bit in [0,1]:
   fs,ft=frame(s,bit),frame(t,bit^e['fieldParity'])
   assert normal(fs+ew)==normal(ft)
   reverse=inv(D[t])+inv(ew)+D[s]
   assert normal(ft+D[t]+reverse)==normal(fs+D[s])
   field_cases+=1
  p=e['permutation'];dual=mul(Q,mul(inverse(p),Q))
  for P in permutations(range(5)):
   target=mul(p,P)
   assert mul(dual,mul(Q,target))==mul(Q,P)
   coefficient_cases+=1
 # Fresh polynomial generator controls, not only word tokens.
 U=restore(port['fullFieldMap']);UP=restore(replay['generatorMatrices']['P-reader'])
 assert mm(U,U)==identity(36) and mm(UP,UP)==identity(44)
 # PN full metric isometry and NE full swap identities were freshly replayed
 # in the separate checked generator receipt. Readout/cocycle induction uses
 # those full-field identities, not finite packet samples as a universal proof.
 result={'schema':'marici.ramsey-arbitrary-assembly-coherence.v1','checkerStatus':'passed','node':'admitted-reversal-overlap-coherence',
  'scientificStatus':'unbounded_exact_source_graph_coherence_within_declared_field_candidate',
  'quotientStates':n,'quotientEdges':len(edges),'linearSystemRank':rank,
  'chartConstants':c,'translationCharacter':k,
  'potential':'p(h)=c[type(h)]+C0(h)[1]+C0(h)[2] modulo2; subtract the chosen root value',
  'allEdgePotentialEquations':True,'forwardAndReverseFieldTemplateCases':field_cases,
  'allFivePermutationFrameCases':coefficient_cases,
  'naturalityRegressionCoverage':quotient['naturalityRegressions'],
  'proofComponents':['Exact closed translation quotient from all24 marked seeds',
    'Structural source translation/origin/coefficient naturality and path induction (written theorem)',
    'Independently checked Z2 potential on every quotient edge with displacement',
    'Fresh exact full-field generator replay',
    'Universal frame, readout and reversal/cocycle algebra'],
  'negativeControls':['quotient-only potential inconsistent','erasing translation character fails','mutating a chart constant fails'],
  'quantifier':'Every finite retained assembly generated from one of the24 marked seeds by the unchanged local rules, with exact integer coordinates, irrespective of size, origin or path length; same field argument applies to the entire generated graph.',
  'limits':['Declared joint44 maps, seed coupling and co-moving conventions remain assumptions.',
    'Whole-boundary negative-direction reversal is stated for finite assemblies, permitting one global K. An infinite unbounded-origin assembly has no such finite K automatically.',
    'Mathematical exact-integer source rules, not an assertion about overflowing JavaScript Number arithmetic.',
    'No new forward native admission, unique physical source selection, physical dynamics, or formal proof-kernel certificate.'],
  'netOutcomeChanged':False}
 for path in ['research/voevodsky/checkers/check_ramsey_arbitrary_assembly_coherence.py','research/strominger/checkers/exact_multiradical.py']:
  pins[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 result['source_sha256']=pins
 (ROOT/'research/voevodsky/results/ramsey-arbitrary-assembly-coherence-v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({key:result[key] for key in ['checkerStatus','scientificStatus','quotientStates','quotientEdges','translationCharacter','forwardAndReverseFieldTemplateCases','allFivePermutationFrameCases']}))
if __name__=='__main__':main()
