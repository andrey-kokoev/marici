# The RH spectral gate is separation from one in a semidefinite Green pencil

## Three distinct claims

Let

\[
F_X(s)=U_XU_X^*
\]

and let \(B_X(s)\) be the complete diagonal Green boundary form in one open
sector. The residual is

\[
R_X(s)=B_X(s)-F_X(s).
\]

Three statements must not be identified.

### Exact zero exclusion

\[
\ker R_X(s)=0.
\]

When normalization is valid, this is equivalent to

\[
1\notin\sigma(K_X(s)).
\]

### Positive-order exclusion

\[
R_X(s)>0.
\]

When \(B_X>0\), this is equivalent to

\[
K_X(s)<I.
\]

### Uniform contraction

On a compact \(C\) in the open sector, there is \(\varepsilon_C>0\) with

\[
\lVert K_X(s)\rVert\le1-\varepsilon_C
\]

for every cutoff \(X\) and \(s\in C\).

Uniform contraction implies positive-order exclusion and exact zero exclusion.
The converses fail. In particular, a positive \(K_X\) may have eigenvalues
larger than one while avoiding one.

## What polarization actually gives

If the full polarized Green identity is exact,

\[
\mathcal B_X(\eta,\zeta)
=
(\zeta+\bar\eta)
G_X(\eta)^*G_X(\zeta),
\]

then on the right-sector diagonal,

\[
B_{+,X}(\zeta)
=
2\operatorname{Re}\zeta\,
G_X(\zeta)^*G_X(\zeta)
\ge0.
\]

On the left sector, after the authorized sign reversal,

\[
B_{-,X}(\zeta)
=
-2\operatorname{Re}\zeta\,
G_X(\zeta)^*G_X(\zeta)
\ge0.
\]

Thus the complete diagonal form is positive semidefinite if every boundary
component has genuinely been included in the polarized identity.

Polarization does not by itself give coercivity. One has

\[
\ker B_X=\ker G_X.
\]

Any invisible Green direction prevents ordinary inversion and makes
\(B_X^{-1/2}\) unavailable on the whole carrier.

## Nullspace audit

Let

\[
N_X=\ker B_X.
\]

For \(h\in N_X\),

\[
R_Xh=-F_Xh.
\]

Hence a common null direction

\[
h\in\ker B_X\cap\ker F_X
\]

is automatically in \(\ker R_X\). Exact zero exclusion therefore requires

\[
\ker B_X\cap\ker F_X=0.
\]

More generally, \(N_X\) must be treated before any Birman--Schwinger
normalization. Quotienting it away is authorized only if the complete source
observer family declares it invisible and removes it from the state object.

This is the first hostile test for the proposed \(B_X\).

## Form domination gate

A bounded normalized operator exists on the Green support when the arithmetic
frame form is dominated by the Green form:

\[
\langle h,F_Xh\rangle
\le c_X
\langle h,B_Xh\rangle.
\]

Equivalently,

\[
\operatorname{ran}F_X^{1/2}
\subseteq
\operatorname{ran}B_X^{1/2}
\]

in the finite-dimensional case, with the corresponding form-domain condition
at completion.

Then the Moore--Penrose normalized operator

\[
K_X
=
B_X^{\dagger/2}
F_X
B_X^{\dagger/2}
\]

is positive on

\[
H_X^{B}
=
\overline{\operatorname{ran}B_X^{1/2}}.
\]

Here \(B_X^{\dagger/2}\) denotes inverse square root on the support and zero on
the nullspace. This notation does not erase the separate nullspace audit.

If form domination fails, the normalized operator is unbounded or undefined.
The correct object is the generalized pencil

\[
F_Xh=\lambda B_Xh.
\]

## Exact generalized-eigenvalue criterion

A residual zero is exactly a nonzero solution of

\[
F_Xh=B_Xh.
\]

Thus RH-strength finite exclusion is

\[
\lambda=1
\]

not being a generalized eigenvalue of the pair \((F_X,B_X)\), together with
absence of common null directions.

When \(B_X>0\), this reduces to

\[
1\notin\sigma
\left(
B_X^{-1/2}F_XB_X^{-1/2}
\right).
\]

