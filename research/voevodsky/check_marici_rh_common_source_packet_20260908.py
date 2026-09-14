#!/usr/bin/env python3
"""Validate the frozen common-source packet and its authoritative evidence digests."""
import argparse,json,hashlib
from pathlib import Path

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--packet',default='research/voevodsky/marici_rh_common_source_packet_20260908.json');p.add_argument('--output',default='research/voevodsky/marici_rh_common_source_packet_certificate_20260908.json');a=p.parse_args();r=Path(a.root)
 packet=json.loads((r/a.packet).read_text());checks=0
 assert packet['schema']=='marici.rh.common-source-packet.v1' and packet['owner']=='marici.Voevodsky';checks+=2
 assert packet['claim']=='construct the common level-zero incidence from the global theta/Tate source to the six-normal endpoint/conductor source';checks+=1
 actual={}
 for e in packet['evidence']:
  path=r/e['path'];assert path.is_file();checks+=1
  actual[e['path']]=sha(path);assert actual[e['path']]==e['sha256'];checks+=1
 assert packet['observer_theory']['static_theta_rank']==4 and packet['observer_theory']['declared_directions']==6;checks+=2
 assert packet['observer_theory']['static_theta_status'].startswith('synthetic SCC negative fixture');checks+=1
 assert packet['observer_theory']['six_normal_target_rank']==6;checks+=1
 assert packet['residuals']==['kernel','cokernel','topological','authority'];checks+=4
 assert packet['forbidden_shortcuts'];checks+=1
 raw=(r/a.packet).read_bytes()
 out={'schema':'marici.rh.common-source-packet-check.v1','status':'frozen_valid','checks':checks,
  'packet_sha256':hashlib.sha256(raw).hexdigest(),'evidence_sha256':actual,
  'next_constructor':'derive the RH source-incidence matrix from cited source maps; do not promote the synthetic SCC rank fixture',
  'next_hostile':'after source derivation, delete one independently derived incidence and require the rank to fall; retain completion margin separately'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'frozen_valid','checks':checks,'evidence':len(actual),'packet_sha256':out['packet_sha256']}))
if __name__=='__main__':main()
