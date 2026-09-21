"""Read-only audit of the Voevodsky numerical adapter's output conventions."""
from pathlib import Path
import sys
import cmath
import json

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky'))
from clark_feature_evaluator import ClarkFeatureEvaluator, Shell


def exact(left,right,z):
    out=[]
    for degree in (0,1):
        for sigma in (1,-1):
            a=-1+sigma*1j*z
            if degree==0:
                value=(cmath.exp(a*right)-cmath.exp(a*left))/a
            else:
                value=(cmath.exp(a*right)*(a*right-1)-cmath.exp(a*left)*(a*left-1))/a**2
            out.append(value)
    return out


def main():
    left,right=0.1,0.4
    ev=ClarkFeatureEvaluator([Shell(left,right)],lambda x:cmath.exp(-x),quadrature=4096)
    z,w=0.7+1.4j,0.3+1.1j
    expected_z,expected_w=exact(left,right,z),exact(left,right,w)
    raw_z,raw_w=ev.interval_feature(left,right,z),ev.interval_feature(left,right,w)
    reorder=lambda h:(h[0],h[2],h[1],h[3])
    raw_error=max(abs(a-b) for a,b in zip(raw_z,expected_z))
    repaired_error=max(abs(a-b) for a,b in zip(reorder(raw_z),expected_z))
    assert raw_error>1e-2 and repaired_error<1e-8
    twice_C=((0,0,-1,1),(0,0,-1,1),(-1,-1,0,0),(1,1,0,0))
    kernel=lambda hu,hv:sum(hu[i].conjugate()*twice_C[i][j]*hv[j]/2
                           for i in range(4) for j in range(4))/(-1j*(z-w.conjugate()))
    expected_kernel=kernel(expected_w,expected_z)
    repaired_kernel=kernel(reorder(raw_w),reorder(raw_z))
    assert abs(expected_kernel-repaired_kernel)<1e-8
    smoke_convention=ev.divided_difference([(left,right)],[(left,right)],w,z,twice_C)
    assert abs(smoke_convention-expected_kernel)>1e-4
    result={
        'schema':'marici.nima.clark-evaluator-conventions.v1','audit_passed':True,
        'upstream_convention_check_passed':False,
        'observed_order':['+,0','+,1','-,0','-,1'],
        'declared_clark_order':['+,0','-,0','+,1','-,1'],
        'smoke_test_matrix_is_twice_clark_coefficient':True,
        'raw_component_error':raw_error,'reordered_component_error':repaired_error,
        'reordered_normalized_kernel_error':abs(expected_kernel-repaired_kernel),
        'smoke_convention_kernel_error':abs(smoke_convention-expected_kernel),
        'scope':'Closed-form exp(-x) compact-shell numerical regression; not interval certification or completed theta normalization. Upstream files unchanged.'}
    out=ROOT/'research/nima/results/clark-evaluator-conventions.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
