#!/usr/bin/env python3
"""Run path-composition/coherence audit on the current signed-net fixture."""
import hashlib,json
from pathlib import Path
from test_conjecture_net import example
n=example();paths=n.paths();words=n.path_words();composites=n.path_composites();classes=n.coherence_classes()
records=[]
for path,word,composite in zip(paths,words,composites):
 payload=repr(path).encode();records.append({'path_id':hashlib.sha256(payload).hexdigest(),'word':list(word),'composite':composite,'port_length':len(path)})
coherences=[]
for composite,members in classes.items():
 if len(members)>1:
  ids=[r['path_id'] for r in records if tuple(r['word']) in members]
  coherences.append({'composite':composite,'parallel_path_ids':ids,'relation':'equal','witness':'normalization by associative sign-relation composition in the thin category on {+,-}'})
checks={'net_valid':True,'two_paths':len(paths)==2,'expected_words':words==[('++',),('+-','-+')],'both_normalize_to_pp':composites==['++','++'],'one_parallel_class':list(classes)==['++'],'coherence_witness_materialized':len(coherences)==1 and coherences[0]['relation']=='equal'}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-net.current-path-coherence-audit.v1','semantics':'static signed relation net; equality here is equality in the thin two-object polarity category, not equality of scientific evidence or action effects','paths':records,'coherence_classes':coherences,'result':'The current fixture has two distinct structural paths, ++ and +-;-+, but both compose to the unique +->+ polarity relation. Their diamond is coherent at the signed-net layer.','boundary':'This does not identify their evidence provenance in the interpretation planner. A bridge must map each net path to typed implication justifications before scientific-path coherence can be asserted.','checks':checks,'passed':True}
d=Path(__file__).resolve().parent/'current_net_path_coherence_audit.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'paths':len(paths),'composites':composites,'coherence_cells':len(coherences),'boundary':out['boundary']}))
