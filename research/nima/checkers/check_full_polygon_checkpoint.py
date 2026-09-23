"""Real rank-two retirement: full hexagon coverage, coherent lifts, restriction."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import copy,gzip,json,hashlib
from full_polygon_checkpoint import FullPolygonSession,verify_full_polygon,polygon_targets,coverage_rows,check_section
from checked_retirement_interface import migrate,source,freeze
ROOT=Path(__file__).resolve().parents[3];G=ROOT/'research/grothendieck/results';OUT=ROOT/'research/nima/results'

def certificate(rows,target):
    n,b=target
    for i,(a,h) in enumerate(rows):
        for k in range(2):
            if not a[k]:continue
            w=n[k]/a[k]
            if w>=0 and tuple(w*x for x in a)==n and w*h<=b:
                result=[Q(0)]*len(rows);result[i]=w;return list(map(str,result))
    for i,j in combinations(range(len(rows)),2):
        a,h=rows[i];c,k=rows[j];d=a[0]*c[1]-a[1]*c[0]
        if not d:continue
        u=(n[0]*c[1]-n[1]*c[0])/d;v=(a[0]*n[1]-a[1]*n[0])/d
        if u>=0 and v>=0 and u*h+v*k<=b:
            result=[Q(0)]*len(rows);result[i]=u;result[j]=v;return list(map(str,result))
    raise AssertionError('no two-row implication')
def main():
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    index=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');plan=plans[index];case=cases[index]
    state=migrate(plan,case,retain_lift=True);session=FullPolygonSession();boot=session.bootstrap(plan,case,retain_lift=True)
    assert plan['m']==3 and plan['audits']==[0] and plan['retire']==0
    _,_,observe,caps=source(plan['m'],plan['audits']);a,b,c=Q(10),caps[1],caps[2]
    lifts=[(Q(0),Q(0),Q(0)),(Q(0),Q(0),c),(Q(0),b,c),(a,b,c),(a,b,Q(0)),(a,Q(0),Q(0))]
    vertices=[list(map(str,observe(t)[:2])) for t in lifts];polygon=[tuple(map(Q,p)) for p in vertices]
    packet={'migration_binding':boot['state']['migration_binding'],'polygon':vertices,'vertices':vertices,
      'source_lifts':[list(map(str,t)) for t in lifts],'triangles':[[0,i,i+1] for i in range(1,5)],
      'coverage_weights':[certificate(coverage_rows(state),target) for target in polygon_targets(polygon)]}
    expected_work=verify_full_polygon(state,vertices,packet);rejected=[]
    def reject(name,action):
        try:action()
        except (AssertionError,ValueError,PermissionError,KeyError,IndexError):rejected.append(name)
        else:raise AssertionError(name+' accepted')
    for defect in ('missing-implication','negative-weight','wrong-source-lift','foreign-migration','missing-triangle','overlapping-triangle'):
        bad=copy.deepcopy(packet)
        if defect=='missing-implication':bad['coverage_weights'].pop()
        if defect=='negative-weight':bad['coverage_weights'][0][0]='-1'
        if defect=='wrong-source-lift':bad['source_lifts'][2]=['0','0','0']
        if defect=='foreign-migration':bad['migration_binding']='foreign'
        if defect=='missing-triangle':bad['triangles'].pop()
        if defect=='overlapping-triangle':bad['triangles'].append(copy.deepcopy(bad['triangles'][0]))
        reject(defect,lambda:session.attach_full_polygon(boot['handle'],boot['state'],vertices,bad))
    # Smaller geometrically valid section: all lifts are admitted, but it
    # misses a real domain sliver. Candidate coverage flags cannot rescue it.
    small=copy.deepcopy(packet)
    small_vertices=[[str(Q(x)/2) for x in p] for p in vertices]
    small['polygon']=small_vertices;small['vertices']=small_vertices
    small['source_lifts']=[[str(Q(x)/2) for x in t] for t in packet['source_lifts']]
    for p,t in zip(small_vertices,small['source_lifts']):
        check_section(state,[p],{'migration_binding':state.migration_binding,'vertices':[p],'source_lifts':[t]})
    # Re-scale the normals of the old implications to match the new facets.
    # Their upper bounds then expose precisely the missing domain coverage.
    small['coverage_weights']=[[str(Q(w)/2) for w in row] for row in packet['coverage_weights']]
    reject('omitted-domain-sliver',lambda:session.attach_full_polygon(boot['handle'],boot['state'],small_vertices,small))
    # A nonconforming mesh is valid only when the coarse edge's affine lift
    # agrees with the finer side's T-junction value.
    refined=copy.deepcopy(packet);mid=[str((Q(x)+Q(y))/2) for x,y in zip(vertices[0],vertices[3])]
    mid_lift=[str((x+y)/2) for x,y in zip(lifts[0],lifts[3])]
    refined['vertices']=copy.deepcopy(vertices)+[mid];refined['source_lifts'].append(mid_lift)
    refined['triangles']=[[0,1,2],[0,2,6],[6,2,3],[0,3,4],[0,4,5]]
    verify_full_polygon(state,vertices,refined)
    incoherent=copy.deepcopy(refined)
    incoherent['source_lifts'][6]=[str(Q(x)+Q(d,1000)) for x,d in zip(mid_lift,(1,-129,128))]
    check_section(state,[mid],{'migration_binding':state.migration_binding,'vertices':[mid],'source_lifts':[incoherent['source_lifts'][6]]})
    reject('fine-admitted-incoherent-shared-edge',lambda:session.attach_full_polygon(boot['handle'],boot['state'],vertices,incoherent))
    attached=session.attach_full_polygon(boot['handle'],boot['state'],vertices,packet);sid=attached['section_id'];handle=attached['handle']
    assert attached['attachment_work']==expected_work
    queries=vertices+[mid]
    for ids in packet['triangles']:
        queries.append([str(sum(Q(vertices[i][j]) for i in ids)/3) for j in range(2)])
    answers=[]
    for p in queries:
        t=session.covered_lift(handle,sid,p)
        check_section(state,[p],{'migration_binding':state.migration_binding,'vertices':[p],'source_lifts':[t]})
        answers.append({'point':p,'source_lift':t})
    reject('outside-runtime-domain',lambda:session.covered_lift(handle,sid,['217','0']))
    reject('nonpublic-point',lambda:session.covered_lift(handle,sid,['0','0','0']))
    op={'kind':'append-public','normal':['1','0'],'upper':'162'};next_state=state.refine(op['normal'],op['upper'])
    answer=next_state.maximize([1,0]);after=session.advance(handle,attached['state'],op,[1,0],answer)
    p=[str(Q(3,4)*x) for x in polygon[3]];t=session.covered_lift(after['handle'],sid,p)
    assert t==[str(Q(3,4)*x) for x in lifts[3]]
    check_section(next_state,[p],{'migration_binding':state.migration_binding,'vertices':[p],'source_lifts':[t]})
    reject('excluded-old-vertex',lambda:session.covered_lift(after['handle'],sid,vertices[3]))
    reject('stale-handle',lambda:session.covered_lift(handle,sid,vertices[0]))
    reject('archive-escalation',lambda:session.reexpose(after['handle']))
    reject('domain-widening-operation',lambda:session.advance(after['handle'],after['state'],{'kind':'replace-public','normal':['1','0'],'upper':'1000'},[1,0],answer))
    other=FullPolygonSession();no_lift=other.bootstrap(plan,case,retain_lift=False)
    reject('missing-fine-lift-capability',lambda:other.attach_full_polygon(no_lift['handle'],no_lift['state'],vertices,packet))
    final=session._receipt();assert final['section_work']['vertex_checks']==6 and final['section_work']['interpolated_lifts']==len(queries)+1
    paths=[Path(__file__),Path(__file__).with_name('full_polygon_checkpoint.py'),Path(__file__).with_name('verify_scalar_envelope_band.py'),
      ROOT/'research/voevodsky/checkers/migration_section_checkpoint.py',ROOT/'research/voevodsky/checkers/migration_checkpoint.py',
      ROOT/'research/voevodsky/checkers/checked_retirement_interface.py',ROOT/'research/voevodsky/checkers/full_segment_checkpoint.py',
      ROOT/'research/grothendieck/checkers/verify_audit_elimination.py',ROOT/'research/grothendieck/checkers/joint_audit_tail_interface.py',
      G/'audit-elimination-contract.json',G/'audit-elimination.json.gz']
    report={'passed':True,'migration':plan['name'],'expected_plan':plan,'polygon':vertices,'packet':packet,
      'attachment':attached,'answers':answers,'restriction':{'operation':op,'answer':answer,'point':p,'source_lift':t},
      'successor':after,'final':final,'valid_nonconforming_mesh_checked':True,'rejections':rejected,
      'bindings':{str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
      'scope':'Real rank-two full-domain section, exact old-fine lifts and restriction reuse. Shared verification kernel; no archive escalation.'}
    (OUT/'full-polygon-checkpoint.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'passed':True,'attachment_work':expected_work,'interpolated_lifts':len(queries)+1,'rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
