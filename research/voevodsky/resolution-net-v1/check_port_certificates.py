"""Regenerate concrete fixtures, replay snapshots, export and freshly check Agda."""
from pathlib import Path
from copy import deepcopy
import hashlib,json,subprocess
from reference import Package,Admission,Rule,Step,unit,map_seeds
from local_net import Net
from port_refinement import diagram
from port_certificates import Exporter,snapshot,restore,encode
root=Path(__file__).resolve().parent;repo=root.parents[2]
p=Package('P',('exact fixture payload',));s=unit(Admission(p,'seed-proof'));u=Rule('u',(p,),p,'witness-u');v=Rule('v',(p,p),p,'witness-v')
a=Step(u,(s,));h=Step(v,(a,Step(v,(s,a))))
net=Net(map_seeds(unit,h));records=[];exporter=Exporter(p);proofs=[]
while net.active():
 pair=net.active()[-1];before=deepcopy(net);net.rewrite(pair);after=deepcopy(net)
 records.append({'before':snapshot(before),'pair':list(pair),'after':snapshot(after),'diagram':diagram(before,pair,after)})
 proofs.append(exporter.certificate(len(proofs),before,pair,after))
if net.readback()!=h:raise RuntimeError('wrong final history')
packet={'package':encode(p),'rules':[encode(r) for r in exporter.rules],'seed_evidence':[encode(a) for a in exporter.seeds],'steps':records}
packet_path=root/'results/concrete-port-certificates.json';packet_path.write_text(json.dumps(packet,indent=2)+'\n')
# Round-trip actual serialized bytes, not the original in-memory records.
loaded=json.loads(packet_path.read_text())
for record in loaded['steps']:
 b=restore(record['before']);a=restore(record['after']);pair=tuple(record['pair']);diagram(b,pair,a)
 replay=deepcopy(b);replay.rewrite(pair)
 if snapshot(replay)!=record['after']:raise RuntimeError('concrete wire replay mismatch')
# Corrupt reciprocal wiring and witness data independently.
bad=deepcopy(loaded['steps'][0]['before']);bad['wires'][0][1]=[999,0]
try:restore(bad)
except ValueError:pass
else:raise RuntimeError('corrupt wiring accepted')
packet_hash=hashlib.sha256(packet_path.read_bytes()).hexdigest()
header='''{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetPortCertificates where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ)
open import CoherenceResolutionClosure
open import ResolutionNetLocalSimulation
open import ResolutionNetCompression
open Closure Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ)
open Local Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ) (λ _ → ℕ)
open Compression Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ) (λ _ → ℕ)
'''
source=root/'agda/ResolutionNetPortCertificates.agda';source.write_text(header+'\n-- Concrete packet SHA256: '+packet_hash+'\n\n'+'\n'.join(proofs),encoding='utf-8')
command=['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(repo/'research/nima/agda'),'-i','C:/Users/andrey/tools/cubical-agda/cubical-0.9',str(source)]
run=subprocess.run(command,capture_output=True,text=True);(root/'results/agda-port-certificates.log').write_text(run.stdout+'\n'+run.stderr)
if run.returncode:raise RuntimeError('Agda rejected export; see log')
# A syntactically plausible proof with a wrong target must fail type checking.
bad_source=root/'agda/ResolutionNetRejectedCertificate.agda'
bad_source.write_text(header.replace('ResolutionNetPortCertificates','ResolutionNetRejectedCertificate')+'\ninvalid : RepresentedStep (pending (seed (seed 0))) (keep (seed 1))\ninvalid = represented (F-seed (seed 0)) same\n',encoding='utf-8')
bad_run=subprocess.run(command[:-1]+[str(bad_source)],capture_output=True,text=True)
(root/'results/agda-rejected-certificate.log').write_text(bad_run.stdout+'\n'+bad_run.stderr)
if bad_run.returncode==0:raise RuntimeError('wrong typed witness accepted')
# Keep the rejected test as text, not a permanently failing live Agda module.
(root/'results/rejected-certificate.agda.txt').write_text(bad_source.read_text(encoding='utf-8'),encoding='utf-8');bad_source.unlink()
files=[root/n for n in ('port_certificates.py','check_port_certificates.py','port_refinement.py','local_net.py','admission.py','reference.py')]+list((root/'agda').glob('ResolutionNet*.agda'))
report={'passed':True,'concrete_steps':len(records),'packet_sha256':packet_hash,'generated_agda_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'fresh_agda_exit_code':run.returncode,'corrupt_wire_snapshot_rejected':True,'wrong_witness_agda_rejected':True,'source_sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},'scope':'Finite single-package certificate bridge: exact snapshot replay in Python and typed abstract RepresentedStep proofs in Agda. The codec/reifier/exporter and correspondence of strings to natural-number codes remain trusted Python; not universal verified port semantics.'}
(root/'results/port-certificates.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
