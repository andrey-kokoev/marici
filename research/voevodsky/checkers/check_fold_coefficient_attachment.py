"""Iteration 4: attach retained directions to the actual AB coefficient frame.
The coordinate-to-port bridge is explicitly declared, not a particle law.
Real geometric inputs and general Q(sqrt(-3)) inputs are distinguished.
"""
from fractions import Fraction as Q
from itertools import permutations
from copy import deepcopy
from pathlib import Path
from hashlib import sha256
import json

from check_fold_bearing_vertex import verify as verify_resolved, point_of_simplex, blowdown
from check_proton_merkle_reassembly import verify as verify_focus, weight, plus, times, ZERO, ONE, POINTS
from potential_complex_pullback import digest, depth

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/fold_bearing_vertex_store.json'
AXES=('x','y','z')

def neg(z): return -z[0],-z[1]
def sub(a,b): return plus(a,neg(b))
def embed(x): return Q(x),Q(0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def kmul(a,v): return [sumk(times(x,y) for x,y in zip(row,v)) for row in a]
def sumk(values):
    result=ZERO
    for v in values: result=plus(result,v)
    return result

def inverse(matrix):
    rows=[list(row)+[Q(i==j) for j in range(3)] for i,row in enumerate(matrix)]
    for j in range(3):
        p=next((i for i in range(j,3) if rows[i][j]),None)
        if p is None: raise ValueError('singular recovery matrix')
        rows[j],rows[p]=rows[p],rows[j]; d=rows[j][j]; rows[j]=[x/d for x in rows[j]]
        for i in range(3):
            if i!=j:
                d=rows[i][j]; rows[i]=[x-d*y for x,y in zip(rows[i],rows[j])]
    return [row[3:] for row in rows]

def source_data(packet):
    focus=packet['source']['focus']; _,rows=verify_focus(focus)
    store=focus['objects']; root=store[focus['root']]; geo=store[root['geometry']]['payload']
    triangle=next(r for r in geo['triangles_and_transports'] if r['outer_arrow']=='AB')
    matrix=[[ZERO for j in AXES] for i in AXES]
    for r in rows:
        if r['source'][:2]==['raw','AB'] and r['target'][:2]==['local','AB']:
            matrix[AXES.index(r['target'][2])][AXES.index(r['source'][2])]=weight(r)
    arrow_refs=[]; ports=set()
    for ref,a in store.items():
        if a['kind']!='arrow': continue
        s,t=store[a['source']],store[a['target']]
        if (s['stage'],s['triangle'],t['stage'],t['triangle'])==('raw','AB','local','AB'):
            arrow_refs.append(ref); ports.update((a['source'],a['target']))
    a=[Q(v) for v in POINTS['A']]; b=[Q(v) for v in POINTS['B']]
    f=[sum(Q(POINTS[v][i]) for v in 'ABC')/3 for i in range(3)]
    n=cross([x-y for x,y in zip(a,f)],[x-y for x,y in zip(b,f)])
    leading=next(x for x in n if x); n=[x/leading for x in n]
    return focus,matrix,n,sorted(arrow_refs),sorted(ports),triangle

def direction(v,alignment='ABCD'):
    if len(v)!=4 or depth(v)!=1: raise ValueError('not a potential boundary direction')
    return [sum(v[i]*Q(POINTS[alignment[i]][a]) for i in range(4)) for a in range(3)]

def mode(matrix,d): return kmul(matrix,list(map(embed,d)))
def encode_kmatrix(matrix): return [[list(map(str,z)) for z in row] for row in matrix]

def construct(source):
    focus,p,n,refs,ports,triangle=source_data(source)
    complement=[[sub(ONE if i==j else ZERO,p[i][j]) for j in range(3)] for i in range(3)]
    nn=dot(n,n); recovery=inverse([[p[i][j][0]+n[i]*n[j]/nn for j in range(3)] for i in range(3)])
    return {'kind':'fold-direction-coefficient-attachment','source_root':source['root'],'focus_root':focus['root'],
            'triangle':triangle,'original_local_arrow_refs':refs,'original_port_refs':ports,
            'input_type':'real geometric direction on boundary Delta3; not an arbitrary complex coefficient state',
            'declared_alignment':['A','B','C','D'],
            'coordinate_bridge':'d(v)=sum_i v_i*POINTS[alignment_i], interpreted in AB raw x/y/z ports',
            'mode_matrix':encode_kmatrix(p),'complement_matrix':encode_kmatrix(complement),
            'normal':list(map(str,n)),'real_recovery_matrix':[[str(x) for x in row] for row in recovery],
            'direction_readout':'L_AB d(v); defined on resolved directions, does not descend through center blowdown',
            'position_readout':'h_T(x) L_AB d(v); descends to the original realization but vanishes at its center',
            'full_coefficient_retention':'keep both L_AB z and (I-L_AB)z, reconstruct z by addition',
            'physical_interpretation':'none assigned'}

def verify(packet):
    if set(packet)!={'schema','source','record','root'} or packet['schema']!='marici.fold-coefficient-attachment.v1': raise ValueError('schema')
    verify_resolved(packet['source'])
    if digest(packet['record'])!=packet['root'] or packet['record']!=construct(packet['source']): raise ValueError('source-bound attachment mismatch')
    return True

def rejected(fn):
    try: fn()
    except (ValueError,KeyError,TypeError): return True
    return False

def main():
    source=json.loads(SOURCE.read_text(encoding='utf-8')); verify_resolved(source)
    focus,p,n,refs,ports,triangle=source_data(source); record=construct(source)
    packet={'schema':'marici.fold-coefficient-attachment.v1','source':source,'record':record,'root':digest(record)}
    verify(packet)
    nn=dot(n,n); recovery=[[Q(x) for x in row] for row in record['real_recovery_matrix']]
    complement=[[sub(ONE if i==j else ZERO,p[i][j]) for j in range(3)] for i in range(3)]
    zero=[ZERO]*3
    front=(Q(1,3),Q(1,3),Q(1,3),Q(0)); back=(Q(0),Q(0),Q(0),Q(1))
    d1=direction(front); d2=direction(back)
    checks={'actual_source_local_arrows_and_ports_bound':len(refs)==9 and len(ports)==6,
            'matrix_is_exact_projector':all(sumk(times(p[i][k],p[k][j]) for k in range(3))==p[i][j] for i in range(3) for j in range(3)),
            'host_normal_is_annihilated':kmul(p,list(map(embed,n)))==zero,
            'distinct_fold_directions_have_identical_zero_mode':d1!=d2 and mode(p,d1)==mode(p,d2)==zero,
            'normal_residual_distinguishes_lost_directions':dot(n,d1)!=dot(n,d2)}
    restored=True; positional=True; direction_at_center=set()
    # Includes the literal exceptional-fiber vertices.
    samples=[tuple(map(Q,x)) for x in source['record']['directions']['vertices'].values()]
    for simplex in source['record']['Q']['maximal_simplices']:
        x,v=point_of_simplex(source['record'],source['source'],simplex,[Q(i,15) for i in range(1,6)])
        samples.append(v)
        t=depth(x); _,old_y=blowdown(x,v)
        old_displacement=[sum(old_y[i]*Q(POINTS['ABCD'[i]][a]) for i in range(4)) for a in range(3)]
        positional &= mode(p,old_displacement)==[times(embed(t),z) for z in mode(p,direction(v))]
    for v in samples:
        d=direction(v); selected=mode(p,d); normal=dot(n,d)
        rhs=[selected[i][0]+normal*n[i]/nn for i in range(3)]
        recovered=[dot(row,rhs) for row in recovery]
        recovered_bary=tuple((1+dot([Q(a) for a in POINTS[k]],recovered))/4 for k in 'ABCD')
        restored &= recovered==d and recovered_bary==v
        direction_at_center.add(tuple(selected))
    checks['real_mode_plus_normal_reconstructs_every_sampled_direction']=restored
    checks['position_readout_commutes_with_radial_blowdown']=positional
    checks['direction_readout_does_not_descend_to_single_old_center']=len(direction_at_center)>1
    # IMPORTANT: the preceding real recovery is not a recovery of arbitrary K3.
    # Cross a nonzero row of P with the normal to find a complex null vector.
    row=p[0]; en=list(map(embed,n))
    complex_kernel=[sub(times(row[1],en[2]),times(row[2],en[1])),
                    sub(times(row[2],en[0]),times(row[0],en[2])),
                    sub(times(row[0],en[1]),times(row[1],en[0]))]
    checks['real_recovery_not_misrepresented_as_complex_injectivity']=any(z!=ZERO for z in complex_kernel) and kmul(p,complex_kernel)==zero and sumk(times(embed(a),z) for a,z in zip(n,complex_kernel))==ZERO
    checks['full_complex_residual_reconstructs_all_basis_states']=all(
        [plus(a,b) for a,b in zip(kmul(p,z),kmul(complement,z))]==z
        for z in [[ONE if i==j else ZERO for i in range(3)] for j in range(3)]+[complex_kernel])
    # Audit all 24 vertex-label alignments rather than silently selecting one.
    alignment_reports=[]
    for perm in permutations('ABCD'):
        zeros=[]
        for label,encoded in source['record']['directions']['vertices'].items():
            if mode(p,direction(tuple(map(Q,encoded)),perm))==zero: zeros.append(label)
        alignment_reports.append({'alignment':''.join(perm),'zero_mode_direction_vertices':zeros})
    checks['each_of_24_alignments_has_the_same_two_direction_collision']=all(len(r['zero_mode_direction_vertices'])==2 and sorted(map(len,r['zero_mode_direction_vertices']))==[1,3] for r in alignment_reports)
    # The host coordinate does not enter the directional readout. Keeping v
    # fixed around the actual six-link cycle therefore returns the same state.
    circle=['0','01','1','12','2','02','0']; host=source['source']['record']['contract']['T']
    loop_ok=True
    for v in samples[:14]:
        expected=mode(p,direction(v))
        for a in circle:
            u=tuple(map(Q,host['vertices'][a])); x=tuple(Q(1,6)+w/2 for w in u)
            loop_ok &= depth(x)==Q(1,2) and mode(p,direction(v))==expected
    checks['actual_frame_attachment_does_not_force_belt_permutation']=loop_ok
    bad=deepcopy(packet); bad['record']['mode_matrix'][0][0]=['1','0']; bad['root']=digest(bad['record'])
    checks['rehashed_replacement_projector_rejected']=rejected(lambda:verify(bad))
    bad=deepcopy(packet); bad['record']['original_port_refs'].pop(); bad['root']=digest(bad['record'])
    checks['rehashed_missing_typed_port_rejected']=rejected(lambda:verify(bad))
    checks['complete_packet_replays']=verify(json.loads(json.dumps(packet)))
    result={'schema':'marici.fold-coefficient-attachment-check.v1','passed':all(checks.values()),'checks':checks,
            'root':packet['root'],'source_root':source['root'],'sampled_directions':len(samples),
            'collision':{'potential_face_center':list(map(str,front)),'opposite_vertex':list(map(str,back)),
                         'normal_readouts':[str(dot(n,d1)),str(dot(n,d2))]},'matrix':record['mode_matrix'],
            'complex_null_witness':[list(map(str,z)) for z in complex_kernel],
            'alignments':alignment_reports,'source_file_sha256':sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Source-bound geometric-to-coefficient interface with explicit lost-mode witnesses. The bridge is a declared alignment; neither electron dynamics nor an H-1/H-2 total count is supplied.'}
    out=BASE/'results'
    (out/'fold_coefficient_attachment_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (out/'fold_coefficient_attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
