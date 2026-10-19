"""Exact local-versus-collective response on retained tetrahedral geometry.

Source support is imported, not regenerated. The static face-flux norm is a
DECLARED Maxwell-shaped realization, not the native L/G/N dynamics. Primitive
unit occurrences are not identified with antisymmetric field coordinates.
No physical time, SI conversion, rest offset or mass fit.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import isqrt, sqrt
import hashlib,json,sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from check_proton_merkle_reassembly import verify, ARROWS, GEOMETRY


@dataclass(frozen=True,eq=False)
class Q:
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    def __add__(self,x):
        x=cast(x);return Q(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,x):return self+-cast(x)
    def __rsub__(self,x):return cast(x)+-self
    def __mul__(self,x):
        x=cast(x);return Q(self.a*x.a+6*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=cast(x);den=x.a*x.a-6*x.b*x.b
        if not den:raise ZeroDivisionError()
        return self*Q(x.a/den,-x.b/den)
    def __rtruediv__(self,x):return cast(x)/self
    def __eq__(self,x):
        if isinstance(x,(Q,int,F)):return self.a==cast(x).a and self.b==cast(x).b
        return False
    def __bool__(self):return self.a!=0 or self.b!=0
    def sign(self):
        if not self:return 0
        if self.a>=0 and self.b>=0:return 1
        if self.a<=0 and self.b<=0:return -1
        comparison=self.a*self.a-6*self.b*self.b
        return (1 if comparison>0 else -1) if self.a>0 else (-1 if comparison>0 else 1)
    def record(self):return {'rational':str(self.a),'sqrt6':str(self.b)}
    def approximate(self):return float(self.a)+sqrt(6)*float(self.b)


def cast(x):return x if isinstance(x,Q) else Q(x)
def rational_sqrt(x):
    x=F(x);a=isqrt(x.numerator);b=isqrt(x.denominator)
    return F(a,b) if a*a==x.numerator and b*b==x.denominator else None

def root_ratio(x):
    direct=rational_sqrt(x)
    if direct is not None:return Q(direct)
    coefficient=rational_sqrt(x/6)
    if coefficient is None:raise ValueError('Ratio outside the declared Q(sqrt6) fixtures')
    return Q(0,coefficient)


def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),Q()) for col in zip(*b)] for row in a]
def mv(a,v):return [sum((x*y for x,y in zip(row,v)),Q()) for row in a]
def difference(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inverse(a):
    n=len(a);work=[list(map(cast,row))+eye(n)[i] for i,row in enumerate(a)]
    for c in range(n):
        p=next(i for i in range(c,n) if work[i][c]);work[c],work[p]=work[p],work[c]
        divisor=work[c][c];work[c]=[x/divisor for x in work[c]]
        for i in range(n):
            if i!=c:
                factor=work[i][c];work[i]=[x-factor*y for x,y in zip(work[i],work[c])]
    out=[r[n:] for r in work];assert mm(a,out)==eye(n);return out

def rank(a):
    work=[list(map(cast,row)) for row in a];r=0
    for c in range(len(work[0])):
        p=next((i for i in range(r,len(work)) if work[i][c]),None)
        if p is None:continue
        work[r],work[p]=work[p],work[r];divisor=work[r][c];work[r]=[x/divisor for x in work[r]]
        for i in range(r+1,len(work)):
            factor=work[i][c];work[i]=[x-factor*y for x,y in zip(work[i],work[r])]
        r+=1
        if r==len(work):break
    return r


def encoded(a):return [[cast(x).record() for x in row] for row in a]
def vector(v):return [cast(x).record() for x in v]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a):return dot(a[0],cross(a[1],a[2]))
def area_squared(points,face):
    a,b,c=(points[v] for v in face);normal=cross(sub(b,a),sub(c,a));return dot(normal,normal)/4

def boundary_chain(triangles):
    result={}
    for a,b,c in triangles:
        for u,v in ((a,b),(b,c),(c,a)):
            key=tuple(sorted((u,v)));result[key]=result.get(key,F(0))+(1 if u<v else -1)
    return {key:value for key,value in result.items() if value}


def stiffness(C,weights):return mm(transpose(C),[[weights[i]*x for x in row] for i,row in enumerate(C)])
def solve(K,C,weights,s):
    system=[[x+Q(s)*Q(i==j) for j,x in enumerate(row)] for i,row in enumerate(K)]
    R=inverse(system);force=[Q(1)]+[Q()]*5;response=mv(R,force);flux=mv(C,response)
    assert mv(system,response)==force
    # An independent full/environment Schur construction at the anchored edge.
    rest=inverse([r[1:] for r in system[1:]])
    coupling=[r[0] for r in system[1:]];link=mv(rest,coupling)
    schur=system[0][0]-sum((x*y for x,y in zip(system[0][1:],link)),Q())
    anchored=1/schur;rebuilt=[anchored]+[-x*anchored for x in link]
    assert rebuilt==response
    local=1/system[0][0]
    energy=sum((w*b*b for w,b in zip(weights,flux)),Q())/2
    assert energy==sum((x*y for x,y in zip(response,mv(K,response))),Q())/2
    return {'R':R,'response':response,'flux':flux,'local':local,'energy':energy,'schur':schur}


def main():
    source=ROOT/'research/voevodsky/results/proton_merkle_store.json'
    freeze=ROOT/'research/strominger/inputs/arrow-anchored-response-freeze.json'
    frozen=json.loads(freeze.read_text());assert frozen['disposition']=='preregistered; not yet computed'
    packet=json.loads(source.read_text());verified,source_rows=verify(packet);assert verified['verified']
    objects=packet['objects'];root=objects[packet['root']];geom=objects[root['geometry']]['payload']
    for key,path in [('arrows_sha256',ARROWS),('geometry_sha256',GEOMETRY)]:
        assert hashlib.sha256(path.read_bytes()).hexdigest()==root['source_files'][key]
    points={}
    for sector in root['sectors']:
        for label,coords in objects[objects[sector]['geometry']]['vertices'].items():
            if label=='O':continue
            point=tuple(map(F,coords));assert label not in points or points[label]==point;points[label]=point
    labels='ABCD';assert set(points)==set(labels)
    edges=list(combinations(labels,2));edge_labels=[''.join(e) for e in edges];faces=list(combinations(labels,3))
    original={row['outer_arrow']:row for row in geom['triangles_and_transports']}
    assert set(original)=={a+b for a in labels for b in labels if a!=b}
    primitives=[{'label':name,'tail':name[0],'head':name[1],'weight':'1',
                 'source_triangle':original[name]['triangle'],'reverse_occurrence':name[::-1]} for name in sorted(original)]
    C=[];chains={}
    for face in faces:
        name=''.join(face)
        triangles=[row['triangle'] for row in original.values() if ''.join(sorted(row['triangle'][0][2:]))==name]
        assert len(triangles)==3
        chain=boundary_chain(triangles);assert set(chain)==set(combinations(face,2))
        chains[name]={'source_triangles':triangles,'whole_face_boundary':{''.join(k):str(v) for k,v in chain.items()}}
        C.append([Q(chain.get(edge,0)) for edge in edges])
    G=[[Q(v==b)-Q(v==a) for v in labels] for a,b in edges]
    assert mm(C,G)==[[Q()]*4 for _ in range(4)]
    assert all(sum((row[j] for row in C),Q())==0 for j in range(6))
    assert rank(C)==rank(G)==3
    checks={'fresh_merkle_source_and_all_twelve_primitive_labels':True,
            'source_subdivision_boundaries_reproduce_all_four_face_loops':True,
            'boundary_of_boundary_and_gauge_kernel_exact':True}
    readout=[[Q(int(name==e)-int(name==e[::-1])) for e in edge_labels] for name in sorted(original)]
    assert rank(readout)==6 and sum(F(row['weight']) for row in primitives)==12
    checks['twelve_unit_occurrences_retained_despite_six_antisymmetric_field_coordinates']=True
    # Proper rational hinge of D about AB. A, B and C stay fixed. Both anchor
    # faces preserve ALL side lengths; only the remote edge CD changes.
    hinge=[[F(1,3),F(-2,3),F(2,3)],[F(2,3),F(2,3),F(1,3)],[F(-2,3),F(1,3),F(2,3)]]
    assert det(hinge)==1 and mm(transpose(hinge),hinge)==eye(3)
    axis=sub(points['B'],points['A']);assert mv(hinge,axis)==list(axis)
    moved=dict(points);moved['D']=tuple(points['A'][i]+sum(hinge[i][j]*(points['D'][j]-points['A'][j]) for j in range(3)) for i in range(3))
    local_edges=['AB','AC','BC','AD','BD']
    length=lambda p,e:dot(sub(p[e[1]],p[e[0]]),sub(p[e[1]],p[e[0]]))
    assert all(length(points,e)==length(moved,e) for e in local_edges)
    assert length(points,'CD')!=length(moved,'CD')
    assert det([sub(points[k],points['A']) for k in 'BCD'])*det([sub(moved[k],moved['A']) for k in 'BCD'])>0
    checks['proper_remote_geometry_change_preserves_complete_anchor_face_geometry']=True
    areas={name:[area_squared(p,face) for face in faces] for name,p in [('source',points),('hinged',moved)]}
    assert areas['source']==[F(12)]*4 and areas['hinged'][:2]==areas['source'][:2]
    metric={name:[root_ratio(areas['source'][0]/area) for area in values] for name,values in areas.items()}
    assert metric['hinged'][2:]==[Q(0,F(3,8))]*2
    assert all(w.sign()>0 for values in metric.values() for w in values)
    checks['positive_face_metric_derived_from_actual_face_areas']=True
    records={};outcomes={};primary_packet_equal=True;control_packet_different=True;force=[Q(1)]+[Q()]*5
    for multiplier in (1,2):
        branch='source_face_metric' if multiplier==1 else 'unequal_incident_metric_control'
        weights={name:[w*(multiplier if i==1 else 1) for i,w in enumerate(values)] for name,values in metric.items()}
        K={name:stiffness(C,values) for name,values in weights.items()}
        assert K['source'][0]==K['hinged'][0]
        assert all(mm(matrix,G)==[[Q()]*4 for _ in range(6)] for matrix in K.values())
        assert all(rank(matrix)==3 for matrix in K.values())
        if multiplier==1:
            for matrix in K.values():
                bright=mv(matrix,force)
                assert mv(matrix,bright)==[4*x for x in bright]
                assert mv(C,bright)[2:]==[Q(),Q()]
        entries=[]
        for s in (1,2):
            solved={name:solve(matrix,C,weights[name],F(s)) for name,matrix in K.items()}
            assert solved['source']['local']==solved['hinged']['local']
            assert all(sum(obj['flux'],Q())==0 for obj in solved.values())
            difference_packet=[x-y for x,y in zip(solved['hinged']['response'],solved['source']['response'])]
            delta_R=difference(solved['hinged']['R'],solved['source']['R'])
            assert rank(delta_R)==2
            if multiplier==1:
                assert all(x==0 for x in difference_packet)
                for name,obj in solved.items():
                    predicted=[force[i]/s-mv(K[name],force)[i]/(s*(s+4)) for i in range(6)]
                    assert obj['response']==predicted and obj['flux'][2:]==[Q(),Q()]
                    assert obj['response'][0]!=obj['local']
                primary_packet_equal=primary_packet_equal and not any(difference_packet)
            else:
                assert any(difference_packet)
                assert (solved['hinged']['response'][0]-solved['source']['response'][0]).sign()>0
                assert any(solved['source']['flux'][i]!=0 for i in (2,3))
                control_packet_different=control_packet_different and any(difference_packet)
            entries.append({'probe_s':s,'local_response':solved['source']['local'].record(),
                'full_response_difference_rank':rank(delta_R),
                'anchored_packet_difference':vector(difference_packet),
                'anchored_response_source_approx':solved['source']['response'][0].approximate(),
                'anchored_response_hinged_approx':solved['hinged']['response'][0].approximate(),
                'configurations':{name:{'all_edge_response':vector(obj['response']),
                    'all_twelve_occurrence_readout':vector(mv(readout,obj['response'])),
                    'all_face_curvature':vector(obj['flux']),'whole_resolvent':encoded(obj['R']),
                    'anchored_schur':obj['schur'].record(),'curvature_form_value':obj['energy'].record()}
                    for name,obj in solved.items()}})
        records[branch]={'ABD_metric_multiplier':multiplier,
                        'face_metrics':{name:vector(v) for name,v in weights.items()},
                        'operators':{name:encoded(v) for name,v in K.items()},'cases':entries}
    checks['full_and_environment_schur_reconstruction_agree_at_all_four_probes']=True
    checks['source_metric_full_anchored_packet_is_shielded_not_merely_a_scalar_readout']=primary_packet_equal
    checks['whole_configuration_resolvent_changes_despite_shielded_anchor']=True
    checks['unequal_incident_metric_control_restores_remote_sensitivity']=bool(control_packet_different)
    checks['all_closure_and_gauge_records_retained_without_a_mass_offset']=True
    result={'status':'passed','checks':checks,
        'scientific_disposition':'The preregistered universal-sensitivity conjecture is falsified in the source face-metric branch. The entire AB packet is protected by equal incident weights. Global resolvents still differ with rank two; a declared unequal-weight control exposes remote sensitivity.',
        'four_roles':{'primitive':'Twelve distinct unit occurrences, not six mass units after cochain antisymmetry.',
            'configuration':'Source geometry, source boundary chains, all face metrics and full edge operator.',
            'anchored_local':'Complete AB row and clamped response. They stay fixed through the hinge.',
            'anchored_collective':'Entire six-coordinate response, all twelve readouts, all curvatures, Schur complement and full configuration resolvent.'},
        'source_coefficient_transfers_verified':len(source_rows),'primitive_registry':primitives,
        'field_coordinate_order':edge_labels,'face_order':[''.join(f) for f in faces],
        'source_boundary_chains':chains,'face_incidence':encoded(C),'vertex_gradient':encoded(G),
        'primitive_readout':encoded(readout),
        'geometries':{name:{label:list(map(str,v)) for label,v in p.items()} for name,p in [('source',points),('hinged',moved)]},
        'face_area_squared':{name:list(map(str,v)) for name,v in areas.items()},
        'hinge_rotation':[list(map(str,row)) for row in hinge],
        'shielding_identity':'For equal unit incident weights, K(K e_AB)=4 K e_AB and remote face rows annihilate K e_AB. Hence R_s e_AB=e_AB/s-K e_AB/[s(s+4)], independent of remote face weights.',
        'sensitivity_identity':'For a face weight w_f, d(R_s)_AB,AB/dw_f=-(C_f R_s e_AB)^2. The two remote curvature entries vanish in the source branch and become nonzero in the control.',
        'branches':records,
        'scope':'Static geometry-derived surface flux norm; a declared Maxwell-shaped response realization, not the native source dynamics or a physical Maxwell/time/particle-mass derivation.',
        'metric_rule':'Reference face area divided by each face area; no SI normalization or neutron/electron mass target.',
        'not_interpreted':['Probe s is not physical time or a rest-energy offset.','Zero cochain sum does not erase primitive traversal weight.','A change of global geometry does not necessarily change every anchored response.']}
    inputs=[source,ARROWS,GEOMETRY,freeze,Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/check_proton_merkle_reassembly.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/arrow-anchored-response.json';out.write_text(json.dumps(result,indent=2)+'\n')
    summary={name:[{'s':case['probe_s'],'local':case['local_response'],
                    'full_source':case['anchored_response_source_approx'],'full_hinged':case['anchored_response_hinged_approx']}
                  for case in data['cases']] for name,data in records.items()}
    print(json.dumps({'status':'passed','checks':len(checks),'disposition':result['scientific_disposition'],'responses':summary},indent=2))

if __name__=='__main__':main()
