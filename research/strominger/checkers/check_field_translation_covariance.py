"""Exact covariance of geometric field generators under rigid translations."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research/nima/checkers'),str(ROOT/'research/voevodsky/checkers')]
import check_twelve_triangle_positive_geometry as pgeo
from check_belt_operator_inputs import frame,mean
from check_coupled_six_piece_belt import R
BASE=ROOT/'research/strominger/results';NATIVE=ROOT/'research/voevodsky/results'
probe=json.loads((BASE/'window-translation-covariance/verification.json').read_text());patches=json.loads((BASE/'tetrahedral-field-attachment/verification.json').read_text())['gridGeometry'];ng=json.loads((NATIVE/'four_six_center_cones.json').read_text());ambient=json.loads((NATIVE/'coupled_six_piece_belt_store.json').read_text())['record']
pp=dict(pgeo.POINTS)
for rec in patches:
    name=rec['surfaceTriangle'][0];pp[name]=pgeo.mean([pp[k] for k in name[2:]])
np={k:tuple(map(F,v)) for k,v in ng['belt_scaled_coordinates'].items()}
for face in ng['belt_faces']:np['F_'+'_'.join(sorted(face))]=mean([np[k] for k in face])
np={k:tuple(R(*x) for x in frame(v)) for k,v in np.items()};coeff=(pgeo.ONE,pgeo.OMEGA,pgeo.zmul(pgeo.OMEGA,pgeo.OMEGA));countP=countN=0
for shift in probe['translationTest']['shifts']:
    # The sum-zero four-coordinate lattice is embedded using tetrahedral axes.
    t=tuple(sum(F(shift[k],2)*pgeo.POINTS['ABCD'[k]][i] for k in range(4)) for i in range(3));translatedP={k:tuple(v[i]+t[i] for i in range(3)) for k,v in pp.items()}
    for rec in patches:
        triangle=rec['surfaceTriangle'];v=pgeo.zmv(pgeo.transpose(tuple(pp[k] for k in triangle)),coeff);w=pgeo.zmv(pgeo.transpose(tuple(translatedP[k] for k in triangle)),coeff);assert v==w
        assert pgeo.projector(v)==pgeo.projector(w)
        rot=tuple(tuple(F(x) for x in row) for row in rec['rotation'])
        for k in triangle:assert pgeo.mv(rot,tuple(translatedP[k][i]-t[i] for i in range(3)))==pgeo.mv(rot,pp[k])
        countP+=1
    translatedN={k:tuple(v[i]+R(t[i]) for i in range(3)) for k,v in np.items()}
    for f,a,b in ambient['triangles']:
        def mode(points):return (tuple(points[f][i]-(points[a][i]+points[b][i])/2 for i in range(3)),tuple((points[a][i]-points[b][i])/2 for i in range(3)))
        assert mode(np)==mode(translatedN);countN+=1
paths=[Path(__file__).resolve(),BASE/'window-translation-covariance/verification.json',BASE/'tetrahedral-field-attachment/verification.json',BASE/'neutron-belt-field-attachment/verification.json',NATIVE/'four_six_center_cones.json',NATIVE/'coupled_six_piece_belt_store.json']
result={'status':'rigid-translation-field-generators-exactly-invariant','translationDirections':12,'protonPatchChecks':countP,'neutronPatchChecks':countN,'transport':'U_s=I in translated co-moving component charts','reason':'Cyclic coefficients sum to zero; neutron centroid differences and plane axes are translation invariant. Centered rotation frames and sector grouping translate unchanged. Hence the deterministic geometric L/G/metric constructors are unchanged.','scope':'Exact geometric primitive test for rigidly translating the same decorated P tetrahedron or N belt and its reader chart. Does not supply the 36-amplitude transport for native NN moves or compare changing readers, and does not cover E. Not evidence for torus topology or arbitrary position-dependent fields.','sourceHashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(BASE/'window-translation-covariance/field-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='sourceHashes'}))
