"""Certify noncancellable independent fermionic components of two positive cube families."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_cube_families_offface_chi1_chi5_independence as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
face=previous.face;wall=face.wall;first=wall.first;cube=wall.cube;Z9=wall.old.Z9
vars=wall.vars;w2,w4,w5,w6,w7,w8,t,u=vars
assert all(M[:,1]==s.zeros(2,1) for M in list(cube.E.values())+list(cube.F.values()))
assert all(face.C[key][:,2]==s.zeros(2,1) for key in ('zero3_E_B','zero3_F_B'))
evalue=s.S.One
p=dict(zip(vars,(evalue,1,1,1,1,1,3,2)))
Y=cube.E['E'].subs(p)*Z9;B=Y[:,:2].inv()*Y[:,2:]
z=Z9[:,2:]-Z9[:,:2]*B;h=Z9[:,:2]
rows=[]
for name in ('E_B','F_B'):
 key='zero3_'+name;C=face.C[key]
 point={v:s.factor(wall.points[name][v].subs(wall.e,evalue)) for v in vars}
 assert all(point[v]>0 for v in vars[:6]) and point[u]>0 and point[t]>point[u]
 J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0
 minor25=s.factor(C[:,[1,4]].det().subs(point));assert minor25!=0
 coeff=s.factor(cube.orient[name]*minor25**4*(C.subs(point)*h).det()**4/
                (s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u])*J))
 rows.append({'cell':name,'chi2_power4_chi5_power4_oriented_coefficient':str(coeff)})
newpair=s.factor(sum(s.Rational(r['chi2_power4_chi5_power4_oriented_coefficient']) for r in rows))
oldcube=s.Rational(first.support.report['complete_eight_cell_positive_supported_chi3_power4_chi5_power4_coefficient'])
assert newpair!=0 and oldcube!=0
report={'schema':'marici.nima.nine-point-two-cube-families-fermionic-support-separation.v1',
 'passed':True,'common_positive_target':'E source (1,1,1,1,1,1,3,2)',
 'zero_phys2_eight_cell_positive_supported_chi3_power4_chi5_power4':str(oldcube),
 'zero_phys2_eight_cell_chi2_power4_chi5_power4_identically_zero':True,
 'zero_phys3_positive_pair_chi2_power4_chi5_power4_terms':rows,
 'zero_phys3_positive_pair_chi2_power4_chi5_power4_nonzero_sum':str(newpair),
 'zero_phys3_eight_cell_chi3_power4_chi5_power4_identically_zero':True,
 'fermionic_component_matrix_diagonal_nonzero':True,
 'consequence':'On a common positive regular target open, full positive-supported zero-physical2 eight-cell form and positive-supported zero-physical3 EB/FB pair occupy mutually distinguishing chi3^4chi5^4 and chi2^4chi5^4 components. Neither contribution is a target-independent scalar multiple of nor cancels the other; no nontrivial constant relative weighting can annihilate BOTH superforms.',
 'scope':'Geometric positive-supported candidate sums at one target, not physically sourced n9 contour, global form or image-coverage result.'}
(OUT/'nine-point-two-cube-families-fermionic-support-separation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'two_independent_nonzero_fermionic_components':True,
 'zero3_chi2_chi5_pair_nonzero':True},indent=2))
