"""Six-edit double-add branch only. Enumerate removals first; use exact degree increments before testing blue eights."""
import gzip,json,ast,subprocess,tempfile,math
from pathlib import Path
from ramsey_retention_slice import CAT,D

def audit():
    weights=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)])
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:seeds=[s.decode() for l in f if sum((s:=l.rstrip())[1:].translate(weights))==85]
    assert len(seeds)==4
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'six.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);v=ast.literal_eval(subprocess.run([str(exe)],input='\n'.join(seeds)+'\n',capture_output=True,text=True,check=True).stdout)
    assert v[0]==48 and v[1]==48*math.comb(78,4);out=dict(zip(('deletions','four_edge_removals','degree_increment_histogram_pass','degree_and_triangle_pass','also_blue_eight_free','also_face_matching'),v));print(out);(D.parent/'ramsey_matrix_six_double_add.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
