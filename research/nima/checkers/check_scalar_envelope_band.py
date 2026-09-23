"""Coarsened fan experiment, exact cell certificates and interior attacks."""
from pathlib import Path
from fractions import Fraction as Q
import copy,json,hashlib
from verify_scalar_envelope_band import check,cross,value,area
OUT=Path(__file__).resolve().parents[1]/'results'
def points(n):return [(Q(i,n),Q(i,n)**2) for i in range(1,n+1)]
def interpolate(vertices,heights):
    a,b,c=vertices;ha,hb,hc=heights;d=cross(a,b,c);assert d
    x=((hb-ha)*(c[1]-a[1])-(hc-ha)*(b[1]-a[1]))/d
    y=((b[0]-a[0])*(hc-ha)-(c[0]-a[0])*(hb-ha))/d
    return (x,y,ha-x*a[0]-y*a[1])
def cell(vertices,formula):return {'vertices':[[str(x) for x in v] for v in vertices],'formula':list(map(str,formula))}
def fan(n,stride):
    vertices=points(n);cells=[];a=1
    while a<n-1:
        b=min(n-1,a+stride);corners=[vertices[k] for k in (0,a,b)]
        f=interpolate(corners,[v[0]**3 for v in corners]);cells.append(cell([vertices[0]]+vertices[a:b+1],f));a=b
    return cells

def core_and_caps(n,stride):
    vertices=points(n);selected=list(range(0,n,stride))
    if selected[-1]!=n-1:selected.append(n-1)
    cells=[]
    # The coarse inner polygon has an EXACT section: interpolate true heights.
    for i in range(1,len(selected)-1):
        triangle=[vertices[k] for k in (selected[0],selected[i],selected[i+1])]
        cells.append(cell(triangle,interpolate(triangle,[v[0]**3 for v in triangle])))
    # Each omitted boundary cap gets a local cubic interpolant. Its third
    # interpolation point need not be an original polygon vertex.
    for a,b in zip(selected,selected[1:]):
        if b==a+1:continue
        left,right=vertices[a][0],vertices[b][0];middle=(left+right)/2
        f=(-(left*middle+left*right+middle*right),left+middle+right,left*middle*right)
        cells.append(cell(vertices[a:b+1],f))
        assert all(abs(value(f,v)-v[0]**3)<=(right-left)**3/8 for v in vertices[a:b+1])
    return cells

