"""Independent line-normal coordinate coefficient checks, no old-period imports."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();count=0
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  for ratio in map(F,('1/4','1/2','3/4')):
   x=a*ratio
   for E in map(F,('1/16','1/32')):
    ell=a+b-E;g=(a*a+b*b-ell*ell)/2;dgeom=a-g/a
    u=ell*(a-x)/dgeom;t=ell-u
    assert 0<u<ell
    k=1/(2*u)+1/(2*t)
    assert k==ell/(2*u*t)
    # Sphere factor at epsilon0 is2pi; radial Mellin pole is1/(2epsilon).
    # Remove pi and the common smooth F_E factor from the residue.
    direct=(1/(E*k))*(ell/dgeom)
    transported=2*u*t/(E*dgeom)
    assert direct==transported>0
    count+=1
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'fixtures':count,
 'coordinate':'ell-point A+u*e+eta, rho=|eta|; transverse dimension2+2epsilon',
 'q3_quadratic':'ell*rho^2/(2*u*(ell-u))',
 'radial_power':'rho^(-1+2epsilon)',
 'independent_pole':'A_chi(E)=(2pi/E) integral chi(x,w_star)*s_c*t_c*F_E/dgeom dx',
 'agrees_with_transport':True,
 'scope':'Exact coefficient/Jacobian fixtures. Rotational dimensional continuation and local Mellin extraction are written proofs; no physical subtraction or continued cycle certified.'}
(HERE/'triangle-cartesian-pole.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
