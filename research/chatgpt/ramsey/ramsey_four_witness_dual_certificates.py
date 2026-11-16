#!/usr/bin/env python3
"""Generate/check exact rational duals for all 688 profiles excluded by 4-local Hall, triangle and degree constraints.
Generation uses SciPy LP; verification is independent of LP, rational arithmetic only.
"""
import gzip,json,time
from collections import Counter
from fractions import Fraction
from pathlib import Path
import ramsey_fractional_witness_certificate as cert
from ramsey_obstruction_order_audit import solve

SOURCE=cert.constraints

def four_constraints(masks):
    edges,hall,triangles=SOURCE(masks)
    return edges,[(U,idx) for U,idx in hall if len(U)<=4],triangles

cert.constraints=four_constraints
TARGET=Path(__file__).with_name('ramsey_four_witness_dual_certificates.json.gz')

def generate():
    t0=time.time(); records=[]; open_cases=[];counts=Counter()
    for r in range(5):
        for s in cert.support_classes(r)[0]:
            if not solve(s,4,True):
                open_cases.append((r,list(s)))
                counts[(r,'open')]+=1
                continue
            record=cert.derive_dual_certificate(s)
            record['r']=r
            bound=cert.verify_entry(record)
            assert bound>0
            records.append(record)
            counts[(r,'refuted')]+=1
        print('r',r,'refuted',counts[r,'refuted'],'open',counts[r,'open'],'elapsed',round(time.time()-t0,1),flush=True)
    assert len(records)==688 and len(open_cases)==7
    obj={'schema':'ramsey.four-witness-dual-certificate.v1','records':records,'open':open_cases}
    with gzip.open(TARGET,'wt') as fh:json.dump(obj,fh,separators=(',',':'))
    print('saved',TARGET,'bytes',TARGET.stat().st_size,'time',round(time.time()-t0,1))

def verify():
    with gzip.open(TARGET,'rt') as fh:obj=json.load(fh)
    assert obj['schema']=='ramsey.four-witness-dual-certificate.v1'
    c={(x['r'],tuple(x['supports'])):x for x in obj['records']}
    op={(r,tuple(s)) for r,s in obj['open']}
    all_keys={(r,s) for r in range(5) for s in cert.support_classes(r)[0]}
    assert set(c).isdisjoint(op) and (set(c)|op)==all_keys and len(c)==688 and len(op)==7
    bounds=[cert.verify_entry(c[k]) for k in c]
    print('EXACT VERIFIED: 688 four-witness positive rational LP duals, 7 recorded exceptions')
    print('minimum dual bound',min(bounds),'maximum',max(bounds))
    print('Exceptions by r',dict(Counter(r for r,s in op)))
    return True

if __name__=='__main__':
    import sys
    if '--generate' in sys.argv:generate()
    verify()
