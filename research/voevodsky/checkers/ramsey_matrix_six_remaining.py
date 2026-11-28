"""Replay remaining six-edit branches after deleting one vertex. No endpoint coloring."""
import ast,gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_retention_slice import CAT,D

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);lines=[]
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for i,l in enumerate(f,1):
            s=l.rstrip()
            if 85<=sum(s[1:].translate(w))<=89:lines.append(f'{i} {s.decode()}')
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'six.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True);v=ast.literal_eval(p.stdout)
    keys=['deletions','triangle_and_blue_eight_free','and_degree_correct','and_face_matching'];out=dict(zip(['six_removals','five_removals_one_addition'],[dict(zip(keys,b)) for b in v]));out['first_face_pass']=p.stderr.strip();print(out);(D.parent/'ramsey_matrix_six_remaining.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
