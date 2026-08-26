#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/stable-seam-decoder.json"

def main():
    records=[]
    e2=Matrix([0,1])
    for n in [1,2,4,8,16]:
        H=Matrix.diag(1,Rational(1,n)); R=Matrix.eye(2); S=Matrix.diag(1,n)
        assert S*H==R
        weak_data=H*e2
        reconstructed=S*weak_data
        assert reconstructed==e2
        records.append({"N":n,"decoder_norm":n,"weak_data_norm":str(Rational(1,n)),"reconstructed_residual_norm":1})
    # Kernel inclusion failure forbids a decoder.
    Hbad=Matrix([[1,0]]); Rbad=Matrix.eye(2)
    witness=e2
    assert Hbad*witness==Matrix.zeros(1,1) and Rbad*witness!=Matrix.zeros(2,1)
    payload={"schema":"marici.kitaev.stable_seam_decoder.v1","status":"pass","cutoffwise_exact_decoder":True,"uniform_decoder_bound":False,"records":records,"kernel_failure_witness":[0,1],"physical_repair_authorized":False,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
