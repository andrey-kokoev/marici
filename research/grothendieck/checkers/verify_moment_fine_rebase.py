"""Rebase checker. Predecessor head must already be independently verified.
Shares the established source/master and compaction kernels, not the producer.
"""
from fractions import Fraction as Q
import json,hashlib
from verify_active_cap_moment_master import block,admitted,verify
from moment_column_checkpoints import encode,verify_compaction
if not __debug__:raise RuntimeError('Assertions required')
def digest(x):return hashlib.sha256(encode(x)).hexdigest()
def data(state):
 assert set(state)<= {'intervals','objective','frames','local_frames','point','fine_edges'}
 B=len(state['intervals']);assert B and len(state['objective'])==4
 assert all(len(f['normal'])==4 for f in state['frames']+state.get('local_frames',[]))
 fine=state.get('fine_edges',[]);assert all(type(e['block'])==int and 0<=e['block']<B for e in fine)
 return [block(interval,[e for e in fine if e['block']==b]) for b,interval in enumerate(state['intervals'])]
def successor(before,operation):
 after=json.loads(encode(before));after.setdefault('fine_edges',[]).append(json.loads(encode(operation)));data(after);return after

def summary(answer):return {k:answer[k] for k in ('status','value','source_lift','block_lifts','separator') if k in answer}
def from_answer(state,answer,compaction,seeds=None):
 data(state);verify(state,answer,seeds);columns=verify_compaction(state,answer,compaction);bounds=[]
 for price in answer['trace'][-1]['pricing']:
  c=price['certificate'];bounds.append({'objective':price['objective'],'flow':c['flow'],'upper':c['value'],'witness':c['potential']})
 return {'state':state,'result':summary(answer),'columns':columns,'weights':[p['weight'] for p in compaction],'bounds':bounds}

def flow_check(source,bound):
 ids,s,edges=source;a=tuple(map(Q,bound['objective']));assert len(a)==4
 q=tuple(s[i]*(a[0]*int(i==0)+a[1]*int(i==len(ids)-1)+a[2]+a[3]*Q(1,128**j)) for i,j in enumerate(ids))
 f=tuple(map(Q,bound['flow']));assert len(f)==len(edges) and all(v>=0 for v in f);normal=[Q(0)]*(len(ids)+1)
 for weight,(u,v,w) in zip(f,edges):normal[v]+=weight;normal[u]-=weight
 assert tuple(normal)==(-sum(q),*q) and sum(weight*w for weight,(u,v,w) in zip(f,edges))==Q(bound['upper'])
 if bound['witness'] is not None:
  p=tuple(map(Q,bound['witness']));assert len(p)==len(ids)+1 and p[0]==0;admitted(source,p[1:],True)
  assert sum(a*b for a,b in zip(q,p[1:]))==Q(bound['upper'])
 return q

def mixed_result(state,columns,weights,value):
 sources=data(state);weights=tuple(map(Q,weights));assert len(weights)==len(columns) and all(v>0 for v in weights);lifts=[]
 for b,source in enumerate(sources):
  chosen=[(tuple(map(Q,c['potential'])),w) for c,w in zip(columns,weights) if c['block']==b];assert sum(w for z,w in chosen)==1
  for z,w in chosen:admitted(source,z,True)
  z=tuple(sum(w*z[i] for z,w in chosen) for i in range(len(source[0])));lifts.append(admitted(source,z))
 assert all(lifts[b][-1]==lifts[b+1][0] for b in range(len(lifts)-1))
 glued=lifts[0]+tuple(v for t in lifts[1:] for v in t[1:]);ids=range(state['intervals'][0][0],state['intervals'][-1][1]+1)
 observed=(glued[0],glued[-1],sum(glued),sum(Q(1,128**j)*v for j,v in zip(ids,glued)))
 assert sum(Q(a)*v for a,v in zip(state['objective'],observed))==Q(value)
 if 'point' in state:assert observed==tuple(map(Q,state['point']))
 assert all(sum(Q(a)*v for a,v in zip(f['normal'],observed))<=Q(f['upper']) for f in state['frames'])
 for f in state.get('local_frames',[]):
  b=f['block'];t=lifts[b];local=(t[0],t[-1],sum(t),sum(Q(1,128**j)*v for j,v in zip(sources[b][0],t)))
  assert sum(Q(a)*v for a,v in zip(f['normal'],local))<=Q(f['upper'])
 return {'status':'OPTIMUM','value':str(Q(value)),'source_lift':list(map(str,glued)),'block_lifts':[list(map(str,t)) for t in lifts]}