def width_bounded(n,eta):
    eta=Q(eta);assert eta>=0
    stride=max([1]+[s for s in range(2,n) if Q(s**3,8*n**3)<=eta])
    return stride,core_and_caps(n,stride)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    contract={'family':'owning-m4-moment-curve-two-history-v1','requests':[
      {'n':n,'eta':eta} for n in (6,10,18) for eta in ('0','1/1000','1/100','1/10','1/2')],
      'scope':'Exact coarsened fans and coarse-core/local-cap certificates; general cubic-width upper bound proved in the accompanying note.'}
    packets=[];reports=[];width_packets=[];width_reports=[]
    for request in contract['requests']:
        n=request['n'];eta=Q(request['eta']);choices=[]
        width_stride,width_cells=width_bounded(n,eta)
        width_packet={'request':request,'cells':width_cells};width_metrics=check(request,width_packet)
        assert width_metrics['cells']<=n-2 and (width_metrics['cells']-1)**3*eta<=8
        width_packets.append(width_packet);width_reports.append({**request,'stride':width_stride,**width_metrics})
        for strategy,constructor in (('fan',fan),('core-and-caps',core_and_caps)):
            for stride in range(1,n):
                cells=constructor(n,stride)
                # Selection only; the verifier checks every envelope plane,
                # exact domain coverage and continuity independently.
                needed=max(abs(value(tuple(map(Q,c['formula'])),tuple(map(Q,v)))-Q(v[0])**3) for c in cells for v in c['vertices'])
                if needed<=eta:choices.append((len(cells),strategy,stride,cells,needed))
        if eta>=Q(1,2):choices.append((1,'constant',0,[cell(points(n),(Q(0),Q(0),Q(1,2)))],Q(1,2)))
        _,strategy,stride,cells,needed=min(choices,key=lambda x:(x[0],x[1],x[2]))
        packet={'request':request,'cells':cells};metrics=check(request,packet)
        packets.append(packet);reports.append({**request,'strategy':strategy,'stride':stride,'boundary_error_bound':str(needed),**metrics})
    exact={'n':6,'eta':'0'};base={'request':exact,'cells':fan(6,1)};check(exact,base)
    attacks=[]
    for defect in ('missing-cell','overlapping-cell','discontinuous-formula','altered-request'):
        bad=copy.deepcopy(base)
        if defect=='missing-cell':bad['cells'].pop()
        if defect=='overlapping-cell':
            bad['cells'].pop(1);bad['cells'] += [copy.deepcopy(bad['cells'][0]) for _ in range(3)]
            def total_area(packet):return sum(area([tuple(map(Q,v)) for v in c['vertices']]) for c in packet['cells'])
            assert total_area(bad)==total_area(base)  # area alone would accept
        if defect=='discontinuous-formula':bad['cells'][0]['formula'][2]=str(Q(bad['cells'][0]['formula'][2])+Q(1,100))
        if defect=='altered-request':bad['request']['eta']='1'
        try:check(exact,bad)
        except AssertionError:attacks.append(defect)
        else:raise AssertionError('invalid certificate accepted')
    vertices=[tuple(map(Q,v)) for v in base['cells'][0]['vertices']]
    center=tuple(sum(v[k] for v in vertices)/3 for k in range(2));bad=copy.deepcopy(base);parts=[]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        triangle=[a,b,center];parts.append(cell(triangle,interpolate(triangle,[a[0]**3,b[0]**3,Q(2)])))
    bad['cells']=parts+bad['cells'][1:]
    # Every original public vertex still has its exact cubic value.
    for v in points(6):
        seen=False
        for c in bad['cells']:
            p=[tuple(map(Q,w)) for w in c['vertices']]
            if all(cross(a,b,v)>=0 for a,b in zip(p,p[1:]+p[:1])):
                seen=True;assert value(tuple(map(Q,c['formula'])),v)==v[0]**3
        assert seen
    loose=copy.deepcopy(bad);loose['request']={'n':6,'eta':'2'};check(loose['request'],loose)
    try:check(exact,bad)
    except AssertionError:attacks.append('interior-bump-with-exact-original-vertices')
    else:raise AssertionError('vertex-only approximation mistaken for domain proof')
    # Isolate the continuity gate by making the band deliberately permissive.
    broken=copy.deepcopy(base);broken['request']={'n':6,'eta':'2'}
    broken['cells'][0]['formula'][2]=str(Q(broken['cells'][0]['formula'][2])+Q(1,100))
    try:check(broken['request'],broken)
    except AssertionError:attacks.append('discontinuity-inside-permissive-band')
    else:raise AssertionError('discontinuous section accepted')
    contract['bindings']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(__file__).with_name('verify_scalar_envelope_band.py'))}
    cp=OUT/'scalar-envelope-band-contract.json';pp=OUT/'scalar-envelope-band-packets.json';wp=OUT/'scalar-envelope-band-width-packets.json'
    cp.write_text(json.dumps(contract,indent=2)+'\n');pp.write_text(json.dumps(packets,indent=2)+'\n');wp.write_text(json.dumps(width_packets,indent=2)+'\n')
    result={'passed':True,'whole_polygon_certificates':len(packets)+len(width_packets),'cases':reports,
      'width_rule_cases':width_reports,'width_packets_sha256':hashlib.sha256(wp.read_bytes()).hexdigest(),'attacks_rejected':attacks,
      'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'packets_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),
      'scope':'All envelope planes on all cell vertices, exact coverage and continuity. Experiments do not by themselves prove an asymptotic theorem.'}
    (OUT/'scalar-envelope-band.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('cases','width_rule_cases')},indent=2))
if __name__=='__main__':main()
