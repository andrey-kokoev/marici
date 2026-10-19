#!/usr/bin/env python3
"""Assemble the nine-model research collection from checked, hash-pinned results."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def load_checked(name):
    result=json.loads((ROOT/'research/strominger/results'/name).read_text())
    assert result['status']=='passed'
    for path,digest in result['source_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, f'Stale source: {path}'
    return result

def main():
    positron=load_checked('positron_reversed_seed.json')
    photon=load_checked('photon_shared_edge_seed.json')
    reversed_matter=load_checked('reversed_matter_seeds.json')
    models=positron['collection']+[{
        key:photon[key] for key in ('label','source_path','source_sha256','effective_source','geometry','assembly_stage','physical_identification_derived','arrow_reversal_of')
    }]+reversed_matter['models']
    assert len(models)==9 and len({m['label'] for m in models})==9
    for model in models:
        assert hashlib.sha256((ROOT/model['source_path']).read_bytes()).hexdigest()==model['source_sha256'], f"Stale model source: {model['label']}"
    result={'schema':'marici.strominger.arrow-particle-collection.v3','status':'passed','models':models,'result_sources':['research/strominger/results/positron_reversed_seed.json','research/strominger/results/photon_shared_edge_seed.json','research/strominger/results/reversed_matter_seeds.json'],'physical_identification_derived':False}
    (ROOT/'research/strominger/results/arrow_particle_collection.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','models':[m['label'] for m in models]},indent=2))
if __name__=='__main__':main()
