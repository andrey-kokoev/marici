"""Independent exact language-upgrade and fiber-forgetting replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(A):
    if not A:return Q(1)
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
@lru_cache(None)
def vertices(rows):
    answer=set()
    if any(not any(a) and b<0 for a,b in rows):return ()
    for selected in combinations(rows,3):
        matrix=[list(a) for a,b in selected];rhs=[b for a,b in selected];d=det(matrix)
        if d==0:continue
        x=tuple(det([row[:j]+[rhs[i]]+row[j+1:] for i,row in enumerate(matrix)])/d for j in range(3))
        if all(dot(a,x)<=b for a,b in rows):answer.add(x)
    return tuple(sorted(answer))
def cross(a,b,x):return (b[0]-a[0])*(x[1]-a[1])-(b[1]-a[1])*(x[0]-a[0])
def extreme(points):
    points=sorted(set(points))
    if len(points)<2:return set(points)
    out=set()
    for a,b in combinations(points,2):
        signs=[cross(a,b,x) for x in points]
        if min(signs)>=0 or max(signs)<=0:
            on_line=[x for x,s in zip(points,signs) if s==0];out.add(min(on_line));out.add(max(on_line))
    return out

def polygon_constraints(points):
    points=sorted(set(points))
    if not points:return (((Q(0),Q(0)),Q(-1)),)
    out=set()
    # Box plus all supporting lines handles polygons, segments and points.
    for j in (0,1):
        for sign in (-1,1):
            a=tuple(Q(sign if i==j else 0) for i in range(2));out.add((a,max(dot(a,x) for x in points)))
    for x,y in combinations(points,2):
        a=(y[1]-x[1],x[0]-y[0]);b=dot(a,x)
        if all(dot(a,z)<=b for z in points):out.add((a,b))
        if all(dot(a,z)>=b for z in points):out.add((tuple(-v for v in a),-b))
    return tuple(sorted(out))
def decoded(rows):return tuple((tuple(map(Q,r['a'])),Q(r['b'])) for r in rows)

def main():
    cp=OUT/'query-language-upgrade-contract.json';rp=OUT/'query-language-upgrade.json';pp=OUT/'query-language-upgrade-packet.json.gz'
    c,r=load(cp),load(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    owning_path=ROOT/'grothendieck/results/query-relative-tail-interface.json';assert sha(owning_path)==c['source_interface_sha256'];own=load(owning_path)
    source=tuple((tuple(map(Q,a)),Q(b)) for a,b in zip(own['source_constraints']['A'],own['source_constraints']['b']))
    w=tuple(map(Q,own['objective_coefficients']));M=tuple(tuple(map(Q,row)) for row in p['forward']);I=tuple(tuple(map(Q,row)) for row in p['inverse'])
    assert M==((Q(1),Q(1),Q(1)),w,(Q(1),Q(0),Q(0)))
    for left,right in ((M,I),(I,M)):
        assert all(sum(left[i][k]*right[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
    def obs(x):return sum(x),dot(w,x)
    def pull(frame):
        a,b=frame;return tuple(a[0]+a[1]*v for v in w),b
    def rows_from_polygon(q):return source+tuple(pull(f) for f in polygon_constraints(q))
    center=(Q(1000),)*3;point=obs(center)
    eq=[((Q(1),Q(0)),point[0]),((Q(-1),Q(0)),-point[0]),((Q(0),Q(1)),point[1]),((Q(0),Q(-1)),-point[1])]
    histories={'initial':[],'collision-fiber':eq,'zero-fiber':[((Q(1),Q(0)),Q(0))],
      'constant-S-segment':[((Q(1),Q(0)),Q(3000)),((Q(-1),Q(0)),Q(-3000))]}
    for name,trace in own['traces'].items():
        frames=[]
        for j,state in enumerate(trace):
            frame=state['frame'];frames.append((tuple(map(Q,frame['coefficients'])),Q(frame['upper'])))
            histories[name+'/'+str(j+1)]=list(frames)
    total=0
    for record in p['upgrades']:
        assert decoded(record['frames'])==tuple(histories[record['name']])
        direct=source+tuple(pull(f) for f in histories[record['name']]);dv=vertices(direct)
        q=[tuple(map(Q,v)) for v in record['polygon']];assert set(q)==extreme(obs(x) for x in dv)
        upgraded=decoded(record['upgraded_rows'])
        assert upgraded[:9]==tuple((tuple(sum(a[k]*I[k][j] for k in range(3)) for j in range(3)),b) for a,b in source)
        assert len(upgraded)<=c['bounds']['upgraded_rows']
        uv=vertices(upgraded);assert uv==tuple(tuple(map(Q,v)) for v in record['upgraded_vertices'])
        assert set(uv)=={tuple(dot(row,x) for row in M) for x in dv}
        assert len(uv)==len(record['source_lifts'])<=c['bounds']['upgraded_vertices']
        for u,encoded in zip(uv,record['source_lifts']):
            x=tuple(map(Q,encoded));assert x==tuple(dot(row,u) for row in I)
            assert all(dot(a,x)<=b for a,b in direct);total+=1
        values=[x[0] for x in dv]
        truth='INCONSISTENT' if not values else 'ALWAYS_TRUE' if max(values)<=1000 else 'ALWAYS_FALSE' if min(values)>1000 else 'MIXED'
        assert truth==record['x1_le_1000']
        assert all(max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=8192 for a,b in upgraded for v in (*a,b))
    low_frame=((Q(1),Q(0),Q(0)),Q(1000));high_frame=((Q(-1),Q(0),Q(0)),Q(-1000));fiber=source+tuple(pull(f) for f in eq)
    expected={'no_hidden_restriction':source,'redundant_bin_cap':source+(((Q(1),Q(0),Q(0)),source[3][1]),),
      'hidden_lower_half':fiber+(low_frame,),'hidden_upper_half':fiber+(high_frame,),
      'hidden_bound_then_S_le_500':source+(low_frame,((Q(1),Q(1),Q(1)),Q(500)))}
    unsafe=0
    for record in p['downgrades']:
        current=decoded(record['current_rows']);assert current==expected[record['name']]
        cv=vertices(current);assert cv==tuple(tuple(map(Q,v)) for v in record['current_vertices'])
        q=[tuple(map(Q,v)) for v in record['polygon']];assert set(q)==extreme(obs(x) for x in cv)
        reopened=rows_from_polygon(q);rv=vertices(reopened)
        assert rv==tuple(tuple(map(Q,v)) for v in record['reopened_vertices'])
        safe=all(all(dot(a,x)<=b for a,b in current) for x in rv)
        assert safe==record['safe_to_forget_fiber_constraints']
        if not safe:
            x=tuple(map(Q,record['obstruction']));assert all(dot(a,x)<=b for a,b in reopened)
            assert any(dot(a,x)>b for a,b in current);unsafe+=1
    collision=p['hidden_fiber_collision'];assert tuple(map(Q,collision['common_stored_lift']))==center
    low=tuple(map(Q,collision['low_witness']));high=tuple(map(Q,collision['high_witness']));alpha=Q(collision['new_query_upper'])
    assert obs(low)==obs(high)==obs(center)==tuple(map(Q,collision['observable']))
    assert all(dot(a,low)<=b for a,b in fiber+(low_frame,)) and low[0]<=alpha<1000
    assert all(dot(a,high)<=b for a,b in fiber+(high_frame,)) and high[0]>1000
    assert all(dot(a,center)<=b for a,b in fiber+(low_frame,high_frame))
    assert all(x[0]>alpha for x in vertices(fiber+(high_frame,)))
    certificate=p['redundancy_certificate'];rows=certificate['rows'];rhs=list(map(Q,certificate['rhs']));weights=list(map(Q,certificate['multipliers']))
    assert all(v>=0 for v in weights)
    assert tuple(sum(weights[i]*rows[i][j] for i in range(3)) for j in range(3))==(1,0,0)
    assert dot(rhs,weights)==500<=1000
    false=tuple(map(Q,own['rectangle_false_point']));assert not vertices(rows_from_polygon([false]))
    assert len(p['upgrades'])==9 and len(p['downgrades'])==5 and unsafe==2
    result={'passed':True,'report_sha256':sha(rp),'exact_upgrade_cases':9,'verified_source_lifts':total,
      'downgrade_cases':5,'unsafe_downgrades':unsafe,'lawful_forgetting_after_visible_refinement':True,
      'conclusion':'Model-based upgrades are exact under fiber saturation; identical polygons and stored lifts do not establish that invariant.',
      'scope':c['scope']}
    (OUT/'query-language-upgrade-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
