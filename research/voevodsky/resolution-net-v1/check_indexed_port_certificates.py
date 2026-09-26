from pathlib import Path
from copy import deepcopy
import hashlib,json,subprocess
from reference import Admission,unit,map_seeds
from resource_signature import seed,consume,join,validate_history
from local_net import Net
from port_certificates import encode,snapshot,restore
from indexed_port_certificates import IndexedExporter
root=Path(__file__).resolve().parent;repo=root.parents[2]
a=seed(('a',),'grant-a');b=seed(('b',),'grant-b');left=consume(a,'a');right=consume(b,'b');h=join(left,right);validate_history(h)
exporter=IndexedExporter();net=Net(map_seeds(unit,h));steps=[];proofs=[]
while net.active():
 pair=net.active()[0];before=deepcopy(net);net.rewrite(pair);after=deepcopy(net)
 steps.append({'before':snapshot(before),'pair':list(pair),'after':snapshot(after)})
 proofs.append(exporter.certificate(len(proofs),before,pair,after))
# Include another declared witness of the SAME package to test non-collapse.
alternative=Admission(a.package,'different-grant-a');exporter.history(unit(alternative))
packet={'packages':[encode(p) for p in exporter.packages],'rules':[encode(r) for r in exporter.rules],'evidence':[encode(e) for e in exporter.seeds],'steps':steps}
packet_file=root/'results/indexed-port-packet.json';packet_file.write_text(json.dumps(packet,indent=2)+'\n')
for item in json.loads(packet_file.read_text())['steps']:
 restored=restore(item['before']);restored.rewrite(tuple(item['pair']))
 if snapshot(restored)!=item['after']:raise RuntimeError('snapshot replay mismatch')
packet_hash=hashlib.sha256(packet_file.read_bytes()).hexdigest();module='ResolutionNetIndexedPortCertificates'
source=root/'agda'/f'{module}.agda';source.write_text(exporter.header(module)+'\n-- Packet SHA256: '+packet_hash+'\n\n'+'\n'.join(proofs),encoding='utf-8')
command=['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(repo/'research/nima/agda'),'-i','C:/Users/andrey/tools/cubical-agda/cubical-0.9']
run=subprocess.run(command+[str(source)],capture_output=True,text=True);(root/'results/agda-indexed-port.log').write_text(run.stdout+'\n'+run.stderr)
if run.returncode:raise RuntimeError('indexed certificates rejected')
rule_a=exporter.rule(left.rule);seed_b=exporter.history(b);pa=exporter.package(left.package)
old=exporter.history(a);new=exporter.history(unit(alternative));pinitial=exporter.package(a.package)
negatives=[('WrongPackage',f'invalid : Resolve Evidence {pa}\ninvalid = unary {rule_a} {seed_b}\n'),
 ('WrongWitness',f'invalid : RepresentedStep (pending (seed {old})) (keep {new})\ninvalid = represented (F-seed {old}) same\n')]
for suffix,body in negatives:
 name='ResolutionNetReject'+suffix;path=root/'agda'/f'{name}.agda'
 text='{-# OPTIONS --safe --cubical --guardedness #-}\nmodule '+name+' where\nopen import '+module+'\n'+body
 path.write_text(text,encoding='utf-8')
 bad=subprocess.run(command+[str(path)],capture_output=True,text=True)
 log=bad.stdout+'\n'+bad.stderr;(root/'results'/f'agda-reject-{suffix}.log').write_text(log)
 (root/'results'/f'{name}.agda.txt').write_text(text,encoding='utf-8');path.unlink()
 if bad.returncode==0 or '[UnequalTerms]' not in log:raise RuntimeError('negative did not fail by type inequality: '+suffix)
files=[Path(__file__),root/'indexed_port_certificates.py',root/'port_certificates.py',root/'port_refinement.py',root/'resource_signature.py',source]
report={'passed':True,'package_constructors':len(exporter.packages),'unary_rules':sum(len(r.inputs)==1 for r in exporter.rules),'binary_rules':sum(len(r.inputs)==2 for r in exporter.rules),'seed_witness_constructors':len(exporter.seeds),'wire_steps':len(steps),'wrong_package_rejected_by_agda':True,'same_package_wrong_witness_rejected_by_agda':True,'packet_sha256':packet_hash,'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'Finite heterogeneous indexed signature and concrete snapshot replay. Agda checks declared constructor endpoints and step proofs; declaration admission, serialization and wire reification remain trusted Python, not verified global graph decoding or authority.'}
(root/'results/indexed-port-certificates.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))
