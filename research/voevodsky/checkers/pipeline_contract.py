"""Public/private stream partition and global data/producer coverage audit.
Compiler stage declarations are checked; allocator state is a separate premise.
"""
from check_port_multigraph_forest import forest

def validate(net):
 assert isinstance(net.stage_ops,tuple),'stage declarations'
 assert all(op in ('add','member','union') for op in net.stage_ops),'stage operation'
 assert set(net.stage)==set(net.types),'stage coverage'
 arities={k:set(ps) for k,ps in {'RET':'p','OUT':'p','N':'p','TRUE':'p','FALSE':'p','E':'p','B0':'pa','B1':'pa','K':'pa','COPY':'pab','QB':'par','QS':'par','QR':'pr','AB':'par','AS':'par','AR':'pr','UL':'par','U0':'par','U1':'par'}.items()}
 groups=[[] for op in net.stage_ops]
 permitted={'add':{'AB','AS','AR'},'member':{'COPY','QB','QS','QR','E'},'union':{'UL','U0','U1'}}
 all_controls=set().union(*permitted.values())
 for n,ports in net.types.items():
  k=net.kind(n);t=net.stage[n]
  assert k in arities and len(ports)==len(set(ports)) and set(ports)==arities[k],'arity'
  assert type(t) is int and -1<=t<len(net.stage_ops),'stage bounds'
  if k in all_controls:
   assert t>=0 and k in permitted[net.stage_ops[t]],'stage control'
   groups[t].append(k)
  if k in ('OUT','TRUE','FALSE'):
   assert t>=0 and net.stage_ops[t]=='member','result declaration'
 assert {n for n in net.types if net.kind(n)=='RET'}=={'RET'} and net.stage['RET']==-1,'RET boundary'
 for op,ks in zip(net.stage_ops,groups):
  if op=='member':
   assert ks.count('COPY')<=1 and sum(k in ('QB','QS','QR') for k in ks)<=1,'member cardinality'
  else:assert len(ks)<=1,'stage cardinality'
 assert len(net.outputs)==len(set(net.outputs)),'output duplication'
 assert [net.stage[o] for o in net.outputs]==[i for i,op in enumerate(net.stage_ops) if op=='member'],'declared outputs'
 assert forest(net),'forest'
 data=set();frontiers=set();bools=set()
 public={('COPY','a'),('AB','r'),('AS','r'),('AR','r'),('UL','r'),('U0','r'),('U1','r')}
 def walk(port,mode,t):
  while True:
   n,p=port.split('.');k=net.kind(n);s=net.stage[n]
   if p!='p':
    assert port not in frontiers,'duplicate frontier'
    if mode=='P':assert k=='COPY' and p=='b' and s==t,'private frontier'
    else:
     assert mode in ('S','A') and (k,p) in public,'public frontier'
     assert s<=t if mode=='S' else s<t,'frontier ceiling'
    frontiers.add(port);return
   assert n not in data,'duplicate data'
   assert k in ({'K','N'} if mode=='K' else {'B0','B1','N'}),'stream type'
   assert s==t if mode in ('P','K','L') else s<=t,'data ceiling'
   data.add(n)
   if k=='N':return
   port=net.wires[n+'.a']
 def input(n,p,mode,t):walk(net.wires[n+'.'+p],mode,t)
 controls={'COPY','QB','QS','QR','E','AB','AS','AR','UL','U0','U1'}
 for n in net.types:
  k=net.kind(n);t=net.stage[n]
  if k=='COPY':input(n,'p','S',t-1)
  elif k in ('QB','AB'):
   input(n,'p','K',t);input(n,'a','P' if k=='QB' else 'A',t)
  elif k in ('QS','AS'):
   input(n,'p','P' if k=='QS' else 'A',t);input(n,'a','K',t)
  elif k in ('QR','AR'):input(n,'p','P' if k=='QR' else 'A',t)
  elif k=='UL':input(n,'p','S',t-1);input(n,'a','L',t)
  elif k in ('U0','U1'):input(n,'p','L',t);input(n,'a','S',t-1)
  elif k=='E':
   peer=net.wires[n+'.p'].split('.')[0]
   input(n,'p','K' if net.kind(peer)=='K' else 'P',t)
  elif k not in ('B0','B1','K','N','TRUE','FALSE','OUT','RET'):raise AssertionError('unknown kind')
  if k in ('QB','QS','QR'):
   out,p=net.wires[n+'.r'].split('.')
   assert out in net.outputs and p=='p' and net.stage[out]==t,'query result'
 for out in net.outputs:
  n,p=net.wires[out+'.p'].split('.');k=net.kind(n)
  assert net.stage[n]==net.stage[out],'output stage'
  if k in ('TRUE','FALSE'):assert p=='p';bools.add(n)
  else:assert k in ('QB','QS','QR') and p=='r'
 input('RET','p','S',len(net.stage_ops)-1)
 assert data=={n for n in net.types if net.kind(n) in ('B0','B1','K','N')},'data coverage'
 expected={n+'.'+p for n in net.types for p in net.types[n] if (net.kind(n),p) in public or (net.kind(n),p)==('COPY','b')}
 assert frontiers==expected,'producer coverage'
 assert bools=={n for n in net.types if net.kind(n) in ('TRUE','FALSE')},'boolean coverage'
 assert set(net.outputs)=={n for n in net.types if net.kind(n)=='OUT'},'output coverage'
 return True
