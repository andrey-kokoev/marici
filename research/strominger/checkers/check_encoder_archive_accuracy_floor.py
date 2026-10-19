"""Exact binary-rational hostile against an all-accuracy archived-matrix target.

No NumPy dependency: decode the saved NPY float64 arrays using the standard
library. This tests literal archived whole-encoder entries, not the exact polar
operator or a bright-sector-only specification.
"""
import ast
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import struct
import zipfile

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]


def read_matrix(archive, name):
    with zipfile.ZipFile(archive) as z:
        raw = z.read(name+'.npy')
    assert raw[:6] == b'\x93NUMPY'
    version = tuple(raw[6:8])
    if version == (1,0):
        length = struct.unpack('<H',raw[8:10])[0]
        offset = 10
    else:
        assert version in ((2,0),(3,0))
        length = struct.unpack('<I',raw[8:12])[0]
        offset = 12
    header = ast.literal_eval(raw[offset:offset+length].decode('latin1').strip())
    assert header['descr'] in ('<f8','=f8')
    rows, cols = header['shape']
    payload = raw[offset+length:]
    assert len(payload)==8*rows*cols
    values = [F(x[0]) for x in struct.iter_unpack('<d',payload)]
    if header['fortran_order']:
        return [[values[j*rows+i] for j in range(cols)] for i in range(rows)]
    return [values[i*cols:(i+1)*cols] for i in range(rows)]


def inspect(A):
    rows, cols = len(A), len(A[0])
    candidates = []
    for j in range(cols):
        squared = sum((row[j]**2 for row in A),F(0))
        defect = squared-1
        assert 0<squared<4
        # Any exact isometry V has ||V e_j||=1. Reverse triangle inequality:
        # ||(A-V)e_j|| >= |sqrt(squared)-1| = |defect|/(sqrt(squared)+1)
        # > |defect|/3 when defect != 0 and squared < 4.
        candidates.append((abs(defect)/3,j,squared,defect))
    floor,j,squared,defect = max(candidates)
    return {'rows':rows,'columns':cols,'witness_column':j,
            'exact_column_norm_squared':str(squared),
            'exact_norm_squared_defect':str(defect),
            'strict_operator_distance_lower_bound_to_any_isometry':str(floor),
            'lower_bound_decimal_display':float(floor),
            'nonzero_archive_accuracy_floor':bool(floor)}


def main():
    p = BASE/'results/neutron-comparison-memory.npz'
    raw = p.read_bytes()
    metadata_path = BASE/'results/neutron-comparison-memory.json'
    metadata_raw = metadata_path.read_bytes()
    metadata = json.loads(metadata_raw)
    digest = hashlib.sha256(raw).hexdigest()
    assert metadata['npz_sha256']==digest
    results = {key:inspect(read_matrix(p,key)) for key in ('encoder','ready_embedding')}
    # The question is answered by the measured flag, not an assertion forcing
    # the archive to be defective. Replacing it by an exact isometry would pass
    # the zero-floor control and change the disposition.
    exact_control = inspect([[F(1),F(0)],[F(0),F(1)]])
    bad_control = inspect([[F(1)+F(1,10**20),F(0)],[F(0),F(1)]])
    assert not exact_control['nonzero_archive_accuracy_floor']
    assert bad_control['nonzero_archive_accuracy_floor']
    # Demonstrate why float evaluation cannot be the exact hostile here.
    assert float(F(1)+F(1,10**20))==1.0
    epsilon=F(1,10**18)
    for result in results.values():
        result['requested_epsilon']=str(epsilon)
        result['epsilon_impossible_for_literal_archive_target']=epsilon <= F(result['strict_operator_distance_lower_bound_to_any_isometry'])
    report = {'status':'pass','archive_sha256':digest,'results':results,
        'controls':{'exact_identity_zero_floor':True,'sub_float_resolution_rational_defect_detected':True},
        'scope':'Literal archived whitened full matrices only. Not a no-go for the exact polar operator, precision refinement, or the bright-sector-restricted task. No control word or optimizer was tested.',
        'source_hashes':{p.relative_to(ROOT).as_posix():digest,
                        metadata_path.relative_to(ROOT).as_posix():hashlib.sha256(metadata_raw).hexdigest(),
                        Path(__file__).resolve().relative_to(ROOT).as_posix():hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    for path,h in report['source_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    (BASE/'results/encoder-archive-accuracy-floor.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:{k:res[k] for k in ['witness_column','lower_bound_decimal_display','epsilon_impossible_for_literal_archive_target']} for key,res in results.items()}))


if __name__=='__main__':
    main()
