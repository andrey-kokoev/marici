"""Reciprocity obstruction and conditional binding on a declared half-line.
Exact finite matrix dynamics plus exact infinite-domain bound-state equations.
Only owner-local outputs are written; native stores remain read only.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_electron_single_link_potential import ROOT,parse,decode,ginv,mat,neg
from check_electron_tetrahedral_spinor import D,cast,pos,G0,G1,ga,gm,gc,gmm,adj,sm,act,norm,ident,encode
from check_spinor_potential_link_bridge import construct,reconstruct,realmode
from check_projector_fold_sheets import parameters,verify as verify_atlas


def add(A,B):return tuple(tuple(ga(x,y) for x,y in zip(a,b)) for a,b in zip(A,B))
def cm(q,A):return tuple(tuple(gm(q,z) for z in row) for row in A)
def diag(entries):return tuple(tuple((cast(entries[i]),D()) if i==j else G0 for j in range(len(entries))) for i in range(len(entries)))
def outer(v,w):return tuple(tuple(gm(x,gc(y)) for y in w) for x in v)
def powreal(q,n):
    result=D(1)
    for _ in range(n):result=result*q
    return result

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/single-port-binding-dynamics-v1.json';c=json.loads(cp.read_text())
    pp,ep,ap,bp=[ROOT/c[k] for k in ('proton','electron','potential','bridge')]
    ports,ops=parse(json.loads(pp.read_text()));Np=tuple(tuple((D(a),D(0,b)) for a,b in row) for row in ops[2]);assert adj(Np)==Np and gmm(Np,Np)==Np
    pi=ports.index(('AB','x'));h=tuple(row[pi] for row in Np);eta=cast(norm(h));assert eta==Np[pi][pi][0] and pos(eta)
    e=json.loads(ep.read_text());P=tuple(tuple(tuple(decode(z) for z in row) for row in face) for face in e['face_projectors']);E=tuple(row for face in P for row in face);ell=E[0]
    b=tuple(gc(z) for z in ell);d=(neg(ell[1]),ell[0]);delta=cast(norm(b));assert norm(d)==delta and pos(delta)
    assert gmm(adj(E),E)==sm(2,ident(2))
    # On basis (h,Eb,Ed), native Euclidean metric is diag(eta,2delta,2delta).
    # The projected directed map has the lone coefficient (p,bright)=delta.
    M=diag((eta,2*delta,2*delta));S=diag((1,-1,-1));I=ident(3)
    forward=((G0,(delta,D()),G0),(G0,G0,G0),(G0,G0,G0))
    assert gmm(adj(forward),M)!=gmm(M,forward)
    Bplus=((G0,(delta,D()),G0),((eta/2,D()),G0,G0),(G0,G0,G0))
    assert gmm(adj(Bplus),M)==gmm(M,Bplus)
    k=eta*delta/2;assert pos(k)
    bright_support=diag((1,1,0))
    assert gmm(Bplus,Bplus)==sm(k,bright_support)
    assert gmm(gmm(S,Bplus),S)==sm(-1,Bplus)
    # Test arbitrary complex weights at several exact controls, not a fitted
    # coupling strength. Cayley evolution is reversible/unitary in metric M.
    dynamics=[]
    for g in ((D(1),D()),(D(2),D(-1)),(D(0,F(1,3)),D(F(2,3)))):
        H=((G0,gm(g,(delta,D())),G0),(gm(gc(g),(eta/2,D())),G0,G0),(G0,G0,G0))
        k_g=gm(gc(g),g)[0]*k
        assert gmm(adj(H),M)==gmm(M,H)
        H2=gmm(H,H);assert gmm(H2,H)==sm(k_g,H)
        for dt in (F(1,3),F(2),F(-1,3)):
            denominator=cast(1+dt*dt*k_g)
            U=add(add(I,cm((D(),-D(2*dt)/denominator),H)),sm(-D(2*dt*dt)/denominator,H2))
            assert gmm(gmm(adj(U),M),U)==M
            assert gmm(gmm(adj(U),gmm(M,H)),U)==gmm(M,H)
            assert act(U,(G0,G0,G1))==(G0,G0,G1)
            dynamics.append({'g':encode(g),'step':str(dt),'cayley':mat(U)})
    # Quadratic port energy is an operator on the tensor pair internal space,
    # identified with C2 because the selected proton line has dimension1.
    # Normalized encoder J contributes the factor1/2.
    K=sm(eta/2,outer(b,b));Q=sm(D(1)/delta,outer(b,b))
    assert gmm(Q,Q)==Q and adj(Q)==Q and K==sm(k,Q)
    assert act(Q,b)==b and act(Q,d)==(G0,G0)
    assert gmm(diag((-1,-1)),Q)==gmm(Q,diag((-1,-1)))
    qi=(F(0),F(1),F(0),F(0))
    from check_electron_tetrahedral_spinor import spin
    Uspin=spin(qi);assert gmm(gmm(Uspin,Q),adj(Uspin))!=Q
    bridge=json.loads(bp.read_text());assert bridge['passed']
    twirl=tuple(tuple(G0 for _ in range(2)) for _ in range(2))
    for action in bridge['binary_tetrahedral_transport']:
        Uspin=spin(tuple(map(F,action['quaternion'])))
        twirl=add(twirl,gmm(gmm(Uspin,Q),adj(Uspin)))
    twirl=sm(F(1,24),twirl);assert twirl==sm(F(1,2),ident(2))
    # This averaging is a separate interaction permission; it is not implied
    # by the fixed-port arrow. At fixed total u it gives strength u/2 to each
    # spin, so both channels bind iff u>2t, preserving the whole doublet.
    # Exact bound state on n>=1: kinetic t(2I-S-S*) and -u|1><1|Q.
    # In the bright sector, u>t gives q=t/u in(0,1) and
    # energy 2t-u-t^2/u=-t(1-q)^2/q below continuum[0,4t].
    # At u<=t, the form is t sum|psi[n+1]-psi[n]|^2+(t-u)|psi[1]|^2>=0.
    lattice=[]
    for t,u in ((F(1),F(2)),(F(3),F(4)),(F(2),F(7))):
        q=t/u;energy=2*t-u-t*t/u
        assert 0<q<1 and energy==-t*(1-q)**2/q and energy<0
        psi=lambda n:q**(n-1)
        assert (2*t-u)*psi(1)-t*psi(2)==energy*psi(1)
        for n in range(2,33):assert 2*t*psi(n)-t*psi(n-1)-t*psi(n+1)==energy*psi(n)
        partial=sum(psi(n)**2 for n in range(1,33));tail=q**64/(1-q*q)
        assert (1-q*q)*(partial+tail)==1
        # Explicit Rayleigh calculation for this infinite geometric sequence.
        difference_sum=(1-q)**2/(1-q*q)
        norm_sum=1/(1-q*q)
        assert (t*(1+difference_sum)-u)/norm_sum==energy
        lattice.append({'t':str(t),'u':str(u),'kappa':[str((D(u)/k).a),str((D(u)/k).b)],
            'q':str(q),'energy':str(energy),'normalization_squared':str(1-q*q),
            'boundary_equation':True,'bulk_equation':True,'infinite_norm_squared':str(norm_sum)})
    for t,u in ((F(1),F(0)),(F(1),F(1,2)),(F(1),F(1))):
        for psi in ((F(1),),(F(1),F(-2),F(3)),(F(2),F(1),F(0),F(-1))):
            # zero tail, with Dirichlet origin; check form identity independently.
            adjacent=sum(psi[i]*psi[i+1] for i in range(len(psi)-1))
            direct=2*t*sum(x*x for x in psi)-2*t*adjacent-u*psi[0]**2
            diffs=sum((psi[i+1]-psi[i])**2 for i in range(len(psi)-1))+psi[-1]**2
            assert direct==t*diffs+(t-u)*psi[0]**2 and direct>=0
    # q=1 at threshold is not square summable; for u<t the formal q>1
    # solution grows. Negative-energy solutions have0<q<1, and boundary
    # equation forces u=t/q, proving the threshold, not just sample evidence.
    # Transport the retained potential codec. A bound spatial profile changes
    # local norm, not the bright ray or its Gamma. Every other fold stays in
    # the kinematic carrier; a ground state need not occupy every direction.
    packet=json.loads(ap.read_text());verify_atlas(packet);p0,normal,recovery=parameters(packet['source']);p=tuple(tuple((D(a),D(0,bb)) for a,bb in row) for row in p0)
    host=(D(F(1,3)),)*3
    bright_record=construct(b,host,ell,p);dark_record=construct(d,host,ell,p)
    assert bright_record['potential']==(D(0),D(0),D(0),D(1))
    assert dark_record['potential']==(D(F(1,3)),D(F(1,3)),D(F(1,3)),D(0))
    assert bright_record['mode']==dark_record['mode']==(G0,G0,G0)
    for n in range(1,17):
        local=tuple(gm((powreal(D(F(1,2)),n-1),D()),z) for z in b)
        record=construct(local,host,ell,p)
        assert record['potential']==bright_record['potential'] and reconstruct(record,ell,p)==local
    owners=set()
    for w in bridge['interior_witness_for_every_fold']:
        seed=tuple(decode(z) for z in w['seed']);r=construct(seed,host,ell,p)
        from check_spinor_potential_link_bridge import flag
        assert flag(r['potential'])==tuple(w['owner']) and reconstruct(r,ell,p)==seed
        # Isotropic fixture t=1,total u=4: each spin sees attraction2,
        # q=1/2,E=-1/2, so every original fold has a bound spinor witness.
        assert act(twirl,seed)==tuple(gm((D(F(1,2)),D()),z) for z in seed)
        for site in (1,2,5):
            local=tuple(gm((D(F(1,2)**(site-1)),D()),z) for z in seed)
            rr=construct(local,host,ell,p)
            assert rr['potential']==r['potential'] and reconstruct(rr,ell,p)==local
        owners.add(tuple(w['owner']))
    assert len(owners)==24
    result={'schema':'marici.single-port-binding-dynamics.v1','passed':True,
      'classification':'conditional_half_line_pair_binding_with_direct_sum_symmetry_obstruction',
      'native_port_factors':{'eta':[str(eta.a),str(eta.b)],'delta':[str(delta.a),str(delta.b)],'K_bright_eigenvalue':[str(k.a),str(k.b)]},
      'reciprocal_direct_sum':{'metric':mat(M),'weight1_H':mat(Bplus),'cayley_checks':dynamics,
        'self_adjoint':True,'unitary_metric_dynamics':True,'original_forward_only_self_adjoint':False,
        'additional_adjoint_raw_transfer_required':1,'central_symmetry_preserved_by_scalar_g':False,
        'finite_bright_energies':'+-sqrt(|g|^2 eta delta/2)','dark_energy':'0','finite_level_splitting_is_spatial_binding':False},
      'pair_sector':{'source_port_quadratic_K':mat(K),'normalized_bright_projector':mat(Q),
        'central_symmetry_preserved':True,'full_binary_rotation_invariance_at_fixed_port':False,
        'quadratic_energy_rule_derived_from_source_transfer':False},
      'relative_half_line':{'kinetic':'t(2I-S-S*)','potential':'-u |1><1| tensor Q, u=kappa eta delta/2',
        'continuum':'[0,4t] in each free spin channel','binding_iff':'u>t','bright_bound_state':'sqrt(1-q^2) q^(n-1), q=t/u',
        'bound_energy':'2t-u-t^2/u','threshold_state_normalizable':False,'dark_channel_bound_state':False,
        'fixtures':lattice,'radial_coordinate_law_source_derived':False,'calibrated_physical_length_or_energy':False},
      'isotropic_extension':{'averaged_projector':mat(twirl),'averaging_derived_from_fixed_arrow':False,
        'number_of_orientation_terms':24,'binding_iff_at_fixed_total_u':'u>2t','bound_spin_degeneracy':2,
        'fixture':{'t':'1','total_u':'4','per_spin_u':'2','q':'1/2','energy':'-1/2'},'every_fold_has_bound_spinor_witness':True},
      'potential_retention':{'all_fold_interiors':24,'bound_bright_ray':'D','unbound_dark_ray':'ABC face centre','both_zero_potential_mode':True,'local_profile_codec_verified':True},
      'physical_hydrogen_binding_derived':False,'source_stores_modified':False,'scope':c['scope']}
    paths=[cp,pp,ep,ap,bp,Path(__file__),base/'checkers/check_spinor_potential_link_bridge.py',base/'checkers/check_proton_electron_single_link_potential.py',base/'checkers/check_electron_tetrahedral_spinor.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}
    (base/'results/single-port-binding-dynamics-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'reciprocal_scalar_mixing_spin_symmetry':False,'declared_pair_binding_iff':'u>t','exact_bound_fixtures':len(lattice),'potential_folds_retained':24,'physical_binding_derived':False},indent=2))
if __name__=='__main__':main()
