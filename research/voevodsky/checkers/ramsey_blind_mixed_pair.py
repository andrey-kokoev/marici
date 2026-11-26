"""For the two exceptional cores, exhaust fixed panels with one exact reading per side. Evaluate each panel on every hidden chord, not just the discovery chord. Countermodels rule out many panels at once. Also evaluate a predeclared score-only selector: highest overlap on each side, include ties."""
import itertools,json,time
from pysat.solvers import Solver
from pysat.card import CardEnc
from pysat.formula import IDPool
from ramsey_retention_slice import D
P=D.parent;marks={r['core_index']:r for r in json.loads((P/'ramsey_attachment_rule_transfer.json').read_text()) if r['status']=='tested'};cores=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'];out=[]
import sys
for idx in ((7,) if {'--feedback','--log-audit'}.intersection(sys.argv) else sorted(marks) if '--structural' in sys.argv else (7,28)):
 a=cores[idx]['core'];z=marks[idx];old=list(map(set,z['red_supports']));C=range(16);J=range(6);E=list(itertools.product(*z['mark']));p=IDPool();V={(i,j):p.id((i,j)) for i in C for j in J};cs=[]
 for i in C:cs+=CardEnc.equals([V[i,j] for j in J],len(old[i]),vpool=p).clauses
 for j in J:cs+=CardEnc.equals([V[i,j] for i in C],5,vpool=p).clauses;cs.extend([[-V[i,j],-V[h,j]] for i,h in itertools.combinations(C,2) if a[i]>>h&1])
 gates={};spec={};inputs={}
 for side,ids,other in [('C',C,J),('J',J,C)]:
  gates[side]=[]
  for i,h in itertools.combinations(ids,2):
   if side=='C' and a[i]>>h&1:continue
   gate=p.id();pairs=[((i,j),(h,j)) if side=='C' else ((j,i),(j,h)) for j in other];ys=[];k=sum(v in old[u] and y in old[x] for (u,v),(x,y) in pairs)
   for f,b in pairs:
    y=p.id();u,v=V[f],V[b];cs.extend([[-y,u],[-y,v],[y,-u,-v]]);ys.append(y)
   cs.extend([[-gate,*cl] for cl in CardEnc.equals(ys,k,vpool=p).clauses]);gates[side].append(gate);spec[gate]=[side,i,h,k];inputs[gate]=ys
 if '--structural' in sys.argv:
  from ramsey_structural_panel import run
  out.append(run(idx,E,V,cs,spec,P,z));(P/('ramsey_panel_feedback.json' if '--feedback' in sys.argv else 'ramsey_panel_log_audit.json' if '--log-audit' in sys.argv else 'ramsey_pair_score_panel.json' if '--pair-score' in sys.argv else 'ramsey_expanded_panel.json' if '--expand' in sys.argv else 'ramsey_structural_panel.json')).write_text(json.dumps(out)+'\n');continue
 if '--minimum-two' in sys.argv:
  from ramsey_minimum_panel import run
  out.append(run(idx,E,V,cs,spec,inputs,erasures=2));(P/'ramsey_minimum_two_panel.json').write_text(json.dumps(out)+'\n');continue
 if '--two' in sys.argv:
  from ramsey_two_erasure import run
  out.append(run(idx,E,V,cs,spec,inputs,P,z));(P/'ramsey_two_erasure.json').write_text(json.dumps(out)+'\n');continue
 if '--minimum' in sys.argv:
  from ramsey_minimum_panel import run
  out.append(run(idx,E,V,cs,spec,inputs));(P/'ramsey_minimum_panel.json').write_text(json.dumps(out)+'\n');continue
 panels=list(itertools.product(*gates.values()));scores=dict.fromkeys(panels,0);top=[t for gs in gates.values() for t in gs if spec[t][-1]==max(spec[v][-1] for v in gs)];topforced=[]
 with Solver(name='g4',bootstrap_with=cs) as s:
  for e in E:
   obs=[V[e]]+[-V[f] for f in E if f!=e];todo=set(panels)
   if not s.solve(assumptions=obs+top):topforced.append(e)
   while todo:
    pair=next(iter(todo));
    if not s.solve(assumptions=obs+list(pair)):scores[pair]+=1;todo.remove(pair);continue
    pos=set(s.get_model());match={v for v,ys in inputs.items() if sum(i in pos for i in ys)==spec[v][-1]};todo.difference_update(itertools.product((v for v in gates['C'] if v in match),(v for v in gates['J'] if v in match)))
 best=max(scores.values());examples=[k for k,v in scores.items() if v==best];rec=dict(core=idx,panels=len(scores),best=best,tied=len(examples),example=[spec[v] for v in examples[0]],highest_count_panel=len(top),highest_count_forced=topforced);out.append(rec);print(rec,flush=True)
if not {'--minimum','--two','--minimum-two','--structural'}.intersection(sys.argv):(P/'ramsey_blind_mixed_pair.json').write_text(json.dumps(out,indent=1)+'\n')