When \(B_X\ge0\) only, the pencil formulation is primary.

## Correct uniform completion condition

The weakest natural compact-local completion condition is spectral separation:

\[
\operatorname{dist}
\left(
1,\sigma(K_X(s))
\right)
\ge\varepsilon_C>0
\]

for every \(X\) and \(s\in C\), together with uniform control of the Green
support and no common nullspace.

This allows spectrum on both sides of one. It is sufficient to prevent finite
eigenvalues from converging to one at completion.

Uniform contraction,

\[
\sigma(K_X(s))\subset[0,1-\varepsilon_C],
\]

is a stronger one-sided theorem. It follows from the strict comparison

\[
F_X(s)
\le
(1-\varepsilon_C)B_X(s).
\]

That inequality would give a positive residual and a canonical half-plane
orientation, but it must not be called equivalent to RH-strength
nonvanishing.

## Why the stronger inequality remains attractive

If the source Green identity proves

\[
F_X\le(1-\varepsilon_C)B_X,
\]

then:

- \(K_X\) is bounded, positive, and compact when the relative frame is compact;
- \(R_X\) is positive on the Green support;
- determinant orientation is fixed;
- completion kernels are excluded quantitatively;
- reciprocal transfer needs only preserve the ordered forms.

This is a powerful sufficient route. Its additional content is strict
dissipativity or strict observability, not merely absence of zeros.

A hostile model with \(K_X=2I\) has no eigenvalue one but violates contraction.
It shows the logical gap exactly.

## Sectorial alternative

If the actual complete boundary block is sectorial or non-normal rather than
the diagonal Green form above, no positive square-root normalization is
authorized.

One must then study the pencil

\[
F_X-\lambda B_X
\]

using sectorial forms, Krein geometry, or a source-derived symmetrizer. The
relevant completion margin is a lower bound on

\[
\lVert(B_X-F_X)h\rVert
\]

relative to the declared graph norm, not a norm bound on a positive
Birman--Schwinger operator.

Therefore the first construction test is whether the proposed \(B_X\) is
literally the diagonal of the complete polarized Green kernel or a different
transfer operator that only shares its scalar shadow.

## Reciprocal transfer

The reciprocal source map \(J_X\) must carry both forms:

\[
J_X^*B_{-,X}(1-s)J_X=B_{+,X}(s)
\]

and

\[
J_X^*F_{-,X}(1-s)J_X=F_{+,X}(s).
\]

Then it intertwines the generalized pencils and preserves their eigenvalue-one
condition.

Comparing only the normalized \(K\) operators presupposes compatible support
choices and square-root frames. Form-level comparison is prior and safer.

## Finite falsifiers

1. A nonzero common kernel of \(B_X\) and \(F_X\) is an immediate residual
   zero.
2. Positivity of the diagonal scalar flux without the full polarized kernel
   does not establish \(B_X\ge0\) on the typed carrier.
3. Failure of form domination makes \(K_X\) undefined.
4. \(1\notin\sigma(K_X)\) does not imply \(\lVert K_X\rVert<1\).
5. Finite spectral gaps tending to zero permit a completion collision.
6. Reciprocal determinant equality does not intertwine the pencils.
7. A square-root normalization chosen independently in both sectors can smear
   the reciprocal frame.

## Revised theorem stack

The clean next theorem has four ordered parts:

1. the complete polarized Green form is positive semidefinite in each open
   sector after the authorized sign;
2. its nullspace has trivial intersection with the arithmetic frame nullspace;
3. the arithmetic frame is relatively form-bounded, producing a positive
   compact \(K_X\) on the Green support;
4. the spectrum of \(K_X\) is compact-locally separated from one through
   completion.

A fifth, stronger theorem may replace item four by strict domination
\(F_X\le(1-\varepsilon_C)B_X\), but that is additional orientation.

## Verdict

The primary RH object is the generalized Green pencil

\[
F_X-\lambda B_X.
\]

Positivity of the polarized diagonal permits Birman--Schwinger normalization
only after a nullspace and form-domain audit. Exact RH-strength exclusion is
absence of the generalized eigenvalue one. Uniform contraction is a stronger
sufficient theorem whose extra content must be derived, not assumed.
