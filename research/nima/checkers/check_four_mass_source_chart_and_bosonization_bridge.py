"""Exact starred psi source chart, orientation, and published bosonization arrow."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=(ROOT/'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex').read_text(encoding='utf8')
start=source.index(r'\psi\,\left[A,1,2,3,4\right]');row=source[start-900:start+120]
assert r'(1\,2)&(3\,4)&(5\,6)&(7\,8)' in row
assert r'\{2,5,4,7,6,9,8,11\}' in row
assert r'\alpha_{2}\pl\alpha_{3}' in row and r'\alpha_{3}\,\alpha_{5}' in row
paper=(ROOT/'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex').read_text(encoding='utf8')
anchor=paper.index(r'\section{The Superamplitude}');extract=paper[anchor:anchor+8500]
assert r'\delta^{4k|4k}(C_{\alpha a}(z) {\cal Z}_a)' in extract
assert r'\Omega^\Gamma' in extract and r'\omega_{n,k}(Y_0;Z_a)' in extract
alpha=s.symbols('alpha1:9',positive=True);p1,p2,p3,p4,p5,p6,p7,p8=alpha
# Source's starred G_+(2,8) chart, transcribed from the published row:
C=s.Matrix([[1,p1,p2+p3,(p2+p3)*p4,p3*p5,p3*p6,0,0],
            [0,0,1,p4,p5,p6,p7,p8]])
gauge=C[:,[0,2]].inv()*C
w2,w4,w5,w6,w7,w8,t,u=(p1,p4,p2*p5,p2*p6,(p2+p3)*p7,(p2+p3)*p8,1/p2,1/(p2+p3))
ours=s.Matrix([[1,w2,0,0,-w5,-w6,-w7,-w8],
               [0,0,1,w4,w5*t,w6*t,w7*u,w8*u]])
assert all(s.cancel(gauge[i,j]-ours[i,j])==0 for i in range(2) for j in range(8))
coords=(w2,w4,w5,w6,w7,w8,t,u)
J=s.factor(s.Matrix(coords).jacobian(alpha).det())
source_coefficient=s.factor(-J/(u*w2*w4*w5*w6*w7*w8*(t-u)))
ratio=s.factor(source_coefficient*s.prod(alpha))
assert ratio in (-1,1)
assert J!=0 and p2>0 and (p2+p3)>0
# Anti-symmetry of one swapped source coordinate reverses the oriented
# exterior product; replacing t by u collapses the genuine angular pole.
assert s.simplify(s.Matrix(coords).jacobian((p2,p1,p3,p4,p5,p6,p7,p8)).det()+J)==0
prior=json.loads((OUT/'nine-point-zero-column-residue.json').read_text());assert prior['passed']
assert prior['oriented_residue_ratio_to_eight_column_top_form']=='1'
packet={'schema':'marici.nima.four-mass-source-chart-bosonization-bridge.v1','passed':True,
 'source_four_mass_permutation':[2,5,4,7,6,9,8,11],
 'published_positive_coordinates_to_intrinsic_cell':dict(zip(('w2','w4','w5','w6','w7','w8','t','u'),map(str,coords))),
 'oriented_intrinsic_residue_to_published_dlog_product':str(ratio),
 'nine_column_zero_column_residue_to_eight_column_top_form':'1',
 'source_superamplitude_map':'arXiv:1312.2007 section The Superamplitude: integrate dlog(alpha_1)..dlog(alpha_8) against delta^{8|8}(C(alpha) super-Z); equivalently evaluate global Omega at Y0 with external Z=(z,phi eta) and integrate d^4phi_1 d^4phi_2',
 'scope':'Source-typed identification of the RELABELLED eight-point starred psi on-shell invariant, up to the recorded orientation ratio. Source theorem supplies the complete superfunction after the two-solution pushforward. It does NOT show this cell occurs as one term in the authored nine-point generalized-R tree sum or prove a nine-point image triangulation.'}
(OUT/'four-mass-source-chart-bosonization-bridge.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'passed':True,'source_form_orientation_ratio':str(ratio),
 'full_superfunction_bridge_from_source':True,'nine_point_history_term_identified':False},indent=2))
