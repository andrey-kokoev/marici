"""Full-history stasis versus a reconstructing invariant payload decoder."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from check_four_packet_record_feedback import basis,rank
from check_memory_return_phase_policy import ONE,ZERO,OMEGA,step,plus,project
ROOT=Path(__file__).resolve().parents[1]

def main():
    src=ROOT/'agda/AgreementPolicyBoundary.agda'
    receipt=json.loads((ROOT/'results/agda-AgreementPolicyBoundary.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
    assert receipt['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
    # Two reconstruction contracts: initially D(x,0)=x; after first lossless
    # write D(Px,Qx)=x. Their domains span the 23D physical state sector.
    zero=(F(0),)*12;inputs=[]
    for x in basis(12):
        p=(sum(x)/12,)*12;q=tuple(a-b for a,b in zip(x,p))
        inputs.extend((x+zero,p+q))
        assert tuple(a+b for a,b in zip(p,q))==x
    assert rank(tuple(inputs))==23
    # Hence the only linear decoder on mean-zero records is D(x,w)=x+w.
    physical=[]
    for x in basis(12):physical.append((tuple((a,F(0)) for a in x),(ZERO,)*12))
    for k in range(11):
        physical.append(((ZERO,)*12,tuple((F(int(i==k)-int(i==11)),F(0)) for i in range(12))))
    alternatives=[]
    for name,eta in (('identity',ONE),('sign reversal',(-F(1),F(0))),('third-root',OMEGA)):
        mean_fixed=True;decoded_fixed=True
        for x,w in physical:
            y,v=step(x,w,eta)
            mean_fixed &= project(y)==project(x)
            decoded_fixed &= plus(y,v)==plus(x,w)
        assert decoded_fixed==(eta==ONE) and mean_fixed
        alternatives.append(dict(phase=name,mean_readout_fixed=mean_fixed,reconstructed_payload_fixed=decoded_fixed))
    result=dict(schema='marici.nima.agreement-payload-policy.v1',status='pass',
        formal_boundary='Existing typed tetrahedral comparison has equal route effects and invariant decoded payload, yet exchange changes its retained history. A blanket effect-agreement-implies-record-stasis policy is refuted.',
        reconstruction_span_dimension=23,
        conditional_unique_decoder='D(x,w)=x+w on Pw=0, forced by linear reconstruction both before and after first empty-bank write.',
        phase_controls=alternatives,
        implication='Preserving this reconstructing payload decoder selects eta=1 without demanding that every agreeing native history be frozen.',
        remaining_assumptions=['Identify the source decoded payload with this numerical coefficient payload.',
                               'Use a fixed linear decoder on the stated current-state sector, rather than a history-dependent decoder.',
                               'Retain the declared port, metric and lossless first-write contract.'],
        scope='A checked source distinction plus a conditional numerical adapter selection, not an end-to-end native-to-physical identification.')
    (ROOT/'results/agreement-payload-policy.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
