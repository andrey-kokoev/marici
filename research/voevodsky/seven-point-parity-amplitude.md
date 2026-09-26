# Seven-point NNMHV: independent parity comparison started

Target is the complete7-point NNMHV tree superamplitude, not a selected boundary invariant. The source recursion is specialized to its six histories. The comparison route evaluates the ordinary six-term7-point NMHV expression after exchanging lambda and tilde-lambda, then performs componentwise Grassmann Fourier complementation. It does NOT evaluate the same NNMHV formula in a different cyclic frame.

Implementation: checkers/check_seven_point_parity.py, using the existing exact rational region-spinor utilities. Reconstruct tilde-lambda from X_i-X_(i+1)=tilde-lambda_i lambda_i^T epsilon, verify momentum conservation, and build dual momentum twistors from the swapped spinors. Convert each R numerator from chi to eta via chi_i=sum_(j<i)<j i>eta_j; include the two supermomentum rows and the full Parke-Taylor denominator. The universal momentum-conservation delta and common coupling/overall amplitude phase are stripped on both sides.

For a four-element flavor subset I, Grassmann Fourier comparison uses its three-element complement and the Hodge sign (-1)^(sum_(i in I)(i-1)-6). Multiply these signs across all four flavors. Gluon-only fourth powers hide this sign, so mixed-flavor tests are included explicitly.

Fresh result: all35 four-negative-helicity gluon components agree at each of two rational inputs (a moment curve and seeded general integer twistors). An additional64 mixed-flavor subsets per input agree with the Fourier signs. Total70 gluon and128 mixed-component checks, all exact rational. Every input and output coefficient is in results/seven-point-parity.json.

Reproduce: uv run --with sympy python research/voevodsky/checkers/check_seven_point_parity.py.

Remaining: replace sampled mixed components by an exhaustive tensor comparison, preferably exploiting the rank-six sum of fourth tensor powers rather than expanding1,500,625 coordinates naively. Then derive a symbolic or suitably bounded algebraic identity and connect the six histories to explicit positive cells. Current success is a substantive independent parity check, not an all-kinematics proof or full geometric derivation.
