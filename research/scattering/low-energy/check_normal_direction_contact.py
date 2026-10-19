"""Conservation test of a conjectural normal-direction contact readout (EF1-N)."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from pathlib import Path
import check_hinge_phase_continuation as phase

hinge=phase.hinge;ROOT=hinge.ROOT;HOME=hinge.HOME;BASE=hinge.BASE
CONTRACT=HOME/'contracts/normal-direction-contact.v1.json'
PROOF=HOME/'NORMAL-DIRECTION-CONTACT-TEST.md'
RESULT=HOME/'results/normal-direction-contact.v1.json'


def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a

def pa(*args):
    out=[Q()]*max(map(len,args),default=1)
    for a in args:
        for i,v in enumerate(a):out[i]+=v
    return trim(out)
def ps(c,a):return trim([c*v for v in a])
def pm(a,b):
    out=[Q()]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)
def peval(a,r):
    v=Q()
    for c in reversed(a):v=v*r+c
    return v

def pcross(a,b):return [pa(pm(a[1],b[2]),ps(-1,pm(a[2],b[1]))),
    pa(pm(a[2],b[0]),ps(-1,pm(a[0],b[2]))),pa(pm(a[0],b[1]),ps(-1,pm(a[1],b[0])))]
def psub(a,b):return [pa(x,ps(-1,y)) for x,y in zip(a,b)]
def imul(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def ipoly(a,interval):
    v=(Q(),Q())
    for c in reversed(a):
        lo,hi=imul(v,interval);v=(lo+c,hi+c)
    return v

def points_polynomial():
    source={k:tuple(map(Q,v)) for k,v in hinge.POINTS.items()}
    M=hinge.mean([source[k] for k in 'AB']);c=hinge.sub(source['C'],M);d=hinge.sub(source['D'],M)
    D=[Q(1),Q(),Q(2)];an=[Q(1),Q(),Q(-2)];bn=[Q(),Q(1)]
    P={k:[ps(v,D) for v in point] for k,point in source.items()}
    P['E']=[pa(ps(m,D),ps(v,pa(an,ps(-1,bn))),ps(3*w,bn)) for m,v,w in zip(M,c,d)]
    P['F']=[pa(ps(m,D),ps(-3*v,bn),ps(w,pa(an,bn))) for m,v,w in zip(M,c,d)]
    return P,D

def partitions():return [('A'+''.join(pair),''.join(k for k in 'ABCDEF' if k not in ('A',)+pair))
                         for pair in combinations('BCDEF',2)]
def normal(P,t):return hinge.cross(hinge.sub(P[t[1]],P[t[0]]),hinge.sub(P[t[2]],P[t[0]]))
def pnormal(P,t):return pcross(psub(P[t[1]],P[t[0]]),psub(P[t[2]],P[t[0]]))

def validate_contract(c):
    assert c['schema']=='marici.scattering.normal-direction-contact.v1'
    assert c['candidate_id']=='EF1-N' and c['candidate_disposition']=='restricted_generic_edge_candidate_refuted'
    assert c['witness_parameter']=='2' and c['common_excluded_interval']==['1999/1000','2001/1000']
    for key in ('normal_direction_map_source_derived','fully_specified_contact_generator_constructed',
                'all_two_triangle_constructions_excluded','EF1_as_a_whole_refuted','three_photon_production_derived',
                'branching_ratio_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=phase.build();assert parent==json.loads(phase.RESULT.read_text(encoding='utf-8')),'stale phase continuation'
    P,D=points_polynomial();r=Q(c['witness_parameter']);interval=tuple(Q(v) for v in c['common_excluded_interval'])
    assert 0<Q(1,2)<interval[0]<r<interval[1]
    witness={k:tuple(peval(v,r)/peval(D,r) for v in point) for k,point in P.items()}
    audits=[];ratios=[];crosses={}
    for left,right in partitions():
        cross=pcross(pnormal(P,left),pnormal(P,right));crosses[left+'/'+right]=cross
        n,m=normal(witness,left),normal(witness,right);v=hinge.cross(n,m)
        assert hinge.dot(n,n)>0 and hinge.dot(m,m)>0 and hinge.dot(v,v)>0
        ratio=hinge.dot(v,v)/(hinge.dot(n,n)*hinge.dot(m,m));ratios.append(ratio)
        component=max(range(3),key=lambda i:abs(peval(cross[i],r)))
        enclosure=ipoly(cross[component],interval);assert enclosure[0]*enclosure[1]>0
        audits.append({'triangles':[left,right],'sine_squared_at_witness':str(ratio),
            'nonzero_cross_component':component,'cleared_component_polynomial':[str(v) for v in cross[component]],
            'common_interval_component_enclosure':[str(v) for v in enclosure]})
    assert len(audits)==10 and min(ratios)==Q(104,729)
    # Original ACE/BDF cannot pass at ANY non-superposed finite hinge angle.
    expected=ps(-128,pm([Q(),Q(),Q(2),Q(),Q(1)],pm(D,D)))
    assert crosses['ACE/BDF'][2]==expected
    source={k:tuple(map(Q,v)) for k,v in hinge.POINTS.items()};M=hinge.mean([source[k] for k in 'AB'])
    opposite=dict(source);opposite['E']=hinge.sub(hinge.scale(2,M),source['C']);opposite['F']=hinge.sub(hinge.scale(2,M),source['D'])
    at_pi=[]
    for left,right in partitions():
        n,m=normal(opposite,left),normal(opposite,right)
        if hinge.cross(n,m)==(0,0,0) and hinge.dot(n,n)*hinge.dot(m,m)>0:at_pi.append([left,right])
    assert at_pi==[['ACD','BEF'],['ACF','BDE'],['ADE','BCF'],['AEF','BCD']]
    original_faces={''.join(t) for cell in ('ABCD','ABEF') for t in combinations(cell,3)}
    native_faces_at_pi=[pair for pair in at_pi if all(t in original_faces for t in pair)]
    assert native_faces_at_pi==[['ACD','BEF'],['AEF','BCD']]
    for a,b in (('A','B'),('C','E'),('D','F')):assert hinge.mean([opposite[a],opposite[b]])==M
    assert hinge.cross(normal(opposite,'ACE'),normal(opposite,'BDF'))[2]==-32
    # Source ABC face-sharing configuration: the three extracted triangles.
    source['e']=hinge.sub(hinge.scale(2,hinge.mean([source[k] for k in 'ABC'])),source['D'])
    normals=[normal(source,t) for t in ('ADe','BDe','CDe')]
    assert tuple(sum(n[i] for n in normals) for i in range(3))==(0,0,0)
    assert all(hinge.dot(n,n)==Q(512,9) for n in normals)
    assert all(hinge.dot(a,b)==Q(-256,9) for a,b in combinations(normals,2))
    assert hinge.dot(hinge.cross(normals[0],normals[1]),hinge.cross(normals[0],normals[1]))>0
    refused=[]
    for key in ('normal_direction_map_source_derived','fully_specified_contact_generator_constructed',
                'all_two_triangle_constructions_excluded','EF1_as_a_whole_refuted',
                'three_photon_production_derived','branching_ratio_derived','physical_outcomes_admitted'):
        bad=copy.deepcopy(c);bad[key]=True
        try:validate_contract(bad)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported conservation-test promotion: '+key)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((phase.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_normal_direction_contact.py',
                  ROOT/'research/nima/photon-two-packet-construction.md'))
    return {'schema':'marici.scattering.normal-direction-contact-receipt.v1','status':'pass',
        'scope_verdict':'restricted_normal_readout_refuted_not_a_general_photon_no_go',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'candidate_id':'EF1-N','candidate_disposition':c['candidate_disposition'],
        'witness_parameter':'2','witness_cosine':'-7/9','witness_scaled_sine':'2/9',
        'witness_coordinates':{k:[str(v) for v in point] for k,point in witness.items()},
        'complementary_triangle_partition_audits':audits,'common_excluded_interval':c['common_excluded_interval'],
        'minimum_unoriented_angle_sine_squared':'104/729','maximum_absolute_angle_cosine':'25/27',
        'half_angle_cone_threshold_sine_squared':'1/27',
        'original_ACE_BDF_cross_z':'-128*r^2*(r^2+2)/(1+2*r^2)^2',
        'nondegenerate_parallel_partitions_at_pi':at_pi,
        'already_present_input_face_pairs_at_pi':native_faces_at_pi,
        'face_three_normals':[[str(v) for v in n] for n in normals],
        'face_three_pairwise_cosine':'-1/2','face_three_cm_energy_fractions':['1/3']*3,
        'face_three_kinematic_configuration_allowed':True,'normal_direction_map_source_derived':False,
        'fully_specified_contact_generator_constructed':False,'all_two_triangle_constructions_excluded':False,
        'EF1_as_a_whole_refuted':False,'three_photon_production_derived':False,'branching_ratio_derived':False,
        'analytic_argument_machine_formalized':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'unsupported_promotions_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale normal-direction contact test'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','candidate_disposition','minimum_unoriented_angle_sine_squared',
        'original_ACE_BDF_cross_z','nondegenerate_parallel_partitions_at_pi','face_three_cm_energy_fractions',
        'fully_specified_contact_generator_constructed','EF1_as_a_whole_refuted')}))


if __name__=='__main__':main()
