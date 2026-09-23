"""Independent rational certificate/vertex replay, without producer or solver."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def geometry(rows):return tuple((tuple(map(Q,r['a'])),Q(r['b'])) for r in rows)
def normalize(rows):
    out={}
    for a,b in rows:
        pivot=next((x for x in a if x),None)
        if pivot is None:
            if b<0:return ((tuple(Q(0) for _ in a),Q(-1)),)
            continue
        d=abs(pivot);a=tuple(x/d for x in a);b/=d
        if a not in out or b<out[a]:out[a]=b
    return tuple(sorted(out.items()))
def fm(rows,index):
    pos=[r for r in rows if r[0][index]>0];neg=[r for r in rows if r[0][index]<0]
    result=[r for r in rows if r[0][index]==0]
    for a,b in pos:
        for d,e in neg:
            # Multiply rather than use the producer's divided-pair construction.
            result.append((tuple(-d[index]*x+a[index]*y for x,y in zip(a,d)),-d[index]*b+a[index]*e))
    return normalize(result)
def det(A):
    if not A:return Q(1)
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
@lru_cache(None)
def vertices(rows,keep):
    rows=normalize(rows);n=len(keep);answer=set()
    if any(not any(a) and b<0 for a,b in rows):return ()
    for chosen in combinations(rows,n):
        matrix=[[a[j] for j in keep] for a,b in chosen];rhs=[b for a,b in chosen];denominator=det(matrix)
        if denominator==0:continue
        point=tuple(det([row[:j]+[rhs[i]]+row[j+1:] for i,row in enumerate(matrix)])/denominator for j in range(n))
        if all(sum(a[j]*point[k] for k,j in enumerate(keep))<=b for a,b in rows):answer.add(point)
    return tuple(sorted(answer))
def main():
    cp=OUT/'analytical-cut-composition-contract.json';rp=OUT/'analytical-cut-composition.json';pp=OUT/'analytical-cut-composition-packet.json.gz'
    c,r=load(cp),load(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    source_path=ROOT/'grothendieck/results/ternary-tail-budget-dpc.json';assert sha(source_path)==c['source_sha256'];source=load(source_path)
    caps=list(map(Q,source['atom_capacity_upper']));budgets=list(map(Q,source['prefix_budget_upper']));weights=[Q(v['lower']) for v in source['weights']]
    base=[]
    for i in range(3):base.append((tuple(Q(-int(j==i)) for j in range(4)),Q(0)))
    for i in range(3):base.append((tuple(Q(int(j==i)) for j in range(4)),caps[i]))
    for i in range(3):base.append((tuple(Q(int(j<=i)) for j in range(4)),budgets[i]))
    base.extend([(tuple([-w for w in weights]+[Q(1)]),Q(0)),(tuple(weights+[Q(-1)]),Q(0))])
    assert geometry(p['source_rows'])==tuple(base)
    bad=list(map(Q,source['pairwise_LP']['primal']));good=list(map(Q,source['full_LP']['primal']));threshold=Q(source['block_threshold'])
    prefix_values={'zero':[Q(0),Q(0)],'owning_full_optimizer':good[:2],'owning_pair_candidate':bad[:2],'half_pair_candidate':[v/2 for v in bad[:2]]}
    refinements={'objective_at_most_threshold':[((Q(0),Q(0),Q(0),Q(1)),threshold)],
      'objective_at_least_threshold':[((Q(0),Q(0),Q(0),Q(-1)),-threshold)],
      'third_cap_half':[((Q(0),Q(0),Q(1),Q(0)),caps[2]/2)],
      'third_floor_quarter':[((Q(0),Q(0),Q(-1),Q(0)),-caps[2]/4)],
      'inconsistent_third_interval':[((Q(0),Q(0),Q(-1),Q(0)),-caps[2]/2),((Q(0),Q(0),Q(1),Q(0)),caps[2]/3)],
      'coupled_objective_third_cap':[((Q(0),Q(0),-weights[2],Q(1)),Q(source['full_LP']['value'])/2)]}
    row_checks=0;stage_checks=0;vertex_lifts=0;empty_checks=0
    def certificates(rows,basis):
        nonlocal row_checks
        assert len(rows)<=c['bounds']['retained_rows_per_stage']
        for row in rows:
            a=tuple(map(Q,row['a']));b=Q(row['b']);proof=list(map(Q,row['proof']))
            assert len(proof)==len(basis) and all(v>=0 for v in proof)
            assert a==tuple(sum(proof[k]*basis[k][0][j] for k in range(len(basis))) for j in range(4))
            assert b==sum(proof[k]*basis[k][1] for k in range(len(basis)))
            assert all(max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=c['bounds']['rational_numerator_denominator_bits'] for v in (*a,b,*proof));row_checks+=1
    for plan in p['plans']:
        name=plan['name'].split('/');expected=list(base)
        if name[0]!='unconditioned':
            for i,value in enumerate(prefix_values[name[0]]):
                a=tuple(Q(int(i==j)) for j in range(4));expected.extend([(a,value),(tuple(-v for v in a),-value)])
        if len(name)>1:expected+=refinements[name[1]]
        basis=geometry(plan['basis']);assert basis==tuple(expected)
        keep=tuple(plan['keep']);order=plan['order'];assert set(order)==set(range(3))-set(keep) and 3 in keep
        late=plan['late_count'];initial=basis[:-late] if late else basis
        axes=[((Q(0),Q(0),Q(0),Q(1)),Q(0)),((Q(0),Q(0),Q(0),Q(-1)),-dot(weights,caps))]
        current=normalize(initial+tuple(axes))
        for index,stage in zip(order,plan['stages']):
            assert stage['variable']==index and geometry(stage['before'])==current
            certificates(stage['before'],basis);certificates(stage['after'],basis)
            before=geometry(stage['before']);pos=sum(a[index]>0 for a,b in before);neg=sum(a[index]<0 for a,b in before)
            assert pos*neg+sum(a[index]==0 for a,b in before)<=c['bounds']['generated_rows_per_stage']
            current=fm(current,index)
            assert geometry(stage['after'])==current, (plan['name'],order,index,len(current),len(stage['after']),list(set(current)-set(geometry(stage['after']))))
            stage_checks+=1
        assert len(plan['stages'])==len(order)
        if late:
            assert all(all(not a[j] for j in order) for a,b in basis[-late:]);current=normalize(current+basis[-late:])
        assert geometry(plan['rows'])==current;certificates(plan['rows'],basis)
        if not any(not any(a) and b<0 for a,b in current):
            for j in keep:
                for sign in (-1,1):assert any(sign*a[j]>0 and all(not a[k] for k in range(4) if k!=j) for a,b in current)
        calculated=vertices(current,keep);assert calculated==tuple(tuple(map(Q,v)) for v in plan['projected_vertices'])
        reduced=tuple((tuple(a[i]+a[3]*weights[i] for i in range(3)),b) for a,b in basis)
        original=tuple(tuple(v)+(dot(weights,v),) for v in vertices(reduced,(0,1,2)))
        assert original==tuple(tuple(map(Q,v)) for v in plan['source_vertices'])
        assert len(plan['lifts'])==len(calculated)
        for point,encoded in zip(calculated,plan['lifts']):
            witness=tuple(map(Q,encoded));assert tuple(witness[j] for j in keep)==point
            assert all(dot(a,witness)<=b for a,b in basis);vertex_lifts+=1
        assert all(all(dot(a,v)<=b for a,b in current) for v in original)
        assert bool(calculated)==bool(original)
        if not calculated:
            contradiction=plan['infeasibility'];assert contradiction is not None
            certificates([contradiction],basis);assert not any(map(Q,contradiction['a'])) and Q(contradiction['b'])<0;empty_checks+=1
        else:assert plan['infeasibility'] is None
    for group in p['order_groups']:
        assert all(p['plans'][i]['projected_vertices']==p['plans'][group[0]]['projected_vertices'] for i in group)
    for a,b in p['refinement_commutations']:
        x,y=p['plans'][a],p['plans'][b];assert x['basis']==y['basis'] and x['keep']==y['keep'] and x['projected_vertices']==y['projected_vertices']
    for local in p['pairwise_negative']:
        certificates(local['rows'],tuple(base[:9]))
        expected=fm(normalize(tuple(base[:9])),local['missing']);assert geometry(local['rows'])==expected
        assert all(dot(a,tuple(bad)+(Q(0),))<=b for a,b in expected)
        lift=tuple(map(Q,local['lift']));assert all(dot(a,lift)<=b for a,b in base[:9])
        assert all(lift[j]==bad[j] for j in local['keep'])
    assert sum(bad)>budgets[2] and dot(weights,bad)<threshold<Q(source['full_LP']['value'])
    chosen=next(plan for plan in p['plans'] if plan['name']=='unconditioned' and plan['keep']==[2,3])
    assert any(dot(a,tuple(bad)+(dot(weights,bad),))>b for a,b in geometry(chosen['rows']))
    assert len(p['plans'])==167 and len(p['refinement_commutations'])==72 and empty_checks==64
    result={'passed':True,'report_sha256':sha(rp),'plans':len(p['plans']),'elimination_stages':stage_checks,
      'nonnegative_row_certificates':row_checks,'constructive_vertex_lifts':vertex_lifts,'farkas_inconsistency_certificates':empty_checks,
      'refinement_commutations':72,'negative_control':'Exact pair projections still fail global assembly; full shared-factor elimination rejects the owning candidate.',
      'scope':c['scope'],'proof_method':'Complete bounded-polytope vertex enumeration plus exact elimination and row certificates, not finite grid sampling.'}
    (OUT/'analytical-cut-composition-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
