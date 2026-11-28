"""Count face candidates with a protected-edge bound and with an exact one-star cover."""
import gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_retention_slice import CAT,D

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);data=[]
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for i,l in enumerate(f,1):
            s=l.rstrip()
            if 85<=sum(s[1:].translate(w))<=89:data.append(f'{i} {s.decode()}')
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'locks.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(data),text=True,capture_output=True,check=True)
    h=[list(map(int,row.split())) for row in p.stdout.splitlines()];out=dict(columns=['vertices_with_at_most_four_protected_edges','vertices_with_four_neighbor_cover','deletions'],hist=h,edge_reject=sum(c for n,m,c in h if n<6),cover_reject=sum(c for n,m,c in h if m<6),total=sum(c for n,m,c in h),max_faces=max(m for n,m,c in h),example=p.stderr.strip());assert out['total']==1016807;print({k:v for k,v in out.items() if k!='hist'});(D.parent/'ramsey_matrix_face_lock.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
