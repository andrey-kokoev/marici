# Spin(5) Finite Threshold Matching Does Not Select the Portal Jump

## Question

Does either anomaly-free completion in WP879 turn WP883's free threshold
coefficient (eta=g_+/g_-) into a source-selected number?

## One-loop matching family

After a completion is chosen, a generic one-loop matching relation for the
allowed Hodge-odd portal operator has the form

\[
\eta_C(\mu)=1+\alpha_C\log\frac{M_C}{\mu}+k_C,
\]

where (C\in\{A,B\}), (alpha_C) is fixed only after the complete
representation and coupling normalization are fixed, (M_C) is a physical
threshold mass, and (k_C) is the finite matching constant in the declared
renormalization prescription.

WP879 distinguishes the two completions through

\[
b_0^A=\frac92,
\qquad b_0^B=\frac{13}{2},
\qquad b_0^B-b_0^A=2.
\]

This fixes neither (M_C) nor (k_C). Anomaly cancellation constrains the
representation sums but contains no equation for the radial breaking scales,
Yukawa masses, subtraction condition, or portal finite part.

## Exact fiber

For every chosen nonzero (M_C), scale (mu), coefficient (alpha_C), and
target (eta_*), the finite term

\[
k_C=\eta_*-1-\alpha_C\log\frac{M_C}{\mu}
\]

reproduces that target. Even if a prescription fixes (k_C=0), a free mass
gives

\[
M_C=\mu\exp\left(\frac{\eta_*-1}{\alpha_C}\right)
\]

when (alpha_C\ne0). Thus selecting a completion or its logarithmic slope
does not select the matching value.

The local constraint

\[
F_C=\eta-1-\alpha_C m-k_C=0,
\qquad m=\log(M_C/\mu),
\]

has gradient ((1,-\alpha_C,-1)) on ((\eta,m,k_C)). It is one transverse
source equation in three variables and leaves a two-dimensional solution
fiber. Appending detector rows can identify a realized (eta), but cannot
make the source equation select it.

## Aspect transverse-balance gate

Aspect's source-balance lesson distinguishes a genuine source repair from an
added observer. The required repair here would be a source-derived relation
transverse to the surviving (eta) kernel together with independent source
equations fixing (m) and (k_C). Neither completion currently supplies
those equations.

Setting (M_C=\mu) and (k_C=0) yields (eta=1), but this is a coordinated
choice of matching scale and finite prescription. It is not a source theorem.
Likewise, measuring (eta) precisely supplies a readout, not a constructor.

## Scheme boundary

The finite constant by itself is not physical. A scheme change shifts
(k_C) while compensating Wilson coefficients or parameter definitions so
complete amplitudes remain invariant. Selector authority can therefore be
claimed only for a scheme-independent physical prediction after all matched
coefficients and observables are included, not for the isolated coordinate
(eta_C(\mu)).

## Smallest exact falsifiers

1. Same completion and mass, different finite terms (k_C=0,1), give
   different (eta).
2. Same completion and (k_C=0), different allowed masses give different
   (eta).
3. The conventional point (M_C=\mu,k_C=0) returns (eta=1) without any
   source selection.
4. Adding an arbitrarily faithful detector for (eta) leaves the source
   solution fiber unchanged.

## Verdict

WP879's completion choice changes the beta and threshold coefficients but
does not select the portal jump. The finite threshold branch closes negative
at current source support. Progress requires a mass-generating action and a
scheme-independent matching observable derived from the same completion.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp884_spin5_finite_threshold_selector_obstruction.py
~~~
