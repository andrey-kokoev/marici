"""Test closure of ALL proper partial repair obligations, not only singleton defects. Initially triples from both Hall types; size configurable up to five."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,argparse
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,apply,sevens

def hit(mask,edges):return any(mask>>a&1 and mask>>b&1 for a,b in edges)
def disjoint_collections(moves,k,start=0,used=0,chosen=()):
 if not k:yield chosen;return
 for i in range(start,len(moves)-k+1):
  if not moves[i]['support']&used:yield from disjoint_collections(moves,k-1,i+1,used|moves[i]['support'],chosen+(i,))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--size',type=int,default=3,choices=(2,3,4,5));parser.add_argument('--all-regular',action='store_true');parser.add_argument('--all-extremal',action='store_true');args=parser.parse_args();data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());report=[]
 records=data['regular']
 if args.all_extremal:
  lines=(Path(__file__).with_name('pauli-realization-catalogues')/'r37_22.g6').read_bytes().splitlines();records=[{'record':i,'graph6':line.decode()} for i,line in enumerate(lines,1)]
 for record in records:
  if not (args.all_regular or args.all_extremal) and record['record'] not in (190,191):continue
  A=decode(record['graph6'].encode());moves=list(switches(A));stats=Counter();counterexample=None;valid_example=None;cache={(i,):s['bad'] for i,s in enumerate(moves)}
  def graph(ids):
   B=A[:]
   for i in ids:B=apply(B,moves[i]['removed'],moves[i]['added'])
   return B
  def defects(ids):
   if ids not in cache:cache[ids]=list(sevens(graph(ids)))
   return cache[ids]
  for ids in disjoint_collections(moves,args.size):
   stats['disjoint_collections']+=1;closed=True
   for size in range(1,args.size):
    for subset in combinations(ids,size):
     remaining=[e for i in ids if i not in subset for e in moves[i]['added']]
     if not all(hit(mask,remaining) for mask in defects(subset)):closed=False;break
    if not closed:break
    stats[f'closed_through_subset_size_{size}']+=1
   if not closed:continue
   stats['closed_collections']+=1;bad=defects(ids)
   if not bad:
    stats['valid_closed_collections']+=1
    if valid_example is None:
     valid_example={'switches':[moves[i] for i in ids],'proper_subset_counts':[{'subset':[ids.index(i) for i in subset],'independent_sevens':len(defects(subset))} for size in range(1,args.size) for subset in combinations(ids,size)],'output_adjacency':graph(ids)}
    continue
   stats['counterexamples']+=1
   if counterexample is None:
    evidence=[]
    for size in range(1,args.size):
     for subset in combinations(ids,size):evidence.append({'subset':[ids.index(i) for i in subset],'independent_sevens':defects(subset)})
    assert all(not(set(row['independent_sevens'])&set(bad)) for row in evidence)
    counterexample={'switches':[moves[i] for i in ids],'proper_subset_evidence':evidence,'full_only_obstructions':[[v for v in range(22) if mask>>v&1] for mask in bad]}
  result={'source':record['record'],'size':args.size,'stats':dict(stats),'first_counterexample':counterexample,'first_valid_example':valid_example};report.append(result);print({k:v for k,v in result.items() if k not in ('first_counterexample','first_valid_example')},flush=True)
 Path(__file__).with_name(f'ramsey_closed_repair_{"all_extremal_" if args.all_extremal else "all_regular_" if args.all_regular else ""}size{args.size}.json').write_text(json.dumps(report,indent=2)+'\n')
