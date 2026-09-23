"""General boundary certificates plus a nonsymmetric free-formula counterexample."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import copy,json,gzip,hashlib
from verify_boundary_obligations import owning_source,data,check,obligations,reference_check,digest
from full_polygon_checkpoint import cross,interpolate
from migration_section_checkpoint import rank
from checked_retirement_interface import migrate
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
def solve(columns,target):
    k=len(columns);a=[[col[i] for col in columns]+[target[i]] for i in range(len(target))];r=0
    for j in range(k):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:return None
        a[r],a[pivot]=a[pivot],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
    if any(all(x==0 for x in row[:k]) and row[-1]!=0 for row in a):return None
    return [a[i][-1] for i in range(k)]
def support_weights(rows,target,bound):
    for k in range(1,len(target)+1):
        for ids in combinations(range(len(rows)),k):
            w=solve([rows[i][0] for i in ids],target)
            if w is not None and all(x>=0 for x in w) and sum(x*rows[i][1] for x,i in zip(w,ids))==bound:
                full=[Q(0)]*len(rows)
                for i,x in zip(ids,w):full[i]=x
                return full
    raise AssertionError('no sparse source support proof')
def project(observer,t):return tuple(sum(a*b for a,b in zip(row,t)) for row in observer)
def clip(vertices,lifts,bound):
    result=[]
    for p,t,q,u in zip(vertices,lifts,vertices[1:]+vertices[:1],lifts[1:]+lifts[:1]):
        a,b=bound-p[0],bound-q[0]
        if a>=0:result.append((p,t))
        if a*b<0:
            w=a/(a-b);result.append((tuple(x+w*(y-x) for x,y in zip(p,q)),tuple(x+w*(y-x) for x,y in zip(t,u))))
    unique=[]
    for pair in result:
        if pair[0] not in [p for p,t in unique]:unique.append(pair)
    return [p for p,t in unique],[t for p,t in unique]
def lower_reference(observer,bound):
    # Three lower-fiber box faces meet at (0,102,0). Their projected
    # triangulation is a continuous whole-domain three-formula section.
    z=Q(0);a,b,c=Q(10),Q(102),Q(104)
    source=[(z,z,z),(z,z,c),(z,b,c),(a,b,c),(a,b,z),(a,z,z),(z,b,z)]
    points=[project(observer,t) for t in source];vertices=[];lifts=[];triangles=[]
    for j in range(6):
        ids=[6,j,(j+1)%6];p,t=clip([points[i] for i in ids],[source[i] for i in ids],bound)
        if len(p)<3:continue
        local=[]
        for v,w in zip(p,t):
            if v in vertices:i=vertices.index(v);assert lifts[i]==w
            else:i=len(vertices);vertices.append(v);lifts.append(w)
            local.append(i)
        for i in range(1,len(local)-1):triangles.append([local[0],local[i],local[i+1]])
    return {'vertices':[list(map(str,p)) for p in vertices],'source_lifts':[list(map(str,t)) for t in lifts],'triangles':triangles}
def packet(spec,polygon,lifts,reference,point):
    O,rows=data(spec);edges=[];forced=[]
    for i,(a,b) in enumerate(zip(polygon,polygon[1:]+polygon[:1])):
        n=(b[1]-a[1],a[0]-b[0]);bound=sum(x*y for x,y in zip(n,a))
        target=tuple(sum(n[k]*O[k][j] for k in range(2)) for j in range(len(O[0])))
        w=support_weights(rows,target,bound);r=rank([*O,*[a for x,(a,h) in zip(w,rows) if x>0]])
        proof={'weights':list(map(str,w)),'fiber_rank':r,'kind':'forced' if r==len(O[0]) else 'nonunique'}
        if proof['kind']=='forced':forced.append(i)
        else:
            p=tuple((x+y)/2 for x,y in zip(a,b));t=tuple((x+y)/2 for x,y in zip(lifts[i],lifts[(i+1)%len(lifts)]))
            u=tuple(x+Q(d,1000) for x,d in zip(t,(1,-129,128)))
            proof.update(point=list(map(str,p)),witnesses=[list(map(str,t)),list(map(str,u))])
        edges.append(proof)
    target,metrics=reference_check(spec,polygon,reference,tuple(map(Q,point)))
    return {'source_digest':digest(spec),'polygon':[list(map(str,p)) for p in polygon],
      'vertex_lifts':[list(map(str,t)) for t in lifts],'edges':edges,'reference':reference,'point':point,
      'analysis':obligations(polygon,lifts,forced,tuple(map(Q,point)),target),'reference_metrics':metrics}
def main():
    oldpath=OUT/'selector-approximation-contract.json';old=json.loads(oldpath.read_text())
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans'];cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence');plan=plans[i]
    state=migrate(plan,cases[i],retain_lift=True);assert old['expected_plan']==plan
    reference={k:copy.deepcopy(old['reference'][k]) for k in ('vertices','source_lifts','triangles')}
    polygon=[tuple(map(Q,p)) for p in old['scope']]
    lifts=[tuple(map(Q,t)) for t in reference['source_lifts'][:6]];point=old['center']
    spec=owning_source(plan,state);full=packet(spec,polygon,lifts,reference,point)
    frame={'normal':['1','0'],'upper':'162'};restricted=state.refine(frame['normal'],frame['upper']);cut_spec=owning_source(plan,restricted)
    cut_polygon,cut_lifts=clip(polygon,lifts,Q(162));cut_reference=lower_reference(data(cut_spec)[0],Q(162))
    truncated=packet(cut_spec,cut_polygon,cut_lifts,cut_reference,point)
    results=[check(s,point,p) for s,p in ((spec,full),(cut_spec,truncated))]
    assert results[0]['forced_edges']==6 and results[0]['error_gate']['error_lower_bound']=='129/1000'
    assert results[1]['forced_edges']==5 and results[1]['reference']['formulas']==3
    assert results[1]['error_gate']['status']=='UNPINNED_FORMULA_FAMILIES'
    assert results[1]['error_gate']['pinned_only_probe_distance']=='45/32'
    assert results[1]['error_gate']['error_lower_bound'] is None
    rejected=[]
    for defect in ('negative-support-weight','false-unique-fiber','identical-ambiguity-witnesses','omitted-compatible-group','invented-formula-bound','free-as-pinned','false-positive-error-bound','wrong-source','wrong-point'):
        bad=copy.deepcopy(truncated)
        if defect=='negative-support-weight':bad['edges'][0]['weights'][0]='-1'
        if defect=='false-unique-fiber':next(e for e in bad['edges'] if e['kind']=='nonunique')['kind']='forced'
        if defect=='identical-ambiguity-witnesses':
            e=next(e for e in bad['edges'] if e['kind']=='nonunique');e['witnesses'][1]=e['witnesses'][0]
        if defect=='omitted-compatible-group':bad['analysis']['compatible_groups'].pop()
        if defect=='invented-formula-bound':bad['analysis']['minimum_formula_lower_bound']=4
        if defect=='free-as-pinned':next(g for g in bad['analysis']['compatible_groups'] if g['kind']=='free')['kind']='pinned'
        if defect=='false-positive-error-bound':bad['analysis']['error_gate']={'status':'ALL_MINIMUM_COVERS_PINNED','error_lower_bound':'45/32','pinned_only_probe_distance':'45/32'}
        if defect=='wrong-source':bad['source_digest']='foreign'
        if defect=='wrong-point':bad['point']=['0','0']
        try:check(cut_spec,point,bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('unsound boundary certificate accepted')
    paths=[Path(__file__),Path(__file__).with_name('verify_boundary_obligations.py'),Path(__file__).with_name('full_polygon_checkpoint.py'),
      Path(__file__).with_name('verify_scalar_envelope_band.py'),ROOT/'research/voevodsky/checkers/migration_section_checkpoint.py',
      ROOT/'research/voevodsky/checkers/checked_retirement_interface.py',oldpath,G/'audit-elimination-contract.json',G/'audit-elimination.json.gz']
    contract={'plan':plan,'cases':[{'public_frames':frames,'expected_source':s,'point':point,'reference_digest':digest(p['reference'])}
      for frames,s,p in (([],spec,full),([frame],cut_spec,truncated))],
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    cp=OUT/'boundary-obligations-contract.json';pp=OUT/'boundary-obligations-packets.json'
    cp.write_text(json.dumps(contract,indent=2)+'\n');pp.write_text(json.dumps([full,truncated],indent=2)+'\n')
    report={'passed':True,'cases':results,'rejections':rejected,'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
      'packets_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),
      'counterexample':'A fine-admissible three-formula reference has zero error to itself, despite pinned-pair-only distance 45/32. Free singleton obligations cannot be discarded.'}
    (OUT/'boundary-obligations.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
