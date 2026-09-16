"""Unified conservative census of computad edges/faces lacking analytic realizations."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).parents[1]
SIG=ROOT/'coherence-pyramid-computad-signature.json'
CELLS=ROOT/'coherence-pyramid-cells-and-laws.json'
OVERLAY=ROOT/'coherence-pyramid-overlay-registry-v3.json'
REG=ROOT/'coherence-pyramid-analytical-realization-registry.json'
OUT=ROOT/'results'/'coherence-pyramid-analytical-frontier.json'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def transitive_reach(deps):
 nodes=set(deps)
 for values in deps.values(): nodes.update(values)
 reach={n:set(deps.get(n,[])) for n in nodes}
 changed=True
 while changed:
  changed=False
  for n in nodes:
   new=set().union(*(reach.get(x,set()) for x in list(reach[n]))) if reach[n] else set()
   if not new<=reach[n]:reach[n]|=new;changed=True
 return reach
def minimal_missing(required,true,reach):
 missing=set(required)-true
 # Remove a missing consequence when one of its missing prerequisites is also reported.
 return sorted(x for x in missing if not any(y in reach.get(x,set()) for y in missing if y!=x))
def main():
 sig,cells,overlay,reg=map(load,(SIG,CELLS,OVERLAY,REG))
 allowed=set(reg['allowed_statuses']);records=reg['realizations'];ids=[r['id'] for r in records]
 assert len(ids)==len(set(ids));assert all(r['status'] in allowed for r in records)
 by={(r['kind'],r['id']):r for r in records}
 true={k for k,v in reg['current_certificates'].items() if v is True};reach=transitive_reach(reg['certificate_dependencies'])
 arrows=sig['one_generators'];edge_rows=[]
 for name,data in sorted(arrows.items()):
  rec=by.get(('edge',name));required=data['required_certificates'];missing=minimal_missing(required,true,reach)
  status=rec['status'] if rec else 'unregistered'
  edge_rows.append({'id':name,'source_sort':data['source_sort'],'target_sort':data['target_sort'],'status':status,'analytically_realized':status=='realized','minimal_missing_certificates':missing,'evidence':rec.get('source') if rec else None})
 face_rows=[]
 for name,data in sorted(cells['cells'].items()):
  rec=by.get(('face',name));required=data['admission']+data.get('invertibility',[]);missing=minimal_missing(required,true,reach);status=rec['status'] if rec else 'unregistered'
  face_rows.append({'id':name,'boundary':data['boundary'],'law':data['law'],'status':status,'analytically_realized':status=='realized','minimal_missing_certificates':missing,'evidence':rec.get('source') if rec else None})
 law_rows=[]
 for name,required in sorted(cells['coherence_obligations'].items()):
  rec=by.get(('law',name));status=rec['status'] if rec else 'unregistered'
  law_rows.append({'id':name,'status':status,'verified':status=='realized','minimal_missing_certificates':minimal_missing(required,true,reach),'evidence':rec.get('source') if rec else None})
 dangling=[x for x in reg['external_fragments'] if x['status']=='realized_unlinked']
 checks={'all_signature_edges_censused':len(edge_rows)==len(arrows),'all_declared_faces_censused':len(face_rows)==len(cells['cells']),'all_laws_censused':len(law_rows)==len(cells['coherence_obligations']),'registry_ids_unique':len(ids)==len(set(ids)),'global_nonpromotion_respected':not overlay['global_status']['full_coherence_pyramid_equipment_verified'],'unlinked_realizations_exposed':bool(dangling)}
 out={'schema':'marici.voevodsky.coherence-pyramid-analytical-frontier.v1','summary':{'edges_total':len(edge_rows),'edges_without_analytic_realization':sum(not x['analytically_realized'] for x in edge_rows),'faces_total':len(face_rows),'faces_without_analytic_realization':sum(not x['analytically_realized'] for x in face_rows),'laws_total':len(law_rows),'laws_without_verification':sum(not x['verified'] for x in law_rows),'realized_but_unlinked_fragments':len(dangling)},'edges':edge_rows,'faces':face_rows,'laws':law_rows,'realized_but_unlinked_fragments':dangling,'checks':checks,'passed':all(checks.values()),'claim_boundary':'This scanner detects missing realizations only for declared computad generators and explicit registry links; it does not infer generators or proofs from prose.'}
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
