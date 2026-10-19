# Six-active Gaussian-jet successor: kernel repair versus arithmetic form

Targets: `rh:successor-form-candidate` (constructed kernel-safe tuple) and `rh:weil-form-comparison` (rejected for this tuple).
Tuple: `research/conjecture_net/contracts/rh-gaussian-jet-successor-candidate.v1.json`.
Checker: `research/voevodsky/checkers/check_gaussian_jet_successor.py`.
Receipt: `research/voevodsky/results/gaussian-jet-successor-v1.json`.
Run: `uv run research/voevodsky/checkers/check_gaussian_jet_successor.py`.

## Candidate fixed independently of arithmetic values

Keep the original twelve-arrow source and its Hamiltonian, and reuse the existing ordered six-coordinate energy observer P6, section E6 and stationary archive N6. Prepare the six active coefficients as the ordered monomial Gaussian jet basis

    R(x)(u) = sum_{j=0}^5 (P6 x)_j u^j f0(u),
    f0(u) = (2*pi/10)^(-1/2) exp(-5u^2).

This is an explicit supplied test-preparation convention. It is not derived from the source's native rules and is not claimed to preserve the additive Fourier action. No orthonormalization, coordinate rescaling or coefficient fit to the Weil form is performed. The purpose is to test whether faithful active information plus a natural fixed Gaussian test frame suffices to identify the unchanged form.

The domain is the full real source, with its zero-energy archive retained. The analytic image is the six-dimensional span of these tests, endowed with its transported finite-coordinate topology. Polynomial Gaussians belong to the already admitted rapidly decreasing analytic test space. There is no new infinite completion, density or global positivity claim.

## Kernel gate passes

Because f0 is nowhere zero, independence of the six functions reduces to independence of monomials. Evaluating at six distinct real points gives the exact Vandermonde determinant checked by the script. Hence ker R=ker P6.

The existing source-derived factorization K12=P6^T K6 P6 and K12 N6=0 establishes ker R contained in the radical of the source energy form. The old hidden-energy witness h and the visible Riemann-collapse witness v now both have nonzero analytic images; their unchanged energies remain 980 and 20. Neither previous rejection is withdrawn: their maps were different.

This successor therefore passes a genuinely stronger necessary condition than the original four-port attachment. It is not the old direct skew-Fourier extension, whose energy vanished on every even test.

## One admitted test still rejects the form identity

Choose x0=E6 e0. Then R(x0)=f0 exactly. The checker computes its rational source energy from the unchanged K12 and compares it with the pre-existing certified positive half-Weil interval near 2.104799795822351e-9. The receipt stores the full exact source vector, active reader/Hessian and a strictly positive rational lower bound for the difference.

No new quadrature is needed: the earlier certified arithmetic interval and source hashes are revalidated. This is a comparison on a nonzero admitted test in this candidate's actual image, not an unjustified extension from a comb image to all Schwartz functions.

The rejection means that passing the radical condition and preserving all active energy directions is not sufficient for Weil equality. Changing scale after observing the mismatch, or replacing K6 with the Weil Gram matrix by definition, would be a new candidate requiring independent source justification. The present test does not exclude other preparations or source operators.

## Disposition boundary

The candidate-specification acceptance is met: its tuple is fixed and its radical gate passes. Register that node as constructed, not rejected. The subsequent Weil-form-comparison node is rejected: H(E6 e0)=5 is strictly above the certified half-Weil interval. The evidence supports rejection of this explicitly frozen Gaussian-jet candidate for the proposed Weil-form identity. The kernel/descent part is constructed and useful; the arithmetic identification fails. Retain both older counterexamples, the even-Gaussian mismatch and this new information-preserving preparation test. No RH truth or physical result follows.

The live gates are intentionally different: source information preservation does not imply arithmetic equality. The negative form verdict blocks the required constructed-form port of `rh-cross-realization-assembly`. All formal outcomes remain null. A future map/form/domain repair requires a versioned successor retaining this counterexample; it cannot overwrite this tested tuple or supply a positive assembly witness merely by changing scale.

Next: advance the independently open common-source map/continuation tasks, or propose a new independently justified form/preparation with fresh lineage. Do not rerun the unchanged Gaussian-jet equality as if unresolved.
