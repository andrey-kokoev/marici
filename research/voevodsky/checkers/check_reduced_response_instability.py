"""Scalar estimates supporting the reduced-response compactness proof."""
from pathlib import Path
import json
import sympy as s
x,g,R,N=s.symbols('x g R N',positive=True)
# Tail controlling the compact archimedean multiplier approximation.
tail=(s.log(N)**2+2*s.log(N)+2)/N
assert s.simplify(s.diff(tail,N)+s.log(N)**2/N**2)==0
# Fixed high-frequency packet n^-1 exp(i n x) chi, real chi.
n,c,cp=s.symbols('n c cp',positive=True)
assert s.expand((cp+s.I*n*c)*(cp-s.I*n*c)/n**2)==c*c+cp*cp/n**2
# Endpoint values on a translated, source-weight-normalized bump.
for a in (s.Rational(1,2),-s.Rational(1,2)):
    assert s.simplify(s.exp(-g*R)*s.exp(a*(x+R))
                     -s.exp(-(g-a)*R)*s.exp(a*x))==0
# Summable prime tail at sigma=gamma+1/2.
sigma=s.symbols('sigma',positive=True)
majorant=N**(1-sigma)*(s.log(N)/(sigma-1)+1/(sigma-1)**2)
assert s.simplify(s.diff(majorant,N)+s.log(N)*N**(-sigma))==0
result={'passed':True,'checks':{'gamma_high_frequency_tail':True,
 'unit_graph_norm_oscillation_scaling':True,'translated_endpoint_scaling':True,
 'prime_operator_tail_majorant':True},
 'scope':'Exact scalar estimates only. Compactness, infinite rank, nonclosed range and weakly null packets are proved analytically in the note. Kernel injectivity is not claimed.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/reduced-response-instability.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
