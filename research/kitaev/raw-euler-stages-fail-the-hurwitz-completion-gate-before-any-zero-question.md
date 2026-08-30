# Raw Euler stages fail the Hurwitz completion gate before any zero question

## Question

Can the zero-free finite Euler products be normalized by one cutoff-dependent
scalar so that Hurwitz's theorem applies on a right-half-plane domain entering
the critical strip?

No.  Two positive real sample points already rule this out.

## Finite units

Let

\[
E_N(s)=\prod_{p\leq N}(1-p^{-s})^{-1}.
\]

Every `E_N` is holomorphic and zero-free for `Re s>0`.  For real
`0<sigma<=1`,

\[
\log E_N(\sigma)
=
\sum_{p\leq N}-\log(1-p^{-\sigma})
\geq
\sum_{p\leq N}p^{-\sigma},
\]

and the prime sum diverges.

Choose

\[
0<\sigma_1<\sigma_2\leq1.
\]

Then

\[
\log\frac{E_N(\sigma_1)}{E_N(\sigma_2)}
=
\sum_{p\leq N}
\left[
-\log(1-p^{-\sigma_1})
+\log(1-p^{-\sigma_2})
\right]
\longrightarrow+\infty.
\]

The divergence follows already from the eventually positive difference
`p^(-sigma_1)-p^(-sigma_2)`.

## No scalar normalization

Let `a_N` be any nonzero scalar depending only on the cutoff.  If
`a_N E_N(sigma_2)` remains bounded away from zero, then
`a_N E_N(sigma_1)` diverges.  If the first point is normalized instead, the
second collapses toward zero along the relative ratio.

Therefore no cutoff-only determinant-frame rescaling produces a locally
bounded, nonzero family on a domain containing both points.  In particular,
the raw Euler stages cannot converge compact-open to the completed section in
the critical strip.

This failure occurs before any discussion of Riemann zeros.  It is a topology
and renormalization obstruction.

## Required repair

A viable finite-to-infinite system needs a parameter-dependent holomorphic
unit `R_N(s)` such that

\[
\widetilde E_N(s)=R_N(s)E_N(s)
\]

is locally bounded and source-unique on the target domain.  Because `R_N`
changes relative values at different `s`, it is not an innocuous choice of
one determinant-line frame.  It is a new transition constructor with its own
cocycle, sheet, endpoint, gamma, and cutoff laws.

To retain the Hurwitz conclusion, every `R_N` must itself be zero-free on the
common domain.  The programme must then prove:

1. source authority for `R_N` before scalar completion;
2. exact naturality of `R_{N+1}/R_N` under Euler-stage inclusion;
3. local boundedness of `R_N E_N`;
4. a fixed nonzero normalization port;
5. uniqueness of the compact-open limit;
6. identification of that limit with the completed theta/Tate section.

Gamma and endpoint completion may contribute to such a relative
renormalization, but their fixed global factors do not by themselves cancel
the cutoff-dependent prime divergence.  A cutoff-dependent source cocycle is
required.

## Architectural consequence

There are now three distinct objects:

- zero-free finite Euler units;
- a renormalized compact-open determinant system;
- the analytically continued completed section.

The first does not automatically construct the second, and the second must be
proved equal to the third.  Treating analytic continuation as if it were
compact-open Euler completion silently crosses both missing arrows.

## Falsifiers

- Normalization at one real point below `1` while ignoring divergence at a
  second point.
- A cutoff-only scalar claimed to yield local boundedness on the strip.
- A parameter-dependent counterterm introduced without a source cocycle.
- A counterterm with zeros or poles in the common domain.
- Local convergence in `Re s>1` followed by untyped continuation across
  `Re s=1`.
- Equality with the completed section checked only after taking scalar
  limits.

## Verdict

The raw finite Euler tower cannot be the Hurwitz tower on the critical strip.
The next constructive question is exact:

> Which theta/Tate source operation supplies the parameter-dependent
> zero-free renormalization cocycle that turns finite Euler units into a
> normalized compact-open family before analytic continuation?

Without that cocycle, finite invertibility has no continuous scalar route to
the completed proposition.
