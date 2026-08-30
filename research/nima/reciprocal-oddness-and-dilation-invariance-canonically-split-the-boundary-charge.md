# Reciprocal oddness and dilation invariance canonically split the boundary charge

## Theorem

Let \(J\) be a bounded measurable boundary potential on \(\mathbb R\setminus\{0\}\) satisfying:

1. reciprocal oddness,
   \[
   J(-q)=-J(q);
   \]
2. dilation invariance,
   \[
   J(aq)=J(q)
   \qquad(a>0);
   \]
3. boundary charge
   \[
   J(+\infty)-J(-\infty)=\chi.
   \]

Then, almost everywhere away from the origin,
\[
J(q)=\frac{\chi}{2}\operatorname{sgn}(q).
\]

## Proof

Dilation invariance acts transitively on each open ray. Hence \(J\) is constant almost everywhere on \((0,\infty)\), say \(J=c_+\), and on \((-\infty,0)\), say \(J=c_-\).

Reciprocal oddness gives
\[
c_-=-c_+.
\]
The boundary charge gives
\[
c_+-c_-=2c_+=\chi.
\]
Therefore
\[
c_+=\frac{\chi}{2},
\qquad
c_-=-\frac{\chi}{2}.
\]

The value at the origin is a separate point convention and does not affect the distributional boundary class.

## Canonical section

The boundary-charge exact sequence
\[
0
\longrightarrow
\ker\partial_\infty
\longrightarrow
\mathcal J_{\mathrm{odd}}
\xrightarrow{\partial_\infty}
\mathbb C_{\mathrm{odd}}
\longrightarrow
0
\]
therefore has a canonical source-character section
\[
\sigma(\chi)
=
\frac{\chi}{2}\operatorname{sgn}.
\]

It is selected jointly by reciprocal character and dilation degree, not by fitting a Green norm.

For any admissible odd potential \(J\), define
\[
J_{\mathrm{jump}}
=
\sigma(\partial_\infty J),
\qquad
J_0
=
J-J_{\mathrm{jump}}.
\]
Then
\[
\partial_\infty J_0=0.
\]

This removes the one-parameter splitting gauge from the previous rank-three extension, provided the source category really requires bounded degree-zero jump representatives.

## Distributional incidence

Since
\[
D\operatorname{sgn}=2\delta_0,
\]
the canonical jump representative obeys
\[
D\sigma(\chi)=\chi\delta_0.
\]

Thus the odd boundary charge and the localized delta incidence are two representations of the same one-dimensional source coordinate:
\[
\chi
\longmapsto
\frac{\chi}{2}\operatorname{sgn}
\xrightarrow{D}
\chi\delta_0.
\]

The ordered inverse derivative returns
\[
S(\chi\delta_0)
=
-\chi\operatorname{sgn}
=
-2\sigma(\chi).
\]

All signs are fixed by the previously frozen conventions for \(D\), \(S\), and reciprocal reflection.

## Scope

The theorem does not show that a labelled arithmetic potential \(J_p\) exists, has finite boundary charge, or has a zero-charge residual with adequate decay. It proves that once those properties hold, the jump section is no longer arbitrary.

If dilation covariance is twisted by an Euler half-density, the theorem must be applied after conjugating to the intensive degree-zero frame. Using raw weighted coordinates can otherwise introduce a false scale factor.

## Completion consequence

The jump section is isometric up to the fixed normalization of the one-dimensional charge line. It cannot develop cutoff-dependent shear. Completion instability can only enter through:

- the arithmetic charge coefficients \(\chi_p\);
- the zero-charge residual \(J_{p,0}\);
- the incidence from the charge line into the seam/archimedean observer.

## Hostile

Any alternative bounded jump representative with the same charge but a nonconstant profile on one ray violates dilation invariance. Any even correction violates reciprocal oddness. Hence the source-character laws jointly reject the splitting gauge.

## Revised frontier

The rank-three constructor now has a canonical algebraic split:
\[
J_p
=
\frac{\chi_p}{2}\operatorname{sgn}
+
J_{p,0},
\qquad
\partial_\infty J_{p,0}=0.
\]

The next unresolved calculation is source-specific: derive \(J_p\) and prove that \(\chi_p\) equals the frozen primitive first-cumulant coefficient while \(J_{p,0}\) has a completion-summable ordered return.
