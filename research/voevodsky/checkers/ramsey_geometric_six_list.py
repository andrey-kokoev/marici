"""Construct six-address candidates from the address catalogue, not from a core. Order by number of eligible links (disjoint pairs). Skip groups already covered by a smaller Hall-deficient subset, including when adjoined to Q. Test each threshold under the smaller source rules."""
import json,z3
from itertools import combinations,permutations
from pathlib import Path
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(e):i for i,e in enumerate(src['edge_order'])};idx=[i for i,s in enumerate(S) if s!=66];q=S.index(60);v=[z3.Bool(f'x{i}') for i in range(len(E))];s=z3.SolverFor('QF_FD');bad=set();groups={}
for k in range(3,7):
 for J in combinations(idx,k):
  ls=[E[e] for e in combinations(J,2) if e in E];u=0
  for j in J:u|=S[j]
  if k==3 and len(ls)==3:s.add(z3.Or(*[~v[i] for i in ls]))
  if u.bit_count()>=k:continue
  m=sum(1<<j for j in J)
  if not any(m^(1<<j) in bad for j in J):s.add(z3.Or(*[v[i] for i in ls]))
  bad.add(m)
for J in combinations([i for i in idx if S[i] not in (60,65)],6):
 K=(*J,q);m=sum(1<<i for i in K)
 if any(sum(1<<j for j in sub) in bad for k in (5,6) for sub in combinations(K,k)):continue
 ls=[E[e] for e in combinations(J,2) if e in E];groups.setdefault(len(ls),[]).append((J,ls))
rows=[];acc=[]
for n,gs in sorted(groups.items()):
 if n==5:
  # Forget all address names. Two candidates have the same shape iff some permutation of their six vertices matches their eligible edges.
  types={}
  for J,ls in gs:
   edges=[(i,j) for i,j in combinations(range(6),2) if not S[J[i]]&S[J[j]]];shape=min(tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in edges)) for p in permutations(range(6)));types.setdefault(shape,[]).append((J,ls))
  shapes=list(sorted(types));print('shape counts',[len(types[h]) for h in shapes]);assert len(shapes)<10;subsets=[]
  for k in range(len(shapes)+1):
   for subset in combinations(range(len(shapes)),k):
    added=[x for t in subset for x in types[shapes[t]]];s.push();s.add([z3.Or(*[v[i] for i in ls]) for J,ls in added]);stats=[]
    for b in (0,1):
     s.push();s.add(v[4]==bool(b),v[74]!=bool(b));res=s.check();assert res in (z3.sat,z3.unsat);stats.append(str(res));s.pop()
    s.pop();subsets.append(dict(types=subset,status=stats,total=len(acc)+len(added),remaining=[sum(pin not in ls for J,ls in acc+added) for pin in (74,4)]))
  print('sufficient',sorted((x['total'],x['types'],x['remaining']) for x in subsets if x['status']==['unsat','unsat'])[:5]);(D/'results/ramsey_five_link_shapes.json').write_text(json.dumps(dict(shapes=shapes,counts=[len(types[h]) for h in shapes],subsets=subsets),indent=2)+'\n')
 if n==5:
  import sys
  ordered='--ordered-endpoints' in sys.argv;iso_out=[]
  for b,pin in enumerate((74,4)):
   ends=next(e for e,i in E.items() if i==pin);classes={}
   if ordered:
    ends=sorted(ends,key=lambda j:bool(S[j]&~S[q]));assert not S[ends[0]]&~S[q] and S[ends[1]]&~S[q]
   for J,ls in gs:
    if pin in ls:continue
    isolated,=[i for i in J if all(i==j or S[i]&S[j] for j in J)];overlap=[(S[isolated]&S[j]).bit_count() for j in ends];profile=tuple(overlap if ordered else sorted(overlap));classes.setdefault(profile,[]).append(ls)
   cases=[];base_count=sum(pin not in ls for J,ls in acc)
   for k in range(len(classes)+1):
    for use in combinations(sorted(classes),k):
     keep=[ls for p in use for ls in classes[p]];s.push();s.add(v[4]==bool(b),v[74]!=bool(b));s.add([z3.Or(*[v[i] for i in ls]) for ls in keep]);st=s.check();assert st in (z3.sat,z3.unsat);s.pop();cases.append(dict(use=use,tests=base_count+len(keep),status=str(st)))
   best=min(x['tests'] for x in cases if x['status']=='unsat');print('iso',b,{str(k):len(z) for k,z in classes.items()},[x for x in cases if x['tests']==best and x['status']=='unsat']);iso_out.append(dict(slot4=b,red=pin,counts={str(k):len(z) for k,z in classes.items()},base_count=base_count,cases=cases))
  (D/'results'/('ramsey_ordered_red_endpoints.json' if ordered else 'ramsey_isolated_red_spoke.json')).write_text(json.dumps(iso_out,indent=2)+'\n')
 acc.extend(gs);s.add([z3.Or(*[v[i] for i in ls]) for J,ls in gs]);tests=[]
 for b in (0,1):
  s.push();s.add(v[4]==bool(b),v[74]!=bool(b));res=s.check();tests.append(dict(status=str(res),remaining=sum((4 if b else 74) not in ls for J,ls in acc)));s.pop()
 rows.append(dict(max_links=n,total=len(acc),tests=tests));print(rows[-1]);
 if all(t['status']=='unsat' for t in tests):break
(D/'results/ramsey_geometric_six_list.json').write_text(json.dumps(rows,indent=2)+'\n')
