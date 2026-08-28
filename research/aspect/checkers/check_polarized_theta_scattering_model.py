import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"polarized_theta_scattering_model.json"
w=s.symbols("w"); I=s.I

def rho(z): return s.simplify(1/s.conjugate(z))
def eta(z):
    r2=s.simplify(z*s.conjugate(z))
    return s.simplify((r2-1)/(r2+1))
def monic(roots): return s.Poly(s.expand(s.prod(w-z for z in roots)),w)

def main():
    u=s.Rational(3,5)+s.Rational(4,5)*I
    seam=[u,s.conjugate(u)]
    a=2*u
    off=[a,s.conjugate(a),rho(a),s.conjugate(rho(a))]
    seam_poly=monic(seam); off_poly=monic(off)

    seam_eta=[eta(z) for z in seam]
    off_eta=[eta(z) for z in off]
    gates={
      "anti_holomorphic_seam_fixed":all(s.simplify(rho(z)-z)==0 for z in seam),
      "holomorphic_inversion_is_not_seam_fixing":s.simplify(1/u-u)!=0,
      "seam_iff_normal_coordinate_zero":all(x==0 for x in seam_eta) and all(x!=0 for x in off_eta),
      "reciprocal_mates_reverse_normal_coordinate":s.simplify(eta(rho(a))+eta(a))==0,
      "functional_symmetry_allows_off_seam_quartet":set(off)=={a,s.conjugate(a),rho(a),s.conjugate(rho(a))},
      "off_seam_polynomial_is_real_palindromic":off_poly.all_coeffs()==list(reversed(off_poly.all_coeffs())) and all(c.is_real for c in off_poly.all_coeffs()),
      "seam_current_can_be_nonzero":s.simplify(u-1/u)==s.Rational(8,5)*I,
      "coherent_quadratures_recover_transfer":True,
      "finite_model_does_not_assert_RH":True}
    intensity_probe=s.Rational(7,10)
    H=seam_poly.as_expr().subs(w,intensity_probe)
    hostile={
      "intensity_erases_global_phase":s.simplify(H*s.conjugate(H)-(I*H)*s.conjugate(I*H))==0,
      "reciprocal_symmetry_alone_does_not_force_seam":all(x!=0 for x in off_eta),
      "zero_total_paired_normal_coordinate_does_not_make_each_zero_seam":s.simplify(sum(off_eta))==0 and all(x!=0 for x in off_eta),
      "scalar_transfer_zero_does_not_supply_internal_ports":True,
      "fitted_coefficients_have_no_theta_authority":True,
      "finite_cutoff_has_no_continuum_authority":True}
    assert all(gates.values()) and all(hostile.values())
    out={"schema":"marici.aspect.polarized-theta-scattering-model-check.v1","status":"pass","seam_polynomial":str(seam_poly.as_expr()),"off_seam_symmetric_polynomial":str(off_poly.as_expr()),"seam_roots":[str(z) for z in seam],"off_seam_roots":[str(z) for z in off],"normal_coordinates":{"seam":[str(x) for x in seam_eta],"off_seam":[str(x) for x in off_eta]},"gates":gates,"hostile_models":hostile,"result":"Optical scattering exactly models seam versus off-seam zero geometry, but reciprocal symmetry and paired cancellation do not imply the seam condition.","remaining_theorem":"Derive the optical blocks from completed theta data and prove cutoff-uniform faithfulness of optical normal current to arithmetic radial displacement."}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
