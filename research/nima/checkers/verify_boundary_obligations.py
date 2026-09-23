"""Boundary obligations for affine selectors of rational polyhedral images.

Input source rows and observer are independently expected. Complete subset
replay is exponential; no oracle flags or polynomial complexity are claimed.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,hashlib,gzip
from full_polygon_checkpoint import cross,area,intersection,interpolate
from migration_section_checkpoint import rank
from checked_retirement_interface import migrate,source,freeze
if not __debug__:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def owning_source(plan,state):
    m=plan['m'];_,_,_,caps=source(m,plan['audits'])
    observer=[[Q(1)]*m,[Q(1,128**j) for j in range(m)]]
    joint=observer+[[Q(int(i==j)) for j in range(m)] for i in plan['audits']];rows=[]
    for j,cap in enumerate(caps):
        for sign,bound in ((-1,Q(0)),(1,cap)):rows.append(([Q(sign*int(i==j)) for i in range(m)],bound))
    for r in plan['frames']:
        a=list(map(Q,r['normal']));assert len(a)==len(joint)
        rows.append(([sum(c*row[j] for c,row in zip(a,joint)) for j in range(m)],Q(r['upper'])))
    for a,b in state.public_frames:
        rows.append(([sum(c*row[j] for c,row in zip(a,observer)) for j in range(m)],b))
    return {'context':state.descriptor(),'observer':[[str(x) for x in r] for r in observer],
            'rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows]}
def data(spec):
    O=[tuple(map(Q,row)) for row in spec['observer']];assert len(O)==2 and len(O[0])>=2 and len(O[0])==len(O[1])
    rows=[(tuple(map(Q,r['normal'])),Q(r['upper'])) for r in spec['rows']]
    assert rows and all(len(a)==len(O[0]) for a,b in rows)
    return O,rows
def admitted(O,rows,p,t):
    assert len(t)==len(O[0]) and len(p)==2
    assert all(sum(a*x for a,x in zip(normal,t))<=b for normal,b in rows)
    assert tuple(sum(a*x for a,x in zip(normal,t)) for normal in O)==p

def affine_system(points,lifts):
    # Solve all source-coordinate interpolation equations simultaneously.
    a=[list(p)+[Q(1)]+list(t) for p,t in zip(points,lifts)];r=0;pivots=[]
    for col in range(3):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];q=a[r][col];a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                q=a[i][col];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        pivots.append(col);r+=1
    if any(all(x==0 for x in row[:3]) and any(x!=0 for x in row[3:]) for row in a):return None
    result={'rank':r,'kind':'pinned' if r==3 else 'free'}
    if r==3:result['formula']=[[str(a[j][3+i]) for j in range(3)] for i in range(len(lifts[0]))]
    return result

def reference_check(spec,polygon,packet,point):
    O,rows=data(spec);vertices=[tuple(map(Q,p)) for p in packet['vertices']];lifts=[tuple(map(Q,t)) for t in packet['source_lifts']]
    assert len(vertices)==len(lifts) and len(set(vertices))==len(vertices)
    for p,t in zip(vertices,lifts):
        admitted(O,rows,p,t);assert all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]))
    cells=[];used=set();forms=[];values=[]
    for ids in packet['triangles']:
        assert len(ids)==3 and len(set(ids))==3 and all(type(i) is int and 0<=i<len(vertices) for i in ids)
        used.update(ids);p=[vertices[i] for i in ids];t=[lifts[i] for i in ids];assert area(p)>0
        cells.append((p,t));form=affine_system(p,t);assert form['kind']=='pinned';forms.append(freeze(form['formula']))
        if all(cross(a,b,point)>=0 for a,b in zip(p,p[1:]+p[:1])):values.append(interpolate(p,t,point))
    assert cells and used==set(range(len(vertices))) and sum(area(p) for p,t in cells)==area(polygon)
    for (p,t),(q,u) in combinations(cells,2):
        common=intersection(p,q);assert area(common)==0
        assert all(interpolate(p,t,v)==interpolate(q,u,v) for v in common)
    assert values and len(set(values))==1
    return values[0],{'formulas':len(set(forms)),'triangles':len(cells)}

def obligations(polygon,lifts,forced,point,target):
    N=len(forced);assert N>0;groups={}
    for mask in range(1,1<<N):
        edges=[forced[j] for j in range(N) if mask>>j&1]
        ids=sorted({j for e in edges for j in (e,(e+1)%len(polygon))})
        solved=affine_system([polygon[i] for i in ids],[lifts[i] for i in ids])
        if solved is not None:groups[mask]={'edges':edges,**solved}
    memo={0:[[]]}
    def partitions(mask):
        if mask in memo:return memo[mask]
        bit=mask&-mask;best=[];size=N+1
        for group in groups:
            if group&bit and group&mask==group:
                for tail in partitions(mask^group):
                    candidate=[group]+tail
                    if len(candidate)<size:best=[];size=len(candidate)
                    if len(candidate)==size:best.append(candidate)
        assert best;memo[mask]=best;return best
    covers=partitions((1<<N)-1);minimum=len(covers[0])
    active=sorted({g for partition in covers for g in partition})
    pinned=[g for g in active if groups[g]['kind']=='pinned'];free=[g for g in active if groups[g]['kind']=='free']
    errors=[]
    for g in pinned:
        value=[sum(Q(c)*x for c,x in zip(row,(*point,Q(1)))) for row in groups[g]['formula']]
        errors.append(max(abs(a-b) for a,b in zip(value,target)))
    gate={'status':'UNPINNED_FORMULA_FAMILIES' if free else 'ALL_MINIMUM_COVERS_PINNED',
          'error_lower_bound':None if free else str(min(errors)),
          'pinned_only_probe_distance':str(min(errors)) if errors else None}
    return {'forced_edges':forced,'compatible_groups':[{'mask':mask,**g} for mask,g in groups.items()],
      'minimum_formula_lower_bound':minimum,'minimum_partitions':covers,
      'unresolved_groups':free,'error_gate':gate}

def check(spec,expected_point,packet):
    assert packet['source_digest']==digest(spec) and packet['point']==expected_point
    O,rows=data(spec);m=len(O[0]);polygon=[tuple(map(Q,p)) for p in packet['polygon']]
    lifts=[tuple(map(Q,t)) for t in packet['vertex_lifts']];assert len(polygon)==len(lifts)>=3
    assert len(set(polygon))==len(polygon) and area(polygon)>0
    assert all(cross(polygon[i-1],polygon[i],polygon[(i+1)%len(polygon)])>0 for i in range(len(polygon)))
    assert all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]) for p in polygon)
    for p,t in zip(polygon,lifts):admitted(O,rows,p,t)
    assert len(packet['edges'])==len(polygon);forced=[]
    for i,(a,b,proof) in enumerate(zip(polygon,polygon[1:]+polygon[:1],packet['edges'])):
        normal=(b[1]-a[1],a[0]-b[0]);bound=sum(x*y for x,y in zip(normal,a))
        target=tuple(sum(normal[k]*O[k][j] for k in range(2)) for j in range(m))
        w=list(map(Q,proof['weights']));assert len(w)==len(rows) and all(x>=0 for x in w)
        assert tuple(sum(x*n[j] for x,(n,h) in zip(w,rows)) for j in range(m))==target
        assert sum(x*h for x,(n,h) in zip(w,rows))==bound
        active=[n for x,(n,h) in zip(w,rows) if x>0];r=rank([*O,*active]);assert proof['fiber_rank']==r
        if proof['kind']=='forced':assert r==m;forced.append(i)
        else:
            assert proof['kind']=='nonunique' and r<m;p=tuple(map(Q,proof['point']));u,v=[tuple(map(Q,t)) for t in proof['witnesses']]
            assert cross(a,b,p)==0 and all(min(x,y)<=z<=max(x,y) for x,y,z in zip(a,b,p))
            assert p not in (a,b) and u!=v;admitted(O,rows,p,u);admitted(O,rows,p,v)
    point=tuple(map(Q,expected_point));assert len(point)==2
    target,metrics=reference_check(spec,polygon,packet['reference'],point)
    expected=obligations(polygon,lifts,forced,point,target)
    assert packet['analysis']==expected and packet['reference_metrics']==metrics
    return {'reference':metrics,'forced_edges':len(forced),'minimum_formula_lower_bound':expected['minimum_formula_lower_bound'],
            'error_gate':expected['error_gate'],'minimum_partitions':len(expected['minimum_partitions']),
            'subsets_replayed':2**len(forced)-1,'compatible_groups':len(expected['compatible_groups']),
            'certificate_bytes':len(freeze(packet).encode())}

def main():
    cp=OUT/'boundary-obligations-contract.json';pp=OUT/'boundary-obligations-packets.json'
    c=json.loads(cp.read_text());packets=json.loads(pp.read_text());report=json.loads((OUT/'boundary-obligations.json').read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256']
    assert hashlib.sha256(pp.read_bytes()).hexdigest()==report['packets_sha256']
    for p,h in c['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');assert c['plan']==plans[i]
    base=migrate(plans[i],cases[i],retain_lift=True);results=[]
    assert len(c['cases'])==len(packets)==2
    for request,packet in zip(c['cases'],packets):
        state=base
        for frame in request['public_frames']:state=state.refine(frame['normal'],frame['upper'])
        spec=owning_source(plans[i],state);assert spec==request['expected_source']
        assert digest(packet['reference'])==request['reference_digest']
        results.append(check(spec,request['point'],packet))
    assert report['cases']==results
    assert results[0]['error_gate']['error_lower_bound']=='129/1000'
    assert results[1]['reference']['formulas']==3 and results[1]['minimum_formula_lower_bound']==3
    assert results[1]['error_gate']=={'status':'UNPINNED_FORMULA_FAMILIES','error_lower_bound':None,'pinned_only_probe_distance':'45/32'}
    polygon=[tuple(map(Q,p)) for p in packets[1]['polygon']]
    assert len(polygon)==6 and len({tuple(x+y for x,y in zip(polygon[i],polygon[i+3])) for i in range(3)})>1
    result={'passed':True,'cases':results,'nonsymmetric_counterexample':True,
      'scope':'Boundary set-cover lower bounds; finite error gate only when every minimum-cover formula is pinned. Not a complete selector-complexity algorithm.'}
    (OUT/'boundary-obligations-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
