"""Compile singleton and pair-born blue defects into repair implications, then predict all larger disjoint coalitions without enumerating their defects. Check predicted outputs independently."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,sevens,apply
from ramsey_closed_repair_conjecture import disjoint_collections
D=Path(__file__).parent;data=json.loads((D/'ramsey_hall_center_conjecture.json').read_text());report=[]
for record in data['regular']:
 A=decode(record['graph6'].encode());moves=list(switches(A));edge_repairers={}
 for i,s in enumerate(moves):
  for e in s['added']:
   e=tuple(sorted(e));edge_repairers[e]=edge_repairers.get(e,0)|(1<<i)
 rules={};stats=Counter()
 def compile_rules(birth,defects):
  union=0
  for i in birth:union|=moves[i]['support']
  compatible=sum(1<<j for j,s in enumerate(moves) if not s['support']&union);heads=set()
  for I in defects:
   repairers=0
   for edge in combinations([v for v in range(22) if I>>v&1],2):repairers|=edge_repairers.get(edge,0)
   heads.add(repairers&compatible)
  minimal=sorted(h for h in heads if not any(g!=h and g&h==g for g in heads));rules[birth]=minimal;stats[f'arity{len(birth)}_rules']+=len(minimal)
 for i,s in enumerate(moves):compile_rules((i,),s['bad'])
 for i,j in disjoint_collections(moves,2):
  B=apply(apply(A,moves[i]['removed'],moves[i]['added']),moves[j]['removed'],moves[j]['added']);emergent=set(sevens(B))-set(moves[i]['bad'])-set(moves[j]['bad']);compile_rules((i,j),emergent)
 predicted=Counter();false_positive=[];examples={}
 for size in range(1,6):
  for selected in disjoint_collections(moves,size):
   stats['coalitions_tested']+=1;mask=sum(1<<i for i in selected)
   if not all(all(head&mask for head in rules[birth]) for arity in (1,2) for birth in combinations(selected,arity)):continue
   predicted[size]+=1;B=A[:]
   for i in selected:B=apply(B,moves[i]['removed'],moves[i]['added'])
   bad=list(sevens(B))
   if bad:false_positive.append({'selected':selected,'unpredicted_defects':bad})
   examples.setdefault(size,selected)
 result={'source':record['record'],'stats':dict(stats),'predicted_nonempty_models':dict(predicted),'false_positives':false_positive,'examples':examples,'switches':moves,'rules':[{'birth':birth,'repairer_masks':heads} for birth,heads in rules.items() if heads]};report.append(result);print({k:v for k,v in result.items() if k not in ('switches','rules')})
(D/'ramsey_block_selection_repair_rules.json').write_text(json.dumps(report,indent=2)+'\n')
