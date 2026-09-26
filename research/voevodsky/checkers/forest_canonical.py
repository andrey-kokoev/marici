"""Exact port-labelled finite forest encoding, independent of allocation names."""
from check_port_multigraph_forest import forest

def canonical(net, tagged=False):
 if not forest(net):raise ValueError('requires port multigraph forest')
 def kind(n):
  parts=n.rsplit('_',1)
  return parts[0] if len(parts)==2 and parts[1].isdigit() else n
 def encode(n,parent=None):
  edges=[]
  for p in sorted(net.types[n]):
   other,q=net.wires[n+'.'+p].split('.')
   if other!=parent:edges.append((p,q,encode(other,n)))
  return (kind(n),net.tags.get(n,'') if tagged else '',tuple(edges))
 unseen=set(net.types);components=[]
 while unseen:
  start=next(iter(unseen));nodes=set();queue=[start]
  while queue:
   n=queue.pop()
   if n in nodes:continue
   nodes.add(n)
   queue.extend(net.wires[n+'.'+p].split('.')[0] for p in net.types[n])
  unseen-=nodes
  components.append(min(encode(n) for n in nodes))
 return tuple(sorted(components))
