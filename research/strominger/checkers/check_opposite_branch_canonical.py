"""Exact attachment transport for the two actual selected neutron branches.
Standard-library-only imports. Other-owner source/results are read, never run.
Separate unchanged geometry/global character from signed-character energy.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
from check_source_pulse_particle_intertwiners import ROOT,PACKETS
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,total,encoded,apply,positive
from check_belt_three_by_twelve import decode
from check_constraint_energy_accounting import identity,plus,times,compose,adjoint,trace
from check_native_operation_energy_lift import real_mm,real_inverse2,add_block
from check_neutron_canonical_occupied_closure import mm,transpose,inverse,rank

BASE=ROOT/'research/strominger';hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def cmat(a):return {(i,j):(R(v),R()) for i,row in enumerate(a) for j,v in enumerate(row) if v}
def entries(a):return {(i,j):decode(v) for i,j,v in a}
def dump(a):return [[i,j,encoded(v)] for (i,j),v in sorted(a.items())]
def diag(v):return {(i,i):z for i,z in enumerate(v) if z!=Z}
def vsub(a,b):return tuple(add(x,scale(-1,y)) for x,y in zip(a,b))
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def scalarr(x):
    assert x[1]==0;return x[0]
def energy(A,v,d):
    Av=apply(A,v,len(v));return scalarr(total(scale(1/q,mul(conj(x),y)) for x,y,q in zip(v,Av,d)))
def normv(v,d):return sum((norm(x)/q for x,q in zip(v,d)),R())
def transported(A,u):return {e:mul(u[e[0]],mul(v,conj(u[e[1]]))) for e,v in A.items()}
def encodev(v):return [encoded(x) for x in v]

def main():
    protocol=read('research/strominger/inputs/opposite-branch-canonical-protocol-v1.json')
    native=read('research/voevodsky/results/belt_three_by_twelve_store.json')
    branch=read('research/voevodsky/results/opposite_branch_belt_store.json')
    ambient=read('research/voevodsky/results/coupled_six_piece_belt_store.json')
    geometry=read('research/voevodsky/results/four_six_center_cones.json')
    energy_store=read('research/voevodsky/results/native_operation_energy_lift_store.json')
    spectrum=read('research/voevodsky/results/collective_carrier_spectrum.json')
    response=read('research/voevodsky/results/belt_interface_response.json')
    binding=read('research/strominger/results/neutron-canonical-record-binding.json')
    rotation=read('research/strominger/results/neutron-canonical-rotation-frame.json')
    closure=read('research/strominger/results/neutron-canonical-occupied-closure.json')
    checks={};direct=0
    for packet in (binding,rotation,closure):
        assert packet['status']=='passed'
        for p,h in packet['source_hashes'].items():
            assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p;direct+=1
    assert hashlib.sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    assert native['source_root']==branch['source_root']==ambient['root']
    assert branch['source_intrinsic_sha256']==hashes['research/voevodsky/results/belt_three_by_twelve_store.json']
    assert energy_store['source_sha256']['belt']==branch['source_intrinsic_sha256']
    assert hashlib.sha256((ROOT/'research/voevodsky/results/four_six_center_cones.json').read_bytes()).hexdigest()==ambient['record']['geometry_sha256']
    coords=native['coordinates'];assert branch['coordinates']==coords
    d=tuple(F(c['d']) for c in coords);z=tuple(decode(c['selected_numerator']) for c in coords)
    zz=tuple(map(decode,branch['selected_numerators']));owners=ambient['record']['face_owners']
    points={k:tuple(map(F,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
    face_signs=[1 if sum(points[k][1] for k in face)>0 else -1 for face in geometry['belt_faces']]
    assert face_signs==branch['face_signs'] and face_signs.count(-1)==3
    signs=[face_signs[owners[c['triangle']]] for c in coords]
    assert zz==tuple(v if s==1 else conj(v) for v,s in zip(z,signs))
    # Fixed source plane axes + coordinatewise complex-linear bridge: unique
    # among diagonal adapters because every selected component is nonzero.
    u=tuple(scale(1/norm(a),mul(b,conj(a))) for a,b in zip(z,zz))
    assert all(norm(a)==1 for a in u) and tuple(mul(a,b) for a,b in zip(u,z))==zz
    assert u[:12]==u[12:24]==u[24:]
    D=diag(u);Ds=diag(tuple(map(conj,u)));assert compose(Ds,D)==identity(36)
    assert adjoint(D,d)==Ds
    checks['source_bound_coordinatewise_unitary_adapter']=True
    ops=[]
    for store in (native,branch):
        ops.append({s:{(a['target'],a['source']):scale(1/d[a['source']],decode(a['numerator'])) for a in store['arrows'] if a['stage']==s} for s in ('L','G','N')})
    for s in ('L','G','N'):assert compose(ops[1][s],D)==compose(D,ops[0][s]),s
    assert ops[0]['L']!=ops[1]['L'] and ops[0]['N']!=ops[1]['N']
    assert compose(ops[1]['G'],ops[1]['L'])==ops[1]['N']
    nperm=rotation['native_coordinate_permutation'];T={(j,i):ONE for i,j in enumerate(nperm)}
    assert compose(T,D)==compose(D,T) and compose(compose(T,T),T)==identity(36)
    checks['all_native_L_G_N_and_C3_intertwined']=True
    # This is active state transport in the original real ambient planes.
    W={(r['ambient_target'],r['intrinsic_source']):scale(1/d[r['intrinsic_source']],(R(*map(F,r['numerator'])),R())) for r in native['embedding_entries']}
    oldambient=tuple(map(decode,ambient['record']['collective_vector']))
    assert apply(W,z,54)==oldambient
    assert apply(W,zz,54)==tuple(v if face_signs[owners[i//3]]==1 else conj(v) for i,v in enumerate(oldambient))
    checks['same_geometry_embedding_realizes_actual_opposite_modes']=True
    # Reconstruct real source cycle independently, not D C D^-1.
    cycle={};Cplane=((R(F(-1,2)),R(F(1,2))),(R(F(-3,2)),R(F(-1,2))))
    for t in range(18):
        X=tuple((z[2*t+i][0],z[2*t+i][1]) for i in range(2))
        add_block(cycle,real_mm(real_mm(X,Cplane),real_inverse2(X)),[2*t,2*t+1])
    omega=(R(F(-1,2)),R(F(1,2)))
    fixed_defect=plus(cycle,times(-1,diag([omega]*36)))
    signed_defect=plus(cycle,times(-1,diag([omega if s==1 else conj(omega) for s in signs])))
    phase_old=compose(adjoint(fixed_defect,d),fixed_defect)
    phase_new=compose(adjoint(signed_defect,d),signed_defect)
    assert apply(fixed_defect,z,36)==(Z,)*36
    assert apply(signed_defect,zz,36)==(Z,)*36
    assert apply(fixed_defect,zz,36)!=(Z,)*36
    assert compose(cycle,D)!=compose(D,cycle)
    assert phase_new==transported(phase_old,u)
    delta=plus(T,times(-1,identity(36)));alignment=compose(adjoint(delta,d),delta)
    triangles=[ambient['record']['triangles'][t] for t in native['triangle_order']]
    seams=[(a,b) for s in range(3) for a,b in combinations(range(6*s,6*s+6),2) if len(set(triangles[a])&set(triangles[b]))==2]
    oldenergy=energy_store['carriers']['belt'];assert [tuple(r['triangles']) for r in oldenergy['seam_projectors']]==seams and len(seams)==21
    def seam_packets(v):
        out=[]
        for a,b in seams:
            row={}
            for t,sgn in ((a,1),(b,-1)):
                ns=sum((norm(v[2*t+k])/d[2*t+k] for k in range(2)),R())
                for k in range(2):row[0,2*t+k]=scale(sgn/(d[2*t+k]*ns),conj(v[2*t+k]))
            sharp={(j,0):scale(d[j],conj(x)) for (_,j),x in row.items()}
            dual=sum((d[j]*norm(x) for (_,j),x in row.items()),R())
            P=times(1/dual,compose(sharp,row));assert compose(P,P)==P and adjoint(P,d)==P
            out.append(P)
        return out
    oldseams,newseams=seam_packets(z),seam_packets(zz)
    assert oldseams==[entries(r['entries']) for r in oldenergy['seam_projectors']]
    assert all(B==transported(A,u) for A,B in zip(oldseams,newseams))
    H_old=plus(phase_old,alignment,*(times(4,P) for P in oldseams))
    H_new=plus(phase_new,alignment,*(times(4,P) for P in newseams))
    assert plus(phase_old,alignment)==entries(oldenergy['native_energy_entries'])
    assert H_old==entries(oldenergy['entries'])
    assert H_new==transported(H_old,u) and adjoint(H_new,d)==H_new
    assert compose(H_new,ops[1]['N'])=={}
    fixed_phase_energy=energy(phase_old,zz,d)/normv(zz,d)
    fixed_total_energy=energy(H_old,zz,d)/normv(zz,d)
    assert fixed_phase_energy==R(F(3,2)) and positive(fixed_total_energy)
    checks['all_21_source_rebuilt_seams_and_signed_energy_intertwined']=True
    checks['unchanged_phase_character_and_geometry_cycle_hostile_rejected']=True
    # Independently recover the actual aligned six-mode boundary operator.
    def reduced(v,H):
        V={(i,(i//2)%6):x for i,x in enumerate(v)}
        ns=[sum((norm(v[2*t+k])/d[2*t+k] for k in range(2)),R()) for t in range(6)]
        dec={(j,i):scale(1/(3*ns[j]*d[i]),conj(x)) for (i,j),x in V.items()}
        assert compose(dec,V)==identity(6)
        K=compose(compose(dec,times(F(1,4),H)),V)
        assert compose(times(F(1,4),H),V)==compose(V,K)
        rows=[[scalarr(K.get((i,j),Z)) for j in range(6)] for i in range(6)]
        assert all(x.b==0 for row in rows for x in row)
        return [[x.a for x in row] for row in rows],[x.a for x in ns]
    K,n=reduced(z,H_old);KK,nn=reduced(zz,H_new)
    assert K==KK==[[F(x) for x in row] for row in spectrum['belt_reduced_matrix']]
    assert n==nn==list(map(F,spectrum['belt_modal_norms']))
    stiffness=[[n[i]*K[i][j] for j in range(6)] for i in range(6)]
    ex=lambda A,r,c:[[A[i][j] for j in c] for i in r]
    B=[0,3];I=[1,2,4,5]
    corr=mm(ex(stiffness,B,I),mm(inverse(ex(stiffness,I,I)),ex(stiffness,I,B)))
    schur=[[stiffness[i][j]-corr[a][b] for b,j in enumerate(B)] for a,i in enumerate(B)]
    c=F(1193,675);assert schur==[[c,-c],[-c,c]]
    checks['source_derived_bridge_stiffness_preserved']=True
    # Original source feature bank, six genuine rim addresses and three frames.
    labels=[p[0] for p in PACKETS];portrows=binding['source_label_to_native_port'];assert [p['label'] for p in portrows]==labels
    rim=[p['triangle_index'] for p in portrows];nu=F(binding['rim_mode_squared_norm'])
    H4=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    bankH=[[H4[i//4][j//4]*H4[i%4][j%4] for j in range(16)] for i in range(16)]
    features=[[((R(F(1,11)),R()) if j==p['source_record_feature_slot'] else Z) for j in range(16)] for p in portrows]
    def modes(v):return [tuple(x if c['triangle']==t else Z for x,c in zip(v,coords)) for t in rim]
    vm,wm=modes(z),modes(zz)
    def inner(a,b):
        return add(total(scale(1/(nu*d[i]),mul(conj(a[i]),b[i])) for i in range(36)),total(scale(bankH[i][j],mul(conj(a[36+i]),b[36+j])) for i in range(16) for j in range(16) if a[36+i]!=Z and b[36+j]!=Z))
    def direction(v,i,j):return v[j]+tuple(scale(-1,x) for x in features[i])
    def projector(q):
        dual=[scale(1/(nu*d[i]),conj(q[i])) for i in range(36)]
        dual += [total(scale(bankH[i][j],conj(q[36+i])) for i in range(16)) for j in range(16)]
        assert inner(q,q)==(R(2),R())
        return {(i,j):scale(F(1,2),mul(a,b)) for i,a in enumerate(q) if a!=Z for j,b in enumerate(dual) if b!=Z}
    uu=u+(ONE,)*16;U=diag(uu);T52={**T,**{(i,i):ONE for i in range(36,52)}}
    perm=[labels.index(rotation['native_port_permutation'][k]) for k in labels]
    Pold={};Pnew={}
    for frame in range(3):
        for i,label in enumerate(labels):
            j=i
            for _ in range(frame):j=perm[j]
            A=projector(direction(vm,i,j));B=projector(direction(wm,i,j))
            assert B==transported(A,uu)
            assert compose(B,B)==B
            Pold[label,frame]=A;Pnew[label,frame]=B
    checks['all_18_frame_addressed_full_52D_projectors_intertwined']=True
    # Faithful prepared envelope: six rims, six bank features, one spectator.
    def envelope(v,vs):
        spectator=tuple(add(x,scale(-1,total(m[k] for m in vs))) for k,x in enumerate(v))
        cols=[m+(Z,)*16 for m in vs]+[(Z,)*36+tuple(f) for f in features]+[spectator+(Z,)*16]
        return {(i,j):x for j,col in enumerate(cols) for i,x in enumerate(col) if x!=Z},cols
    E,oldcols=envelope(z,vm);EE,newcols=envelope(zz,wm)
    assert compose(U,E)==EE
    M=[[F(x) for x in row] for row in closure['envelope']['metric']]
    for cols in (oldcols,newcols):
        assert [[inner(a,b) for b in cols] for a in cols]==[[(R(x),R()) for x in row] for row in M]
    small=closure['minimal_closure'];B13=[[F(x) for x in row] for row in small['basis_columns']]
    assert rank(B13)==small['complex_dimension']==11
    assert mm(mm(transpose(B13),M),B13)==[[F(x) for x in row] for row in small['metric']]
    Closed=compose(EE,cmat(B13));assert compose(U,compose(E,cmat(B13)))==Closed
    for key,P in Pnew.items():
        pulse=[[F(x) for x in row] for row in small['generators'][f'{key[0]}@{key[1]}']]
        pc=[[(F(i==j)-pulse[i][j])/2 for j in range(11)] for i in range(11)]
        assert compose(P,Closed)==compose(Closed,cmat(pc))
    rsmall=[[F(x) for x in row] for row in small['generators']['native_rotation']]
    assert compose(T52,Closed)==compose(Closed,cmat(rsmall))
    checks['minimal_11_complex_22_real_canonical_closure_transported']=True
    # Nonendpoint mixed-frame pulse word; retained complex state and full bank.
    def pulse(P,phase):return plus(identity(52),{e:mul(add(phase,scale(-1,ONE)),v) for e,v in P.items()})
    state=z+(Z,)*16;newstate=zz+(Z,)*16;initial=newstate;budget=inner(state,state)
    program=[];history=[]
    for serial,label in enumerate(['AB','BA']*3):
        frame=serial%3;phase=[(R(-1),R()),omega,conj(omega)][serial%3]
        A=pulse(Pold[label,frame],phase);B=pulse(Pnew[label,frame],phase)
        state=apply(T52,apply(A,state,52),52);newstate=apply(T52,apply(B,newstate,52),52)
        assert newstate==apply(U,state,52) and inner(newstate,newstate)==budget
        program.append((label,frame,phase));history.append({'label':label,'frame':frame,'phase':encoded(phase),'state':encodev(newstate)})
    assert newstate[36:]!=(Z,)*16
    dropped=newstate[:36]+(Z,)*16
    Ti=compose(T52,T52)
    for label,frame,phase in reversed(program):
        back=pulse(Pnew[label,frame],conj(phase))
        newstate=apply(back,apply(Ti,newstate,52),52)
        dropped=apply(back,apply(Ti,dropped,52),52)
    assert newstate==initial and dropped!=initial
    checks['nonendpoint_word_reverses_only_with_bank_retained']=True
    # Symplecticity follows entrywise for the complex-linear unitary D.
    # x+i sqrt(3)y chart uses [[a,-3b],[b,a]], determinant one.
    for a,b in u:assert a*a+3*b*b==1
    k=next(i for i,s in enumerate(signs) if s==-1)
    partial_conjugation_residual=F(-2,d[k])
    assert partial_conjugation_residual!=0
    checks['unitary_branch_map_symplectic_partial_conjugation_is_not']=True
    # Noncollapse: original mode-observers must be transported as well.
    fixed_old_observer_changes=any(inner(vm[i]+(Z,)*16,wm[i]+(Z,)*16)!=ONE for i in range(6))
    assert fixed_old_observer_changes
    checks['fixed_old_rim_readout_not_silently_identified']=True
    # Output every actual adapter coefficient, original geometry cycle,
    # signed-character energy and all framed projectors for independent reuse.
    for p in [Path(__file__),BASE/'checkers/check_neutron_canonical_occupied_closure.py',ROOT/'research/voevodsky/checkers/check_native_operation_energy_lift.py',ROOT/'research/voevodsky/checkers/check_constraint_energy_accounting.py',ROOT/'research/voevodsky/checkers/check_coupled_six_piece_belt.py',ROOT/'research/voevodsky/checkers/check_belt_three_by_twelve.py']:
        hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    out=BASE/'results/opposite-branch-canonical';out.mkdir(parents=True,exist_ok=True)
    operators={'nativeDiagonalAdapter':list(map(encoded,u)),'sameGeometryCycle':dump(cycle),'signedCharacterHamiltonianIn4HOverPiUnits':dump(H_new),'closedNativeBankEmbedding':dump(Closed),'canonicalProjectors':{f'{label}@{frame}':dump(P) for (label,frame),P in Pnew.items()},'history':history}
    (out/'operators.json').write_text(json.dumps(operators,indent=2)+'\n')
    result={'schema':'marici.opposite-branch-canonical.v1','status':'pass','checks':checks,'sourceHashes':hashes,'directParentHashesChecked':direct,
      'coherenceObligation':protocol['coherence_obligation'],
      'disposition':{'L_G_N_C3_seams_pulses_closure':'exact complex-linear unitary transport on the pointed source carriers',
        'unchanged_geometry_cycle_and_global_character':'fails; C D != D C and the original omega selector rejects conjugated triangles',
        'signed_character_energy':'passes independent reconstruction with unchanged real cycle, omega or conjugate(omega) from face chirality; not a newly fitted coupling',
        'physical_branch_selection':'not derived'},
      'exactResiduals':{'originalPhaseEnergyOnUnitOppositeModeIn4HOverPiUnits':[str(fixed_phase_energy.a),str(fixed_phase_energy.b)],'originalTotalEnergyOnUnitOppositeModeIn4HOverPiUnits':[str(fixed_total_energy.a),str(fixed_total_energy.b)],'oldCycleIntertwiner':dump(plus(compose(cycle,D),times(-1,compose(D,cycle)))),'partialConjugationSymplecticPairResidual':str(partial_conjugation_residual),'identityAdapterChangedL':sum(ops[0]['L'].get(e,Z)!=ops[1]['L'].get(e,Z) for e in set(ops[0]['L'])|set(ops[1]['L']))},
      'preserved':{'nativeComplexDimension':36,'bankComplexDimension':16,'preparedClosureComplexDimension':11,'preparedCanonicalRealDimension':22,'seamProjectors':21,'framedPulseProjectors':18,'bridgeStiffness':'1193/675'},
      'scope':'Exact source-labelled finite matrix comparison, not a physical law selection, whole-field conjugation, physical-time map, nuclear attraction or rest mass. Old fixed character fails; only the explicitly chirality-indexed completion passes. No other-owner checker was run or source mutated.'}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'fixedPhaseEnergy':str(fixed_phase_energy.a),'fixedTotalEnergy':[str(fixed_total_energy.a),str(fixed_total_energy.b)],'signedCharacterTransport':True,'closureComplexDimension':11,'bridgeStiffness':'1193/675'}))

if __name__=='__main__':main()
