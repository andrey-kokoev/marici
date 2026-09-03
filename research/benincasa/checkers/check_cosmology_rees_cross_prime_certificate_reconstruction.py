#!/usr/bin/env python3
"""DPC cross-prime reconstruction protocol for labelled provenance vectors."""
import hashlib,json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_rees_checkpointed_provenance_replay.json').read_text());assert prior['passed']
labels=['row:g1:0','row:g2:1','row:g3:2','row:g23:3'];primitive=[2,-3,5,7];digest=hashlib.sha256(json.dumps(labels).encode()).hexdigest()
def cert(p):
 inv=pow(primitive[0],p-2,p);return {'prime':p,'input_digest':digest,'support':labels,'normalized':{k:(v*inv)%p for k,v in zip(labels,primitive)}}
def crt(a,p,b,q):return (a+((b-a)*pow(p,-1,q)%q)*p)%(p*q)
def reconstruct(residue,modulus,bound=20):
 found=[]
 for den in range(1,bound+1):
  for num in range(-bound,bound+1):
   if math.gcd(abs(num),den)==1 and (den*residue-num)%modulus==0:found.append(Fraction(num,den))
 assert len(found)==1,found;return found[0]
c1,c2=cert(101),cert(103);M=101*103
ratios=[]
for label in labels:ratios.append(reconstruct(crt(c1['normalized'][label],101,c2['normalized'][label],103),M))
lcm=math.lcm(*(x.denominator for x in ratios));candidate=[int(x*lcm) for x in ratios];g=math.gcd(*map(abs,candidate));candidate=[x//g for x in candidate];assert candidate==primitive
c3=cert(107)
def validates(c):
 p=c['prime'];inv=pow(candidate[0],p-2,p);return c['input_digest']==digest and c['support']==labels and all(c['normalized'][k]==(v*inv)%p for k,v in zip(labels,candidate))
assert validates(c3)
bad=json.loads(json.dumps(c3));bad['normalized'][labels[2]]=(bad['normalized'][labels[2]]+1)%107;assert not validates(bad)
out={'schema':'marici.benincasa.cosmology-rees-cross-prime-certificate-reconstruction.v1','problem':'decide whether labelled modular certificates define one integral candidate rather than unrelated prime-field vectors','bold_conjecture':'stable support at two good primes with a coefficient bound reconstructs a unique primitive candidate that an independent prime can validate','rivals':['support-only matching','unbounded rational reconstruction','single-prime promotion'],'risky_consequences':'two-prime CRT reconstruction must be unique within the preregistered bound; a good third prime must validate; one changed coefficient must be rejected','strongest_falsification_attempt':{'labels':labels,'input_digest':digest,'reconstruction_primes':[101,103],'crt_modulus':M,'numerator_denominator_bound':20,'reconstructed_ratios':[str(x) for x in ratios],'primitive_candidate':candidate,'validation_prime':107,'good_certificate_validates':validates(c3),'altered_certificate_validates':validates(bad)},'exact_residual':'the good third-prime residual vanishes; the altered coefficient fails validation','conjecture_disposition':'retained for the bounded labelled protocol','required_authority':['stable source-row labels','identical input digest','preregistered reconstruction bound','independent-prime validation','exact integral replay after reconstruction'],'two_primes_alone_certify_integrality':False,'integral_source_generator_constructed':False,'next_conjecture':'exact integer replay of the reconstructed primitive vector verifies a boundary-zero source relation and rejects a coefficient corruption','next_falsifier':'apply the candidate to labelled integer source rows and record the exact nonzero residual of a corrupted vector','passed':True};(R/'cosmology_rees_cross_prime_certificate_reconstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
