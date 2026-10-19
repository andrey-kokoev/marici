"""Coefficient elimination versus occupied support on actual saved PE witnesses.

No new occupancy law is admitted. The zero-middle calculation is conditional
on interpreting absent occupied support as a zero coefficient response.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results';log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_terminal_pe_independent as independent
    import check_graded_path_rules as graded

hashes={}
def load(path):
    raw=path.read_bytes();hashes[path.relative_to(ROOT).as_posix()]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def rank(matrix):
    rows=[list(map(F,row)) for row in matrix];pivot=0
    for col in range(len(rows[0])):
        found=next((i for i in range(pivot,len(rows)) if rows[i][col]),None)
        if found is None:continue
        rows[pivot],rows[found]=rows[found],rows[pivot]
        value=rows[pivot][col];rows[pivot]=[v/value for v in rows[pivot]]
        for i in range(pivot+1,len(rows)):
            value=rows[i][col]
            if value:rows[i]=[v-value*w for v,w in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==len(rows):break
    return pivot

def equations(pn,ne):
    rows=[]
    for i in range(5):
        row=[0]*15;row[5+i]=1;row[pn[i]]=-1;rows.append(row)
        row=[0]*15;row[10+i]=1;row[5+ne[i]]=-1;rows.append(row)
    return rows

def response(permutation,values):return tuple(values[i] for i in permutation)
def admits(required,occupied):return required<=occupied

def audit_case(label,p,n,e,pn,ne,occupied,reference,geometry,origin):
    assert len({p,n,e})==3 and set((p,n,e))<=reference
    assert p in occupied and e in occupied and n not in occupied
    assert sorted(pn)==sorted(ne)==list(range(5))
    composite=graded.product(pn,ne)
    native_support=frozenset((p,n,e));contracted_support=frozenset((p,e))
    original=equations(pn,ne)
    zero_middle=[[int(j==5+i) for j in range(15)] for i in range(5)]
    endpoints=[]
    for i in range(5):
        row=[0]*10;row[5+i]=1;row[composite[i]]=-1;endpoints.append(row)
    assert rank(original)==10 and rank(endpoints)==5
    assert rank(original+zero_middle)==15
    # Coefficient projection is lossless on this solution space: N is uniquely
    # reconstructed from P. Test each ambient coefficient basis, not just counts.
    for j in range(5):
        source=tuple(F(int(i==j)) for i in range(5))
        middle=response(pn,source);target=response(ne,middle)
        assert target==response(composite,source)
        assert sum(v*v for v in source)==sum(v*v for v in middle)==sum(v*v for v in target)==1
        assert any(middle)
        assert response(graded.inverse(composite),target)==source
        all_values=source+middle+target
        assert all(sum(F(a)*v for a,v in zip(row,all_values))==0 for row in original)
    # Two explicit support policies have exactly the same occupied-blind view.
    view={'endpoints':[p,e],'origin':origin,'grade':0,'geometry':geometry,
          'referenceSupport':sorted(reference),'coefficientMap':list(composite)}
    native={'view':view,'requiredOccupied':native_support}
    extension={'view':dict(view),'requiredOccupied':contracted_support}
    assert native['view']==extension['view'] and native!=extension
    assert not admits(native_support,occupied) and admits(contracted_support,occupied)
    assert admits(native_support,occupied|{n}) and admits(contracted_support,occupied|{n})
    # This last support containment comparison is not permission to apply the
    # experimental rewrite with N occupied: its separate vacancy guard forbids it.
    rp=graded.Reader(0,'proton',p,origin);rn=graded.Reader(1,'neutron',n,origin);re=graded.Reader(2,'electron',e,origin)
    left=graded.Arrow(rp,rn,0,tuple(pn),frozenset((p,n)),frozenset((p,n)),(('PN',False),))
    right=graded.Arrow(rn,re,0,tuple(ne),frozenset((n,e)),frozenset((n,e)),(('NE',False),))
    full=graded.then(left,right)
    short=graded.Arrow(rp,re,0,composite,contracted_support,frozenset(reference),(('PE-contraction',False),))
    assert graded.transfer(full)==graded.transfer(short)
    for arrow in (full,short):
        reverse=arrow.reverse()
        assert reverse.occupied==arrow.occupied and reverse.reference==arrow.reference
        assert reverse.permutation==graded.inverse(arrow.permutation)
        assert admits(reverse.occupied,occupied)==admits(arrow.occupied,occupied)
        assert reverse.reverse()==arrow
    return {'case':label,'origin':origin,'endpoints':[p,e],'referenceNeutron':n,'nativeSupport':sorted(native_support),
            'contractedSupport':sorted(contracted_support),'referenceSupport':sorted(reference),
            'compositeMap':list(composite),'ambientCoefficientSolutionDimensions':{'native':5,'eliminatedEndpoints':5,'zeroMiddle':0},
            'nativeSupportSatisfied':False,'experimentalSupportSatisfied':True,'sameOccupancyBlindView':True}

probe=load(BASE/'terminal-pe-probe/verification.json')
hydrogen=load(BASE/'hydrogen-edge-attachment/verification.json')
cases=[]
for i,h in enumerate(hydrogen['rows']):
    p,n,e=h['packets'];pb,nb,eb=h['bodies']
    assert [body['species'] for body in h['bodies']]==['proton','neutron','electron']
    pn=tuple(independent.MAPS['PN']);ne=tuple(independent.MAPS['NE'])
    assert response(pn,p['permutation'])==tuple(n['permutation'])
    assert response(ne,n['permutation'])==tuple(e['permutation'])
    assert p['origin']==n['origin']==e['origin']
    cases.append(audit_case(f'H-1 marking {i}',pb['cell'],nb['cell'],eb['cell'],pn,ne,
                           {pb['cell'],eb['cell']},{pb['cell'],nb['cell'],eb['cell']},
                           [body['aliases'] for body in h['bodies']],p['origin']))
for isotope in ('n15','ne22'):
    base=BASE/f'reference-{isotope}-search';summary=load(base/'verification.json')
    row=next(row for row in summary['rows'] if row['witnessFile'])
    witness=load(base/row['witnessFile'])['witness']
    packets={p['id']:p for p in witness['packets']};charts={int(c['id'].split('-')[-1]):c for c in witness['charts']}
    operations={op['id']:op for op in witness['operations']}
    for deletion in probe['deletions']:
        if deletion['sourceIsotope']!=isotope or not deletion['variants']['electron-and-proton-record-terminal']['passesHypotheticalChecks']:continue
        occupied={charts[packets[i]['chart']]['cell'] for i in deletion['selectedPackets']}
        for shortcut in deletion['shortcuts']:
            if not shortcut['recordTerminal']:continue
            pn,ne=(operations[i] for i in shortcut['nativeFactors'])
            assert pn['kind']=='PN' and ne['kind']=='NE' and pn['target']==ne['source']
            assert pn['phaseDelta']==ne['phaseDelta']==0
            p,n,e=(packets[i] for i in (pn['source'],pn['target'],ne['target']))
            pc,nc,ec=(charts[item['chart']] for item in (p,n,e))
            assert response(tuple(pn['permutation']),p['permutation'])==tuple(n['permutation'])
            assert response(tuple(ne['permutation']),n['permutation'])==tuple(e['permutation'])
            result=audit_case(f'{isotope} deletion {deletion["deletedNeutron"]["cell"]}: {p["id"]}->{e["id"]}',
                              pc['cell'],nc['cell'],ec['cell'],tuple(pn['permutation']),tuple(ne['permutation']),occupied,
                              {pc['cell'],nc['cell'],ec['cell']},[pc['aliases'],nc['aliases'],ec['aliases']],p['origin'])
            assert result['referenceNeutron']==shortcut['referenceNeutronCell']
            assert result['compositeMap']==shortcut['permutation']
            cases.append(result)
assert len(cases)==30
# The actual guard permits neither blanket support deletion nor occupied-N rewrites.
assert graded.counts['contractions']==6 and graded.counts['negativeControls']==24
# A nonzero endpoint vector cannot satisfy PN with a literal zero middle vector.
source=tuple(map(F,(1,2,3,4,5)));middle=response(tuple(independent.MAPS['PN']),source)
assert middle!=(F(0),)*5
zero_middle_residual=tuple(-v for v in middle)
assert sum(v*v for v in zero_middle_residual)==55
report={'schema':'marici.neutron-support-obligation.v1','status':'pass','local_cases':len(cases),'hydrogen_markings':24,'isotope_shortcuts':6,
 'cases':cases,'ambient_coefficient_basis_checks':5*len(cases),
 'coefficient_elimination':'exact and uniquely liftable; intermediate reference response is determined, not zeroed',
 'occupancy_elimination':'not implied by coefficient projection, metric preservation or reversal',
 'conditional_zero_middle_result':'PN and NE plus zero N response force zero P and E responses',
 'nonzero_fixture_zero_middle_squared_residual':str(sum(v*v for v in zero_middle_residual)),
 'fresh_independent_isotope_positives':sum(case['passes'] for case in independent.results),
 'fresh_support_guard_negative_controls':graded.counts['negativeControls'],
 'scope':'Ambient five-coordinate linear response audit and support-policy separation on saved finite witnesses. Not a physical vacuum model, new occupancy permission, native isotope admission or fresh lattice search.',
 'prerequisite_replay':log.getvalue()}
for path in (Path(__file__),Path(independent.__file__),Path(graded.__file__),ROOT/'research/strominger/neutron-support-obligation-v1.md'):
    hashes[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
report['sourceHashes']=hashes
out=BASE/'neutron-support-obligation';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('cases','prerequisite_replay','sourceHashes')},indent=2))
