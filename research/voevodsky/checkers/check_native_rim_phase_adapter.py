"""Metric-unitary local rim adapter and explicit moving-port schedule.
The contraction is a declared edge/transverse coefficient map. Its dilation
retains both port inputs; no full spinor coupling or interaction law is inferred.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from assemble_relative_geometry import apply,dot_metric,subtract
from check_neutron_rim_port_transport import source_vertices,generators,group,mean
from check_belt_operator_inputs import mode,frame,qm

BASE=Path(__file__).resolve().parents[1]


class Scalar:
    """Q(sqrt(151), i sqrt(3)); basis 1,R,J,JR with R^2=151,J^2=-3."""
    def __init__(self,a=0,b=0,c=0,d=0):self.v=tuple(map(Q,(a,b,c,d)))
    @staticmethod
    def cast(x):return x if isinstance(x,Scalar) else Scalar(x)
    def __add__(self,o):return Scalar(*(a+b for a,b in zip(self.v,Scalar.cast(o).v)))
    __radd__=__add__
    def __neg__(self):return Scalar(*(-x for x in self.v))
    def __sub__(self,o):return self+-Scalar.cast(o)
    def __rsub__(self,o):return Scalar.cast(o)+-self
    def __mul__(self,o):
        out=[Q(0)]*4
        for i,a in enumerate(self.v):
            for j,b in enumerate(Scalar.cast(o).v):
                r=i%2+j%2;k=i//2+j//2
                out[r%2+2*(k%2)]+=a*b*(151 if r>=2 else 1)*(-3 if k>=2 else 1)
        return Scalar(*out)
    __rmul__=__mul__
    def conjugate(self):return Scalar(self.v[0],self.v[1],-self.v[2],-self.v[3])
    def __eq__(self,o):return self.v==Scalar.cast(o).v
    def encoded(self):return list(map(str,self.v))


def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def adjoint(A):return [[Scalar.cast(x).conjugate() for x in col] for col in zip(*A)]
def equal(A,B):return len(A)==len(B) and all(len(a)==len(b) and all(Scalar.cast(x)==y for x,y in zip(a,b)) for a,b in zip(A,B))
def diag(xs):return [[v if i==j else 0 for j in range(len(xs))] for i,v in enumerate(xs)]
def vector(A,x):return [row[0] for row in mm(A,[[v] for v in x])]
def norm(x,G):return mm(mm(adjoint([[v] for v in x]),G),[[v] for v in x])[0][0]
def basis(points,face,a,b):
    edge=tuple(x/2 for x in subtract(points[a],points[b]))
    transverse=subtract(mean([points[k] for k in face]),mean([points[a],points[b]]))
    return edge,transverse

def main():
    paths=[BASE/'inputs/relative-proton.json',BASE/'inputs/relative-electron.json',BASE/'inputs/mode-neutron.json',BASE/'results/four_six_center_cones.json',BASE/'results/coupled_six_piece_belt_store.json']
    ps,es,ns,geometry,packet=[json.loads(p.read_text(encoding='utf-8')) for p in paths]
    record=packet['record']
    assert sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()==packet['root']
    assert record['geometry_sha256']==sha256(paths[3].read_bytes()).hexdigest()
    P=source_vertices(3);E=source_vertices(4)
    N={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items() if k!='O'}
    GP=[[Q(v) for v in row] for row in ps['metric']];GE=[[Q(v) for v in row] for row in es['metric']]
    GN=[[Q(8,3)*Q(v) for v in row] for row in ns['metric']]
    gn=generators(ns)[0];ge=generators(es)[0]
    nr={k:{v:n for n,v in N.items()}[apply(gn,p)] for k,p in N.items()}
    er={k:{v:n for n,v in E.items()}[apply(ge,p)] for k,p in E.items()}
    lower_required={chr(65+i):chr(65+int(nr['L'+str(i)][1:])) for i in range(3)}
    pr,pword=next((action,word) for action,word in group(P,generators(ps)) if all(action[k]==v for k,v in lower_required.items()))
    def proton_action(v):
        for i in pword:v=apply(generators(ps)[i],v)
        return v
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:raise AssertionError(name)
    check('source_actions_are_isometries',all(dot_metric(subtract(apply(ge,a),apply(ge,b)),subtract(apply(ge,a),apply(ge,b)),GE)==dot_metric(subtract(a,b),subtract(a,b),GE) for a in E.values() for b in E.values()))
    # Derive chart metrics from actual coordinates, not fitted transition rates.
    initial_face=next(f for f in geometry['belt_faces'] if {'L0','L1'}<=set(f))
    ne,nr0=basis(N,initial_face,'L0','L1');pe,pr0=basis(P,'ABC','A','B')
    edge_norm=dot_metric(ne,ne,GN);beta=dot_metric(nr0,nr0,GN);alpha=dot_metric(pr0,pr0,GP)
    transmission=beta/alpha;defect=alpha-beta;delta=Scalar(0,Q(1,15))
    check('geometry_derived_metric_values',(edge_norm,beta,alpha)==(Q(2),Q(148,675),Q(2,3)))
    check('geometry_derived_contraction_defect',transmission==Q(74,225) and delta*delta==1-transmission and defect==Q(302,675))
    # Coordinates: carrier edge/transverse, belt edge/transverse. The chart
    # matrix is not Euclidean-unitary; it is unitary for the physical Gram metric.
    G=diag([edge_norm,alpha,edge_norm,beta])
    U=[[0,0,1,0],[0,delta,0,transmission],[1,0,0,0],[0,1,0,-delta]]
    check('full_four_coordinate_metric_unitarity',equal(mm(mm(adjoint(U),G),U),G))
    check('adapter_is_exactly_reversible',equal(mm(U,U),eye(4)))
    check('euclidean_chart_unitarity_is_not_assumed',not equal(mm(adjoint(U),U),eye(4)))
    J=Scalar(0,0,1);incoming=[J,Scalar(1),Scalar(0),Scalar(0)]
    outgoing=vector(U,incoming)
    check('native_mode_and_residual_transferred',all(Scalar.cast(a)==b for a,b in zip(outgoing,[0,delta,J,1])))
    check('native_input_norm',norm(incoming,G)==Q(20,3))
    check('retained_residual_norm',norm(outgoing[:2],diag([edge_norm,alpha]))==defect)
    check('belt_native_output_norm',norm(outgoing[2:],diag([edge_norm,beta]))==Q(4198,675))
    check('whole_input_recovered',all(Scalar.cast(a)==b for a,b in zip(vector(U,outgoing),incoming)))
    dropped=[Scalar(0),Scalar(0)]+outgoing[2:]
    check('dropping_residual_breaks_reversal',any(Scalar.cast(a)!=b for a,b in zip(vector(U,dropped),incoming)))
    # Exact matrix equality above covers arbitrary coherent inputs on BOTH ports.
    probes=[[Scalar(i==j) for i in range(4)] for j in range(4)]
    probes.append([Scalar(1,1,1),Scalar(2,0,-1),Scalar(-1,1,0,1),Scalar(0,1,2)])
    check('independent_port_inputs_and_complex_probe_preserved',all(norm(vector(U,v),G)==norm(v,G) and all(Scalar.cast(a)==b for a,b in zip(vector(U,vector(U,v)),v)) for v in probes))
    check('one_sided_transmission_defect_has_rank_one',alpha>beta>0 and edge_norm==dot_metric(pe,pe,GP))
    # Native belt packet agreement, plus all six rim occurrences over the full
    # explicitly supplied joint schedule of 15 macrosteps.
    native_points=dict(N)
    for face in geometry['belt_faces']:native_points['F_'+'_'.join(sorted(face))]=mean([N[k] for k in face])
    triangle_index={tuple(t):i for i,t in enumerate(record['triangles'])}
    nlabels={k:k for k in N};elabels={k:k for k in E};plabels={k:k for k in P}
    snapshots=[];native_checks=0;covariance_checks=0;previous={}
    for tick in range(16):
        mapping={nlabels['U'+str(i)]:elabels['ABC'[i]] for i in range(3)}
        snapshot={'tick':tick,'upper_vertex_map':mapping,'electron_ordered_face':[elabels[k] for k in 'ABC'],
                  'electron_ordered_cell':[elabels[k] for k in 'ABCD'],'neutron_upper_order':[nlabels['U'+str(i)] for i in range(3)],
                  'lower_vertex_map':{nlabels['L'+str(i)]:plabels['ABC'[i]] for i in range(3)}}
        snapshots.append(snapshot)
        for prefix,points,metric,labels,action in [('L',P,GP,plabels,proton_action),('U',E,GE,elabels,lambda v:apply(ge,v))]:
            for i in range(3):
                na=nlabels[prefix+str(i)];nb=nlabels[prefix+str((i+1)%3)]
                face=next(f for f in geometry['belt_faces'] if {na,nb}<=set(f))
                ta=labels['ABC'[i]];tb=labels['ABC'[(i+1)%3]];target_face=[labels[k] for k in 'ABC']
                nedge,nreal=basis(N,face,na,nb);tedge,treal=basis(points,target_face,ta,tb)
                assert dot_metric(nedge,nreal,GN)==dot_metric(tedge,treal,metric)==0
                assert dot_metric(nedge,nedge,GN)==dot_metric(tedge,tedge,metric)==edge_norm
                assert dot_metric(nreal,nreal,GN)==beta and dot_metric(treal,treal,metric)==alpha
                key=(prefix,i)
                if key in previous:
                    oe,orr,ote,otr=previous[key]
                    nlin=lambda v:tuple(sum(gn[0][j][k]*v[k] for k in range(3)) for j in range(3))
                    tlin=lambda v:subtract(action(v),action(tuple(Q(0) for _ in v)))
                    assert nedge==nlin(oe) and nreal==nlin(orr)
                    assert tedge==tlin(ote) and treal==tlin(otr)
                    covariance_checks+=1
                previous[key]=(nedge,nreal,tedge,treal)
                triangle=('F_'+'_'.join(sorted(face)),na,nb)
                assert triangle in triangle_index
                re,im=mode(triangle,native_points)
                assert re==frame(nreal) and im==frame(nedge)
                index=triangle_index[triangle]
                for axis in range(3):
                    expected=tuple(map(Q,record['collective_vector'][3*index+axis]))
                    assert expected==(*re[axis],*im[axis])
                native_norm=sum(qm(x,x)[0]+3*qm(y,y)[0] for x,y in zip(re,im))
                irrational=sum(qm(x,x)[1]+3*qm(y,y)[1] for x,y in zip(re,im))
                assert native_norm==Q(4198,675) and irrational==0
                native_checks+=1
        nlabels={k:nr[v] for k,v in nlabels.items()};elabels={k:er[v] for k,v in elabels.items()};plabels={k:pr[v] for k,v in plabels.items()}
    check('native_modes_equal_stored_packet_every_step',native_checks==96)
    check('local_frame_parallel_transport_covariant',covariance_checks==90)
    check('five_electron_ports_and_cells_retained',len({tuple(s['electron_ordered_face']) for s in snapshots[:5]})==5 and len({tuple(s['electron_ordered_cell']) for s in snapshots[:5]})==5)
    check('five_steps_restore_electron_but_not_joint_registration',snapshots[5]['electron_ordered_face']==snapshots[0]['electron_ordered_face'] and snapshots[5]['upper_vertex_map']!=snapshots[0]['upper_vertex_map'])
    check('joint_labelled_return_is_fifteen',all(s['upper_vertex_map']!=snapshots[0]['upper_vertex_map'] for s in snapshots[1:15]) and snapshots[15]['upper_vertex_map']==snapshots[0]['upper_vertex_map'])
    check('lower_port_intertwines_selected_proton_action',all(s['lower_vertex_map']==snapshots[0]['lower_vertex_map'] for s in snapshots))
    check('fixed_electron_port_is_not_silently_assumed',set(snapshots[1]['electron_ordered_face'])!=set('ABC'))
    inverse_e={v:k for k,v in er.items()}
    backward=dict(snapshots[-1]['upper_vertex_map'])
    reversed_maps=[]
    for tick in range(15,0,-1):
        backward={k:inverse_e[backward[nr[k]]] for k in backward}
        reversed_maps.append(backward==snapshots[tick-1]['upper_vertex_map'])
    check('every_moving_port_identification_reverses',all(reversed_maps))
    check('electron_face_label_alone_loses_registration',snapshots[5]['electron_ordered_face']==snapshots[0]['electron_ordered_face'] and snapshots[5]['electron_ordered_cell']==snapshots[0]['electron_ordered_cell'] and snapshots[5]['upper_vertex_map']!=snapshots[0]['upper_vertex_map'])
    # The record to replay is the inverse schedule plus the complete output,
    # not only the transmitted belt coefficients.
    serialized=json.loads(json.dumps({'output':[Scalar.cast(v).encoded() for v in outgoing],'schedule':snapshots}))
    replay=[Scalar(*v) for v in serialized['output']]
    check('serialized_full_output_replays_inverse',all(Scalar.cast(a)==b for a,b in zip(vector(U,replay),incoming)))
    referenced=[Path(__file__),BASE/'checkers/assemble_relative_geometry.py',BASE/'checkers/check_neutron_rim_port_transport.py',BASE/'checkers/check_belt_operator_inputs.py']
    result={'verification_passed':all(checks.values()),'checks':checks,
        'adapter_contract':'Preserve ordered edge coefficient; send carrier transverse coefficient to belt transverse coefficient; retain residual and independent second-port input.',
        'source_packet_root':packet['root'],'scalar_basis':['1','sqrt(151)','i*sqrt(3)','i*sqrt(453)'],
        'metric_diagonal':list(map(str,[edge_norm,alpha,edge_norm,beta])),
        'adapter_matrix':[[Scalar.cast(v).encoded() for v in row] for row in U],
        'transverse_transmission_probability_in_orthonormal_charts':str(transmission),
        'transverse_retention_probability_in_orthonormal_charts':str(1-transmission),
        'native_norm_budget':{'input':'20/3','transmitted_belt':'4198/675','retained_carrier':'302/675'},
        'independent_local_port_dimensions':{'input_complex':4,'output_complex':4,'one_sided_transmission_defect_rank':1},
        'six_port_direct_sum_complex_dimension':24,'full_independent_port_inputs_retained':True,
        'proton_macrostep_word':pword,'schedule':snapshots,
        'joint_macrostep_labelled_period':15,'physical_clock_derived':False,
        'electron_scope':'Transport of the geometric triangle character inside a moving tetrahedral boundary cell; not the electron spinor operator.',
        'remaining':['Coupling this local adapter to all native L/G/N and spinor operators','Closing an actual collective interaction subspace','Deriving a dynamics or conserved physical energy for the adapter','Asymptotic channels and normalized scattering probabilities'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in paths+referenced}}
    (BASE/'results/native_rim_phase_adapter.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'checks':checks,'native_norm_budget':result['native_norm_budget'],'joint_macrostep_labelled_period':15},indent=2))


if __name__=='__main__':main()