def verify_rebase(head,operation,packet):
 before=head['state'];after=successor(before,operation);old=data(before);new=data(after);B=len(new)
 assert packet['before_digest']==digest(head) and packet['after_digest']==digest(after) and packet['operation']==operation
 assert len(packet['column_status'])==len(head['columns']);kept=[]
 for i,(column,label) in enumerate(zip(head['columns'],packet['column_status'])):
  b=column['block'];z=tuple(map(Q,column['potential']));admitted(old[b],z,True);p=(Q(0),*z)
  assert new[b][0:2]==old[b][0:2] and new[b][2][:len(old[b][2])]==old[b][2]
  survives=all(p[v]-p[u]<=w for u,v,w in new[b][2][len(old[b][2]):]);assert label==('KEEP' if survives else 'DROP')
  if survives:kept.append(column)
 assert len(packet['bounds'])==len(head['bounds'])==B
 for b,(prior,current) in enumerate(zip(head['bounds'],packet['bounds'])):
  flow_check(old[b],prior);assert current['objective']==prior['objective'] and Q(current['upper'])==Q(prior['upper'])
  assert tuple(map(Q,current['flow']))==tuple(map(Q,prior['flow']))+(Q(0),)*(len(new[b][2])-len(old[b][2]));flow_check(new[b],current)
  if current['witness'] is not None:
   allowed=[prior['witness']]+[['0']+c['potential'] for c in kept if c['block']==b]
   assert current['witness'] in allowed
 mode=packet['mode']
 if mode=='RETAINED_OPTIMUM':
  assert head['result']['status']=='OPTIMUM' and kept==head['columns']
  result=mixed_result(after,kept,head['weights'],head['result']['value']);assert packet['result']==result
  return {'state':after,'result':result,'columns':kept,'weights':head['weights'],'bounds':packet['bounds']}
 if mode=='INHERITED_INCONSISTENCY':
  assert head['result']['status']=='INCONSISTENT' and packet['result']=={'status':'INCONSISTENT'}
  return {'state':after,'result':packet['result'],'columns':kept,'weights':None,'bounds':packet['bounds']}
 assert head['result']['status']=='OPTIMUM' and len(kept)<len(head['columns'])
 if mode=='LOCAL_NEGATIVE_CYCLE':
  b=packet['empty_block'];assert type(b)==int and b==operation['block'];edges=new[b][2];cycle=packet['cycle_edges'];assert cycle and all(type(i)==int and 0<=i<len(edges) for i in cycle)
  assert all(edges[cycle[i]][1]==edges[cycle[(i+1)%len(cycle)]][0] for i in range(len(cycle))) and sum(edges[i][2] for i in cycle)<0
  return {'state':after,'result':{'status':'INCONSISTENT'},'columns':kept,'weights':None,'bounds':packet['bounds']}
 assert mode=='REPAIRED';seeds=list(kept);missing=[b for b in range(B) if not any(c['block']==b for c in kept)]
 assert [r['block'] for r in packet['reseed']]==missing
 for r in packet['reseed']:
  c=r['certificate'];assert c['status']=='OPTIMUM';source=new[r['block']]
  flow_check(source,{'objective':['0']*4,'flow':c['flow'],'upper':c['value'],'witness':c['potential']});assert Q(c['value'])==0
  seeds.append({'block':r['block'],'potential':c['potential'][1:]})
 assert seeds==packet['seeds']
 return from_answer(after,packet['answer'],packet['compact'],seeds)

def closure_potential(state):
 # Proof/control metric only; the runtime rebase does not compute closures.
 total=0
 for ids,s,edges in data(state):
  n=len(ids)+1;d=[[Q(0) if i==j else None for j in range(n)] for i in range(n)]
  for u,v,w in edges:d[u][v]=w if d[u][v] is None else min(d[u][v],w)
  for k in range(n):
   for i in range(n):
    for j in range(n):
     if d[i][k] is not None and d[k][j] is not None:
      value=d[i][k]+d[k][j]
      if d[i][j] is None or value<d[i][j]:d[i][j]=value
  if any(d[i][i]<0 for i in range(n)):return None
  caps=[Q(0)]+[Q(100+2*j)/scale for j,scale in zip(ids,s)]
  for u in range(n):
   for v in range(n):
    assert d[u][v] is not None and -caps[u]<=d[u][v]<=caps[v]
    if u!=v:
     term=6*(d[u][v]+caps[u]);assert term.denominator==1 and term>=0;total+=int(term)
 return total

