#!/usr/bin/env python3
"""Audit admitted relative-pairing candidates against the Rees physical-descent interface."""
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';d=json.loads((P/'cosmology_contraction_pairing_domain_audit.json').read_text());f=json.loads((P/'cosmology_minimal_extension_source_realization_functor.json').read_text());h=json.loads((P/'cosmology_aspect_pairing_handoff_disposition.json').read_text())
rows=[]
for name,x in d['candidates'].items():rows.append({'candidate':name,'admitted':x['admitted'],'first_blocker':x['reason']})
weighted=next(x for x in f['candidates'] if x['candidate']=='weighted relative pairing');rows.append({'candidate':'weighted relative pairing source realization','admitted':weighted['realizes_u'],'first_blocker':weighted['first_blocker']})
out={'schema':'marici.benincasa.cosmology-relative-pairing-source-search.v1','candidates':rows,'admitted_pairings_count':sum(x['admitted'] for x in rows),'aspect_request_event':h['request_event'],'aspect_response_received':h['response_received'],'exact_disposition':'no audited candidate defines both a source relative pair and a boundary-invariant pairing typed to the Rees generator','first_missing_typed_object':'a labelled relative homology object paired with the admitted relative de Rham cocycle','next_executable_test':'test whether a sourced mu2 orientation local system supplies the odd integral leg and relative pairing without dividing transfer by two','global_nonexistence':False};assert out['admitted_pairings_count']==0;(P/'cosmology_relative_pairing_source_search.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
