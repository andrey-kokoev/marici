"""Test codimension-two zero-column replacements for three collapsed n=7 positroid tables."""
import json,itertools
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
source=json.loads((N/'results/seven-point-positroid-compiler.json').read_text());collapsed=json.loads((N/'results/seven-point-triple-fibre-obstruction.json').read_text())
assert [r['history_index'] for r in collapsed['rows']]==[1,3,5]
Z=s.Matrix([[s.Integer(j)**k for k in range(6)] for j in range(1,8)])
assert all(Z.extract(list(ids),list(range(6))).det()>0 for ids in itertools.combinations(range(7),6))
zero_indices={1:3,3:1,5:5}
def minor(C,i,j):return s.det(C[:,[i,j]])
def normalized_signs(C):
 vals=[minor(C,i,j) for i,j in itertools.combinations(range(7),2)]
 return {'negative':sum(1 for x in vals if x<0),'positive':sum(1 for x in vals if x>0),'zero':sum(1 for x in vals if x==0)}
# A concrete image point in history-zero's separated-pair source chart.
C0=s.Matrix([[1]*7,[0,1,1,2,3,3,4]]);Y0=C0*Z
rows=[]
for history,zero_label in zero_indices.items():
 kept=[j for j in range(7) if j!=zero_label-1];M=Z.extract(kept,list(range(6)));assert M.det()>0
 # Six source columns are a positive top cell; a zero column has source
 # codimension TWO, yet CZ is an invertible linear change on G(2,6).
 C=s.zeros(2,7)
 for rank,j in enumerate(kept):C[:,j]=s.Matrix([1,rank])
 assert normalized_signs(C)=={'negative':0,'positive':15,'zero':6}
 vanished=[int(x.split('(')[1].split(',')[0]) for x in source['cells'][history]['vanishing_cyclic_minors']]
 assert all(minor(C,i-1,i%7)==0 for i in vanished)
 Cback=s.zeros(2,7);inverse=Y0*M.inv()
 for rank,j in enumerate(kept):Cback[:,j]=inverse[:,rank]
 assert Cback*Z==Y0
 signs=normalized_signs(Cback)
 # The inverse is UNIQUE in this zero-column carrier: no hidden fibre.
 assert (Cback-C)*Z!=s.zeros(2,6)
 rows.append({'history_index':history,'zero_column':zero_label,'original_vanishing_cyclic_edges':vanished,
  'source_dimension':8,'surviving_external_determinant':str(M.det()),
  'positive_chart_sample_minors':normalized_signs(C),
  'inverse_of_history_zero_sample_minors':signs,
  'inverse_of_history_zero_sample_is_positive':signs['negative']==0 and signs['positive']==15})
report={'schema':'marici.nima.seven-point-zero-column-repair.v1','rows':rows,
 'construction':'Replace the two adjacent vanishing cyclic minors by their common column identically zero. This is codimension two in G(2,7) and leaves a positive top cell G_+(2,6). For each replacement, the 6x6 retained Z rows have positive determinant, so CZ is a linear Grassmannian isomorphism on that carrier.',
 'scope':'Candidate image-rank repair, NOT a history-to-cell canonical-form match or complete positive triangulation. A fixed history-zero image sample is tested for membership in each replacement image.'}
(N/'results/seven-point-zero-column-repair.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
