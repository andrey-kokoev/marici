"""Independent expected statements and arithmetic replay; no producer import."""
from pathlib import Path
from fractions import Fraction as Q
import json,copy
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def expected(m_values=(3,4)):
 for m in m_values:
  states=[]
  for A,fs in [([], [(['1','0'],'5')]),([0,m-1],[(['1','0','0','0'],'5')]),
   ([0,m-1],[(['1','0','0','0'],'5'),(['0','0','-1','0'],'-2'),(['1','0','0','1'],'6')]),
   ([0,m-1],[(['1','0','0','0'],'5'),(['0','0','-1','0'],'-2'),(['1','0','0','1'],'6'),(['0','0','1','0'],'1')])]:
   states.append({'m':m,'audits':A,'frames':[{'a':a,'b':b} for a,b in fs],'source':'tail-box-100+2j-128^-j-v1'})
  for s in states:
   for prefix in (['1','0'],['0','1']):yield s,{'kind':'maximize','objective':prefix+['0']*len(s['audits'])}
  yield states[2],{'kind':'maximize','objective':['0','0','1','-1']}
  for p in (['3','257/128','2','0'],['0','0','0','0']):yield states[2],{'kind':'membership','point':p}
def check(s,q,p):
 assert p['state']==s and p['query']==q
 m=s['m'];basis=[[Q(1)]*m,[Q(1,128**j) for j in range(m)]]
 basis += [[Q(int(j==i)) for j in range(m)] for i in s['audits']]
 def translate(a):return [sum(Q(c)*row[j] for c,row in zip(a,basis)) for j in range(m)]
 rows=[]
 for j in range(m):
  row=[Q(int(k==j)) for k in range(m)];rows += [(row,Q(100+2*j)),([-v for v in row],Q(0))]
 rows += [(translate(f['a']),Q(f['b'])) for f in s['frames']]
 if q['kind']=='membership':
  for row,v in zip(basis,map(Q,q['point'])):rows += [(row,v),([-a for a in row],-v)]
  obj=[Q(0)]*m
 else:obj=translate(q['objective'])
 weights=p['weights'];assert len({i for i,v in weights})==len(weights)
 assert all(type(i) is int and 0<=i<len(rows) and Q(v)>=0 for i,v in weights)
 normal=[sum(Q(v)*rows[i][0][j] for i,v in weights) for j in range(m)]
 bound=sum(Q(v)*rows[i][1] for i,v in weights)
 if p['status']=='EMPTY':assert normal==[0]*m and bound<0
 else:
  assert p['status']=='FEASIBLE_OPTIMUM';x=list(map(Q,p['x']));assert len(x)==m
  assert all(sum(a*b for a,b in zip(row,x))<=rhs for row,rhs in rows)
  assert normal==obj and bound==Q(p['value'])==sum(a*b for a,b in zip(obj,x))
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'schema-relative-tail-lp.json').read_text())['packets'];contexts=list(expected());assert len(packets)==len(contexts)==22
 for (s,q),p in zip(contexts,packets):check(s,q,p)
 # Independently known feasibility status, including point-relative emptiness.
 for k,p in enumerate(packets):assert (p['status']=='EMPTY')==(k%11 in (6,7,10))
 attacks=[]
 for field in ('state','query','x','weights'):
  p=copy.deepcopy(packets[4]);s,q=contexts[4]
  if field=='state':p['state']['frames'].pop()
  elif field=='query':p['query']['objective'][0]='2'
  elif field=='x':p['x'][0]='-1'
  else:p['weights'][0][1]=str(Q(p['weights'][0][1])+1)
  try:check(s,q,p)
  except AssertionError:attacks.append(field)
  else:raise AssertionError('attack accepted')
 result={'passed':True,'independent_certificates':len(packets),'attacks_rejected':attacks,
 'scope':'Known expected schemas/histories and exact source-space certificates; no upstream source-admission replay.'}
 (OUT/'schema-relative-tail-lp-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
