#!/usr/bin/env python3
"""Source-version-bound stable row identities for the rank-26 provenance stream."""
import argparse, hashlib, importlib, json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/'research'/'benincasa'; SOURCE=BEN/'check_rank26_total_energy_triple_relation_module.py'
def digest_bytes(data): return hashlib.sha256(data).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True);a=ap.parse_args()
 os.environ['MARICI_FIELD_PRIME']=str(a.prime);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(BEN))
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,columns=rees.column_packet();reverse={index:label for label,index in columns.items()}
 source_digest=digest_bytes(SOURCE.read_bytes());point=(3,6,-3);rows=[];label_hash=hashlib.sha256();support_hash=hashlib.sha256()
 for ordinal,row in enumerate(rees.raw_relations(point,columns)):
  identity=digest_bytes(f'{source_digest}:raw_relations:{ordinal}'.encode());label_hash.update(identity.encode())
  labelled=sorted((repr(reverse[column]),value%a.prime) for column,value in row.items() if value%a.prime)
  support_hash.update(json.dumps([identity,labelled],separators=(',',':')).encode())
  if ordinal<4: rows.append({'ordinal':ordinal,'source_row_id':identity,'labelled_entries':labelled})
 count=ordinal+1
 result={'schema':'marici.aspect.rank26-provenance-stream-preflight.v1','prime':a.prime,'ambient':8,'point':list(point),'source_sha256':source_digest,'row_identity_rule':'sha256(source_sha256:raw_relations:ordinal)','row_count':count,'row_identity_sequence_sha256':label_hash.hexdigest(),'prime_specific_labelled_support_sha256':support_hash.hexdigest(),'sample_rows':rows,'stable_cross_prime_identity_ready':True,'semantic_identity_limitation':'ordinal identity is stable only for the exact source digest','production_witness_reduction_completed':False,'passed':True}
 out=ROOT/f'research/aspect/results/rank26_provenance_stream_preflight_p{a.prime}.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'passed','prime':a.prime,'rows':count,'identity':result['row_identity_sequence_sha256']}))
if __name__=='__main__':main()
