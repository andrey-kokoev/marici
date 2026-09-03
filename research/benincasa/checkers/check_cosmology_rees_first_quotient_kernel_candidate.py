#!/usr/bin/env python3
"""First genuine modular kernel candidate from a faithful A4 quotient complement."""
import contextlib,hashlib,io,json,runpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=int(sys.argv[1]) if len(sys.argv)>1 else 101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r4,r5=g['r4'],g['r5'];complete=g['g'];columns={}
for A in [4,5]:complete['exact_rows'].__globals__['A']=A;m=complete['configure'](P);_,columns[A]=m.column_packet()
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
def add(row,basis,owner):
 row={k:v%P for k,v in row.items() if v%P};steps=[]
 while row and min(row) in basis:
  q=min(row);a=row[q];steps.append((q,a,basis[q]['owner']))
  for k,v in basis[q]['row'].items():row[k]=(row.get(k,0)-a*v)%P
  row={k:v for k,v in row.items() if v}
 if not row:return False,steps,None
 q=min(row);inv=pow(row[q],-1,P);basis[q]={'row':{k:v*inv%P for k,v in row.items() if v*inv%P},'owner':owner};return True,steps,(q,inv)
def indexed(row,cols):return {grade*len(cols)+cols[label]:project(v) for (grade,label),v in row.items()}
# A4 nonpivot coordinate classes are a faithful quotient basis.
b4={}
for i,row in enumerate(r4.values()):add(indexed(row,columns[4]),b4,('relation4',i))
all4=[(grade,label,grade*len(columns[4])+idx) for grade in range(3) for label,idx in columns[4].items()];complement=[x for x in all4 if x[2] not in b4];assert len(b4)==4146 and len(complement)==8814
# Reduce those quotient-basis representatives in A5.
b5={}
for i,row in enumerate(r5.values()):add(indexed(row,columns[5]),b5,('relation5',i))
nodes=[];candidate=None
for grade,label,source_coordinate in complement:
 target_coordinate=grade*len(columns[5])+columns[5][label];i=len(nodes);added,steps,pivot=add({target_coordinate:1},b5,('quotient',i));node={'quotient_index':i,'grade':grade,'label':repr(label),'source_coordinate':source_coordinate,'target_coordinate':target_coordinate,'added':added,'steps':steps,'pivot':pivot};nodes.append(node)
 if not added:candidate=node;break
assert candidate is not None
reachable=set();stack=[o for _,_,o in candidate['steps'] if o[0]=='quotient']
while stack:
 i=stack.pop()[1]
 if i in reachable:continue
 reachable.add(i);stack.extend(o for _,_,o in nodes[i]['steps'] if o[0]=='quotient')
closure={str(i):nodes[i] for i in sorted(reachable)}
out={'schema':'marici.benincasa.cosmology-rees-first-quotient-kernel-candidate.v1','problem':'materialize the first dependency after embedding a faithful A4 quotient-complement basis into A5','coefficient_prime':P,'A4_relation_rank':len(b4),'A4_quotient_dimension':len(complement),'A5_relation_rank':5888,'independent_images_before_candidate':len(nodes)-1,'candidate':candidate,'reachable_quotient_checkpoints':closure,'reachable_quotient_count':len(closure),'candidate_digest':hashlib.sha256(repr(candidate).encode()).hexdigest(),'source_class_nonzero_mod_p':True,'target_class_zero_mod_p':True,'scope':'one genuine modulo-101 quotient-kernel candidate; no rational lift','next_test':'repeat this faithful-complement extraction at 103 and 107, compare expanded quotient coordinates, then reconstruct exactly','passed':True};(R/('cosmology_rees_first_quotient_kernel_candidate.json' if P==101 else f'cosmology_rees_first_quotient_kernel_candidate_p{P}.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['candidate','reachable_quotient_checkpoints']}|{'candidate_summary':{k:v for k,v in candidate.items() if k!='steps'},'candidate_steps':len(candidate['steps'])},indent=2))
