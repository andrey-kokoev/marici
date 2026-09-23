"""Source-bound exact cut composition with independently replayable elimination.

Fourier-Motzkin joins all constraints containing an eliminated variable before
forgetting it. An objective coordinate is retained; it is not reoptimized or
reset independently at each cut.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,permutations
from functools import lru_cache
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
LIMIT_ROWS=128;LIMIT_CANDIDATES=512;LIMIT_BITS=8192
stats={'max_retained_rows':0,'max_generated_rows':0,'max_rational_bits':0}
def check_size(rows):
    stats['max_retained_rows']=max(stats['max_retained_rows'],len(rows));assert len(rows)<=LIMIT_ROWS
    for a,b,p in rows:
        size=max(max(abs(x.numerator).bit_length(),x.denominator.bit_length()) for x in (*a,b,*p))
        stats['max_rational_bits']=max(stats['max_rational_bits'],size);assert size<=LIMIT_BITS

def canonical(rows):
    stats['max_generated_rows']=max(stats['max_generated_rows'],len(rows));assert len(rows)<=LIMIT_CANDIDATES
    result={};contradiction=None
    for a,b,p in rows:
        first=next((v for v in a if v),None)
        if first is None:
            if b>=0:continue
            factor=-1/b;contradiction=(tuple(Q(0) for _ in a),Q(-1),tuple(factor*v for v in p));continue
        factor=1/abs(first);a=tuple(v*factor for v in a);b*=factor;p=tuple(v*factor for v in p)
        if a not in result or b<result[a][0]:result[a]=(b,p)
    out=[contradiction] if contradiction else [(a,b,p) for a,(b,p) in sorted(result.items())]
    check_size(out);return out

def eliminate(rows,index):
    pos=[r for r in rows if r[0][index]>0];neg=[r for r in rows if r[0][index]<0]
    out=[r for r in rows if not r[0][index]]
    for a,b,p in pos:
        for c,d,q in neg:
            u=1/a[index];v=-1/c[index]
            out.append((tuple(u*x+v*y for x,y in zip(a,c)),u*b+v*d,tuple(u*x+v*y for x,y in zip(p,q))))
    return canonical(out)

def solve(A,b):
    n=len(b);m=[list(row)+[rhs] for row,rhs in zip(A,b)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if m[i][k]),None)
        if pivot is None:return None
        m[k],m[pivot]=m[pivot],m[k];d=m[k][k];m[k]=[x/d for x in m[k]]
        for i in range(n):
            if i!=k:
                d=m[i][k];m[i]=[x-d*y for x,y in zip(m[i],m[k])]
    return tuple(row[-1] for row in m)

@lru_cache(None)
def vertices(geometry,keep):
    found=set();d=len(keep)
    if any(not any(a) and b<0 for a,b in geometry):return ()
    for indices in combinations(range(len(geometry)),d):
        point=solve([[geometry[i][0][j] for j in keep] for i in indices],[geometry[i][1] for i in indices])
        if point is not None and all(sum(a[j]*point[k] for k,j in enumerate(keep))<=b for a,b in geometry):found.add(point)
    return tuple(sorted(found))
def geom(rows):return tuple((a,b) for a,b,p in rows)
def enc_rows(rows):return [{'a':list(map(str,a)),'b':str(b),'proof':list(map(str,p))} for a,b,p in rows]
def lift(point,keep,stages):
    full=[Q(0)]*4
    for j,v in zip(keep,point):full[j]=v
    for stage in reversed(stages):
        index=stage['variable'];lower=[];upper=[]
        for a,b,p in stage['before']:
            residual=b-sum(a[j]*full[j] for j in range(4) if j!=index)
            if a[index]>0:upper.append(residual/a[index])
            elif a[index]<0:lower.append(residual/a[index])
            else:assert residual>=0
        lo=max(lower) if lower else None;hi=min(upper) if upper else None
        assert lo is None or hi is None or lo<=hi
        full[index]=lo if lo is not None else hi if hi is not None else Q(0)
    return tuple(full)

def main():
    src=ROOT/'grothendieck/results/ternary-tail-budget-dpc.json';own=load(src)
    c=list(map(Q,own['atom_capacity_upper']));B=list(map(Q,own['prefix_budget_upper']));w=[Q(v['lower']) for v in own['weights']]
    threshold=Q(own['block_threshold']);bad=list(map(Q,own['pairwise_LP']['primal']));optimal=list(map(Q,own['full_LP']['primal']))
    contract={'schema':'analytical-cut-composition-v1','source_sha256':sha(src),
      'variables':['x1','x2','x3','z'],'objective':'z=sum lower_kernel_i*x_i; the owning scalar lower functional, not the exact kernel pairing.',
      'algorithm':'Exact rational Fourier-Motzkin with nonnegative row certificates. Normalize positive scales; retain tightest parallel row. Join every incident factor before eliminating a shared variable.',
      'cuts':'All proper mass-variable subsets with z retained; all elimination orders. Four independently specified prefix commitments add equality rows before elimination.',
      'prefix_controls':['zero','owning_full_optimizer','owning_pair_candidate','half_pair_candidate'],
      'refinements':['objective_at_most_threshold','objective_at_least_threshold','third_cap_half','third_floor_quarter','inconsistent_third_interval','coupled_objective_third_cap'],
      'refinement_language':'Finite conjunctions of rational linear inequalities on retained coordinates. No reads of eliminated coordinates.',
      'bounds':{'retained_rows_per_stage':LIMIT_ROWS,'generated_rows_per_stage':LIMIT_CANDIDATES,'rational_numerator_denominator_bits':LIMIT_BITS},
      'direct_oracle':'Enumerate all vertices of the original bounded 3D carrier after substituting z; check projection and constructive lifts. Do not use a global minimal observer to define interfaces.',
      'negative_control':'Join exact pair mass projections after discarding their common missing-coordinate witnesses.',
      'scope':'Owning Chebyshev-derived three-bin moment relaxation. Not exact prime realizability, full-tail task advancement, general minimality or arbitrary-family storage boundedness.'}
    cp=OUT/'analytical-cut-composition-contract.json';save(cp,contract)
    source_rows=[]
    for i in range(3):source_rows.append((tuple(Q(-int(j==i)) for j in range(4)),Q(0)))
    for i in range(3):source_rows.append((tuple(Q(int(j==i)) for j in range(4)),c[i]))
    for i in range(3):source_rows.append((tuple(Q(int(j<=i)) for j in range(4)),B[i]))
    source_rows += [(tuple([-v for v in w]+[Q(1)]),Q(0)),(tuple(w+[Q(-1)]),Q(0))]
    def initialize(basis):
        n=len(basis);rows=[(a,b,tuple(Q(int(i==j)) for j in range(n))) for i,(a,b) in enumerate(basis)]
        for objective_row,offset in ((9,0),(10,3)):
            proof=[Q(0)]*n;proof[objective_row]=1
            for i in range(3):proof[offset+i]=-w[i]
            rows.append((tuple(sum(proof[k]*basis[k][0][j] for k in range(n)) for j in range(4)),sum(proof[k]*basis[k][1] for k in range(n)),tuple(proof)))
        return canonical(rows)
    def direct_vertices(basis):
        reduced=tuple((tuple(a[i]+a[3]*w[i] for i in range(3)),b) for a,b in basis)
        return [tuple(p)+(dot(w,p),) for p in vertices(reduced,(0,1,2))]
    plans=[]
    def run(name,extra,keep,order,late=None):
        basis=source_rows+extra;late=late or []
        if any(any(a[j] for j in order) for a,b in late):raise ValueError('ELIMINATED_COORDINATE_READ')
        all_basis=basis+late;n=len(all_basis)
        rows=initialize(basis)
        if late:rows=[(a,b,p+(Q(0),)*len(late)) for a,b,p in rows]
        stages=[]
        for index in order:
            before=rows;rows=eliminate(rows,index);stages.append({'variable':index,'before':before,'after':rows})
        if late:
            rows=list(rows)  # Do not mutate the exported final elimination stage.
            for i,(a,b) in enumerate(late,start=len(basis)):
                assert all(not a[j] for j in order)
                rows.append((a,b,tuple(Q(int(i==j)) for j in range(n))))
            rows=canonical(rows)
        # Every retained axis has upper and lower bounds, so vertex checks
        # characterize the entire projected polytope, not just sampled points.
        for j in keep:
            if any(not any(a) and b<0 for a,b,p in rows):break
            assert any(a[j]>0 and all(not a[k] for k in range(4) if k!=j) for a,b,p in rows)
            assert any(a[j]<0 and all(not a[k] for k in range(4) if k!=j) for a,b,p in rows)
        projected=vertices(geom(rows),tuple(keep));original=direct_vertices(all_basis)
        for x in original:assert all(dot(a,x)<=b for a,b,p in rows)
        lifted=[]
        for point in projected:
            x=lift(point,keep,stages)
            assert all(dot(a,x)<=b for a,b in all_basis);lifted.append(x)
        assert bool(projected)==bool(original)
        contradiction=None
        if not projected:
            empty=rows
            for j in keep:empty=eliminate(empty,j)
            contradiction=next(r for r in empty if not any(r[0]) and r[1]<0)
        plan={'name':name,'basis':[{'a':list(map(str,a)),'b':str(b)} for a,b in all_basis],
          'late_count':len(late),'keep':list(keep),'order':list(order),
          'stages':[{'variable':s['variable'],'before':enc_rows(s['before']),'after':enc_rows(s['after'])} for s in stages],
          'rows':enc_rows(rows),'projected_vertices':[list(map(str,p)) for p in projected],
          'source_vertices':[list(map(str,p)) for p in original],'lifts':[list(map(str,p)) for p in lifted],
          'infeasibility':enc_rows([contradiction])[0] if contradiction else None}
        plans.append(plan);return len(plans)-1,rows,projected
    groups=[];commutations=[];base_jobs=[]
    for k in range(3):
        for retained in combinations(range(3),k):
            keep=retained+(3,);orders=list(permutations([i for i in range(3) if i not in retained]));indices=[]
            for order in orders:
                i,rows,v=run('unconditioned',[],keep,order);indices.append(i);base_jobs.append(('unconditioned',[],keep,order,i))
            groups.append(indices)
    for name,prefix in [('zero',[Q(0),Q(0)]),('owning_full_optimizer',optimal[:2]),('owning_pair_candidate',bad[:2]),('half_pair_candidate',[v/2 for v in bad[:2]])]:
        extra=[]
        for i,value in enumerate(prefix):
            a=tuple(Q(int(j==i)) for j in range(4));extra.extend([(a,value),(tuple(-v for v in a),-value)])
        indices=[]
        for order in ((0,1),(1,0)):
            i,rows,v=run(name,extra,(2,3),order);indices.append(i);base_jobs.append((name,extra,(2,3),order,i))
        groups.append(indices)
    refinements=[('objective_at_most_threshold',[((Q(0),Q(0),Q(0),Q(1)),threshold)]),
      ('objective_at_least_threshold',[((Q(0),Q(0),Q(0),Q(-1)),-threshold)]),
      ('third_cap_half',[((Q(0),Q(0),Q(1),Q(0)),c[2]/2)]),
      ('third_floor_quarter',[((Q(0),Q(0),Q(-1),Q(0)),-c[2]/4)]),
      ('inconsistent_third_interval',[((Q(0),Q(0),Q(-1),Q(0)),-c[2]/2),((Q(0),Q(0),Q(1),Q(0)),c[2]/3)]),
      ('coupled_objective_third_cap',[((Q(0),Q(0),-w[2],Q(1)),Q(own['full_LP']['value'])/2)])]
    for name,extra,keep,order,base_id in base_jobs:
        if 2 not in keep:continue
        for refinement,frames in refinements:
            early,er,ev=run(name+'/'+refinement+'/early',extra+frames,keep,order)
            late,lr,lv=run(name+'/'+refinement+'/late',extra,keep,order,frames)
            assert ev==lv;commutations.append([early,late])
    for group in groups:
        first=plans[group[0]]['projected_vertices']
        assert all(plans[i]['projected_vertices']==first for i in group)
    # The known inadmissible triple passes each independently projected pair.
    pair_packets=[]
    for pair in combinations(range(3),2):
        basis=source_rows[:9];rows=[(a,b,tuple(Q(int(i==j)) for j in range(9))) for i,(a,b) in enumerate(basis)]
        rows=canonical(rows);missing=next(i for i in range(3) if i not in pair);before=rows;rows=eliminate(rows,missing)
        test=tuple(bad)+(Q(0),);assert all(dot(a,test)<=b for a,b,p in rows)
        witness=lift(tuple(bad[i] for i in pair),pair,[{'variable':missing,'before':before}])
        assert all(dot(a,witness)<=b for a,b in basis)
        pair_packets.append({'keep':list(pair),'missing':missing,'rows':enc_rows(rows),'lift':list(map(str,witness))})
    assert sum(bad)>B[2]
    test=tuple(bad)+(dot(w,bad),)
    maincut=next(p for p in plans if p['name']=='unconditioned' and p['keep']==[2,3])
    assert any(dot(tuple(map(Q,r['a'])),test)>Q(r['b']) for r in maincut['rows'])
    assert min(v[3] for v in direct_vertices(source_rows))==Q(own['full_LP']['value'])
    assert dot(w,bad)<threshold<Q(own['full_LP']['value'])
    try:run('forbidden_late_read',[],(2,3),(0,1),[((Q(1),Q(0),Q(0),Q(0)),Q(0))])
    except ValueError as error:assert str(error)=='ELIMINATED_COORDINATE_READ'
    else:raise AssertionError('eliminated-coordinate read admitted')
    packet={'source_rows':[{'a':list(map(str,a)),'b':str(b)} for a,b in source_rows],
      'plans':plans,'order_groups':groups,'refinement_commutations':commutations,'pairwise_negative':pair_packets,
      'bad_triple':list(map(str,bad)),'bad_objective':str(dot(w,bad)),
      'forbidden_late_read':{'eliminated_variable':'x1','reason':'Not in the declared retained-coordinate refinement language.'}}
    pp=OUT/'analytical-cut-composition-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'EXACT_COMPOSITION_PASSES_WITH_COMPLETE_SHARED_FACTORS','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'projection_plans':len(plans),'order_comparison_groups':len(groups),'refinement_commutation_pairs':len(commutations),
      'empty_projection_certificates':sum(p['infeasibility'] is not None for p in plans),
      'pairwise_negative':'All three exact pair projections admit the known candidate; the full residual relation rejects it.',
      'resource_usage':stats,'scope':contract['scope'],
      'qualification':'Exact rational polyhedral representation, not a minimal scalar interface. Refinement commutation is asserted only for retained coordinates; no independent witness may replace a shared eliminated variable.'}
    assert sha(src)==contract['source_sha256'];save(OUT/'analytical-cut-composition.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
