# Finite-part extraction does not preserve positivity or orient the theta detector

Owner: `marici.Kitaev`

## Bounded question

Does positivity of the regulated theta/Fock bulk descend through boundary
subtraction to positivity or nonvanishing of the relative finite part?

## Asymptotic finite-part map

On a finite Laurent asymptotic packet

\[
f(\varepsilon)=\sum_{k=-m}^Na_k\varepsilon^k,
\]

the finite-part map is

\[
\operatorname{FP}(f)=a_0.
\]

It is linear. It is not an order-preserving functional on functions that are
positive for sufficiently small positive \(\varepsilon\).

For any real constant (c\),

\[
f_c(\varepsilon)=\varepsilon^{-2}+c
\]

is positive for all sufficiently small \(\varepsilon>0\), while

\[
\operatorname{FP}(f_c)=c.
\]

The finite part can therefore be positive, zero, or negative while the
regulated bulk stays positive.

## Exact square obstruction

The failure persists for literal positive squares:

\[
f(\varepsilon)
=(\varepsilon^{-1}-\varepsilon)^2
=\varepsilon^{-2}-2+\varepsilon^2\ge0.
\]

Yet

\[
\operatorname{FP}(f)=-2.
\]

Thus finite-part extraction is not a positive functional and cannot be a
state on a positive operator algebra without additional relative structure.

## Multiplicativity also fails

Let

\[
f=\varepsilon^{-1}+a,
\qquad
g=\varepsilon+b.
\]

Then

\[
\operatorname{FP}(f)=a,
\qquad
\operatorname{FP}(g)=b,
\]

but

\[
\operatorname{FP}(fg)=1+ab.
\]

Therefore the finite part is neither multiplicative nor determinant-like by
formal algebra alone.

## Theta consequence

Grothendieck's regulated Euler bulk is source-positive in its convergence
regime, and its boundary subtraction is canonical and regulator-universal.
Neither fact supplies an order on

\[
\operatorname{FP}[Z_{\rho,\varepsilon}(s)-B_{\rho,\varepsilon}(s)].
\]

Positive divergent terms can cancel while leaving an arbitrary constant.
This is not a defect of the Gaussian regulator; it is intrinsic to finite-part
projection.

## What an explanatory nonvanishing theorem needs

At least one additional source-derived structure is required:

1. a relative positive quadratic form whose Schur complement is the finite
   part and is proved coercive;
2. a sectorial orientation (\theta(s)\) and positive reserve
   \[
   \operatorname{Re}\left(e^{-i\theta(s)}
   \operatorname{FP}[Z-B]\right)\ge c(s)>0;
   \]
3. a determinant--kernel theorem identifying a scalar zero with failure of a
   separately positive operator;
4. a monotonicity or comparison theorem for the matched bulk-boundary pair,
   not for the bulk alone.

Any one of these would add information not already contained in reconstruction
of \(\zeta(s)\). Without it, the relative detector is canonical but not an
explanation of off-seam divisor avoidance.

## Hostile fixtures

- positive bulk with zero finite part: \(\varepsilon^{-2}\);
- positive bulk with negative finite part:
  \((\varepsilon^{-1}-\varepsilon)^2\);
- arbitrary finite part under a fixed positive leading divergence:
  \(\varepsilon^{-2}+c\);
- failure of multiplicativity:
  \(\operatorname{FP}[(\varepsilon^{-1}+a)(\varepsilon+b)]=1+ab\);
- regulator universality: preserves the same finite part but does not orient
  it.

## Disposition

The heat finite-part construction is a canonical reconstruction theorem, not
yet an explanatory positivity theorem. Off-seam divisor avoidance/nonvanishing
requires a new relative order, sector, or determinant bridge that survives
boundary subtraction.

## Claim strength

Exact algebraic no-go for positivity and multiplicativity of finite-part
extraction. No assertion is made about a future source-derived relative cone.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_finite_part_order.py`.
The result is written to
`research/kitaev/results/theta-finite-part-order.json`.
