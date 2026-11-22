"""Exact face compressions of joint projectors and norm of every directed face-to-face block in the native electron return."""
from pathlib import Path
from fractions import Fraction as F
import sys,json
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'strominger/checkers'))
from assemble_metric_coefficient_protocol import A,ZERO,ONE,read_operator,product

def run():
    d=json.loads((D.parents[1]/'strominger/results/common-three-carrier-protocol/electron.json').read_text());L,G,N=[read_operator(d['operators'][s],8) for s in 'LGN'];assert G==N==product(G,L);out=[]
    for f in range(4):
        ids=range(2*f,2*f+2);assert all(N[i,j]*A(2)==L[i,j] for i in ids for j in ids);assert sum((L[i,i] for i in ids),ZERO)==ONE
        strengths=[]
        for g in range(4):
            value=sum((z.flip(8)*z for (i,j),z in N.items() if i//2==g and j//2==f),ZERO);q=F(1,4) if f==g else F(1,12);assert value==A(q);strengths.append(str(q))
        out.append(dict(face=f,mean_joint=['1/4','1/4','0','1/2'],return_block_norm_squared=strengths))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_electron_face_joint_weights.json').write_text(json.dumps(out)+'\n')
