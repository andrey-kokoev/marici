#!/usr/bin/env python3
"""Independently audit descriptor-level ambient compatibility of canonical q seeds."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research'/'voevodsky'/'results';R=ROOT/'research'/'benincasa'/'results'
expected_file_hashes={12:'6b48987fd1c3fcfb07fd080d52a48879e1f85e6f3ec2c05b580a31bcdd07ed8a',14:'',16:''};packets={}
for A in (12,14,16):
 path=V/f'cosmology_rank26_p_normal_K_q_canonical_signature_a{A}.json';raw=path.read_bytes();packets[A]=json.loads(raw);expected_file_hashes[A]=hashlib.sha256(raw).hexdigest()
def tuples(sig):return sorted((x['mark'],x['q_pole'],tuple(x['levels']),tuple(x['exponent']),x['coefficient']) for x in sig['terms'])
checks={}
for k,n,digest in (('k0',7,'206b994eb6385d038a8f16d9801e52088a18bb63ac06dc6ed1aaa4191792dcdb'),('k1',11,'81abd0f74f88174a36cd67ae019f33c99c00cacd4690be9f8cc939195e13fc44')):
 ts={A:tuples(packets[A]['signatures'][k]) for A in packets};recomputed={A:hashlib.sha256(repr(ts[A]).encode()).hexdigest() for A in ts};assert all(len(x)==n for x in ts.values());assert len({tuple(x) for x in ts.values()})==1;assert set(recomputed.values())=={digest};checks[k]={'row_count':n,'descriptor_coefficient_sha256':digest,'terms_identical_across_degrees':True}
# Type audit: every term is g1 at levels (1,1,2,1,1); this is a marked-q lift, not a tau map.
for A in packets:
 for k in ('k0','k1'):
  assert all(x['mark']=='g1' and x['levels']==[1,1,2,1,1] for x in packets[A]['signatures'][k]['terms'])
out={'schema':'marici.benincasa.cosmology-canonical-q-seed-ambient-audit.v1','source_packet_sha256':expected_file_hashes,'field':32003,'ambient_degrees':[12,14,16],'checks':checks,'all_terms_g1_at_levels_11211':True,'ambient_compatibility_independently_verified':True,'source_natural_uniqueness_verified':False,'two_prime_verified':False,'tau_p_map_constructed':False,'interpretation':'the serialized descriptor-coefficient terms, not merely reported hashes, are identical across the three ambient degrees; they define finite-field marked-q seed compatibility only','next_gate':'obtain a second-prime seed replay and a boundary operator on degrees A-6,A-5,A-4 before proposing induction','passed':True};(R/'cosmology_canonical_q_seed_ambient_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
