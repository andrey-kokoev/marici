"""Autonomous positive two-rim contact with the retained neutron/bank core.

Run: uv run --offline --with numpy --with scipy python <this file>
No physical calibration. Kinetic, contact length, strength and lead thresholds
are explicit fixture inputs. Closed channels and all core directions retained.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import numpy as np
from scipy.linalg import eigh, null_space
from scipy.optimize import brentq
from check_neutron_canonical_occupied_closure import ROOT,mm,transpose,inverse,rank,columns,mv,encoded


def array(a):return np.array(a,dtype=float)
def dagger(a):return a.conj().T


class Contact:
    def __init__(self,K,W,thresholds,kinetic=1.,eta=2.,ell=1.):
        self.K=np.asarray(K,complex);self.W=np.asarray(W,complex)
        self.thresholds=np.array(thresholds,float);self.kinetic=kinetic;self.eta=eta;self.ell=ell
        assert kinetic>0 and eta>=0 and ell>0
        assert np.linalg.norm(dagger(self.W)@self.W-np.eye(2))<1e-11
        assert np.linalg.norm(self.K-dagger(self.K))<1e-11
        self.C=self.K+eta*self.W@dagger(self.W)

    def scatter(self,E,method='full'):
        offsets=E-self.thresholds
        if min(abs(offsets))<1e-10:raise ValueError('Use one-sided threshold limits')
        opened=np.flatnonzero(offsets>0);assert len(opened)>0
        k=np.sqrt((offsets+0j)/self.kinetic);v=2*self.kinetic*k.real
        incoming=np.zeros((2,len(opened)),complex);incoming[opened,np.arange(len(opened))]=1/np.sqrt(v[opened])
        derivative=np.diag(2j*self.kinetic*k);rhs=derivative@incoming
        coupling=self.eta*np.sqrt(self.ell)*self.W
        if method=='full':
            matrix=np.block([[derivative-self.eta*self.ell*np.eye(2),dagger(coupling)],
                             [coupling,E*np.eye(len(self.K))-self.C]])
            forcing=np.vstack((rhs,np.zeros((len(self.K),len(opened)),complex)))
            # At a decoupled dark eigenvalue the continuum solution is unique
            # only after specifying zero incoming bound component. The minimum
            # norm solution implements that convention, with a checked residual.
            if np.linalg.cond(matrix)<1e12:solution=np.linalg.solve(matrix,forcing)
            else:solution=np.linalg.lstsq(matrix,forcing,rcond=1e-13)[0]
            boundary,core=solution[:2],solution[2:]
            full_residual=np.linalg.norm(matrix@solution-forcing)
        elif method=='eliminated':
            link=np.linalg.solve(E*np.eye(len(self.K))-self.C,coupling)
            boundary=np.linalg.solve(derivative-self.eta*self.ell*np.eye(2)-dagger(coupling)@link,rhs)
            core=-link@boundary;full_residual=0.
        else:raise ValueError(method)
        transmit=np.sqrt(v[opened,None])*boundary[opened];reflect=transmit-np.eye(len(opened))
        S=np.block([[reflect,transmit],[transmit,reflect]])
        prob=abs(reflect)**2+abs(transmit)**2
        ledger=[]
        for j,port in enumerate(opened):
            gain=float(prob[:,j]@(self.thresholds[opened]-self.thresholds[port]))
            kout=float(prob[:,j]@(E-self.thresholds[opened]))
            ledger.append({'incident_port':int(port),'reflection':float(np.sum(abs(reflect[:,j])**2)),
                'transmission':float(np.sum(abs(transmit[:,j])**2)),
                'other_port_flux':float(sum(prob[i,j] for i,p in enumerate(opened) if p!=port)),
                'internal_energy_gain':gain,'outgoing_kinetic_energy':kout,
                'energy_balance_residual':abs(kout+gain-(E-self.thresholds[port])),
                'core_residence':float(np.vdot(core[:,j],core[:,j]).real)})
        mismatch=np.sqrt(self.ell)*boundary-dagger(self.W)@core
        jump=derivative@(boundary-incoming)-self.eta*np.sqrt(self.ell)*mismatch
        coreeq=(self.C-E*np.eye(len(self.K)))@core-coupling@boundary
        return {'E':E,'S':S,'boundary':boundary,'core':core,'open':opened,'ledger':ledger,
                'unitarity':float(np.linalg.norm(dagger(S)@S-np.eye(2*len(opened)))),
                'boundary_residual':float(np.linalg.norm(jump)),
                'core_residual':float(np.linalg.norm(coreeq)),'linear_residual':float(full_residual),
                'closed_amplitude':float(np.linalg.norm(boundary[offsets<0]))}

    def accessible_bound_states(self):
        # Call on the invariant bright core only. The separately retained dark
        # eigenstates are not to be mistaken for scattering capture products.
        edge=min(self.thresholds)
        def residual(E):
            q=np.sqrt((self.thresholds-E)/self.kinetic)
            a=np.diag(2*self.kinetic*q+self.eta*self.ell)
            return self.C-self.eta**2*self.ell*self.W@np.linalg.solve(a,dagger(self.W))-E*np.eye(len(self.K))
        lo=-1e-7;hi=edge-1e-9
        assert eigh(residual(lo),eigvals_only=True).min()>0
        count=int(np.sum(eigh(residual(hi),eigvals_only=True)<0));out=[]
        for j in range(count):
            E=brentq(lambda E:eigh(residual(E),eigvals_only=True)[j],lo,hi,xtol=1e-13)
            ev,vec=eigh(residual(E));c=vec[:,np.argmin(abs(ev))]
            q=np.sqrt((self.thresholds-E)/self.kinetic)
            a=np.linalg.solve(np.diag(2*self.kinetic*q+self.eta*self.ell),self.eta*np.sqrt(self.ell)*dagger(self.W)@c)
            norm=np.vdot(c,c).real+np.sum(abs(a)**2/q);a/=np.sqrt(norm);c/=np.sqrt(norm)
            energy=self.kinetic*np.sum(q*abs(a)**2)+np.sum(self.thresholds*abs(a)**2/q)+np.vdot(c,self.K@c).real
            energy+=self.eta*np.linalg.norm(np.sqrt(self.ell)*a-dagger(self.W)@c)**2
            err=abs(energy-E);assert err<1e-10
            out.append({'energy':float(E),'binding_below_lead_threshold':float(edge-E),
                        'core_norm':float(np.vdot(c,c).real),'exterior_norm':float(np.sum(abs(a)**2/q)),
                        'full_normalization_residual':float(abs(np.vdot(c,c).real+np.sum(abs(a)**2/q)-1)),
                        'integrated_energy_residual':float(err)})
        return out


def main():
    paths={k:ROOT/p for k,p in {
        'reuse':'research/strominger/results/high-energy-contact-reuse.json',
        'finite':'research/strominger/results/neutron-two-rim-contact-binding.json'}.items()}
    packets={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for obj in packets.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_source_and_contact_form_receipts']=True
    src=packets['finite'];full=[list(map(F,r)) for r in src['full_joint_H_without_mu']]
    M=[list(map(F,r[2:])) for r in src['source_metric'][2:]];K=[r[2:] for r in full[2:]]
    g=F(src['parameters']['g']);W=[[x/g for x in r[:2]] for r in full[2:]]
    # Exact Krylov construction from the two contact columns.
    basis=[];queue=list(map(list,zip(*W)));cursor=0
    while cursor<len(queue):
        v=queue[cursor];cursor+=1
        if rank(columns(basis+[v]))>len(basis):basis.append(v);queue.append(mv(K,v))
    assert len(basis)==5
    B=columns(basis);metricB=mm(mm(transpose(B),M),B);left=mm(mm(inverse(metricB),transpose(B)),M)
    assert mm(K,B)==mm(B,mm(mm(left,K),B)) and mm(B,mm(left,W))==W
    checks['exact_five_dimensional_bright_closure_and_retained_dark_complement']=True
    L=np.linalg.cholesky(array(M));whiten=L.T
    Kw=whiten@array(K)@np.linalg.inv(whiten)
    assert np.linalg.norm(Kw-Kw.T)<1e-12
    Kw=(Kw+Kw.T)/2 # Remove only verified floating-point antisymmetric roundoff.
    Ww=whiten@array(W)/np.sqrt(3.)
    Q,_=np.linalg.qr(whiten@array(B));dark=null_space(Q.T)
    assert dark.shape==(24,19)
    assert np.linalg.norm(dagger(Q)@Kw@dark)<1e-11 and np.linalg.norm(dagger(dark)@Ww)<1e-11
    Hb=dagger(Q)@Kw@Q;Wb=dagger(Q)@Ww;Hd=dagger(dark)@Kw@dark
    model=Contact(Kw,Ww,[.5,.5]);bright=Contact(Hb,Wb,[.5,.5])
    scans=[];maxima={'unitarity':0.,'boundary':0.,'core':0.,'full_reduced':0.,'full_eliminated':0.,'energy_balance':0.,'dark_population':0.}
    saved_S=[];saved_core=[];saved_boundary=[];energies=np.linspace(.51,4.5,201)
    for E in energies:
        f=model.scatter(float(E));b=bright.scatter(float(E));e=bright.scatter(float(E),'eliminated')
        maxima['unitarity']=max(maxima['unitarity'],f['unitarity'])
        maxima['boundary']=max(maxima['boundary'],f['boundary_residual'])
        maxima['core']=max(maxima['core'],f['core_residual'],f['linear_residual'])
        maxima['full_reduced']=max(maxima['full_reduced'],float(np.linalg.norm(f['S']-b['S'])),float(np.linalg.norm(f['core']-Q@b['core'])))
        maxima['full_eliminated']=max(maxima['full_eliminated'],float(np.linalg.norm(b['S']-e['S'])))
        maxima['energy_balance']=max(maxima['energy_balance'],*(r['energy_balance_residual'] for r in f['ledger']))
        maxima['dark_population']=max(maxima['dark_population'],float(np.linalg.norm(dagger(dark)@f['core'])))
        scans.append({'energy':float(E),'open_ports':len(f['open']),'incident_results':f['ledger']})
        saved_S.append(f['S']);saved_core.append(f['core']);saved_boundary.append(f['boundary'])
    assert max(maxima.values())<1e-8,maxima
    checks['201_energy_full_unit_flux_and_energy_audit']=True
    checks['full_26_unknown_reduced_7_unknown_and_schur_solves_agree']=True
    # An explicitly unequal-threshold control checks virtual closed channels
    # and nontrivial kinetic/internal conversion; not a source threshold claim.
    unequal=Contact(Kw,Ww,[.5,1.5]);closed=unequal.scatter(.8);opened=unequal.scatter(2.0)
    assert len(closed['open'])==1 and closed['closed_amplitude']>1e-8
    assert closed['unitarity']<1e-9 and opened['unitarity']<1e-9
    assert opened['ledger'][0]['internal_energy_gain']>0
    assert max(r['energy_balance_residual'] for r in opened['ledger'])<1e-9
    checks['closed_lead_retained_and_opening_transfers_kinetic_energy']=True
    zero=Contact(Kw,Ww,[.5,.5],eta=0).scatter(.8)
    swap=np.block([[np.zeros((2,2)),np.eye(2)],[np.eye(2),np.zeros((2,2))]])
    assert np.linalg.norm(zero['S']-swap)<1e-11 and np.linalg.norm(zero['core'])<1e-11
    checks['zero_contact_is_perfect_transmission_without_core_excitation']=True
    rng=np.random.default_rng(73019);U,_=np.linalg.qr(rng.normal(size=(24,24))+1j*rng.normal(size=(24,24)))
    phases=np.diag(np.exp(1j*np.array([.31,-.73])))
    transformed=Contact(dagger(U)@Kw@U,dagger(U)@Ww@phases,[.5,.5]).scatter(1.13)
    reference=model.scatter(1.13);pairphase=np.block([[phases,np.zeros((2,2))],[np.zeros((2,2)),phases]])
    frame_residual=float(np.linalg.norm(transformed['S']-dagger(pairphase)@reference['S']@pairphase))
    assert frame_residual<1e-10
    checks['retained_core_and_lead_phase_frame_covariance']=True
    bounds=bright.accessible_bound_states();dark_values=eigh(Hd,eigvals_only=True)
    assert all(row['energy']>0 for row in bounds)
    checks['accessible_bound_levels_include_exterior_norm_and_energy']=True
    controls=[]
    for kinetic in (.5,1.,2.):
        a=Contact(Kw,Ww,[.5,.5],kinetic=kinetic).scatter(1.13)
        controls.append({'kinetic':kinetic,'left_port_conversion':a['ledger'][0]['other_port_flux'],'unitarity':a['unitarity']})
    assert max(x['left_port_conversion'] for x in controls)-min(x['left_port_conversion'] for x in controls)>1e-6
    checks['kinetic_scale_sensitivity_retained']=True
    root=ROOT/'research/strominger/results';npz=root/'neutron-autonomous-rim-scattering.npz'
    np.savez_compressed(npz,energies=energies,S=np.array(saved_S),core=np.array(saved_core),boundary=np.array(saved_boundary),
                        core_operator=Kw,contact=Ww,bright_basis=Q,dark_basis=dark,dark_operator=Hd,core_metric=array(M),whitening=whiten)
    result={'status':'passed','checks':checks,'model':{'space':'L2(R) tensor C2 direct-sum C24','kinetic':1,'eta':2,'ell':1,'lead_thresholds':[.5,.5],
        'energy_unit':'historical native collective/rim model unit; no physical calibration',
        'preparation':'unit-flux incidence in each actual rim port; no incoming dark/bound component',
        'source_core':'H_native/4+sum seam projectors, with all source-bank coordinates retained',
        'sector_scope':'This is the new positive continuum contact, not the previous bare off-diagonal finite contact or a prescribed canonical pulse sequence.'},
        'exact_bright_basis':encoded(B),'bright_dimension':5,'retained_dark_dimension':19,
        'maximum_numerical_residuals':maxima,'frame_covariance_residual':frame_residual,
        'accessible_bound_levels':bounds,'retained_dark_eigenvalues':list(map(float,dark_values)),
        'dark_state_scope':'Decoupled eigenstates retained separately; six zero bank modes remain. Scattering incidence does not populate these states or prove capture into a bound level.',
        'scan':scans,'unequal_threshold_control':{'thresholds':[.5,1.5],'closed_channel_amplitude_at_E_point8':closed['closed_amplitude'],
            'unitarity_at_E_point8':closed['unitarity'],'incident_results_at_E_2':opened['ledger']},
        'kinetic_controls':controls,'npz_sha256':hashlib.sha256(npz.read_bytes()).hexdigest(),
        'limitations':['One-dimensional contact and its coefficients are supplied.','Numerical residuals are not experimental or rigorous interval uncertainties.',
                       'No time-dependent packet or memory-spectrum derivation in this step.','No neutron rest-mass, permanent-capture or physical-clock claim.']}
    inputs=list(paths.values())+[Path(__file__).resolve()]
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=root/'neutron-autonomous-rim-scattering.json';out.write_text(json.dumps(result,indent=2)+'\n')
    examples=[]
    for E in (.8,1.13,2.,3.):
        a=model.scatter(E);examples.append({'energy':E,**a['ledger'][0]})
    print(json.dumps({'status':'passed','checks':len(checks),'maximum_residuals':maxima,'accessible_bound_levels':bounds,
                     'selected_left_incident_results':examples,'kinetic_controls':controls},indent=2))

if __name__=='__main__':main()
