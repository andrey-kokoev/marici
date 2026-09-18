#!/usr/bin/env python3
"""Typed comparison of NNMHV boundary updates with soft/BMS data."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text())
root=load('nima/results/nnmhv-simple-root-interference-control.json')
exchange=load('nima/results/nnmhv-cluster-exchange-weight-gate.json')
seg=load('nima/results/segre-insertion-reflow-orientation.json')
flux=load('nima/results/nnmhv-shell-flux-mechanism.json')
r=Fraction(exchange['with_boundary_update']['R'])
r0=Fraction(exchange['without_boundary_update']['R'])
checks={
 'nnmhv_simple_root_localization_exact':root['checks']['boundary_correction_is_cartan_diagonal'] and root['checks']['alpha2_active_iff_negative_minor'],
 'insertion_reflow_split_exact':flux['checks']['exact_numeric_decomposition'],
 'insertion_is_image_ruling_and_reflow_is_kernel_ruling':seg['checks']['all_images_equal_inserted_spinor'] and seg['checks']['kernel_varies_with_endpoint'],
 'signed_exchange_defect_nonzero':r!=0,
 'boundary_update_changes_exchange_defect':r!=r0,
 'amplitude_to_null_infinity_map_present':False,
 'deformation_coordinate_identified_with_bondi_time':False,
 'nnmhv_defect_has_bms_charge_normalization':False,
 'nnmhv_channels_have_news_shear_or_angular_flux_data':False,
}
out={
 'schema':'marici.strominger.nnmhv-soft-bms-boundary-comparison.v1',
 'status':'passed',
 'classification':'structural analogy only',
 'convention_alignment':{
  'nnmhv_simple_root':'type-A interval boundary b1=b2; discrete history/cluster label',
  'leading_soft_bms':'omega^-1 soft residue; supertranslation Ward charge; zero-frequency shear/displacement memory',
  'subleading_soft_bms':'omega^0 angular-momentum differential operator; superrotation Ward charge; magnetic-parity spin-memory flux',
  'warning':'The three objects inhabit different typed spaces; no map from momentum-twistor/history variables to Bondi (u,z,zbar), news, shear, or BMS smearing data is supplied.'},
 'passed_identities':{
  'nnmhv_flux':'Delta S_n = terminal insertion + retained-history reflow',
  'nnmhv_channel_geometry':'insertion varies the Segre image ruling; reflow varies the kernel ruling',
  'simple_root_control':'alpha_2 boundary correction controls the unique negative composite-root minor'},
 'nonzero_residuals':{
  'exchange_before_boundary_update':str(r0),
  'exchange_after_boundary_update':str(r),
  'boundary_induced_change':str(r-r0)},
 'soft_factor_comparison':{
  'leading':'no equality test is typeable: no soft momentum omega->0, polarization tensor, hard-leg action, or supertranslation smearing function is defined',
  'subleading':'no equality test is typeable: no angular-momentum operator on hard legs, sphere vector field, magnetic projection, or spin-memory contour is defined'},
 'charge_flux_memory_test':'failed to type, not a zero residual: the NNMHV scalar identity is a cutoff-refinement decomposition, while BMS balance requires a cut-to-cut charge difference plus explicitly normalized hard/soft null-infinity flux.',
 'exact_missing_map':['external spinors/momentum twistors -> celestial direction and energy','cutoff n and deformation t -> Bondi cuts/retarded time','boundary replacement -> shear/news zero mode','canonical weight -> normalized BMS charge or memory observable','insertion/reflow signs -> hard/soft flux orientation'],
 'checks':checks,
 'disposition':'The shared boundary/localization/two-channel language is real, but it does not derive a soft theorem, Ward identity, charge-flux law, or memory observable. Do not identify t with physical time.'}
path=ROOT/'strominger/results/nnmhv_soft_bms_boundary_comparison.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
