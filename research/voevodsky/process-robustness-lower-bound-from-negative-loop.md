# Process-robustness lower bound from the negative loop

## Question

Can the scalar convex witness constrain full process-space robustness without reconstructing the underlying process?

## Claim boundary

This packet proves a conditional lower bound for a declared convex process model and bounded affine witness. It does not construct the missing physical associator process or compute its exact process robustness.

## Conditional theorem

Let \(\mathcal C\) be the convex set of positive commutative-factorizable processes, let \(\mathcal N\) be the admitted normalized noise set, and let \(W\) be an affine loop observable satisfying

\[
W(c)\ge0\quad(c\in\mathcal C),
\qquad
W(n)\le M\quad(n\in\mathcal N).
\]

Suppose a process \(x\) has

\[
W(x)=-a<0.
\]

If mixing with weight \(s\) reaches the free set,

\[
\frac{x+sn}{1+s}\in\mathcal C,
\]

then applying \(W\) gives

\[
0\le\frac{-a+sW(n)}{1+s}
\le\frac{-a+sM}{1+s}.
\]

Therefore

\[
s\ge\frac{a}{M}.
\]

For a normalized loop response with \(M=1\) and \(a=1/8\), every compatible process-level robustness is at least \(1/8\).

## Data-processing interpretation

The scalar observable is an affine projection from process space to observable space. A valid resource monotone cannot increase under this projection, so scalar robustness supplies a lower bound on process robustness. Equality need not hold because process space may contain additional nonclassical directions invisible to \(W\).

## Tight and strict fixtures

In a two-coordinate process square with free set \([0,1]^2\) and witness \(W(x_1,x_2)=x_1\):

- \((-1/8,0)\) reaches the free set at \(s=1/8\) by mixing with \((1,0)\), saturating the scalar bound;
- \((-1/8,-1)\) needs at least \(s=1\) to repair the second coordinate, so the scalar bound is strict.

Thus the witness certifies a floor, not the complete process resource.

## Missing physical objects

Applying the theorem to Kitaev's implementation requires:

- a typed process object for the controlled loop constructor;
- the convex positive-commutative process set;
- the admitted normalized noise set;
- proof that the measured Bargmann functional is affine on that process space;
- an exact upper bound \(M\) on the noise set;
- route-identity and shared-control certificates.

Without these, \(1/8\) is a conditional process lower bound, not a demonstrated implementation robustness.

## Pyramid consequence

The partial-representation schema should distinguish:

- `observable_robustness_exact`;
- `process_robustness_lower_bound`;
- `process_robustness_exact`;
- `witness_noise_bound`;
- `process_model_ref`;
- `noise_model_ref`;
- `bound_saturation_status`.

## Disposition

The negative loop can lower-bound full process nonclassicality without being faithful: under a normalized affine process model, process robustness is at least \(1/8\). Exact process robustness remains blocked at the absent physical process and noise objects.

## Verification

- `research/voevodsky/checkers/check_process_robustness_lower_bound.py`
- `research/voevodsky/results/process_robustness_lower_bound.json`
