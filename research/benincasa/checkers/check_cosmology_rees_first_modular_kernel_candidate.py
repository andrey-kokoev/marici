#!/usr/bin/env python3
"""Serialize the first labelled modulo-101 A4-to-A5 quotient-kernel candidate."""
import contextlib,hashlib,io,json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=int(sys.argv[1]) if len(sys.argv)>1 else 101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r5=g['r5'];complete=g['g'];columns={}
for A in [4,5]:complete['exact_rows'].__globals__['A']=A;m=complete['configure'](P);_,columns[A]=m.column_packet()
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
basis={};relation_nodes=[]
def reduce_add(row,input_kind,input_label,stop_on_zero=False):
 steps=[];row={k:v%P for k,v in row.items() if v%P}
 while row:
  q=min(row);a=row[q];steps.append({'pivot':q,'factor':a,'owner':basis[q]['owner']})
  br=basis[q]['row']
  for k,v in br.items():row[k]=(row.get(k,0)-a*v)%P
  row={k:v for k,v in row.items() if v}
 if stop_on_zero:return None,steps
 return None,steps
def add_row(row,owner):
 row={k:v%P for k,v in row.items() if v%P};steps=[]
 while row and min(row) in basis:
  q=min(row);a=row[q];steps.append((q,a,basis[q]['owner']))
  for k,v in basis[q]['row'].items():row[k]=(row.get(k,0)-a*v)%P
  row={k:v for k,v in row.items() if v}
 if not row:return False,steps,None
 q=min(row);inv=pow(row[q],-1,P);row={k:v*inv%P for k,v in row.items() if v*inv%P};basis[q]={'row':row,'owner':owner};return True,steps,(q,inv)
# Relation checkpoints are labelled by insertion index.
for i,row in enumerate(r5.values()):
 indexed={grade*len(columns[5])+columns[5][label]:project(v) for (grade,label),v in row.items()};added,steps,pivot=add_row(indexed,('relation',i));relation_nodes.append({'input':i,'added':added,'steps':steps,'pivot':pivot})
relation_rank=len(basis);source_nodes=[];candidate=None
for grade in range(3):
 for label in columns[4]:
  coordinate=grade*len(columns[5])+columns[5][label];idx=len(source_nodes);added,steps,pivot=add_row({coordinate:1},('source',idx));node={'source_index':idx,'grade':grade,'label':repr(label),'target_coordinate':coordinate,'added':added,'steps':steps,'pivot':pivot};source_nodes.append(node)
  if not added:candidate=node;break
 if candidate:break
assert relation_rank==5888 and candidate is not None
# Replay the candidate dependency against the serialized checkpoint schedule.
r={candidate['target_coordinate']:1}
for q,a,owner in candidate['steps']:
 for k,v in basis[q]['row'].items():r[k]=(r.get(k,0)-a*v)%P
 r={k:v for k,v in r.items() if v}
assert not r
# Materialize the transitive checkpoint closure needed to replay this candidate.
reachable_relation=set();reachable_source=set();stack=[owner for _,_,owner in candidate['steps']]
while stack:
 owner=stack.pop()
 if owner[0]=='relation':
  i=owner[1]
  if i in reachable_relation:continue
  reachable_relation.add(i);stack.extend(x[2] for x in relation_nodes[i]['steps'])
 else:
  i=owner[1]
  if i in reachable_source:continue
  reachable_source.add(i);stack.extend(x[2] for x in source_nodes[i]['steps'])
relation_closure={str(i):relation_nodes[i] for i in sorted(reachable_relation)};source_closure={str(i):source_nodes[i] for i in sorted(reachable_source)}
out={'schema':'marici.benincasa.cosmology-rees-first-modular-kernel-candidate.v2','problem':'materialize one labelled modular kernel candidate required by the exact-lift gate','coefficient_prime':P,'candidate':candidate,'source_checkpoint_nodes_before_candidate':len(source_nodes)-1,'relation_checkpoint_count':len(relation_nodes),'relation_rank':relation_rank,'zero_image_replayed':True,'reachable_relation_checkpoints':relation_closure,'reachable_source_checkpoints':source_closure,'reachable_relation_count':len(relation_closure),'reachable_source_count':len(source_closure),'candidate_digest':hashlib.sha256(repr(candidate).encode()).hexdigest(),'exact_lift_executed':False,'acceptance_next':'construct the label-matched candidate at additional primes and reconstruct its coefficients before exact replay','scope':'one self-contained modulo-101 checkpoint-DAG candidate, not a rational kernel theorem','passed':True};(R/('cosmology_rees_first_modular_kernel_candidate.json' if P==101 else f'cosmology_rees_first_modular_kernel_candidate_p{P}.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['candidate']}|{'candidate_summary':{k:v for k,v in candidate.items() if k!='steps'},'candidate_step_count':len(candidate['steps'])},indent=2))
