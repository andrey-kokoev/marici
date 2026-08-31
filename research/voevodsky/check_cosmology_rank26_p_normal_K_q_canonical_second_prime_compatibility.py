"""Verify canonical q-lift ambient compatibility over F_32009 and compare descriptor support with F_32003."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_canonical_second_prime_compatibility.json'
def packet(p,a):
 path=RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_p{p}_a{a}.json'
 if not path.exists() and p==32003:path=RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_a{a}.json'
 return json.loads(path.read_text())
def main():
 ps={p:{a:packet(p,a) for a in (12,14,16)} for p in (32003,32009)};results={}
 for kp in ('k0','k1'):
  h={p:[ps[p][a]['signatures'][kp]['descriptor_coefficient_sha256'] for a in (12,14,16)] for p in ps};ambient={p:len(set(v))==1 for p,v in h.items()};supports={p:[[ (t['mark'],t['q_pole'],tuple(t['levels']),tuple(t['exponent'])) for t in ps[p][a]['signatures'][kp]['terms']] for a in (12,14,16)] for p in ps};same_support=supports[32003][0]==supports[32009][0]
  results[kp]={'ambient_compatible':ambient,'hashes':{str(p):v[0] for p,v in h.items()},'same_source_descriptor_support_across_primes':same_support,'q_rows':len(supports[32009][0])}
 assert all(all(x['ambient_compatible'].values()) and x['same_source_descriptor_support_across_primes'] for x in results.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-canonical-second-prime-compatibility.v1','status':'canonical_seeds_ambient_compatible_over_both_primes','results':results,'decision':'The 7-row and 11-row canonical seeds are ambient-compatible over F_32009 and use the same typed source descriptors as over F_32003; coefficient hashes differ by field representation.','limitations':['two finite primes','three finite ambient degrees','same support does not prove integral coefficient lift'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
