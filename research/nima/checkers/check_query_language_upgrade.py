"""Recover source possibilities from a saturated observable interface.

The source model is immutable and available. No selected source lift is treated
as the actual source. Hidden restrictions must survive a language downgrade.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def solve(A,b):
    n=len(b);m=[list(a)+[v] for a,v in zip(A,b)]
    for j in range(n):
        k=next((k for k in range(j,n) if m[k][j]),None)
        if k is None:return None
        m[k],m[j]=m[j],m[k];d=m[j][j];m[j]=[v/d for v in m[j]]
        for k in range(n):
            if k!=j:
                d=m[k][j];m[k]=[a-d*b for a,b in zip(m[k],m[j])]
    return tuple(row[-1] for row in m)
def vertices(rows):
    out=set()
    if any(not any(a) and b<0 for a,b in rows):return []
    for selected in combinations(rows,3):
        x=solve([a for a,b in selected],[b for a,b in selected])
        if x is not None and all(dot(a,x)<=b for a,b in rows):out.add(x)
    return sorted(out)
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull(points):
    points=sorted(set(points))
    if len(points)<2:return points
    lo=[];hi=[]
    for x in points:
        while len(lo)>1 and cross(lo[-2],lo[-1],x)<=0:lo.pop()
        lo.append(x)
    for x in reversed(points):
        while len(hi)>1 and cross(hi[-2],hi[-1],x)<=0:hi.pop()
        hi.append(x)
    return lo[:-1]+hi[:-1]
def visible_rows(poly):
    if not poly:return [((Q(0),Q(0)),Q(-1))]
    if len(poly)==1:
        s,f=poly[0];return [((Q(1),Q(0)),s),((Q(-1),Q(0)),-s),((Q(0),Q(1)),f),((Q(0),Q(-1)),-f)]
    if len(poly)==2:
        a,b=poly;d=tuple(y-x for x,y in zip(a,b));n=(-d[1],d[0]);v=dot(n,a)
        return [(n,v),(tuple(-x for x in n),-v),(d,dot(d,b)),(tuple(-x for x in d),-dot(d,a))]
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        n=(b[1]-a[1],a[0]-b[0]);out.append((n,dot(n,a)))
    return out

def main():
    path=ROOT/'grothendieck/results/query-relative-tail-interface.json';p=load(path)
    A=[tuple(map(Q,row)) for row in p['source_constraints']['A']];b=list(map(Q,p['source_constraints']['b']));source=list(zip(A,b));w=list(map(Q,p['objective_coefficients']))
    contract={'schema':'query-language-upgrade-v1','source_interface_sha256':sha(path),
      'old_observables':['S=sum x_i','F=sum lower_kernel_i*x_i'],'new_observable':'x1',
      'positive_admission_invariant':'Initial carrier P is complete for the declared model. All previous evidence is a pullback of an old-observable halfspace. Current carrier is therefore P intersect L^-1(Q).',
      'constructor_inputs':'Only the immutable source inequalities, L and the current polygon Q; no old frame history or selected source lift.',
      'upgrade_rule':'Reconstruct P intersect L^-1(Q), then express it in (S,F,x1). Do not choose an actual source point.',
      'downgrade_rule':'A carrier C may be replaced by L(C) only if C equals P intersect L^-1(L(C)); otherwise preserve fiber constraints or refuse exact upgrading later.',
      'tests':['all owning retained polygons','singleton kernel-collision fiber','zero fiber','constant-S segment','invalid observable singleton',
               'same Q and same stored lift with opposite hidden restrictions','unsafe downgrade after a new bin frame','redundancy after a visible total-mass frame'],
      'bounds':{'source_rows':9,'current_polygon_vertices':16,'upgraded_rows':32,'upgraded_vertices':64,'retained_rational_bits':8192},
      'scope':'Exact possibilities in the owning moment relaxation. No actual-prime selection, authentication or physical action authority.'}
    cp=OUT/'query-language-upgrade-contract.json';save(cp,contract)
    d=w[1]-w[2];assert d
    inverse=[(Q(0),Q(0),Q(1)),(-w[2]/d,1/d,(w[2]-w[0])/d),(w[1]/d,-1/d,(w[0]-w[1])/d)]
    forward=[(Q(1),Q(1),Q(1)),tuple(w),(Q(1),Q(0),Q(0))]
    assert all(dot(row,[inverse[k][j] for k in range(3)])==int(i==j) for i,row in enumerate(forward) for j in range(3))
    def obs(x):return sum(x),dot(w,x)
    def pullback(frame):
        a,bound=frame;return tuple(a[0]+a[1]*v for v in w),bound
    def from_polygon(poly):return source+[pullback(f) for f in visible_rows(poly)]
    peak={'rows':0,'vertices':0,'rational_bits':0}
    def upgrade(poly):
        poly=hull(poly);assert len(poly)<=16
        rows=[(tuple(sum(a[k]*inverse[k][j] for k in range(3)) for j in range(3)),rhs) for a,rhs in source]
        rows += [(tuple(a)+(Q(0),),rhs) for a,rhs in visible_rows(poly)]
        verts=vertices(rows);projected=hull([u[:2] for u in verts])
        if projected!=poly:raise ValueError('INVALID_OBSERVABLE_STATE')
        peak['rows']=max(peak['rows'],len(rows));peak['vertices']=max(peak['vertices'],len(verts))
        entries=[v for a,rhs in rows for v in (*a,rhs)]+[v for x in verts for v in x]
        peak['rational_bits']=max(peak['rational_bits'],max(max(abs(v.numerator).bit_length(),v.denominator.bit_length()) for v in entries))
        assert len(rows)<=32 and len(verts)<=64 and peak['rational_bits']<=8192
        return rows,verts
    scenarios=[('initial',[],[tuple(map(Q,v['observable'])) for v in p['initial_polygon']])]
    for name,trace in p['traces'].items():
        frames=[]
        for i,state in enumerate(trace):
            f=state['frame'];frames.append((tuple(map(Q,f['coefficients'])),Q(f['upper'])))
            scenarios.append((name+'/'+str(i+1),list(frames),[tuple(map(Q,v['observable'])) for v in state['polygon']]))
    center=(Q(1000),)*3;point=obs(center)
    point_frames=visible_rows([point]);scenarios.append(('collision-fiber',point_frames,[point]))
    scenarios.append(('zero-fiber',[((Q(1),Q(0)),Q(0))],[(Q(0),Q(0))]))
    segment=[(Q(3000),Q(3000)*min(w)),(Q(3000),Q(3000)*max(w))]
    scenarios.append(('constant-S-segment',[((Q(1),Q(0)),Q(3000)),((Q(-1),Q(0)),Q(-3000))],segment))
    records=[]
    for name,frames,poly in scenarios:
        rows,vs=upgrade(poly)
        # Direct retained-history oracle is deliberately outside upgrade().
        direct=vertices(source+[pullback(f) for f in frames])
        assert set(vs)=={(sum(x),dot(w,x),x[0]) for x in direct}
        original_lifts=[tuple(dot(row,u) for row in inverse) for u in vs]
        assert all(all(dot(a,x)<=rhs for a,rhs in source) for x in original_lifts)
        values=[u[2] for u in vs]
        truth='INCONSISTENT' if not values else 'ALWAYS_TRUE' if max(values)<=1000 else 'ALWAYS_FALSE' if min(values)>1000 else 'MIXED'
        records.append({'name':name,'frames':[{'a':list(map(str,a)),'b':str(rhs)} for a,rhs in frames],
          'polygon':[list(map(str,u)) for u in hull(poly)],'upgraded_rows':[{'a':list(map(str,a)),'b':str(rhs)} for a,rhs in rows],
          'upgraded_vertices':[list(map(str,u)) for u in vs],'source_lifts':[list(map(str,x)) for x in original_lifts],
          'x1_le_1000':truth})
    assert next(v for v in records if v['name']=='collision-fiber')['x1_le_1000']=='MIXED'
    assert next(v for v in records if v['name']=='zero-fiber')['x1_le_1000']=='ALWAYS_TRUE'
    false_point=tuple(map(Q,p['rectangle_false_point']))
    try:upgrade([false_point])
    except ValueError as e:assert str(e)=='INVALID_OBSERVABLE_STATE'
    else:raise AssertionError('invalid observable point upgraded')
    # Same old geometry AND same feasible stored lift, different source fibers.
    collision=p['out_of_language_collision'];ends=sorted([tuple(map(Q,collision[k])) for k in ('left','right')],key=lambda x:x[0]);low,high=ends
    assert low[0]<1000<high[0] and obs(low)==obs(high)==point
    threshold=(low[0]+1000)/2
    fiber=from_polygon([point]);low_frame=((Q(1),Q(0),Q(0)),Q(1000));high_frame=((Q(-1),Q(0),Q(0)),Q(-1000))
    low_v=vertices(fiber+[low_frame]);high_v=vertices(fiber+[high_frame])
    assert hull([obs(x) for x in low_v])==hull([obs(x) for x in high_v])==[point]
    assert all(dot(a,center)<=rhs for a,rhs in fiber+[low_frame,high_frame])
    assert min(x[0] for x in low_v)<=threshold<min(x[0] for x in high_v)
    # A visible refinement can make an old hidden restriction redundant again.
    cases=[('no_hidden_restriction',source),('redundant_bin_cap',source+[( (Q(1),Q(0),Q(0)),b[3])]),
      ('hidden_lower_half',fiber+[low_frame]),('hidden_upper_half',fiber+[high_frame]),
      ('hidden_bound_then_S_le_500',source+[low_frame,((Q(1),Q(1),Q(1)),Q(500))])]
    downgrades=[]
    for name,current in cases:
        current_vertices=vertices(current);q=hull([obs(x) for x in current_vertices]);reopened=from_polygon(q);reopened_vertices=vertices(reopened)
        offenders=[x for x in reopened_vertices if any(dot(a,x)>rhs for a,rhs in current)]
        safe=not offenders
        assert safe==(name not in ('hidden_lower_half','hidden_upper_half'))
        downgrades.append({'name':name,'current_rows':[{'a':list(map(str,a)),'b':str(rhs)} for a,rhs in current],
          'polygon':[list(map(str,u)) for u in q],'current_vertices':[list(map(str,x)) for x in current_vertices],
          'reopened_vertices':[list(map(str,x)) for x in reopened_vertices],'safe_to_forget_fiber_constraints':safe,
          'obstruction':list(map(str,offenders[0])) if offenders else None})
    # Exact nonnegative implication: S<=500, -x2<=0, -x3<=0 imply x1<=500<=1000.
    assert tuple(a+b+c for a,b,c in zip((1,1,1),(0,-1,0),(0,0,-1)))==(1,0,0)
    packet={'forward':[[str(v) for v in row] for row in forward],'inverse':[[str(v) for v in row] for row in inverse],
      'upgrades':records,'downgrades':downgrades,
      'hidden_fiber_collision':{'observable':list(map(str,point)),'common_stored_lift':list(map(str,center)),
        'low_witness':list(map(str,low)),'high_witness':list(map(str,high)),'new_query_upper':str(threshold),
        'low_feasible':True,'high_feasible':False,'required_disposition_without_saturation':'NEEDS_FIBER_INFORMATION'},
      'invalid_observable_rejected':True,
      'redundancy_certificate':{'rows':[[1,1,1],[0,-1,0],[0,0,-1]],'rhs':['500','0','0'],'multipliers':['1','1','1'],'conclusion':'x1<=500<=1000'}}
    pp=OUT/'query-language-upgrade-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'SATURATED_UPGRADE_AND_CERTIFIED_DOWNGRADE_PASS','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'exact_upgrades':len(records),'downgrade_tests':len(downgrades),'unsafe_downgrades_refused':2,
      'resource_usage':peak,'scope':contract['scope'],
      'conclusion':'Old-observable-only evidence permits exact model-based upgrades without new acquisition. New bin evidence can break that invariant; retain its residual constraint or certify it redundant before downgrading.',
      'boundary':'A recovered possibility set does not select the actual source. One stored feasible lift cannot substitute for the missing fiber relation.'}
    assert sha(path)==contract['source_interface_sha256'];save(OUT/'query-language-upgrade.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
