"""Cross-check the formal integer encoding against the rational source law.
This is a checked interface contract, not extracted Agda execution.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
    src=ROOT/'agda/InterfaceRecordCompletion.agda'
    receipt=json.loads((ROOT/'results/agda-InterfaceRecordCompletion.json').read_text(encoding='utf-8-sig'))
    digest=hashlib.sha256(src.read_bytes()).hexdigest()
    assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
    assert receipt['source_sha256']==digest
    seeds=[(0,)*12,(1,-1)+(0,)*10,tuple(i*i-5*i for i in range(12))]
    seeds += [tuple(int(i==j) for i in range(12)) for j in range(12)]
    count=0
    for exponent in range(3):
        for nums in seeds:
            a,b=nums[:2];outside=sum(nums[2:]);total=a+(b+outside)
            output=(total,)*12;next_exponent=exponent+1
            decoded=tuple(F(v,12**exponent) for v in nums)
            target=sum(decoded)/12
            assert tuple(F(v,12**next_exponent) for v in output)==(target,)*12
            observed_next=(output[0],output[1],sum(output[2:]),next_exponent)
            local_next=(total,total,10*total,next_exponent)
            assert observed_next==local_next
            # Prior packet used exterior mean; the formal package stores total.
            mean=F(outside,10*12**exponent)
            assert (decoded[0]+decoded[1]+10*mean)/12==target
            count+=1
    result=dict(schema='marici.nima.interface-record-completion.v1',status='pass',
        encoding_checks=count,formal_source_sha256=digest,
        fresh_agda_receipt='results/agda-InterfaceRecordCompletion.json',
        formal_results=['commutes for every encoded signed-integer state',
                        'no-coarse-law: no function on the two-coefficient view reproduces all next observations',
                        'native next-witness constructed from two derived routes, not seeded',
                        'observation keeps complete source and supplied function in retained expression'],
        declared_seeds=['initial full state','full update function','observation function','local update function'],
        scope='Application-extended native runtime, not selection by the frozen rule set. Scalar coefficients with denominator 12^n; not all real/complex states. Rational interface checks are independent, not code extraction.')
    (ROOT/'results/interface-record-completion.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
