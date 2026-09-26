"""Finite relational controls for the quantified table-fibration proof."""
from itertools import product
from pathlib import Path
import hashlib,json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normal(rows):return tuple(sorted(rows))
def transpose(q):return normal((label,t,s) for label,s,t in q)
def unique(q):return len({(s,t) for label,s,t in q})==len(q)
def fibrate(q,k,dims):
    rest=tuple(i for i in range(3) if i!=k)
    return tuple((a,tuple(sorted(tuple(r[i] for i in rest) for r in q if r[k]==a)))
                 for a in range(dims[k]))
def restore(g,k):
    rest=tuple(i for i in range(3) if i!=k)
    out=[]
    for a,children in g:
        for child in children:
            r=[None]*3;r[k]=a
            for i,x in zip(rest,child):r[i]=x
            out.append(tuple(r))
    return normal(out)
def unpack_reversed(g):
    return normal((label,inner,outer) for outer,children in g for label,inner in children)
def twice(q,dims):return unpack_reversed(fibrate(q,1,dims))
count=0;coordinate_checks=0
for nl,ns,nt in product(range(3),repeat=3):
    dims=(nl,ns,nt);pairs=tuple(product(range(ns),range(nt)))
    # Each endpoint pair is absent or has exactly one of nl labels.
    for assignment in product(range(-1,nl),repeat=len(pairs)):
        q=normal((label,s,t) for label,(s,t) in zip(assignment,pairs) if label>=0)
        assert unique(q)
        for k in range(3):
            marked=(k,fibrate(q,k,dims))
            assert restore(marked[1],marked[0])==q
            coordinate_checks+=1
        q2=twice(q,dims)
        assert q2==transpose(q)
        q4=twice(q2,(nl,nt,ns))
        assert q4==q and unique(q4)
        count+=1
assert count==147
# The exact same unmarked family can have different coordinate origins.
q=((0,0,1),);qt=transpose(q);dims=(2,2,2)
assert q!=qt and unique(q) and unique(qt)
assert fibrate(q,1,dims)==fibrate(qt,2,dims)
assert restore(fibrate(q,1,dims),1)==q
assert restore(fibrate(qt,2,dims),2)==qt
# Wrong orientation and omitted membership obligations.
assert twice(q,dims)!=q
assert any(row[1]!=0 for row in qt) # these rows cannot belong to source fiber 0
# Row labels are not assumed unique; deduplicating by label loses legal rows.
duplicated_label=((0,0,0),(0,0,1))
g=fibrate(duplicated_label,1,dims)
bad=tuple((a,tuple(dict(children).items())) for a,children in g)
assert unique(duplicated_label) and restore(bad,1)!=duplicated_label
# Labels themselves must be retained alongside the other endpoint.
q0=((0,0,0),);q1=((1,0,0),)
def omit_label(q):return tuple((a,tuple(t for label,t in children)) for a,children in fibrate(q,1,dims))
assert q0!=q1 and omit_label(q0)==omit_label(q1)

rp=BASE/'results/agda-TableFibrationCycle.json'
r=json.loads(rp.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
assert r['owner_source_inventory_sha256']['TableFibrationCycle.agda']==sha(BASE/'agda/TableFibrationCycle.agda')
c=json.loads((BASE/'results/table-fibration-formal-audit.json').read_text(encoding='utf-8-sig'))
assert c['positive_receipt_sha256'].lower()==sha(rp)
assert len(c['controls'])==2
for control in c['controls']:
    assert control['correctly_rejected'] and control['exit_code']!=0
    assert control['source_sha256'].lower()==sha(BASE/f"agda/negative/{control['module']}.agda")
packet={
 'status':'marked-fibration-four-step-table-path-checked',
 'obligations':['forward realization','route/coherencer compatibility','readout descent'],
 'tables':count,'coordinate_roundtrips':coordinate_checks,
 'carrier_cardinalities':[0,1,2],
 'formal_receipt_sha256':sha(rp),
 'source_sha256':sha(BASE/'agda/TableFibrationCycle.agda'),
 'checker_sha256':sha(Path(__file__).resolve()),
 'controls':['unmarked coordinate ambiguity','incorrect endpoint wiring',
             'incorrect fiber membership','duplicate row labels must not merge',
             'enclosed row labels must not be erased'],
 'scope':'Unordered tables; formal families include empty fibers. Generic recovery and univalent table-data equality checked; original Resolve and fully retained derivation equality not claimed.',
 'supplied_structure':['HoTT dependent sums, identity types and univalence',
                       'three column maps and selector',
                       'endpoint wiring convention for the four-step cycle'],
}
(BASE/'results/table-fibration.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {count} tables, {coordinate_checks} marked roundtrips, two/four-step and information-loss controls; source-bound formal closure.')
