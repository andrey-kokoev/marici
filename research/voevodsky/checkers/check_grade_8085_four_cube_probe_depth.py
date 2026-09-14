#!/usr/bin/env python3
"""Two-modulus test of the predicted four-cube probe-depth transition."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/the_grade_8085_four_cube_raises_probe_depth.md'
RESULT=ROOT/'research/voevodsky/results/grade_8085_four_cube_probe_depth.json'
MODULI=(1000000007,1000000009)
SETTINGS=((5,6),(3,4),(7,10))

def primes(n):
 sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if sieve[p]:sieve[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if sieve[i]]

def graph(cutoff):
 ps=primes(cutoff//2+2);edges=[]
 for shell,(p,q) in enumerate(zip(ps,ps[1:]),1):
  for k in range(1,cutoff//(p*q)+1):edges.append((k*p*q,shell,k,k*p,k*q,p,q))
 edges.sort();vertices=sorted({e[3] for e in edges}|{e[4] for e in edges});vi={v:i for i,v in enumerate(vertices)}
 return edges,vertices,vi

def rows(edges,vertices,vi,modulus,setting=None):
 result=[{} for _ in vertices]
 t=None if setting is None else setting[0]*pow(setting[1],modulus-2,modulus)%modulus
 for col,edge in enumerate(edges):
  weight=1 if t is None else pow(t,edge[1],modulus)
  result[vi[edge[3]]][col]=-weight%modulus;result[vi[edge[4]]][col]=weight
 return result

def rank_mod(matrix,modulus):
 basis={}
 for source in matrix:
  row={k:v%modulus for k,v in source.items() if v%modulus}
  while row:
   lead=min(row)
   if lead not in basis:
    inverse=pow(row[lead],modulus-2,modulus)
    basis[lead]={k:v*inverse%modulus for k,v in row.items() if v*inverse%modulus};break
   factor=row[lead]
   for k,v in basis[lead].items():
    value=(row.get(k,0)-factor*v)%modulus
    if value:row[k]=value
    else:row.pop(k,None)
 return len(basis)

def cube():
 base=2*3*5*7;ratios=((3,2),(5,3),(7,5),(11,7));vertices={}
 for mask in range(16):
  value=base
  for i,(q,p) in enumerate(ratios):
   if mask>>i&1:value=value*q//p
  vertices[mask]=value
 edges=[]
 for mask,source in vertices.items():
  for i,(q,p) in enumerate(ratios):
   if not(mask>>i&1):edges.append((mask,i+1,source,vertices[mask|1<<i],source//p*p*q))
 return vertices,edges

census={};checks={}
for cutoff in (8084,8085):
 edges,vertices,vi=graph(cutoff);per_mod=[]
 for modulus in MODULI:
  base=rows(edges,vertices,vi,modulus);boundary_rank=rank_mod(base,modulus);joint=[]
  for count in range(1,4):
   matrix=list(base)
   for setting in SETTINGS[:count]:matrix+=rows(edges,vertices,vi,modulus,setting)
   rank=rank_mod(matrix,modulus);joint.append({'settings':count,'rank':rank,'deficiency':len(edges)-rank})
  per_mod.append({'modulus':modulus,'boundary_rank':boundary_rank,'cycle_dimension':len(edges)-boundary_rank,'joint':joint})
 checks[f'moduli_agree_{cutoff}']=per_mod[0]['boundary_rank']==per_mod[1]['boundary_rank'] and per_mod[0]['joint']==[{**x,'rank':x['rank']} for x in per_mod[1]['joint']]
 census[str(cutoff)]={'edges':len(edges),'vertices':len(vertices),'new_grade_edges':[(e[1],e[2],e[3],e[4],e[5],e[6]) for e in edges if e[0]==cutoff],'ranks':per_mod}
checks['below_two_settings_full']=all(x['joint'][1]['deficiency']==0 for x in census['8084']['ranks'])
checks['at_two_settings_deficiency_one']=all(x['joint'][1]['deficiency']==1 for x in census['8085']['ranks'])
checks['at_three_settings_full']=all(x['joint'][2]['deficiency']==0 for x in census['8085']['ranks'])
checks['cycle_dimension_step_two']=all(a['cycle_dimension']==452 and b['cycle_dimension']==454 for a,b in zip(census['8084']['ranks'],census['8085']['ranks']))
expected_new=[(2,539,1617,2695,3,5),(3,231,1155,1617,5,7),(4,105,735,1155,7,11)]
checks['three_new_edges_exact']=census['8085']['new_grade_edges']==expected_new
all_edges,_,_=graph(8085)
deletion_deficiencies={}
for removed in [edge for edge in all_edges if edge[0]==8085]:
 remaining=[edge for edge in all_edges if edge!=removed]
 remaining_vertices=sorted({e[3] for e in remaining}|{e[4] for e in remaining})
 remaining_vi={v:i for i,v in enumerate(remaining_vertices)}
 values=[]
 for modulus in MODULI:
  matrix=rows(remaining,remaining_vertices,remaining_vi,modulus)
  for setting in SETTINGS[:2]:matrix+=rows(remaining,remaining_vertices,remaining_vi,modulus,setting)
  values.append(len(remaining)-rank_mod(matrix,modulus))
 key=f'shell_{removed[1]}_{removed[3]}_{removed[4]}'
 deletion_deficiencies[key]=values
checks['noncube_new_edges_do_not_restore_rank']=deletion_deficiencies['shell_2_1617_2695']==[1,1] and deletion_deficiencies['shell_3_1155_1617']==[1,1]
checks['cube_final_edge_uniquely_restores_rank_when_deleted']=deletion_deficiencies['shell_4_735_1155']==[0,0]
vertices,cube_edges=cube();max_grade=max(e[4] for e in cube_edges)
checks['boolean_four_cube_has_16_vertices_32_edges']=len(set(vertices.values()))==16 and len(cube_edges)==32
checks['cube_final_grade_8085']=max_grade==8085
checks['unique_latest_cube_edge']=[e for e in cube_edges if e[4]==max_grade]==[(7,4,735,1155,8085)]
text=PACKET.read_text();checks['characteristic_zero_boundary_retained']='Characteristic-zero proof' in text;checks['deletion_result_stated']='uniquely carries the new blind direction' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.grade-8085-four-cube-probe-depth.v1','packet_sha256':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'settings':[f'{a}/{b}' for a,b in SETTINGS],'checks':checks,'passed':all(checks.values()),'census':census,'cube':{'base':210,'vertices':vertices,'edges':cube_edges,'completion_grade':max_grade},'deletion_two_setting_deficiencies':deletion_deficiencies,'disposition':{'prediction':'two settings become deficient by one at four-cube completion; three restore full rank','status':'survives over two tested prime fields and edge-deletion localization','residual':'characteristic-zero proof and general cubical-dimension law'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'checks':len(checks),'8084_two_setting_deficiency':census['8084']['ranks'][0]['joint'][1]['deficiency'],'8085_two_setting_deficiency':census['8085']['ranks'][0]['joint'][1]['deficiency'],'8085_three_setting_deficiency':census['8085']['ranks'][0]['joint'][2]['deficiency']}));raise SystemExit(0 if result['passed'] else 1)
