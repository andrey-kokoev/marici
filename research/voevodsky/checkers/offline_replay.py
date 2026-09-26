"""Replay persisted certificates without importing any production reducer."""
import json
import hashlib
from pathlib import Path
from rule_templates import TEMPLATES,check_template
from certified_replacement import checked_replace,identity
from pure_replacement import validate,require
from initial_net_recognizer import recognize

def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def contract():
 table=json.loads((Path(__file__).resolve().parents[1]/'results/combined-signature.json').read_text())
 return {'templates':TEMPLATES,'signature':table['signature'],'allowed':table['allowed_pairs']}
def replay(trace):
 require(isinstance(trace,dict) and trace.get('schema')=='recurrent-trace-v3','unsupported trace schema')
 require(type(trace.get('complete')) is bool,'completion claim must be Boolean')
 require(trace.get('provenance_status')=='unverified-constructor','unsupported provenance status')
 outputs=trace.get('outputs');tags=trace.get('output_types')
 require(isinstance(outputs,list) and all(isinstance(r,str) for r in outputs),'invalid output roots')
 require(isinstance(tags,list) and len(tags)==len(outputs) and all(t in ('boolean','scan') for t in tags),'invalid output types')
 rules=contract();require(trace['contract_digest']==digest(rules),'contract drift')
 initial=trace['initial'];types={n:tuple(ps) for n,ps in initial['types'].items()};wires=dict(initial['wires']);serial=initial['serial']
 validate(types,wires)
 roots=['RET','ACK']+trace['outputs'];require(len(roots)==len(set(roots)),'duplicate roots')
 for root in roots:require(root in types and types[root]==('p',),'invalid root')
 require(all(identity(r)[0]=='OUT' for r in outputs),'output is not an OUT root')
 # Validate even zero-step initial states.
 require(type(serial) is int and serial>=0,'invalid initial high-water')
 ids=[]
 for n,ps in types.items():
  k,s=identity(n);require(k in rules['signature'] and set(ps)==set(rules['signature'][k]),'initial signature')
  if s is not None:require(s<=serial,'initial high-water');ids.append(s)
 require(len(ids)==len(set(ids)),'duplicate serial')
 declaration=trace.get('declaration')
 require(isinstance(declaration,dict) and set(declaration)=={'bits','program'},'missing source declaration')
 recognize(types,wires,declaration['bits'],declaration['program'],outputs,tags)
 for cert in trace['steps']:
  require(cert['before']==serial,'discontinuous allocator history')
  check_template(types,cert['names'],cert['edges'],cert['new'],before=serial)
  types,wires=checked_replace(types,wires,cert['names'],cert['edges'],cert['new'],before=serial,after=cert['after'],signature=rules['signature'],allowed=rules['allowed'],protected=roots)
  serial=cert['after']
 require(digest({'types':types,'wires':wires,'serial':serial})==trace['final_digest'],'final state mismatch')
 terminal=None
 if trace['complete']:
  # Require exact terminal components, not just absence of admitted pairs.
  used=set(roots);word=[];p=wires['RET.p']
  while True:
   n,port=p.split('.');require(port=='p' and n not in used,'bad returned chain');used.add(n);k=identity(n)[0]
   if k=='N':break
   require(k in ('B0','B1'),'unfinished support');word.append(int(k=='B1'));p=wires[n+'.a']
  for root,heads in [('ACK',('DONE',))]+[(r,('TRUE','FALSE') if tag=='boolean' else ('FOUND','EXHAUSTED')) for r,tag in zip(outputs,tags)]:
   n,port=wires[root+'.p'].split('.');require(port=='p' and n not in used and identity(n)[0] in heads,'unfinished result');used.add(n)
  require(used==set(types),'residual work or garbage')
  values=[]
  for root,tag in zip(outputs,tags):
   kind=identity(wires[root+'.p'].split('.')[0])[0]
   values.append((tag,kind=='TRUE' if tag=='boolean' else kind))
  terminal={'word':tuple(word),'observations':tuple(values)}
 return {'steps':len(trace['steps']),'complete':trace['complete'],'final_digest':trace['final_digest'],'provenance_status':'structurally-matched-declaration','authenticated':False,'terminal':terminal}

if __name__=='__main__':
 import sys
 print(json.dumps(replay(json.loads(Path(sys.argv[1]).read_text()))))
