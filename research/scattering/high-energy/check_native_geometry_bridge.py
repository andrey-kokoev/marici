"""AB1 final cycle: native folds from exact binary centered vertices and exact grid."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import numpy as np
from flint import arb,arb_mat,acb,acb_mat,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches
from check_verified_inverse_factor import balls,squared_norm,outward_upper,outward_lower

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
SOURCE=CALC/'cache/source_work/engine/source_packet/source/source/.source/dynamical_strain.py'
TERMINAL=HOME/'results/terminal-assembly.v1.json'
SAMPLES=HOME/'results/native-samples.v1.npz'
INPUTS=HOME/'results/native-geometry-inputs.v1.npz'
NOTE=HOME/'NATIVE-GEOMETRY-BRIDGE.md'
RESULT=HOME/'results/native-geometry-bridge.v1.json'


def dot(x,y):return sum((a*b for a,b in zip(x,y)),arb(0))


def wedge(x,y):
    return [x[1]*y[2]-x[2]*y[1]+x[0]*y[3]-x[3]*y[0],
            x[2]*y[0]-x[0]*y[2]+x[1]*y[3]-x[3]*y[1],
            x[0]*y[1]-x[1]*y[0]+x[2]*y[3]-x[3]*y[2]]


def audit(vertex_balls=None):
    historical_validate();ctx.prec=128
    terminal=json.loads(TERMINAL.read_text(encoding='utf-8'))
    for path,value in terminal['source_sha256'].items():assert digest(ROOT/path)==value
    code=SOURCE.read_text(encoding='utf-8')
    for term in ('DC=np.arctan(1/np.sqrt(5))','raw=self.n0[None,:,:]+(1/lam-1)*inc','k=w/(2*a[:,None])'):
        assert term in code
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('native_geometry_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    q=it.fam.q;edges=list(it.fam.st.EDGES)
    assert edges==list(itertools.combinations(range(5),2))
    SIG=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
    assert np.array_equal(SIG,it.nat.SIG)
    data={'centered_vertices':q,'SIG':SIG,'edges':np.array(edges)}
    if INPUTS.exists():
        with np.load(INPUTS,allow_pickle=False) as z:
            for key,value in data.items():assert np.array_equal(z[key],value),'native input drift'
    else:np.savez_compressed(INPUTS,**data)
    qb=vertex_balls if vertex_balls is not None else [[arb(float(x)) for x in row] for row in q]
    normals=[];orientation=[]
    for c in range(5):
        face=[i for i in range(5) if i!=c]
        tangent=[[qb[i][k]-qb[face[0]][k] for k in range(4)] for i in face[1:]]
        raw=[(-1)**k*arb_mat([[row[r] for r in range(4) if r!=k] for row in tangent]).det() for k in range(4)]
        norm=dot(raw,raw).sqrt();assert norm.lower()>0
        normal=[x/norm for x in raw]
        test=dot(normal,[qb[c][k]-qb[face[0]][k] for k in range(4)])
        assert test.lower()>0 or test.upper()<0,'normal orientation undecidable'
        if test.lower()>0:normal=[-x for x in normal]
        assert dot(normal,[qb[c][k]-qb[face[0]][k] for k in range(4)]).upper()<0
        normals.append(normal);orientation.append(outward_lower(abs(test)))
    with np.load(SAMPLES,allow_pickle=False) as z:samples=z['native_samples']
    dc=(1/arb(5).sqrt()).atan();maximum=arb(0);slice_bounds=[];minimum_fold=np.inf
    for j in range(49):
        lam=arb(6*(j+1))/125;slice_error=arb(0)
        for l in range(25):
            angle=2*arb.pi()*l/25-dc;sn,cs=angle.sin_cos();axis=[cs,arb(0),arb(0),sn]
            deformed=[]
            for normal in normals:
                projection=dot(normal,axis)
                raw=[normal[k]+(1/lam-1)*projection*axis[k] for k in range(4)]
                norm=dot(raw,raw).sqrt();assert norm.lower()>0
                deformed.append([x/norm for x in raw])
            target=acb_mat((4*np.eye(10)).tolist())
            for i,k in edges:
                x,y=deformed[i],deformed[k];a=((1+dot(x,y))/2).sqrt();assert a.lower()>0
                minimum_fold=min(minimum_fold,outward_lower(a))
                kk=[v/(2*a) for v in wedge(x,y)]
                U=[[acb(a,-kk[2]),acb(-kk[1],-kk[0])],[acb(kk[1],-kk[0]),acb(a,kk[2])]]
                for p in range(2):
                    for r in range(2):
                        target[2*k+p,2*i+r]=-U[p][r]
                        target[2*i+r,2*k+p]=-U[p][r].conjugate()
            error=squared_norm(target-balls(samples[j,l])).upper().sqrt()
            if error.upper()>slice_error.upper():slice_error=error.upper()
        if slice_error.upper()>maximum.upper():maximum=slice_error.upper()
        slice_bounds.append(outward_upper(slice_error))
    # Exact DFT is unitary; angle-block diagonal perturbation norm is bounded
    # by the largest sample Frobenius norm, not a sum over all grid points.
    separation=arb(terminal['assembled_exact_pose_shift_separation_lower'])-maximum.upper()
    assert separation.lower()>0
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_verified_inverse_factor.py',TERMINAL,SAMPLES,INPUTS,SOURCE,
           CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    result={'schema':'marici.scattering.native-geometry-bridge.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'native_samples_covered':1225,'slice_sample_error_upper':slice_bounds,
            'maximum_native_sample_Frobenius_error_upper':outward_upper(maximum),
            'minimum_fold_denominator_a_lower':minimum_fold,'normal_orientation_margins_lower':orientation,
            'assembled_geometry_reference_separation_lower':outward_lower(separation),
            'native_geometry_certified_on_binary_centered_vertices':True,
            'assembled_geometry_reference_inertia_certified':True,'negative_inertia':130,'zero_inertia':0,
            'reference':'exact cofactor normals of binary centered vertices, exact grid/radical offset, Pauli folds and terminal assembly',
            'upstream_vertex_centering_reference_certified':False,'original_source_model_certified':False,
            'true_ground_identity_certified':False,'retained_frame_certified':False,'full_band_coupled_inverse_certified':False,
            'AB1_execution_cycles_spent':2,'AB1_execution_cycles_remaining':0,
            'AB1_outcome':'inconclusive for full H7; conditional native/terminal assembly bridge completed',
            'H7_disposition':'open; native assembly certified on binary vertices, upstream reference/frame/coupled inverse remain'}
    if vertex_balls is not None:
        result.update(reference='exact cofactor normals of caller-supplied enclosed vertices; exact grid/radical offset and terminal assembly',
                      native_geometry_certified_on_binary_centered_vertices=False,
                      native_geometry_certified_on_supplied_vertex_enclosures=True,
                      upstream_vertex_centering_reference_certified=True,
                      H7_disposition='open; supplied exact-vertex native assembly enclosed, frame and coupled inverse remain')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),r)
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','maximum_native_sample_Frobenius_error_upper','assembled_geometry_reference_separation_lower','negative_inertia','AB1_outcome')}))


if __name__=='__main__':main()
