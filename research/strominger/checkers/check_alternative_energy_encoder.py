"""Fixed-energy encoder freedom versus a C3-fixed rational metric obstruction."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_witnessed_interface_compiler import ROOT,BASE,eye,tr,mm,minus,scale,blockdiag,rat,enc,rank,inverse
from check_local_to_polar_encoder import determinant,square
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def charpoly(a):
    n=len(a);powers=[];power=eye(n)
    for k in range(1,n+1):power=mm(power,a);powers.append(sum(power[i][i] for i in range(n)))
    c=[F(1)]
    for k in range(1,n+1):c.append(-sum(c[k-j]*powers[j-1] for j in range(1,k+1))/k)
    return c

def polynomial(c,a):
    n=len(a);out=[[F(0)]*n for _ in range(n)]
    for x in c:
        out=mm(out,a)
        for i in range(n):out[i][i]+=x
    return out

def main():
    read('research/strominger/inputs/alternative-energy-encoder-protocol-v1.json')
    src=read('research/strominger/results/neutron-seam-control-transport.json')
    mem=read('research/strominger/results/neutron-comparison-memory.json')
    scatter=read('research/strominger/results/neutron-autonomous-rim-scattering.json')
    prior=read('research/strominger/results/local-to-polar-encoder/verification.json');assert prior['status']=='pass'
    M=rat(src['metric']);Gamma=rat(mem['memory_metric']);B=rat(mem['residual_incidence'])
    A0=scale(F(1,4),rat(src['native_energy']));Hm=rat(mem['rational_memory_operator'])
    E=rat(scatter['exact_bright_basis']);C=rat(prior['nonzero_image_basis']);V=mm(E,C)
    Splus=rat(prior['positive_restriction']);p=charpoly(Splus)
    assert polynomial(p,Splus)==[[F(0)]*4 for _ in range(4)] and p[-1]!=0
    S=mm(mm(mm(inverse(M),tr(B)),Gamma),B)
    assert mm(S,V)==mm(V,Splus) and mm(A0,V)==[[F(0)]*4 for _ in range(24)]
    Rot=rat(src['native_rotation']);assert mm(Rot,E)==E
    # Construct the memory action from the actual residual occurrences:
    # B R = R_memory B, including orientation signs.
    BR=mm(B,Rot);Rmem=[[F(0)]*21 for _ in range(21)]
    for i,row in enumerate(BR):
        matches=[(j,s) for j,b in enumerate(B) for s in (-1,1) if row==[s*x for x in b]]
        assert len(matches)==1;j,s=matches[0];Rmem[i][j]=F(s)
    assert mm(mm(Rmem,Rmem),Rmem)==eye(21)
    assert mm(mm(tr(Rmem),Gamma),Rmem)==Gamma and mm(Rmem,Hm)==mm(Hm,Rmem)
    # Every three-sector orbit supplies one memory coordinate at fixed C3.
    keys=sorted({tuple(x%6 for x in s['ordered_triangle_positions']) for s in src['seam_controls']})
    assert len(keys)==7
    Fmem=[[F(tuple(x%6 for x in s['ordered_triangle_positions'])==key) for key in keys] for s in src['seam_controls']]
    assert rank(Fmem)==7 and mm(Rmem,Fmem)==Fmem and 21-rank(minus(Rmem,eye(21)))==7
    L=mm(inverse(mm(tr(Fmem),Fmem)),tr(Fmem));H7=mm(mm(L,Hm),Fmem)
    assert mm(Hm,Fmem)==mm(Fmem,H7)
    # Spectral target is selected by p(H), independent of any polar factor.
    native_kernel=24-rank(polynomial(p,A0))
    target_all=21-rank(polynomial(p,Hm));target_fixed=7-rank(polynomial(p,H7))
    Ftarget=mm(B,V)
    assert rank(Ftarget)==4 and mm(Rmem,Ftarget)==Ftarget
    assert mm(Hm,Ftarget)==mm(Ftarget,Splus)
    assert native_kernel==0
    assert target_all==12 and target_fixed==4
    # Consequently every C3-preserving energy embedding of V has its image
    # in this SAME four-dimensional memory space, even if it is not polar.
    gs=mm(mm(tr(V),M),V);gt=mm(mm(tr(Ftarget),Gamma),Ftarget)
    assert gt==mm(gs,Splus)
    ratio=determinant(gs)/determinant(gt)
    assert ratio==1/determinant(Splus) and not square(ratio)
    # Nonpolar encodings do exist analytically. A memory sign change is
    # a nontrivial postcomposition commuting with fixed energy AND C3.
    # It does not require changing either Hamiltonian.
    D=blockdiag(eye(24),scale(-1,eye(21)))
    Metric=blockdiag(M,Gamma);Hafter=blockdiag(A0,Hm);Rall=blockdiag(Rot,Rmem)
    assert mm(D,D)==eye(45) and mm(mm(tr(D),Metric),D)==Metric
    assert mm(D,Hafter)==mm(Hafter,D) and mm(D,Rall)==mm(Rall,D)
    # Since B V has rank4, the polar image is nonzero in memory there;
    # D J differs from J on that sector. Its inverse/readers must include D.
    # These algebraic postcomposition identities do not numerically build J.
    checks={'bright_spectral_polynomial_derived_without_encoder_choice':True,
      'native_post_storage_block_cannot_carry_positive_bright_spectrum':True,
      'full_memory_has12_matching_dimensions':True,'C3_fixed_memory_has_exactly4_matching_dimensions':True,
      'forced_image_metric_discriminant_excludes_all_rational_C3_isometries':True,
      'nonpolar_postcomposition_commutes_with_fixed_energy_metric_and_C3':True}
    for path in [Path(__file__),BASE/'checkers/check_local_to_polar_encoder.py',BASE/'checkers/check_witnessed_interface_compiler.py']:
        hashes[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    out=BASE/'results/alternative-energy-encoder';out.mkdir(parents=True,exist_ok=True)
    report={'status':'pass','checks':checks,'source_hashes':hashes,'positive_bright_polynomial':list(map(str,p)),
      'target_dimensions':{'native_positive_match':native_kernel,'all_memory_positive_match':target_all,'C3_fixed_memory_positive_match':target_fixed},
      'source_positive_basis':enc(V),'forced_memory_image_basis':enc(Ftarget),'source_metric':enc(gs),'target_metric':enc(gt),
      'required_rational_change_of_basis_determinant_square':str(ratio),'ratio_is_rational_square':square(ratio),
      'memory_C3_action':enc(Rmem),'nonpolar_postcomposition':'diag(I24,-I21)',
      'conclusion':'No rational metric-isometric encoder preserving fixed energy and native C3 exists on the positive bright sector, regardless of equality to the polar map. Analytic nonpolar encoders exist by memory sign postcomposition. Without C3 preservation the target has12 matching dimensions and this determinant obstruction is inconclusive.',
      'scope':'Exact rational spectral/metric argument, not a search over physical controls. The analytic nonpolar family relies on the previously established polar existence; its fixed reader must be co-transported. No new Hamiltonian, approximation or source-selected symmetry-breaking rule was constructed.'}
    (out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'dimensions':report['target_dimensions'],'determinant_square_required':str(ratio),'rational_C3_encoder':'excluded','without_C3':'unresolved'}))
if __name__=='__main__':main()
