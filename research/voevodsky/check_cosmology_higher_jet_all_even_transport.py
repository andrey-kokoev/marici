"""Structural exact transport of all order 3-6 certificates and raw zeros."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_higher_jet_all_even_transport.json'
import sys;sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_source_word_axis_square_transport as tr
def shifted(d,path):
 for a in path:d=tr.shift(d,a)
 return d
def main():
 summary=json.loads((RES/'cosmology_higher_jet_exact_membership.json').read_text());certs=json.loads((RES/'cosmology_higher_jet_exact_certificate_words.json').read_text())['records'];ind=json.loads((RES/'cosmology_all_even_linear_transport_induction.json').read_text());assert summary['passed'] and len(certs)==17512 and ind['passed']
 ibp12,K12,q12=tr.descs(12);all12=ibp12+K12+q12;decode={'T':all12,'S_K':K12,'Q':q12};targets={}
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for r in json.loads((RES/name).read_text())['records']:targets[r['source_certificate']['canonical_target_id']]=tr.target_desc(family,r)
 checks={};mixed=0
 for A,paths in {14:[(0,),(1,)],16:[(0,0),(0,1),(1,0),(1,1)]}.items():
  ibp,K,q=tr.descs(A);sets={'T':set(ibp+K+q),'S_K':set(K),'Q':set(q)};targetset=sets['T'];count=0
  for c in certs:
   for path in paths:
    assert shifted(targets[c['target_id']],path) in targetset
    for term in c['word_terms']:assert shifted(decode[term['kind']][term['row_index']],path) in sets[term['kind']]
    count+=1
   if A==16:
    assert shifted(targets[c['target_id']],(0,1))==shifted(targets[c['target_id']],(1,0))
    for term in c['word_terms']:assert shifted(decode[term['kind']][term['row_index']],(0,1))==shifted(decode[term['kind']][term['row_index']],(1,0))
    mixed+=1
  checks[str(A)]={'nonzero_word_descriptor_transports':count,'failures':0}
 checks['16']['mixed_path_equalities']=mixed
 zero=summary['zero_raw_targets'];assert zero==73064
 out={'schema':'marici.voevodsky.cosmology-higher-jet-all-even-transport.v1','status':'all_order_3_to_6_exact_memberships_transport_to_every_even_A','nonzero_words':len(certs),'structural_zero_seed_components':zero,'A14':checks['14'],'A16':checks['16'],'row_naturality':ind['symbolic_domain_proof']['row_naturality'],'exact_transport_argument':'Squared-axis multiplication is parameter-independent, hence commutes with every derivative order. It maps source and target rows identically and acts as the identity on rational coefficients; exact words remain exact and raw zero rows remain zero.','induction':'Descriptor domains are closed under both shifts, mixed shifts commute, and every parity orbit is generated from A12.','theorem':'All raw xyz derivatives of orders 3-6 lie in the unchanged source image for every even A>=12; orders above six vanish by interpolation degree.','claim_boundary':'No higher-jet extension, coherent primitive selector, admissibility rule, geometric comparison, or connecting morphism.','next_gate':'classify-full-algebraic-jet-absorption','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
