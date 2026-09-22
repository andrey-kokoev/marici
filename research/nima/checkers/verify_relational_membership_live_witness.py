"""Independent replay of compiled admission, faithful selector and relations."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def compose(first,second):
    succ=defaultdict(set)
    for a,b in second:succ[a].add(b)
    return {(a,c) for a,b in first for c in succ[b]}
def transpose(r):return {(b,a) for a,b in r}
def main():
    cp=OUT/'relational-membership-live-witness-contract.json';c=load(cp)
    rp=OUT/'relational-membership-live-witness.json';r=load(rp)
    pp=OUT/'relational-live-witness-runtime.json';packet=load(pp)
    assert r['contract_sha256']==sha(cp) and r['runtime_sha256']==sha(pp)
    assert c['input_sha256']==sha(OUT/'causal-interface-construction.json')
    assert c['input_contract_sha256']==sha(OUT/'causal-interface-construction-contract.json')
    data=load(OUT/'causal-interface-construction.json');parent=load(OUT/'causal-interface-construction-contract.json')
    assert packet['context_sha256']==digest(parent['context'])
    labels=packet['labels'];assert labels==c['labels']==parent['labels'] and len(labels)==18
    views=[tuple(data['naive_local_partitions'][n][i] for n in c['local_view_order']) for i in range(70)]
    bits=[s[1] for s in data['states']];keys=list(zip(views,bits));assert len(set(keys))==70
    admitted=set(map(tuple,packet['admitted_view_tuples']));assert admitted==set(views) and len(admitted)==61
    rows={}
    for row in packet['lifted_rows']:
        assert set(row)=={'views','origin','output','transitions'}
        assert type(row['origin']) is int and row['origin'] in (0,1)
        assert all(type(v) is int for v in row['views'])
        key=tuple(row['views']),row['origin'];assert key not in rows;rows[key]=row
        assert len(row['transitions'])==18
    assert set(rows)==set(keys)
    for i,key in enumerate(keys):
        assert rows[key]['output']==data['outputs'][i]
        for label,(accepted,j) in enumerate(data['transitions'][i]):
            assert rows[key]['transitions'][label]==[accepted,list(views[j]),bits[j]]
            assert bits[j]==bits[i]
    carriers=[sorted(set(data['naive_local_partitions'][n])) for n in c['local_view_order']]
    checks=0
    for v in product(*carriers):
        source_fiber={i for i,w in enumerate(views) if w==v}
        assert (v in admitted)==bool(source_fiber)
        for b in (0,1):assert ((v,b) in rows)==any(bits[i]==b for i in source_fiber)
        checks+=1
    assert checks==r['all_local_tuples_checked']==115412
    fibers=defaultdict(set)
    for i,v in enumerate(views):fibers[v].add(data['new_partition'][i])
    assert Counter(map(len,fibers.values()))=={1:52,2:9}
    strata=[(label,accepted) for label in range(18) for accepted in (False,True)]
    original=[{(i,j) for i,row in enumerate(data['transitions']) for a,j in [row[l]] if a==accepted} for l,accepted in strata]
    def image(rel):return {(views[i],views[j]) for i,j in rel}
    def faithful(rel):return {(keys[i],keys[j]) for i,j in rel}
    failures=0
    for a,b in product(original,repeat=2):
        actual=image(compose(a,b));coarse=compose(image(a),image(b))
        assert actual<=coarse;failures+=actual!=coarse
        assert faithful(compose(a,b))==compose(faithful(a),faithful(b))
        assert transpose(compose(a,b))==compose(transpose(b),transpose(a))
    assert failures==r['existential_projection_composition_failures']==12
    for rel in original:
        assert image(transpose(rel))==transpose(image(rel))
        assert faithful(transpose(rel))==transpose(faithful(rel))
    audit0=original[strata.index((16,True))];audit1=original[strata.index((17,True))]
    assert labels[16:]==[['audit-origin',0],['audit-origin',1]]
    assert compose(audit0,audit1)==set() and len(compose(image(audit0),image(audit1)))==9
    v=tuple(r['explicit_false_path']['views']);assert (v,0) in rows and (v,1) in rows
    first=rows[v,0]['transitions'][16];assert first==[True,list(v),0]
    assert rows[v,0]['transitions'][17]==[False,list(v),0]
    assert first!=[True,list(v),1]
    assert len(rows)==c['bounds']['lifted_rows'] and sum(len(row['transitions']) for row in rows.values())==c['bounds']['transition_cells']
    result={'passed':True,'report_sha256':sha(rp),'admission_tuples_checked':checks,
      'admitted_tuples':61,'selector_bits':1,'lifted_behavioral_rows':70,'composition_failures_without_selector':12,
      'accepted_audit0_then_audit1':'Nine false projected paths; no coherent source execution.',
      'with_selector':'Composition and transpose verified for all 1296 stratum pairs and 36 strata.',
      'scope':'Fixed compiled relation/kernel, truthful initialization and retention; not authentication or arbitrary-future admission.'}
    (OUT/'relational-membership-live-witness-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
