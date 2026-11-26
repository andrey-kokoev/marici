"""Sound necessary compatibility test: use pair implications and simplify longer clique rectangles by forced colors. No branching. The caller compares predictions to exact SAT."""
import networkx as nx

def screen(cs):
 clauses=[set(c) for c in cs];fixed=set();rounds=0
 while True:
  rounds+=1;G=nx.DiGraph();G.add_nodes_from(i for i in range(-60,61) if i)
  for c in clauses:
   if not c:return 'rectangle',rounds,len(fixed)
   if len(c)>2:continue
   a=min(c);b=max(c);G.add_edge(-a,b);G.add_edge(-b,a)
  reach={v:nx.descendants(G,v) for v in G};forced={v for v in G if v in reach[-v]}
  if any(-v in forced for v in forced):return 'cycle',rounds,len(fixed)
  if not forced:return 'open',rounds,len(fixed)
  fixed|=forced;clauses=[{v for v in c if -v not in forced} for c in clauses if not c&forced]
