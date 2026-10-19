"""Exact audit of rational rounding only; no certification of analytic quadrature."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from verify_proton_native_task_catalogue import realify,multiply,rank
ROOT=Path(__file__).resolve().parents[3]
def main():
    path=ROOT/'research/voevodsky/results/rh-gaussian-seed-packet-v1.json';p=json.loads(path.read_text())
    for name,h in p['source_hashes'].items():assert sha256(Path(name).read_bytes()).hexdigest()==h,name
    packet=p['rounded_packet'];G=[[F(0)]*3 for _ in range(3)]
    for i,j,x,y in packet['entries']:assert F(y)==0;G[i][j]=F(x)
    assert G==[list(row) for row in zip(*G)]
    # Exact LDL gives a certificate of positive definiteness of this particular
    # rational matrix, without claiming an enclosure of the analytic source.
    L=[[F(i==j) for j in range(3)] for i in range(3)];D=[]
    for j in range(3):
        d=G[j][j]-sum(L[j][k]**2*D[k] for k in range(j));assert d>0;D.append(d)
        for i in range(j+1,3):L[i][j]=(G[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/d
    reconstructed=[[sum(L[i][k]*D[k]*L[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    assert reconstructed==G
    native=json.loads((ROOT/'research/voevodsky/results/proton-native-relationship-structure-v1.json').read_text())
    K=realify(native['hermitian_analysis']['K']);B=realify(p['native_attachment'])
    n,m=p['native_attachment']['shape'];entries=p['native_attachment']['entries']
    # Conjugate transpose in the algebraic field then independent realification.
    Bt={'shape':[m,n],'entries':[[j,i,x,str(-F(y))] for i,j,x,y in entries]}
    assert rank(B)==6 and multiply(multiply(realify(Bt),K),B)==realify(packet)
    audit={'status':'passed','schema':'marici.voevodsky.rh-gaussian-rounded-audit.v1',
      'exact_rational_packet_positive_definite':True,'ldl_pivots':[str(x) for x in D],
      'exact_attachment_pullback_verified':True,'rounded_packet_rank':3,
      'analytic_Weil_packet_positivity_certified':False,'source_and_zero_tail_equality_certified':False,'RH_proved':False,
      'producer_result_sha256':sha256(path.read_bytes()).hexdigest(),'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    out=path.with_name('rh-gaussian-seed-packet-v1-rounded-audit.json');out.write_text(json.dumps(audit,indent=2)+'\n')
    print(json.dumps({k:v for k,v in audit.items() if k!='ldl_pivots'},indent=2))
if __name__=='__main__':main()
