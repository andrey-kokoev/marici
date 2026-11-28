"""Five-edit exhaustive layer, no stored successor input. Reuse monotone edge-removal search."""
import ast,gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_retention_slice import CAT,D


def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);lines=[]
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for i,l in enumerate(f,1):
            s=l.rstrip();n=sum(s[1:].translate(w))
            if 85<=n<=88:lines.append(f'{i} {s.decode()}')
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'five.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_matrix_four_edit.rs')),'-o',str(exe)],check=True);out=ast.literal_eval(subprocess.run([str(exe),'5'],input='\n'.join(lines)+'\n',capture_output=True,text=True,check=True).stdout)
    keys=['deletions','augmentation_choices_including_null','triangle_and_blue_eight_free','and_degree_correct','and_face_matching'];res={k:dict(zip(keys,v)) for k,v in zip(['five_removals','four_removals_one_addition'],out)};print(res);(D.parent/'ramsey_matrix_five_edit_gate.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
