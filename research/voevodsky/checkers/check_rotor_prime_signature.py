# /// script
# dependencies = ["sympy"]
# ///
"""Exact rotor expansion and certified arithmetic control on an even Gaussian.
Zero exit verifies the stated mismatch, not an arithmetic energy derivation.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
ST=ROOT/'research/strominger';sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct


def main():
    arpath=BASE/'results/rh-source-kernel-generation-v1.json'
    arithmetic=json.loads(arpath.read_text());assert arithmetic['passed']
    for p,h in arithmetic['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    sp=ST/'results/source-arrow-hamiltonian-descent.json';src=json.loads(sp.read_text())
    for p,h in src['input_sha256'].items():assert hashlib.sha256((ROOT/'research'/p).read_bytes()).hexdigest()==h,p
    source,C,edges=construct(tuple('ABCD'),src['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    odd=(S.eye(12)-C**2)/2
    assert odd**2==odd and odd.T==odd and odd.rank()==6
    assert source.D.T*source.G*source.D==40*odd
    assert source.K==20*odd # H = x^T K x/2 = 10||odd x||^2
    assert source.D*(S.eye(12)-odd)==S.zeros(12)
    assert (S.eye(12)-odd).rank()==6
    # Formal order-four Fourier realization has the identical polynomial law.
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    D=F-F.T;O=(S.eye(4)-F**2)/2
    assert D.T*D==4*O
    even=S.Matrix([1,2,1,2]);assert D*even==S.zeros(4,1)
    # f0 is even by its explicit formula. Read certified FULL arithmetic bounds,
    # not a midpoint, a truncated zero list, or positive-square reconstruction.
    lo,hi=map(Q,arithmetic['generated_matrix'][0][0]['rational_bounds'])
    assert Q('2.104799795822350e-9')<lo<=hi<Q('2.104799795822353e-9')
    terms=arithmetic['generated_term_records'][0];assert terms['indices']==[0,0]
    term_bounds={k:tuple(map(Q,terms[k]['rational_bounds'])) for k in ('endpoint','gamma','prime')}
    assert term_bounds['endpoint'][0]>0 and term_bounds['gamma'][1]<0 and term_bounds['prime'][1]<0
    sumlo=sum(v[0] for v in term_bounds.values());sumhi=sum(v[1] for v in term_bounds.values())
    assert sumlo>0 and max(sumlo,lo)<=min(sumhi,hi)
    first=terms['primitive_prime_translations'][0]
    assert first['n']==first['base_prime']==2
    assert Q(first['signed_contribution']['rational_bounds'][1])<0
    result={'schema':'marici.rotor-prime-signature.v1','passed':True,
      'claim_effect':'direct Fourier-energy identification falsified',
      'exact_source_energy':'H(x)=10||((I-C^2)/2)x||_2^2',
      'source_active_rank':6,'source_zero_energy_rank':6,
      'all_test_candidate':'Same skew-Fourier generator on scalar tests in the Weil logarithmic variable; an explicit proposed extension, not an already derived domain map',
      'analytic_energy':'H_F(f)=10||f_odd||_2^2',
      'test':'f0(x)=(2*pi/10)^(-1/2)*exp(-5*x^2)',
      'candidate_rotor_energy':0,
      'certified_Weil_interval':[str(lo),str(hi)],
      'certified_Weil_decimal_summary':arithmetic['generated_matrix'][0][0]['ball'],
      'arithmetic_terms':{k:terms[k]['ball'] for k in ('endpoint','gamma','prime')},
      'nonzero_negative_prime2_contribution':first['signed_contribution']['ball'],
      'prime_terms_generated_by_source_energy_expansion':False,
      'arbitrary_alternative_test_maps_ruled_out':False,
      'quadrature_rerun':False,'certified_receipt_source_hashes_revalidated':True}
    files=[Path(__file__),arpath,sp,ST/'checkers/source_arrow_hamiltonian.py',BASE/'rotor-prime-signature-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (BASE/'results/rotor-prime-signature-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
