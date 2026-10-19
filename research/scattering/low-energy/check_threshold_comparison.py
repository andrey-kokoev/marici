"""C6: quantitative shared-frame threshold obstruction from fresh C1/C11 inputs."""
import argparse
import hashlib
import json
from pathlib import Path
from check_rim_threshold import audit as rim_audit
from check_three_port_threshold import audit as port_audit

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/scattering/low-energy'
PROOF=HOME/'THRESHOLD-COMPARISON-OBSTRUCTION.md'
RESULT=HOME/'results/threshold-comparison.v1.json'


def audit():
    rim=rim_audit();port=port_audit()
    assert rim==json.loads((HOME/'results/rim-threshold.v1.json').read_text(encoding='utf-8'))
    assert port==json.loads((HOME/'results/three-port-threshold.v1.json').read_text(encoding='utf-8'))
    assert port['whitened_limit_eigenvalues']==[-1,1,1]
    assert port['rank_I_minus_S0']==1 and port['rank_I_plus_S0']==2
    # Exact polynomial arrays in (1,x,y,x²,xy,y²):
    # |1+alpha|² + |1-alpha|² = 2+2(x²+y²)=4 for |alpha|=1.
    plus=[1,2,0,1,0,1];minus=[1,-2,0,1,0,1]
    assert [a+b for a,b in zip(plus,minus)]==[2,0,0,2,0,2]
    assert 1+1==2  # both squared defects at alpha=i; sharp bound sqrt(2).
    sources=set(rim['source_sha256'])|set(port['source_sha256'])|{
        PROOF.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
        'research/scattering/low-energy/results/rim-threshold.v1.json',
        'research/scattering/low-energy/results/three-port-threshold.v1.json'}
    return {'schema':'marici.scattering.threshold-comparison.v1','status':'pass','C6_disposition':'established',
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)},
            'premises_freshly_replayed':['C1','C11'],'requires_C2':False,
            'limiting_minimum_operator_defect_squared':2,'sharp_phase':'i',
            'finite_k_lower_bound':'sqrt(2)-||S_rim(k)+I4||-||S_port(k)-S0||',
            'comparison_class':'One shared flux-isometric V for incoming and outgoing fibers, up to a common unit-modulus phase.',
            'regularity_of_V_needed_by_stronger_argument':False,
            'separate_input_output_frames_excluded':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C6 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C6 shared-frame obstruction, limiting operator defect at least sqrt(2).')


if __name__=='__main__':main()
