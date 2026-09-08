"""Generate the exact 44-entry endpoint comparison from its certificate."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];cert=ROOT/'research/chatgpt/relative_morse_fibre_comparison_certificate.json';data=json.loads(cert.read_text())
entries=data['comparison_entries'];groups={}
for e in entries: groups.setdefault(e['source_index'],[]).append(e)
assert len(entries)==44 and len(groups)==22 and all(len(v)==2 for v in groups.values())
ids=sorted(groups)
def nat(n):
 z='marici-zero'
 for _ in range(n):z=f'(marici-succ {z})'
 return z
def tup(xs):
 o=xs[-1]
 for x in reversed(xs[:-1]):o=f'({x},{o})'
 return o
def ctor(i):return f'nima-relative-source-column-{i}'
def line(s):return 'nima-endpoint-line-plus' if s=='plus' else 'nima-endpoint-line-minus'
L=['# Sparse endpoint-derived Morse-to-fibre comparison','','Generated directly from `relative_morse_fibre_comparison_certificate.json`.','', '```rzk','#lang rzk-1','#data NimaRelativeSparseSourceColumn','  := '+ctor(ids[0])]+['  | '+ctor(i) for i in ids[1:]]
L += ['','#define NimaRelativePolynomialBoundaryBasis : U := Sigma (_ : NimaEndpointLine), Sigma (_ : NimaRelativeFBasis), NimaPolynomialMonomial','#define NimaRelativePolynomialBoundary : U := NimaZSum NimaRelativePolynomialBoundaryBasis','#define nima-relative-sparse-comparison : NimaRelativeSparseSourceColumn -> NimaRelativePolynomialBoundary','  := \\ c -> match c']
for n,i in enumerate(ids):
 es=groups[i];parts=[]
 for e in es:
  poly=e['polynomial'];assert len(poly)==1 and poly[0]['coefficient']==-1
  mono=tup([nat(x) for x in poly[0]['exponents']]);coord=e['target_J_coordinate'];assert coord in (0,2);fs='nima-relative-f-state-5' if coord==0 else 'nima-relative-f-state-7'
  atom=f'(nima-sum-neg NimaRelativePolynomialBoundaryBasis (nima-sum-atom NimaRelativePolynomialBoundaryBasis ({line(e["target_line"])},({fs},{mono}))))';parts.append(atom)
 expr=f'(nima-sum-add NimaRelativePolynomialBoundaryBasis {parts[0]} (nima-sum-add NimaRelativePolynomialBoundaryBasis {parts[1]} (nima-sum-zero NimaRelativePolynomialBoundaryBasis)))'
 L += [('       (' if n==0 else '       | ')+ctor(i)+' => '+expr]
L += ['       )','#define nima-relative-sparse-column-count : MariciNat := '+nat(len(groups)),'#define nima-relative-sparse-entry-count : MariciNat := '+nat(len(entries)),'```','']
out=ROOT/'research/nima/rzk/35-relative-sparse-comparison.rzk.md';out.write_text('\n'.join(L));meta={'output':out.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),'source_columns':len(groups),'entries':len(entries),'source_indices':ids,'requires_rzk_check':True};(ROOT/'research/nima/results/relative-sparse-comparison-generation.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)
