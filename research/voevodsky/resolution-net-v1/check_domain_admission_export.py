"""Export resource semantics for every constructor of the finite trace signature."""
from pathlib import Path
import hashlib,json,subprocess,sys
from port_certificates import decode
from resource_signature import World
root=Path(__file__).resolve().parent;repo=root.parents[2]
# Refresh the packet and its independent indexed proof/negative checks.
subprocess.run([sys.executable,str(root/'check_indexed_port_certificates.py')],check=True)
packet_path=root/'results/indexed-port-packet.json';raw=packet_path.read_bytes();packet=json.loads(raw)
packages=[decode(x) for x in packet['packages']];rules=[decode(x) for x in packet['rules']];evidence=[decode(x) for x in packet['evidence']]
worlds=[World.decode(p) for p in packages];tokens=sorted(set().union(*(w.owned for w in worlds)))
if not tokens:raise ValueError('nonempty token example required')
def status(w,t):return 'spent' if t in w.spent else ('free' if t in w.owned else 'absent')
lines=['{-# OPTIONS --safe --cubical --guardedness #-}','module ResolutionNetDomainAdmission where',
 'open import Cubical.Foundations.Prelude','import ResolutionNetIndexedPortCertificates as I',
 'import ResolutionNetFootprints as F','import CoherenceResolutionClosure as C',
 'data Token : Type where','  '+' '.join('t'+str(i) for i in range(len(tokens)))+' : Token',
 'module R = F.Resources Token','module RC = C.Closure R.World R.U R.V',
 'world : I.Pkg → R.World']
for i,w in enumerate(worlds):
 for j,t in enumerate(tokens):lines.append(f'world I.p{i} t{j} = F.{status(w,t)}')
lines+=['','unary-rule : {p q : I.Pkg} → I.U p q → R.U (world p) (world q)']
for i,r in enumerate(rules):
 if len(r.inputs)!=1:continue
 a,b=World.decode(r.inputs[0]),World.decode(r.output)
 for j,t in enumerate(tokens):
  x,y=status(a,t),status(b,t)
  if x==y:proof='F.stay F.'+x
  elif (x,y)==('free','spent'):proof='F.consume'
  else:raise ValueError('no domain witness for unary transition')
  lines.append(f'unary-rule I.rule{i} t{j} = {proof}')
lines+=['','binary-rule : {p q r : I.Pkg} → I.V p q r → R.V (world p) (world q) (world r)']
for i,r in enumerate(rules):
 if len(r.inputs)!=2:continue
 a,b=map(World.decode,r.inputs);c=World.decode(r.output)
 for j,t in enumerate(tokens):
  x,y,z=status(a,t),status(b,t),status(c,t)
  if x=='absent' and z==y:proof='F.from-right F.'+y
  elif y=='absent' and z==x:proof='F.from-left F.'+x
  else:raise ValueError('no domain witness for binary transition')
  lines.append(f'binary-rule I.rule{i} t{j} = {proof}')
lines+=['','seed-rule : {p : I.Pkg} → I.Evidence p → R.Initial (world p)']
for i,e in enumerate(evidence):
 for j,t in enumerate(tokens):
  x=status(World.decode(e.package),t)
  if x=='spent':raise ValueError('seed cannot claim spent resource')
  lines.append(f'seed-rule I.evidence{i} t{j} = F.fresh-{x}')
lines+=['','translate : {p : I.Pkg} → I.Resolve I.Evidence p → RC.Resolve R.Initial (world p)',
 'translate (I.seed e) = RC.seed (seed-rule e)',
 'translate (I.unary u d) = RC.unary (unary-rule u) (translate d)',
 'translate (I.binary v d e) = RC.binary (binary-rule v) (translate d) (translate e)',
 '', 'no-double-use : {p : I.Pkg} (d : I.Resolve I.Evidence p) (t : Token) → F.AtMostOne (R.uses (translate d) t)',
 'no-double-use d t = R.no-double-spend (translate d) t',
 'no-duplicate-origin : {p : I.Pkg} (d : I.Resolve I.Evidence p) (t : Token) → F.AtMostOne (R.origins (translate d) t)',
 'no-duplicate-origin d t = R.no-duplicate-origin (translate d) t','']
for i in range(len(packet['steps'])):
 lines += [f'domain-sound{i} : translate (I.interpret I.before{i}) ≡ translate (I.interpret I.after{i})',f'domain-sound{i} = cong translate I.sound{i}','']
source=root/'agda/ResolutionNetDomainAdmission.agda';source.write_text('\n'.join(lines)+'\n',encoding='utf-8')
command=['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(repo/'research/nima/agda'),'-i','C:/Users/andrey/tools/cubical-agda/cubical-0.9']
run=subprocess.run(command+[str(source)],capture_output=True,text=True);(root/'results/agda-domain-admission.log').write_text(run.stdout+'\n'+run.stderr)
if run.returncode:raise RuntimeError('domain proof failed; see log')
# Endpoint-correct declaration is legal, but its semantic witness is impossible.
r=next(r for r in rules if len(r.inputs)==1);old=packages.index(r.output);new=packages.index(r.inputs[0])
bad=['{-# OPTIONS --safe --cubical --guardedness #-}','module ResolutionNetRejectRevival where',
 'open import Cubical.Foundations.Prelude','import ResolutionNetIndexedPortCertificates as I',
 'open import ResolutionNetDomainAdmission','import ResolutionNetFootprints as F',
 'data Forged : I.Pkg → I.Pkg → Type where',f'  revive : Forged I.p{old} I.p{new}',
 'bad-rule : {p q : I.Pkg} → Forged p q → R.U (world p) (world q)']
for j,t in enumerate(tokens):
 x,y=status(worlds[old],t),status(worlds[new],t)
 bad.append(f'bad-rule revive t{j} = '+('F.stay F.'+x if x==y else 'F.consume'))
path=root/'agda/ResolutionNetRejectRevival.agda';text='\n'.join(bad)+'\n';path.write_text(text,encoding='utf-8')
failed=subprocess.run(command+[str(path)],capture_output=True,text=True);log=failed.stdout+'\n'+failed.stderr
(root/'results/agda-reject-revival.log').write_text(log);(root/'results/rejected-revival.agda.txt').write_text(text,encoding='utf-8');path.unlink()
if failed.returncode==0 or '[UnequalTerms]' not in log:raise RuntimeError('revival not rejected by type inequality')
files=[Path(__file__),source,root/'agda/ResolutionNetFootprints.agda',root/'agda/ResolutionNetIndexedPortCertificates.agda']
report={'passed':True,'token_count':len(tokens),'tokens':tokens,'package_count':len(packages),'rule_interpretations':len(rules),'seed_interpretations':len(evidence),'lifted_step_equalities':len(packet['steps']),'typed_revival_domain_witness_rejected':True,'packet_sha256':hashlib.sha256(raw).hexdigest(),'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'Generated finite signature interpreted into checked pointwise resource semantics; all source derivations inherit resource accounting. World decoding, signature generation and concrete wire mapping still trusted Python. Translation is not asserted injective on witnesses and grants no external commit authority.'}
(root/'results/domain-admission.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
