"""VB1 cycle 1: pinned exact radical vertices propagated to native-source inertia."""
import argparse
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx
from check_native_geometry_bridge import audit as native_audit
from high_energy_scattering_net import ROOT,HOME,digest
from receipt_replay import assert_receipt_matches

NOTE=HOME/'H7-VERTEX-FRAME-BRIDGE.md'
GEOMETRY=HOME/'results/source-geometry.v1.json'
RESULT=HOME/'results/exact-vertex-bridge.v1.json'


def audit():
    ctx.prec=128
    engine=ROOT/'.ai/tmp/scattering-h6-response33/calculation/cache/source_work/engine'
    import os
    if os.name=='nt':engine=Path(chr(92)*2+'?'+chr(92)+str(engine.resolve()))
    owner=next(engine.rglob('open_product_solver.py')).parent/'inputs/geometry.json'
    raw=owner.read_bytes()
    if GEOMETRY.exists():assert GEOMETRY.read_bytes()==raw,'pinned geometry snapshot drift'
    else:GEOMETRY.write_bytes(raw)
    geometry=json.loads(raw)
    # Fixed grammar: no arbitrary eval or implicit approximate decimal parsing.
    constants={'0':arb(0),'1':arb(1),'-1':arb(-1),'-sqrt(6)/3':-arb(6).sqrt()/3,
               '-sqrt(30)/3':-arb(30).sqrt()/3,'2*sqrt(6)/3':2*arb(6).sqrt()/3}
    text=geometry['initial_left'];assert len(text)==5 and all(len(row)==4 for row in text)
    vertices=[[constants[value] for value in row] for row in text]
    mean=[sum((row[k] for row in vertices),arb(0))/5 for k in range(4)]
    centered=[[row[k]-mean[k] for k in range(4)] for row in vertices]
    native=native_audit(vertex_balls=centered)
    assert native['native_samples_covered']==1225
    assert native['assembled_geometry_reference_inertia_certified']
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_native_geometry_bridge.py',GEOMETRY]
    return {'schema':'marici.scattering.exact-vertex-bridge.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'exact_vertex_grammar':sorted(constants),
            'geometry_mean_balls':[str(v) for v in mean],
            'native_bridge':native,'exact_radical_vertex_centering_enclosed':True,
            'native_source_geometry_assembly_inertia_certified':True,
            'negative_inertia':native['negative_inertia'],'zero_inertia':0,
            'true_ground_identity_certified':False,'retained_frame_certified':False,'full_band_coupled_inverse_certified':False,
            'VB1_execution_cycles_spent':1,'VB1_execution_cycles_remaining':1,
            'H7_disposition':'open; exact native geometry reference bridged, ground/frame and coupled inverse remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),r)
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','native_sample_error_upper':r['native_bridge']['maximum_native_sample_Frobenius_error_upper'],
                     'negative_inertia':r['negative_inertia'],'H7':r['H7_disposition']}))


if __name__=='__main__':main()
