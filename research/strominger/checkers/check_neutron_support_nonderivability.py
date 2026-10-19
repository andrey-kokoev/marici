"""Premise audit for the written support-invariant nonderivability theorem."""
from pathlib import Path
import contextlib,io,json,hashlib
ROOT=Path(__file__).resolve().parents[3];log=io.StringIO()
with contextlib.redirect_stdout(log):import check_neutron_support_obligation as prior
g=prior.graded;counts={'cases':0,'inverseMapCancellationCounterexamples':0,'contextSupportChecks':0,'structuralEquationChecks':0,'supportErasureControls':0}
for case in prior.cases:
    p,e=case['endpoints']
    n=case['referenceNeutron'];origin=case['origin']
    rp=g.Reader(0,'proton',p,origin);rn=g.Reader(1,'neutron',n,origin);re=g.Reader(2,'electron',e,origin)
    pn=tuple(prior.independent.MAPS['PN']);ne=tuple(prior.independent.MAPS['NE'])
    A=g.Arrow(rp,rn,0,pn,frozenset((p,n)),frozenset((p,n)),(('PN',False),))
    B=g.Arrow(rn,re,0,ne,frozenset((n,e)),frozenset((n,e)),(('NE',False),))
    inverse=g.Arrow(rn,rp,0,tuple(prior.independent.MAPS['inverse-PN']),A.occupied,A.reference,(('inverse-PN',False),))
    path=g.then(A,B);chi=lambda a:int(n in a.occupied)
    assert path.permutation==tuple(case['compositeMap']) and chi(path)==1
    assert chi(path)==(chi(A)|chi(B))
    assert g.then(g.identity(rp),path)==path==g.then(path,g.identity(re));counts['structuralEquationChecks']+=2
    assert g.then(g.then(A,inverse),A)==g.then(A,g.then(inverse,A));counts['structuralEquationChecks']+=1
    assert path.reverse()==g.then(B.reverse(),A.reverse());counts['structuralEquationChecks']+=1
    assert path.reverse().reverse()==path;counts['structuralEquationChecks']+=1
    # An inverse coefficient pair does NOT cancel its occupied history.
    loop=g.then(A,inverse);identity=g.identity(rp)
    assert g.transfer(loop)==g.transfer(identity)
    assert loop.permutation==g.ID and loop!=identity
    assert chi(loop)==1 and chi(identity)==0
    counts['inverseMapCancellationCounterexamples']+=1
    # Observe support in enclosing admissible contexts; it cannot disappear.
    contexts=(path,g.then(g.identity(rp),path),g.then(path,g.identity(re)),path.reverse(),path.reverse().reverse(),g.then(g.then(A,inverse),path))
    for expression in contexts:
        assert chi(expression)==1;counts['contextSupportChecks']+=1
    contracted=g.Arrow(rp,re,0,path.permutation,frozenset((p,e)),path.reference,(('experimental-PE',False),))
    assert g.transfer(path)==g.transfer(contracted) and chi(contracted)==0
    # A coefficient-only equality would falsely identify these arrows.
    def supported_equal(a,b):return a==b
    assert not supported_equal(path,contracted)
    assert not supported_equal(loop,identity)
    counts['supportErasureControls']+=2;counts['cases']+=1
assert counts['cases']==30
report={'schema':'marici.neutron-support-nonderivability.v1','status':'pass','checks':counts,
 'theorem':'The membership-of-N Boolean invariant is preserved by native supported-path structural laws, so those laws cannot derive its erasure from PN;NE.',
 'coefficient_elimination':'provable; uniquely reconstructs the intermediate response',
 'occupancy_permission':'additional rule or independently justified semantics still required',
 'method':'Written structural-induction proof with exact executable premise checks; not a proof-assistant theorem',
 'native_isotope_admission_changed':False,'prerequisite_replay':log.getvalue()}
paths=[Path(__file__),Path(prior.__file__),Path(g.__file__),ROOT/'research/strominger/neutron-support-nonderivability-v1.md']
report['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/neutron-support-nonderivability';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('sourceHashes','prerequisite_replay')},indent=2))
