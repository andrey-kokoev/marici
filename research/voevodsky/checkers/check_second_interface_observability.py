"""Can a second existing local interface observe what the first forgets?
All readouts are evaluated on the SAME retained input. This is not sequential
projection after discarding the original input.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, permutations
from hashlib import sha256
import json
from check_geometric_cycle_reversal import geo, SOURCE, verify, ONE, conj, encode
from check_reversed_coefficient_attachment import weight, ZERO, times, div, multiply, rank
from check_retained_barycenter_attachment import rank_columns

BASE=Path(__file__).resolve().parents[1]

def apply(p,d): return [r[0] for r in multiply(p,[[(x,Q(0))] for x in d])]
def real_rows(p): return [list(z[part] for z in row) for row in p for part in (0,1)]
def real_rank(maps):
    rows=[row for p in maps for row in real_rows(p)]
    return rank_columns([{i:r[j] for i,r in enumerate(rows)} for j in range(3)])
def xyz(v): return tuple(sum(v[i]*geo.POINTS['ABCD'[i]][j] for i in range(4)) for j in range(3))

def main():
    original=SOURCE.read_bytes(); source=json.loads(original); evidence,rows=verify(source)
    objects=source['objects']; geometry=objects[objects[source['root']]['geometry']]['payload']
    triangles={r['outer_arrow']:r for r in geometry['triangles_and_transports']}
    raw={e:[[ZERO]*3 for _ in range(3)] for e in triangles}
    for r in rows:
        if r['source'][0]=='raw' and r['target'][0]=='local':
            assert r['source'][1]==r['target'][1]
            raw[r['source'][1]]['xyz'.index(r['target'][2])]['xyz'.index(r['source'][2])]=weight(r)
    points=dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face]=geo.mean([points[v] for v in face])
    maps={}
    for edge,row in triangles.items():
        X=geo.transpose(tuple(points[k] for k in row['triangle']))
        v=geo.zmv(X,(ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))
        D=[div(x,conj(x)) for x in v]
        maps[edge]=[[times(D[i],conj(x)) for x in row] for i,row in enumerate(raw[edge])]
    owner=lambda edge:triangles[edge]['triangle'][0][2:]
    pair_reports=[]
    for a,b in combinations(sorted(maps),2):
        pair_reports.append({'interfaces':[a,b],'faces':[owner(a),owner(b)],
                             'real_rank':real_rank([maps[a],maps[b]]),
                             'complex_rank':rank(maps[a]+maps[b])})
    first,second='AB','AC'
    chosen=[maps[first],maps[second]]
    # Weighted real Gram matrix of the two complex readouts, with
    # |a+b sqrt(-3)|^2=a^2+3b^2. It is positive definite exactly when
    # the real stacked readout is injective.
    M=[[sum(p[k][i][0]*p[k][j][0]+3*p[k][i][1]*p[k][j][1]
            for p in chosen for k in range(3)) for j in range(3)] for i in range(3)]
    inverse=geo.inv(tuple(tuple(row) for row in M))
    def recover(outputs):
        rhs=tuple(sum(p[k][i][0]*z[k][0]+3*p[k][i][1]*z[k][1]
                      for p,z in zip(chosen,outputs) for k in range(3)) for i in range(3))
        return geo.mv(inverse,rhs)
    front=(Q(1,3),Q(1,3),Q(1,3),Q(0)); back=(Q(0),Q(0),Q(0),Q(1))
    d1,d2=xyz(front),xyz(back)
    witness={e:{'front':encode(apply(maps[e],d1)),'back':encode(apply(maps[e],d2))} for e in (first,second)}
    samples=[]
    for a in range(13):
        for b in range(13-a):
            for c in range(13-a-b):
                samples.append(tuple(Q(x,12) for x in (a,b,c,12-a-b-c)))
    restored=all(recover([apply(p,xyz(v)) for p in chosen])==xyz(v) for v in samples)
    # AB-normal is exactly the real information lost by the first readout.
    n=tuple(Q(x) for x in (1,1,-1))
    first_comparisons={e:apply(maps[e],n)!=[ZERO]*3 for e in maps if e!=first}
    # Sequential processing of an erased readout cannot recover a collision.
    first_zero=apply(maps[first],d1)==apply(maps[first],d2)==[ZERO]*3
    sequential=multiply(maps[second],[[x] for x in apply(maps[first],d1)])==multiply(maps[second],[[x] for x in apply(maps[first],d2)])
    triple_reports=[{'interfaces':list(es),'complex_rank':rank([row for e in es for row in maps[e]])}
                    for es in combinations(sorted(maps),3)]
    checks={
        'source_freshly_verified':evidence['verified'],
        'all_twelve_local_interfaces_have_real_rank_two':all(real_rank([p])==2 for p in maps.values()),
        'all_66_real_pair_ranks_follow_face_normal_rule':len(pair_reports)==66 and all(r['real_rank']==(2 if r['faces'][0]==r['faces'][1] else 3) for r in pair_reports),
        'first_interface_has_exact_distinct_direction_collision':front!=back and first_zero,
        'second_interface_separates_that_collision':apply(maps[second],d1)!=apply(maps[second],d2),
        'nine_different_face_interfaces_reveal_AB_kernel':sum(first_comparisons.values())==9,
        'two_other_same_face_interfaces_remain_blind':sum(not x for x in first_comparisons.values())==2,
        'joint_gram_inverse_exact':geo.mm(tuple(tuple(row) for row in M),inverse)==geo.I,
        'all_455_barycentric_grid_points_recovered':len(samples)==455 and restored,
        'general_inverse_verified_on_real_basis':all(recover([apply(p,tuple(Q(i==j) for i in range(3))) for p in chosen])==tuple(Q(i==j) for i in range(3)) for j in range(3)),
        'erased_first_readout_cannot_be_rescued_by_sequential_projection':sequential,
        'two_complex_rank_one_readouts_do_not_recover_arbitrary_complex_input':all(r['complex_rank']<=2 for r in pair_reports),
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    result={'verification_passed':all(checks.values()),'checks':checks,
        'contract':{'input':'one retained real geometric vector d, read by both local interfaces',
                    'readout':'D_triangle conjugate(L_triangle) d, with D derived from the local generated mode',
                    'not_assumed':'a dynamical measurement law or automatic transfer of the discarded input to a second projector'},
        'chosen_interfaces':[first,second],'collision':{'front_barycentric':list(map(str,front)),'back_barycentric':list(map(str,back)),'readouts':witness},
        'gram_matrix':[[str(x) for x in row] for row in M],
        'inverse_gram':[[str(x) for x in row] for row in inverse],
        'recovery':'d=(sum Re(A* A))^-1 sum Re(A* z), using both interfaces; barycentric_i=(1+POINTS[i].d)/4',
        'pair_counts':{'same_face_rank_two':sum(r['real_rank']==2 for r in pair_reports),'different_face_rank_three':sum(r['real_rank']==3 for r in pair_reports)},
        'complex_triple_rank_counts':{str(k):sum(r['complex_rank']==k for r in triple_reports) for k in (1,2,3)},
        'pairs':pair_reports,'complex_triples':triple_reports,
        'outcome':'Retained differences invisible to one existing interface are visible to another on a different face. Two such readouts reconstruct every real geometric input exactly.',
        'source_sha256':sha256(original).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/second_interface_observability.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pairs','complex_triples')},indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
