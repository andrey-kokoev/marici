"""Independent dense source replay of the audit-aware section; no engine import."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def image(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def section(m,point,s):
    pins={j:Q(h) for j,h in s['pins']};assert len(pins)==len(s['pins'])
    assert all(type(j) is int and 0<=j<m and 0<=h<=100+2*j for j,h in pins.items())
    caps=[Q(0) if j in pins else Q(100+2*j) for j in range(m)]
    slopes=[Q(1,128**j) for j in range(m)]
    offset=(sum(pins.values(),Q(0)),sum(h*slopes[j] for j,h in pins.items()))
    residual=tuple(a-b for a,b in zip(point,offset))
    assert list(map(Q,s['offset']))==list(offset) and list(map(Q,s['residual_point']))==list(residual)
    answer=s['residual_membership']
    if not answer['admitted']:
        sep=answer['separator'];a=tuple(map(Q,sep['normal']));bound=sum(cap*max(Q(0),a[0]+a[1]*r) for cap,r in zip(caps,slopes))
        assert bound==Q(sep['upper']) and sum(x*y for x,y in zip(a,residual))>bound
        return None
    l=answer['lift'];k=l['high_prefix'];h=Q(l['high_partial']);j=l['complement_prefix'];r=Q(l['complement_partial']);theta=Q(l['theta'])
    assert 0<=theta<=1
    for index,partial in ((k,h),(j,r)):
        assert 0<=index<=m
        assert partial==0 if index==m else 0<=partial<caps[index]
    high=[cap if n<k else h if n==k else Q(0) for n,cap in enumerate(caps)]
    complement=[cap if n<j else r if n==j else Q(0) for n,cap in enumerate(caps)]
    low=[cap-v for cap,v in zip(caps,complement)]
    assert sum(high)==sum(low)==residual[0]
    assert [sum(x*r for x,r in zip(profile,slopes)) for profile in (low,high)]==list(map(Q,answer['vertical_bounds']))
    x=[pins[n] if n in pins else (1-theta)*low[n]+theta*high[n] for n in range(m)]
    assert all(0<=v<=100+2*n for n,v in enumerate(x)) and image(x)==point
    assert all(x[n]==h for n,h in pins.items());return x

def main():
    cp=OUT/'audited-tail-section-contract.json';rp=OUT/'audited-tail-section.json';pp=OUT/'audited-tail-section-packet.json.gz'
    c,r=load(cp),load(rp);assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    assert sha(Path(__file__).with_name('check_symbolic_tail_interface.py'))==c['engine_sha256']
    assert sha(OUT/'symbolic-tail-interface.json')==c['owning_report_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    checks=0;nontrivial=0
    for case in p['cases']:
        m=case['m'];sparse={j:Q(v) for j,v in case['source_sparse']};x=[sparse.get(j,Q(0)) for j in range(m)]
        assert all(0<=v<=100+2*j for j,v in enumerate(x))
        point=tuple(map(Q,case['point']));assert image(x)==point
        center=section(m,point,case['section']);assert center is not None
        pins={j:Q(v) for j,v in case['section']['pins']};assert all(x[j]==h for j,h in pins.items())
        changed=sum(a!=b for a,b in zip(x,center));assert changed==case['changed_unpinned_count'];nontrivial+=bool(pins and changed)
        for test in case['contraction_checks']:
            t=Q(test['time']);assert 0<=t<=1
            y=[(1-t)*a+t*b for a,b in zip(x,center)]
            assert all(0<=v<=100+2*j for j,v in enumerate(y)) and image(y)==point
            assert [[j,str(y[j])] for j in sorted(pins)]==test['audits']
            assert all(y[j]==x[j] for j in pins)
            assert list(map(Q,test['moments']))==list(point);checks+=1
    failure=p['old_section_audit_failure'];point=tuple(map(Q,failure['point']));x=list(map(Q,failure['source']))
    assert image(x)==point and x[0]==0
    old=section(3,point,failure['old_section']);new=section(3,point,failure['new_section'])
    assert old[0]>0 and new[0]==0 and new==x
    denied=p['target_without_common_audit'];point=tuple(map(Q,denied['point']))
    assert point==image([Q(100+2*j) for j in range(3)])
    assert section(3,point,denied['section']) is None
    a=list(map(Q,denied['full_separator']['normal']));b=Q(denied['full_separator']['upper'])
    pins={j:Q(h) for j,h in denied['section']['pins']}
    bound=sum(h*(a[0]+a[1]*Q(1,128**j)) for j,h in pins.items())
    bound+=sum(Q(100+2*j)*max(Q(0),a[0]+a[1]*Q(1,128**j)) for j in range(3) if j not in pins)
    assert bound==b and sum(x*y for x,y in zip(a,point))>b
    assert checks==r['contraction_checks']==128 and nontrivial==r['nontrivial_audited_contractions']==9
    result={'passed':True,'report_sha256':sha(rp),'conditional_sections':len(p['cases']),'audited_contractions':checks,
      'nontrivial_audited_contractions':nontrivial,'old_unobserved_audit_change_detected':True,'empty_common_audit_fiber_certified':True,
      'scope':c['scope']}
    (OUT/'audited-tail-section-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
