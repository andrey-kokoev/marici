# First symbolic parity identity, with full fermionic coverage

Fresh mutable-state continuation produced two improvements.

1. The twelve single-flavor vectors (six NNMHV and six Fourier-transformed NMHV) span only a3-dimensional subspace at both existing rational inputs. Reconstructing every one of their35 components from a common basis reduces the full four-flavor identity to15 symmetric quartic coefficient identities. All embedding and quartic checks pass exactly. This is a verified reduction, not a dimension assumption.

2. Applied the same method over Q(t), with external twistors Z_i=(1,i,i^2,i^3) for i=1,...,6 and Z_7=(1,t,t^2,t^3). All420 entries of the35x12 embedding difference vanish symbolically; the selected basis minor is a nonzero rational function; all15 quartic differences vanish symbolically. Thus the COMPLETE superamplitude parity equality now holds as a rational identity on this one-parameter family, not just at selected t values. Evaluation at t=7 only chooses basis columns; no final equality relies on sampling or interpolation.

Caveat: this family is a restricted moment-curve locus, not generic7-point kinematics. The result holds where the original rational expressions are defined; it does not assign values at singular denominators. A generic six-modulus proof remains open.

Implementation changes to parity_kinematics simplify symbolic matrix residuals before equality tests. The first symbolic run exposed an unevaluated zero in a structural matrix comparison, not an amplitude discrepancy; checking the factored residual fixes that. The prior full rational tensor checker was rerun after the change, refreshing its source hashes and passing both inputs and negative controls.

Fresh commands (uv run --with sympy python research/voevodsky/checkers/...):
* check_seven_point_full_parity_tensor.py
* check_seven_point_parity_reduction.py
* check_seven_point_symbolic_parity_line.py

Results are the correspondingly named JSON files under results (seven-point-full-parity-tensor, seven-point-parity-reduction, seven-point-symbolic-parity-line). The symbolic artifact retains all signed weights and reduced coordinates, enabling the15 identities to be reconstructed independently.

Next: extend the symbolic kinematic chart beyond the moment curve, exploiting the rank3 reduction rather than expanding all Grassmann components. Alternatively derive the common3-dimensional embedding from supermomentum constraints once, then check the15 rational identities on a generic momentum-twistor chart. The full amplitude objective is not yet complete.
