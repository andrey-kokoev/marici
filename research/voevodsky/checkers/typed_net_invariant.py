"""Import-safe diagnostic invariant for the restricted tagged copier/query net."""
from check_port_multigraph_forest import forest

def validate(net):
 def need(ok,clause):
  if not ok:raise ValueError(clause)
 def kind(n):
  if n in ('OUT1','OUT2'):return 'OUT'
  if n.startswith(('Q1','Q2')):return 'Q'+n[2:].split('_')[0]
  return n.split('_')[0]
 def peer(n,p):return net.wires[n+'.'+p].split('.')
 arities={'OUT':{'p'},'TRUE':{'p'},'FALSE':{'p'},'N':{'p'},'E':{'p'},'B0':{'p','a'},'B1':{'p','a'},'K':{'p','a'},'COPY':{'p','a','b'},'QB':{'p','a','r'},'QS':{'p','a','r'},'QR':{'p','r'}}
 try:
  for n,ports in net.types.items():need(kind(n) in arities and len(ports)==len(set(ports)) and set(ports)==arities[kind(n)],'arity')
  need(forest(net),'forest')
  need({n for n in net.types if kind(n)=='OUT'}=={'OUT1','OUT2'},'outputs')
  copies=[n for n in net.types if kind(n)=='COPY'];need(len(copies)<=1,'copy-count')
  data={n for n in net.types if kind(n) in ('B0','B1','K','N')}
  need(set(net.tags)==data and set(net.tags.values())<= {'ORIGINAL','COPIED'},'tags')
  live=[n for n in net.origin if n in net.types]
  need({n for n in data if net.tags[n]=='ORIGINAL'}==set(live),'origin-tags')
  need(live==list(net.origin)[len(net.origin)-len(live):] if live else True,'origin-suffix')
  need(bool(live)==bool(copies),'origin-copy')
  if copies:need(peer(copies[0],'p')==[live[0],'p'],'origin-head')
  for a,b in zip(live,live[1:]):need(kind(a) in ('B0','B1') and peer(a,'a')==[b,'p'],'origin-chain')
  if live:need(kind(live[-1])=='N','origin-end')
  for i in (1,2):
   qs=[n for n in net.types if n.startswith('Q'+str(i))];need(len(qs)<=1,'query-count')
   n,p=peer('OUT'+str(i),'p');need((kind(n) in ('TRUE','FALSE') and p=='p') or (n in qs and p=='r'),'output-peer')
  def tail_port(n,p,types,wait=False):
   other,port=peer(n,p)
   need((kind(other) in types and port=='p' and net.tags.get(other)=='COPIED') or (wait and kind(other)=='COPY' and port in ('a','b')),'tail-port')
  for n in net.types:
   k=kind(n)
   if k.startswith('Q'):
    need(peer(n,'r')==['OUT'+n[1],'p'],'query-output')
    tail_port(n,'p',('K','N') if k=='QB' else ('B0','B1','N'),k!='QB')
    if k!='QR':tail_port(n,'a',('B0','B1','N') if k=='QB' else ('K','N'),k=='QB')
   elif k=='E':tail_port(n,'p',('B0','B1','K','N'),True)
   elif k in ('B0','B1','K') and net.tags[n]=='COPIED':tail_port(n,'a',('K','N') if k=='K' else ('B0','B1','N'),k!='K')
   elif k=='COPY':
    for p in ('a','b'):
     other,port=peer(n,p);need((kind(other),port) in {('QB','a'),('QS','p'),('QR','p'),('E','p'),('B0','a'),('B1','a')},'copy-peer')
  adj={n:set() for n in net.types}
  for p,q in net.wires.items():
   a=p.split('.')[0];b=q.split('.')[0];adj[a].add(b)
  def component(start,cut=None):
   seen=set();queue=[start]
   while queue:
    n=queue.pop()
    if n==cut or n in seen:continue
    seen.add(n);queue.extend(adj[n]-seen)
   return seen
  def rooted(c):return any(kind(n) in ('OUT','E') for n in c)
  unseen=set(adj)
  while unseen:
   c=component(next(iter(unseen)));need(rooted(c),'root');unseen-=c
  if copies:
   copy=copies[0];sides=[component(peer(copy,p)[0],copy) for p in ('a','b')]
   need(all(rooted(s) for s in sides) and sides[0].isdisjoint(sides[1]),'branch-anchors')
   need(component(live[0],copy)==set(live),'source-component')
 except (ValueError,AssertionError,KeyError,IndexError) as exc:return str(exc) or 'wiring'
 return None
