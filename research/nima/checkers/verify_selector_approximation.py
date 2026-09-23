"""Whole-domain original-atom error and boundary-forced formula bounds.
No selector constructor or provider router is imported.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,gzip,hashlib
from full_polygon_checkpoint import verify_full_polygon,intersection,interpolate,cross
from migration_section_checkpoint import rank
from checked_retirement_interface import migrate,source,freeze
if not __debug__:raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';G=ROOT/'research/grothendieck/results'
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def cells(packet):
    v=[tuple(map(Q,p)) for p in packet['vertices']];t=[tuple(map(Q,p)) for p in packet['source_lifts']]
    return [([v[i] for i in ids],[t[i] for i in ids]) for ids in packet['triangles']]
def formula(p,t):
    origin=interpolate(p,t,(Q(0),Q(0)));x=interpolate(p,t,(Q(1),Q(0)));y=interpolate(p,t,(Q(0),Q(1)))
    return tuple((a-c,b-c,c) for a,b,c in zip(x,y,origin))
def evaluate(f,p):return tuple(a*p[0]+b*p[1]+c for a,b,c in f)
def program_check(packet,program):
    assert set(program)=={'vertices','triangles','formulas','cell_formula_ids','migration_binding'}
    assert program['vertices']==packet['vertices'] and program['triangles']==packet['triangles']
    assert program['migration_binding']==packet['migration_binding']
    table=[tuple(tuple(map(Q,row)) for row in f) for f in program['formulas']]
    assert len(set(table))==len(table) and len(program['cell_formula_ids'])==len(packet['triangles'])
    assert set(program['cell_formula_ids'])==set(range(len(table)))
    for (p,t),index in zip(cells(packet),program['cell_formula_ids']):
        assert type(index) is int and 0<=index<len(table)
        assert table[index]==formula(p,t)
    return {'formulas':len(table),'triangular_cells':len(packet['triangles']),
      'program_bytes':len(freeze(program).encode()),'section_certificate_bytes':len(freeze(packet).encode())}
def distance(reference,candidate):
    maximum=Q(-1);witness=None;checks=0
    for p,t in cells(reference):
        for q,u in cells(candidate):
            for point in intersection(p,q):
                a,b=interpolate(p,t,point),interpolate(q,u,point);error=max(abs(x-y) for x,y in zip(a,b));checks+=1
                if error>maximum:
                    maximum=error;witness={'point':list(map(str,point)),'reference_lift':list(map(str,a)),'candidate_lift':list(map(str,b))}
    assert maximum>=0
    return {'maximum_atom_error':str(maximum),'attaining_witness':witness,'overlap_vertex_checks':checks}
def check(state,scope,reference,epsilon,candidate,program,claimed):
    verify_full_polygon(state,scope,reference);verify_full_polygon(state,scope,candidate)
    assert Q(epsilon)>=0
    metric=distance(reference,candidate);assert metric==claimed and Q(metric['maximum_atom_error'])<=Q(epsilon)
    return program_check(candidate,program)

def boundary_bound(plan,scope,reference,center):
    # This owning history is exactly a three-atom box with a tighter t0 cap.
    assert plan['m']==3 and plan['audits']==[0] and plan['retire']==0
    _,_,observe,caps=source(3,[0]);caps=list(caps)
    for row in plan['frames']:
        assert list(map(Q,row['normal']))==[Q(0),Q(0),Q(1)]
        caps[0]=min(caps[0],Q(row['upper']))
    assert caps==[Q(10),Q(102),Q(104)]
    v=[tuple(map(Q,p)) for p in scope];assert len(v)==6
    lifts=[]
    for p in v:
        hits=[interpolate(q,t,p) for q,t in cells(reference) if all(cross(a,b,p)>=0 for a,b in zip(q,q[1:]+q[:1]))]
        assert hits and len(set(hits))==1;lifts.append(hits[0])
    slopes=(Q(1),Q(1,128),Q(1,16384))
    for i,(a,b) in enumerate(zip(v,v[1:]+v[:1])):
        normal=(b[1]-a[1],a[0]-b[0]);coeff=[normal[0]+normal[1]*r for r in slopes]
        bound=normal[0]*a[0]+normal[1]*a[1]
        assert sum(c*max(Q(0),w) for c,w in zip(caps,coeff))==bound
        assert sum(w==0 for w in coeff)==1
        for t in (lifts[i],lifts[(i+1)%6]):
            assert observe(t)[:2] in (a,b)
            assert all(w==0 or x==(c if w>0 else 0) for x,c,w in zip(t,caps,coeff))
        # Saturation fixes two atoms; U fixes the remaining atom everywhere
        # on this public edge. Thus all admissible selectors have these edges.
    edges=[(i,(i+1)%6) for i in range(6)]
    def affine_rank(indices):
        points=[lifts[j] for j in indices]
        return rank([tuple(x-y for x,y in zip(p,points[0])) for p in points[1:]])
    for triple in combinations(range(6),3):
        assert affine_rank(sorted({j for i in triple for j in edges[i]}))==3
    # An affine R2 -> R3 map cannot contain three of these forced source
    # edges. With only three formulas, every formula must contain two.
    pairs=[];pcenter=tuple(map(Q,center))
    ref_values=[interpolate(p,t,pcenter) for p,t in cells(reference) if all(cross(a,b,pcenter)>=0 for a,b in zip(p,p[1:]+p[:1]))]
    assert ref_values and len(set(ref_values))==1;target=ref_values[0]
    for pair in combinations(range(6),2):
        indices=sorted({j for i in pair for j in edges[i]})
        if affine_rank(indices)!=2:continue
        ids=next(c for c in combinations(indices,3) if cross(*(v[j] for j in c)))
        p=[v[j] for j in ids];t=[lifts[j] for j in ids]
        if cross(*p)<0:p[1],p[2]=p[2],p[1];t[1],t[2]=t[2],t[1]
        f=formula(p,t)
        assert all(evaluate(f,v[j])==lifts[j] for j in indices)
        at_center=evaluate(f,pcenter);error=max(abs(x-y) for x,y in zip(target,at_center))
        pairs.append({'edges':list(pair),'formula':[[str(x) for x in row] for row in f],
                      'center_lift':list(map(str,at_center)),'center_error':str(error)})
    assert len(pairs)==9
    return {'forced_edges':6,'triple_rank_checks':20,'minimum_admissible_formulas':3,
      'exact_reference_formulas':len({formula(p,t) for p,t in cells(reference)}),
      'three_formula_error_lower_bound':str(min(Q(p['center_error']) for p in pairs)),
      'pair_candidates':pairs}

def main():
    cp=OUT/'selector-approximation-contract.json';pp=OUT/'selector-approximation-packets.json';rp=OUT/'selector-approximation.json'
    contract=json.loads(cp.read_text());packets=json.loads(pp.read_text());report=json.loads(rp.read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==report['contract_sha256']
    assert hashlib.sha256(pp.read_bytes()).hexdigest()==report['packets_sha256']
    for p,h in contract['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    plans=json.loads((G/'audit-elimination-contract.json').read_text())['plans']
    cases=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions']
    i=next(i for i,p in enumerate(plans) if p['name']=='one-sided-audit-evidence')
    assert contract['expected_plan']==plans[i];state=migrate(plans[i],cases[i],retain_lift=True)
    reference=contract['reference'];scope=contract['scope'];assert digest(reference)==contract['reference_digest']
    assert len(contract['epsilons'])==len(packets)==len(report['cases'])
    for epsilon,packet,claimed in zip(contract['epsilons'],packets,report['cases']):
        assert packet['epsilon']==epsilon and packet['reference_digest']==contract['reference_digest']
        metrics=check(state,scope,reference,epsilon,packet['section'],packet['program'],packet['distance'])
        assert claimed=={'epsilon':epsilon,**metrics,**packet['distance']}
    lower=boundary_bound(plans[i],scope,reference,contract['center'])
    assert lower==report['lower_bound_certificate'] and lower['exact_reference_formulas']==6
    assert lower['three_formula_error_lower_bound']=='129/1000'
    assert any(program_check(p['section'],p['program'])['formulas']==3 and p['distance']['maximum_atom_error']=='129/1000' for p in packets)
    result={'passed':True,'whole_domain_certificates':len(packets),'minimum_admissible_formulas':3,
      'optimal_error_for_at_most_three_formulas':'129/1000','exact_reference_formula_lower_bound':6,
      'scope':'This fixed selector and owning hexagon. Intermediate four/five-formula tradeoffs and byte optimality remain open.'}
    (OUT/'selector-approximation-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
