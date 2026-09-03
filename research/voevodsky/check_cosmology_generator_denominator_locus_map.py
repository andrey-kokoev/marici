"""Construct pole-locus signatures and test whether they are geometric supports."""
from __future__ import annotations
import json,os,sys
from collections import Counter
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_source_word_axis_square_transport as transport
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_generator_denominator_locus_map.json'
Q=tuple(rees.NAMES)
def pole_signature(desc):
 family=desc[0]
 if family=='IBP':return ('V(K)',)+tuple(f'V({q})' for q in Q)
 if family=='K':return ('V(K)',)
 if family=='q':return (f'V({Q[desc[1]]})',)
 raise AssertionError(family)
def geometric_support(record):return all(record.get(k) for k in ('locus','cycle_constructor','closed_chain_witness','inclusion_map'))
def main():
 ibp,K,q=transport.descs(12);domains={'T':ibp+K+q,'S_K':K,'Q':q};counts={};transport_failures=0;mapping=[]
 for kind,descs in domains.items():
  census=Counter()
  for desc in descs:
   sig=pole_signature(desc);census[sig]+=1;mapping.append((kind,desc,sig))
   for axis in (0,1):transport_failures+=pole_signature(transport.shift(desc,axis))!=sig
  counts[kind]={'generators':len(descs),'distinct_pole_signatures':len(census),'signature_multiplicities':{' & '.join(k):v for k,v in census.items()}}
 assert sum(v['generators'] for v in counts.values())==43564 and transport_failures==0
 rules={'T/IBP':'pole locus V(K) union all five V(q_i)','T/K and S_K':'pole locus V(K)','T/q and Q':'pole locus V(q_i) selected by q index'}
 fabricated={'locus':'V(K)'};assert not geometric_support(fabricated)
 out={'schema':'marici.voevodsky.cosmology-generator-denominator-locus-map.v1','status':'complete_transport_invariant_pole_locus_map_not_geometric_support','domain_counts':counts,'map_rules':rules,'map_digest':certificate.digest(mapping),'transport_checks':2*len(mapping),'transport_failures':transport_failures,'strongest_falsification':{'candidate':'identify denominator pole locus with geometric support','residual':'43,564 generators map to pole divisors, but zero records contain a cycle constructor, closed-chain witness, or inclusion map. Pole location of a rational presentation does not prove chain support.','fabricated_locus_rejected':True},'surviving_scope':'A complete source-derived, transport-invariant pole-locus signature for every labelled algebraic generator.','first_missing_typed_object':'A geometric cycle or sheaf object on each named locus together with an inclusion into the source complex.','acceptance_test':'Construct the cycle/sheaf object from source geometry, verify closedness and inclusion for every family, and show squared-axis transport preserves the inclusion.','disposition':'Do not populate geometric_supports from pole loci alone. Defer geometric realization at this typed blocker and continue on the independently executable algebraic differential field.','next_gate':'construct-algebraic-source-differential','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
