"""Exact spectral falsifier for one constant residual-exchange pulse.

Rejects exact simultaneous positive-bright transfer by Hc=[[0,Bsharp],[B,0]].
Does not exclude approximate recurrence, switched controls or spectral shaping.
"""
from fractions import Fraction as F
from pathlib import Path
from math import lcm, gcd
from functools import reduce
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, mm, tr, inverse, blockdiag, eye, rank, enc


def characteristic(A):
    n=len(A)
    powers=eye(n)
    traces=[]
    for _ in range(n):
        powers=mm(powers,A)
        traces.append(sum(powers[i][i] for i in range(n)))
    c=[F(1)]
    for k in range(1,n+1):
        c.append(-sum(c[k-i]*traces[i-1] for i in range(1,k+1))/k)
    return c


def main():
    names={'source':'neutron-seam-control-transport.json',
           'memory':'neutron-comparison-memory.json',
           'local':'local-to-polar-encoder/verification.json',
           'scattering':'neutron-autonomous-rim-scattering.json'}
    raw={k:(BASE/'results'/v).read_bytes() for k,v in names.items()}
    data={k:json.loads(v) for k,v in raw.items()}
    M=rat(data['source']['metric'])
    B=rat(data['memory']['residual_incidence'])
    Gamma=rat(data['memory']['memory_metric'])
    sharp=mm(mm(inverse(M),tr(B)),Gamma)
    S=mm(sharp,B)
    E=rat(data['scattering']['exact_bright_basis'])
    g=mm(mm(tr(E),M),E)
    L=mm(mm(inverse(g),tr(E)),M)
    Sb=mm(mm(L,S),E)
    assert mm(S,E)==mm(E,Sb)
    assert Sb==rat(data['local']['bright_residual_operator'])
    C=rat(data['local']['nonzero_image_basis'])
    Ci=mm(inverse(mm(tr(C),C)),tr(C))
    positive=mm(mm(Ci,Sb),C)
    assert rank(C)==4 and mm(Sb,C)==mm(C,positive)
    assert positive==rat(data['local']['positive_restriction'])
    poly=characteristic(positive)
    rational_eigenvalue=F(4485,3292)
    quotient=[poly[0]]
    for c in poly[1:-1]:
        quotient.append(c+rational_eigenvalue*quotient[-1])
    remainder=poly[-1]+rational_eigenvalue*quotient[-1]
    assert remainder==0 and len(quotient)==4
    denominator=lcm(*(c.denominator for c in quotient))
    integer=[int(c*denominator) for c in quotient]
    divisor=reduce(gcd,integer)
    integer=[c//divisor for c in integer]
    irreducible=None
    for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101):
        if integer[0]%p==0:continue
        residues=[]
        for x in range(p):
            v=0
            for c in integer:v=(v*x+c)%p
            residues.append(v)
        if all(residues):
            irreducible={'prime':p,'polynomial_mod_p':[c%p for c in integer],
                         'values_at_all_residues':residues}
            break
    assert irreducible is not None
    Hc=[[F(0)]*24+row for row in sharp]+[row+[F(0)]*21 for row in B]
    metric=blockdiag(M,Gamma)
    assert mm(tr(Hc),metric)==mm(metric,Hc)
    assert mm(Hc,Hc)==blockdiag(S,mm(B,sharp))
    # Restriction positivity: inherited metric Gram and positive seam form.
    V=mm(E,C)
    gp=mm(mm(tr(V),M),V)
    energy=mm(gp,positive)
    assert energy==tr(energy)
    # Exact positive pivots of the restricted energy form.
    a=[row[:] for row in energy]
    pivots=[]
    for k in range(4):
        q=a[k][k]
        assert q>0
        pivots.append(str(q))
        for i in range(k+1,4):
            for j in range(k+1,4):a[i][j]-=a[i][k]*a[k][j]/q
    hashes={(BASE/'results'/names[k]).relative_to(ROOT).as_posix():hashlib.sha256(v).hexdigest() for k,v in raw.items()}
    own=Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    report={'status':'pass','positive_bright_dimension':4,
        'characteristic_polynomial_descending':list(map(str,poly)),
        'rational_positive_eigenvalue':str(rational_eigenvalue),
        'irreducible_cubic_primitive_integer_coefficients':integer,
        'modular_irreducibility_certificate':irreducible,
        'positive_energy_pivots':pivots,
        'residual_coupling_metric_self_adjoint':True,
        'residual_coupling_square_verified':True,
        'disposition':'No single real pulse area simultaneously empties all positive bright native channels under the unshaped residual coupling, even allowing an output memory phase correction.',
        'argument':'Transfer requires cos(t sqrt(lambda))=0 for each positive eigenvalue. A rational eigenvalue and an irrational cubic eigenvalue would then have ratio equal to a square of a ratio of odd integers, contradiction.',
        'scope':'Exact one-pulse transfer only. No lower bound on approximation over unbounded pulse areas; no exclusion of switched or shaped spectral compilers. Hc is a tested candidate coupling, not newly admitted physical control.',
        'source_hashes':hashes}
    (BASE/'results/encoder-single-residual-pulse.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','rational_eigenvalue':str(rational_eigenvalue),'cubic':integer,'irreducible_mod_prime':irreducible['prime'],'exact_single_pulse_transfer':'impossible'}))


if __name__=='__main__':main()
