# Xi-torsion lift iteration 8: the frozen prime majorant gives only a finite strip, not the all-order Köthe space used in the torsion proof

## Correction to iteration 7

The prime-loaded Clark completion uses a majorant of the form

\[
\omega_{p,k}\sim p^{-3/2-\sigma}
\]

with the declared grade attenuation. This proves absolute convergence after
any fixed polynomial loss in `log p`. It does **not** prove membership in the
all-exponential-moment Köthe space

\[
q_\delta(c)<\infty
\qquad\text{for every }\delta>0.
\]

For the frozen coefficient packet `c_(p,1)=1`, the outgoing endpoint series has
the model size

\[
\sum_p p^{-3/2-\sigma}e^{R\log q(p)}.
\]

Since `q(p)` is comparable to `p`, this converges only while

\[
R<\frac12+\sigma
\]

(up to the precise loaded exponent). Thus the source supplies a finite
holomorphic strip, not an entire function with arbitrary horizontal/vertical
observer height.

## Consequence for Bohr recovery

The two-line projective inverse from the theta source recovers `q_delta` using
an observation height satisfying

\[
R>\delta+\text{loading margin}.
\]

For an all-order projective family one must take arbitrarily large `R`. The
bordered endpoint series does not provide those lines from its frozen
prime-weight estimate.

Therefore the claim that `H_border` belongs to the same all-order
Fourier-recoverable source range is unproved. Iterations 4--7 establish
algebraic frequency separation and finite-strip coefficient extraction, but
not the stated global Köthe topology.

## Correct finite-strip space

For a fixed convergence width `A`, use

\[
K_{<A}
=
\bigcap_{0<\delta<A}K_\delta,
\]

or the corresponding Silva germ built from smaller strips. On this space:

- multiplication by `L_(p,k)` is continuous with an arbitrarily small loss
  `delta -> delta+epsilon<A`;
- the opposite-chart inversion remains continuous;
- Bohr extraction is available on lines strictly inside the strip;
- the bordered synthesis is strict only for coefficient seminorms whose
  required observer line fits inside that strip.

This is enough for local finite-order differentiation, but not automatically
for the all-order projective recovery asserted previously.

## Effect on the torsion argument

The Weyl--Cauchy proof is local in the Xi-normal coordinate and may work on a
finite disk. It does not require arbitrary prime-exponential order. However,
the quotient must be strict in one topology that simultaneously contains
`H_border` and permits a recovery line with room to shrink the analytic disk.

Hence Xi-torsion-freeness remains plausible on each interior substrip, but the
following must be checked quantitatively:

\[
\text{recovery height}
<
\text{absolute-convergence width}.
\]

No such inequality was established in iteration 7.

## Analytic-continuation warning

The shell formulas admit holomorphic continuation beyond their initial Laplace
charts termwise. That does not imply the prime sum or its Bohr coefficient
observer continues with uniform bounds. Using scalar analytic continuation of
the assembled `H_border` cannot recover the labelled packet continuously.

## Revised status

- Frequency distinctness and four-chart label recovery: proved.
- Strictness on a suitable finite-strip source: conditional on a nonempty
  recovery-width interval.
- Membership of `H_border` in the all-order Fourier-recoverable range: not
  proved and generally incompatible with the displayed frozen majorant.
- Global Xi-torsion-freeness of the completed bordered cokernel: reopened.

## Next executable calculation

Extract the exact frozen prime-power loading `omega_(p,k)` used in the
assembled independent defect and compute its maximal strip width. Compare it
with the minimal observer height needed to recover the desired weighted
coefficient seminorm. This numerical exponent budget decides whether a
nonempty strict analytic graph category exists for `H_border`.