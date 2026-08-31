#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/aspect/results'
a=json.loads((R/'rank26_provenance_stream_preflight_p32003.json').read_text());b=json.loads((R/'rank26_provenance_stream_preflight_p32009.json').read_text())
assert a['passed'] and b['passed'];assert a['source_sha256']==b['source_sha256'];assert a['row_count']==b['row_count']==9780;assert a['row_identity_sequence_sha256']==b['row_identity_sequence_sha256'];assert [r['source_row_id'] for r in a['sample_rows']]==[r['source_row_id'] for r in b['sample_rows']]
out={'schema':'marici.aspect.rank26-provenance-stream-cross-prime.v1','primes':[32003,32009],'row_count':a['row_count'],'source_sha256':a['source_sha256'],'row_identity_sequence_sha256':a['row_identity_sequence_sha256'],'stable_source_bound_row_identities':True,'semantic_limitation':'identities are ordinal and valid only under the exact source digest','production_witness_reduction_completed':False,'passed':True}
(R/'rank26_provenance_stream_cross_prime.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','rows':out['row_count']}))