def main():
 from pathlib import Path
 path=Path(__file__).resolve().parent.parent/'results/moment-fine-rebase.json';report=json.loads(path.read_bytes())
 for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
 initial={'intervals':[[0,3],[3,7]],'objective':['0','0','1','0'],'frames':[]};assert report['initial']['state']==initial
 initial_head=from_answer(initial,report['initial']['answer'],report['initial']['compact']);head=initial_head
 expected=[(0,0,'1'),(0,0,'1/2'),(0,3,'10'),(1,7,'7/2'),(1,7,'3'),(0,0,'1/3')];assert len(report['records'])==len(expected)
 for (b,j,upper),record in zip(expected,report['records']):
  op={'block':b,'tail':None,'head':j,'upper':upper};assert record['operation']==op;potential=closure_potential(head['state']);head=verify_rebase(head,op,record['candidate']);new_potential=closure_potential(head['state'])
  assert record['closure_potential']==[potential,new_potential] and new_potential<=potential
  if record['candidate']['mode']=='REPAIRED':assert new_potential<potential
  if record['cold'] is not None:
   verify(head['state'],record['cold']);assert record['cold']['status']==head['result']['status']
   if head['result']['status']=='OPTIMUM':assert record['cold']['value']==head['result']['value']
 empty=report['local_empty'];assert empty['operation']=={'block':0,'tail':None,'head':0,'upper':'-1'}
 assert verify_rebase(initial_head,empty['operation'],empty['candidate'])['result']['status']=='INCONSISTENT'
 remote=report['remote'];state={'intervals':[[0,3],[3,7],[7,11],[11,15]],'objective':['0','0','1','0'],'frames':[]};assert remote['state']==state
 before=from_answer(state,remote['answer'],remote['compact']);assert remote['operation']=={'block':3,'tail':None,'head':15,'upper':'15/2'}
 after=verify_rebase(before,remote['operation'],remote['candidate']);new=tuple(map(Q,after['result']['source_lift']));old=tuple(map(Q,before['result']['source_lift']))
 assert new==tuple(Q(1+j%3)*Q(j,2) for j in range(16)) and all(a>b for a,b in zip(old,new))
 generated={e['added']['block'] for e in remote['candidate']['answer']['trace'] if 'added' in e};assert generated=={0,1,2,3}
 assert all(Q(c['potential'][0])==1 for c in before['columns'] if c['block']==0)
 coupled=report['coupled'];raw=tuple(map(Q,initial_head['result']['source_lift']));budget=sum((1+Q(1,128**j))*(v+Q(1+j%3)*Q(j,2))/2 for j,v in enumerate(raw))
 state={**initial,'frames':[{'normal':['1','0','0','0'],'upper':'1/2'},{'normal':['0','0','1','1'],'upper':str(budget)}]};assert coupled['state']==state and coupled['operation']=={'block':1,'tail':None,'head':5,'upper':'15'}
 before=from_answer(state,coupled['answer'],coupled['compact']);after=verify_rebase(before,coupled['operation'],coupled['candidate']);verify(after['state'],coupled['cold'])
 assert Q(after['result']['value'])<Q(before['result']['value']) and after['result']['value']==coupled['cold']['value']
 for h in (before,after):assert sum((1+Q(1,128**j))*Q(v) for j,v in enumerate(h['result']['source_lift']))==budget
 assert any(t.get('added',{}).get('block')==0 for t in coupled['candidate']['answer']['trace'])
 pairs=[tuple(map(Q,t)) for t in coupled['same_observation_fiber_pair']];assert len(pairs)==2;observations=[];local_observations=[];whole=block([0,7])
 for raw in pairs:
  assert len(raw)==8;admitted(whole,tuple(v/s for v,s in zip(raw,whole[1])))
  observed=(raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*v for j,v in enumerate(raw)));observations.append(observed)
  assert observed[0]<=Q(1,2) and observed[2]+observed[3]<=budget
  local_observations.append((raw[3],raw[7],sum(raw[3:]),sum(Q(1,128**j)*raw[j] for j in range(3,8))))
 assert observations[0]==observations[1] and local_observations[0]==local_observations[1] and pairs[0][5]>45>pairs[1][5]
 replacement=report['replacement'];assert replacement['operation']=={'block':0,'tail':3,'head':None,'upper':'-71/2'}
 repaired=verify_rebase(initial_head,replacement['operation'],replacement['candidate']);assert repaired['result']['value']==initial_head['result']['value'] and replacement['candidate']['mode']=='REPAIRED'
 assert Q(initial_head['bounds'][0]['witness'][-1])<Q(71,2)
 assert replacement['candidate']['bounds'][0]['witness'] is not None and replacement['candidate']['bounds'][0]['witness']!=initial_head['bounds'][0]['witness']
 print('PASS: six semantic rebases, local negative cycle, nonlocal regeneration, active moment-frame repair, hidden-fiber distinction and replacement attainment; authorization is tested separately')

if __name__=='__main__':main()
