"""Full-fermion identity and a selective w2=0 four-mass source-pole residue."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_Y0_Berezin_component as component
 import check_four_mass_source_chart_and_bosonization_bridge as bridge
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
assert component.berezin_constant==2880
assert all(r['extracted_over_sourced_psi']=='2880' for r in json.loads((OUT/'four-mass-Y0-Berezin-component.json').read_text())['witnesses'])
assert json.loads((OUT/'four-mass-source-chart-bosonization-bridge.json').read_text())['oriented_intrinsic_residue_to_published_dlog_product']=='-1'
# For independent odd variables X_(i,A), i=1,2, A=1..4, the integral
# of det(H)^4 over eight phi's has exterior degree eight in EIGHT X's.
# The top exterior space is one dimensional. The checker-independent
# formal ordered-basis evaluation supplies its universal scalar 2880.
# Thus the identity is for the COMPLETE fermionic delta, not only one
# component or the two rational external configurations.
full_fermionic_delta_identity='top_phi[det(sum_A phi_j^A X_iA)_(i,j=1,2)^4] = 2880 * product_(i=1,2;A=1..4) X_iA (ordered i then A)'
w2,w4,w5,w6,w7,w8,t,u=component.variables
C=component.D
source=-1/(w2*w4*w5*w6*w7*w8*u*(t-u))
residue=s.factor((w2*source).subs(w2,0))
assert residue==-1/(w4*w5*w6*w7*w8*u*(t-u))
# The two complete 8-fermion components of the source pole:
# eta1^4 eta5^4 survives; eta2^4 eta5^4 is killed by C_2=w2*C_1.
minor15=s.det(s.Matrix.hstack(C[:,0],C[:,4]))
minor25=s.det(s.Matrix.hstack(C[:,1],C[:,4]))
assert s.factor(minor15-w5*t)==0 and s.factor(minor25-w2*w5*t)==0
surviving=s.factor(residue*minor15.subs(w2,0)**4)
vanishing=s.factor((w2*source*minor25**4).subs(w2,0))
assert surviving==-w5**3*t**4/(w4*w6*w7*w8*u*(t-u)) and vanishing==0
published=s.factor(-surviving)  # the authored alpha1-first dlog orientation
assert s.factor(published/surviving)==-1
sample={w4:1,w5:1,w6:1,w7:1,w8:1,t:3,u:2}
assert surviving.subs(sample)==s.Rational(-81,2)
report={'schema':'marici.nima.four-mass-full-superfunction-source-residue.v1','passed':True,
 'universal_complete_fermion_identity':full_fermionic_delta_identity,
 'reason':'After eight phi variables are saturated, degree eight in the eight independent odd X_(i,A) lies in a one-dimensional top exterior space. Its coefficient is 2880 by explicit ordered sixteen-generator exterior multiplication. For X=C eta this identifies every fermionic component simultaneously, on the simple-fibre z-open set.',
 'w2_source_pole_residue_chi1^4_chi5^4':str(surviving),
 'w2_source_pole_residue_chi2^4_chi5^4':str(vanishing),
 'surviving_residue_at_positive_test':str(surviving.subs(sample)),
 'authored_alpha1_first_orientation_to_declared_residue':'-1',
 'boundary':'This is a genuine intrinsic source-coordinate dlog pole and a full-fermion normalization theorem. It is NOT an independently located or evaluated momentum-twistor z-pole of the globally traced rational superfunction, nor a global Y-dependent bosonic numerator or nine-point history term.'}
(OUT/'four-mass-full-superfunction-source-residue.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'complete_fermion_normalization':2880,'w2_residue_nonzero':True,
 'mutated_component_residue_zero':True,'external_z_pole_identified':False},indent=2))
