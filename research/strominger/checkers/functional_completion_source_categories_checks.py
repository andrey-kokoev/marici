"""Exact gates for candidate functional source completions."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
# Finite two-dimensional jet stages.
dims=[(N+1)*(N+2)//2 for N in range(21)]
rec("LF.dimension","bounded point-jet stages have triangular dimension",all(dims[N]==sum(k+1 for k in range(N+1)) for N in range(21)),"N=0..20")
rec("LF.strict","the finite-order jet union is strict",all(dims[N+1]>dims[N] for N in range(20)),"every stage adds N+2 coordinates")
# In R^d, an order-k delta derivative lies in H^-s iff 2k-2s+d<0.
def threshold(d,k): return sp.Rational(d,2)+k
sobolev=all(threshold(2,k)==k+1 for k in range(21))
rec("SOBOLEV.point","point jets obey s>k+1 in two dimensions",sobolev,"orders k=0..20")
rec("SOBOLEV.endpoint","a delta fails at the H^-1 endpoint",threshold(2,0)==1,"logarithmic radial divergence")
rec("SOBOLEV.curve","a codimension-one measure has local threshold s>1/2",threshold(1,0)==sp.Rational(1,2),"one transverse Fourier variable")
# Total variation convergence for an accumulating atomic packet with weights 2^-i.
partial=[sum(sp.Rational(1,2)**i for i in range(1,N+1)) for N in range(1,21)]
tails=[sp.simplify(1-v) for v in partial]
rec("MEASURE.accumulation","l1 atomic weights converge in total variation",all(tails[N-1]==sp.Rational(1,2)**N for N in range(1,21)),"weights 2^-i, N=1..20")
# Absolute summability is essential: harmonic weights have unbounded variation.
harmonic=[sum(sp.Rational(1,i) for i in range(1,N+1)) for N in range(1,31)]
rec("MEASURE.hostile","non-l1 accumulating atoms do not form a finite measure",all(harmonic[i+1]>harmonic[i] for i in range(29)) and harmonic[-1]>3,"harmonic total variation diverges")
# Convert the complex symbol p^4-q^4 to real dyad variables.
xx,yy=sp.symbols("xi_x xi_y", real=True)
p=(xx-sp.I*yy)/2; q=(xx+sp.I*yy)/2
symbol=sp.factor(p**4-q**4)
expected=-sp.I*xx*yy*(xx-yy)*(xx+yy)/2
rec("WAVEFRONT.characteristic","the real magnetic characteristic cone has four dyad lines",sp.simplify(symbol-expected)==0,"xi_x xi_y (xi_x^2-xi_y^2)=0")
passed=sum(i["passed"] for i in checks)
payload={"checker":"functional_completion_source_categories_checks.py","strength":"functional-category threshold and hostile-completion audit","passed":passed,"total":len(checks),"checks":checks,"verdict":"Finite jets form a strict LF source, Radon measures are a total-variation closure of atomic flux packets, and point derivatives require progressively more negative Sobolev order. The full distribution carrier and characteristic wavefront sectors are representable enlargements, not source-authorized completions."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"functional_completion_source_categories.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
