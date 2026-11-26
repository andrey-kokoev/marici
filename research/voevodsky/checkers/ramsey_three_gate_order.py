"""Add predecessor ORDER inequalities to the remaining body-diagonal search. For a label subset T, remove the 8-|T| excluded newcomers and their neighbors. All |T| other newcomers and core cells with masks contained in T remain, so those vertices form a (3,|T|+1) graph. Exact smaller thresholds bound the number of such cells, independently of their core red edges. Capacities 1,3,5,9,12,16,19 for t=1..7. Indicators are constrained only in the direction needed for upper bounds."""
import sys,itertools,collections,json,time,concurrent.futures as cf
from ramsey_cube_three_gate import P,subdata,encode,V,Solver,CardEnc
f=(0,1,7);caps=[0,1,3,5,9,12,16,19,26]
def strengthen(cs,E):
 fm,h,gs=subdata(f);top=max(abs(x) for c in cs for x in c);lits={};nc=0
 for t in range(255):
  k=t.bit_count();avail=[i for i,s in enumerate(h) if not s&~t];cap=caps[k];
  if len(avail)<=cap:continue
  js=[j for j,l in enumerate(f) if not t>>l&1];xs=[]
  if not js:assert len(avail)<=cap
  for i in avail:
   if len(js)==1:xs.append(-V(i,js[0]));continue
   key=(i,tuple(js))
   if key not in lits:top+=1;lits[key]=top;cs.append([top]+[V(i,j) for j in js])
   xs.append(lits[key])
  b=CardEnc.atmost(xs,cap,top_id=top);top=max(top,b.nv);cs+=b.clauses;nc+=1
 return nc

def work(arg):
 o,budget=arg;cs,E,gs,_=encode(f,5);n= strengthen(cs,E);cs.extend([[V(i,j)*(1 if s>>j&1 else -1)] for i,s in zip(gs[0],o) for j in range(3)]);t=time.perf_counter()
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  sl.conf_budget(budget);ok=sl.solve_limited();return dict(o=o,ok=ok,conflicts=sl.accum_stats()['conflicts'],seconds=time.perf_counter()-t,order_constraints=n)
if __name__=='__main__':
 budget=int(sys.argv[1]);src=json.loads((P/'ramsey_three_gate_5_120000.json').read_text());todo=[c['masks'] for z in src for c in z['cases'] if c['ok'] is None];out=[]
 with cf.ProcessPoolExecutor(3) as ex:
  for fut in cf.as_completed([ex.submit(work,(o,budget)) for o in todo]):out.append(fut.result());print(out[-1],flush=True);(P/f'ramsey_three_gate_order_{budget}.json').write_text(json.dumps(out)+'\n')
