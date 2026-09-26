"""Read-only reuse of WP970's exact source-law nonuniqueness witness."""
import ast,hashlib,json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
source=ROOT/'research/flavor/checkers/wp970_preparation_grammar_source_closure.py'
paths=[Path(__file__),HERE/'source-generation-repeated-preparation-audit.md',source,ROOT/'research/flavor/flavor-preparation-grammar-source-closure.md',ROOT/'research/nima/carrier-generated-sector-interface-falsifier.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();laws={}
for node in ast.parse(source.read_text(encoding='utf-8')).body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ('fresh','shared'):
  laws[node.targets[0].id]=eval(compile(ast.Expression(node.value),str(source),'eval'),{'__builtins__':{},'F':F})
def marginal(law,i,v):return sum(p for xs,p in law if xs[i]==v)
def variance(law):
 mean=sum(F(sum(xs),2)*p for xs,p in law)
 return sum((F(sum(xs),2)-mean)**2*p for xs,p in law)
assert set(laws)=={'fresh','shared'}
for law in laws.values():
 assert sum(p for _,p in law)==1
 assert all(marginal(law,i,v)==F(1,2) for i in (0,1) for v in (-1,1))
assert variance(laws['fresh'])==F(1,2)
assert variance(laws['shared'])==1
for rho in map(F,(-1,F(-1,2),0,F(1,2),1)):
 law=[((a,b),(1+rho*a*b)/4) for a in (-1,1) for b in (-1,1)]
 assert all(p>=0 for _,p in law) and sum(p for _,p in law)==1
 assert variance(law)==(1+rho)/2
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'fresh_mean_variance':'1/2','shared_mean_variance':'1','marginals_identical':True,'first_failed_inference':'one-use kernel determines authorized repeated joint preparation','full_generation_conjecture_refuted':False,'physical_realizations_certified':False,'owner_census_independently_reproved':False}
(HERE/'source-generation-repeated-preparation-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
