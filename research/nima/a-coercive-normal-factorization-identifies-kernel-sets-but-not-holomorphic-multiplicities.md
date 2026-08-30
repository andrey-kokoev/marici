# A coercive normal factorization identifies kernel sets but not holomorphic multiplicities

## Kernel comparison lemma

Let

\[
D(s):\operatorname{Dom}D\subset X\longrightarrow Y
\]

be a closed densely defined boundary pencil, and let \(G(s)\) be a positive
form on \(Y\) satisfying

\[
\langle y,G(s)y\rangle
\ge
m_C\|y\|^2
\]

uniformly for \(s\) in a compact parameter set \(C\).

Define the normal Green form

\[
Q(s)[x]
=
\langle D(s)x,G(s)D(s)x\rangle.
\]

Then

\[
Q(s)[x]=0
\quad\Longleftrightarrow\quad
D(s)x=0.
\]

Equivalently, for the associated nonnegative operator,

\[
\ker\bigl(D(s)^*G(s)D(s)\bigr)
=
\ker D(s).
\]

Thus a coercive normal factorization gives the desired bidirectional kernel
comparison immediately.

## Radical version

If \(G(s)\) is semidefinite, first reduce by its radical. Let
\(\pi_G:Y\to Y/\operatorname{rad}G\). Then

\[
Q(s)[x]=0
\quad\Longleftrightarrow\quad
D(s)x\in\operatorname{rad}G.
\]

Therefore

\[
\ker Q(s)=\ker(\pi_GD(s)).
\]

To recover \(\ker D(s)\), one must additionally prove

\[
\operatorname{ran}D(s)\cap\operatorname{rad}G(s)=\{0\}.
\]

The retained theta endpoint metric closes this condition on the wall--jump
port, while any remaining radical lies in the even zero-trace bulk and must be
audited separately.

## Application to the two RH carriers

Let \(D_{\mathrm{bd}}(s)\) be the ordered reciprocal boundary cone whose
relative determinant line is trivialized by

\[
\det_{\mathrm{rel}}D_{\mathrm{bd}}(s)
=
u(s)\xi(s),
\qquad
u(s)\ne0.
\]

Let \(P_{\mathrm{Green}}(s)\) be the positive polarized Green pencil.

The kernel-set gate is closed if the source proves the form identity

\[
P_{\mathrm{Green}}(s)
=
D_{\mathrm{bd}}(s)^\sharp
G_{\mathrm{src}}(s)
D_{\mathrm{bd}}(s)
\]

on the common stratified graph domain, after the declared radical quotient.
Here \(\sharp\) is the polarized Green adjoint, not necessarily the plain
Hilbert adjoint.

Under coercivity,

\[
\xi(s)=0
\Longrightarrow
\ker D_{\mathrm{bd}}(s)\ne0
\Longleftrightarrow
\ker P_{\mathrm{Green}}(s)\ne0.
\]

The reverse scalar implication additionally uses determinant zero if and only
if boundary-cone noninvertibility.

## Why multiplicity does not follow

Even in one dimension, let

\[
D(s)=s-s_0.
\]

The normal pencil is

\[
D(s)^*D(s)=|s-s_0|^2.
\]

It has the same kernel set, but it is not holomorphic in \(s\), and its real
vanishing order is twice the holomorphic order.

Therefore the positive normal Green pencil cannot by itself preserve the
algebraic multiplicity of the \(\xi\) divisor.

Any claim that equality of kernel sets proves equality of determinant
multiplicities is false.

## First-order multiplicity carrier

Multiplicity must remain on a holomorphic first-order pencil. A sufficient
comparison has the form

\[
\mathcal P_{\mathrm{first}}(s)
=
E(s)D_{\mathrm{bd}}(s)F(s),
\]

where \(E(s)\) and \(F(s)\) are holomorphic invertible families. Then the two
pencils have identical local Smith or Fitting data and equal algebraic
multiplicities.

The positive Green form may be recovered afterward as the normal energy of
\(\mathcal P_{\mathrm{first}}\).

Thus the correct architecture is:

\[
\text{holomorphic boundary pencil}
\longrightarrow
\text{holomorphic first-order Green-equivalent pencil}
\longrightarrow
\text{positive normal energy}.
\]

The middle arrow carries divisor multiplicity; the last carries coercive
seam confinement.

## Completion exactness

At finite cutoff, the factorization is insufficient unless it survives the
limit. One needs:

1. one fixed reduced source carrier;
2. graph or norm-resolvent convergence of the first-order pencils;
3. collective compactness or an equivalent exclusion of spectral pollution;
4. compact-uniform lower bounds for \(G_{\mathrm{src}}\);
5. convergence of the invertible comparison families and their inverses;
6. determinant-line continuity.

A sequence of finite normal factorizations can retain kernel equality at every
cutoff while developing an approximate kernel at completion.

## Minimal source identity

The immediate source calculation is not another determinant. It is the
polarized form comparison

\[
\langle D_{\mathrm{bd}}x,G_{\mathrm{src}}D_{\mathrm{bd}}y\rangle
=
\mathfrak G_{\mathrm{complete}}(x,y)
\]

on a common core, including wall, seam, primitive, square, connected, and
archimedean ports.

Diagonal equality \(x=y\) is insufficient to recover the ordered adjoint and
first-order orientation. Full polarization is required.

## Hostiles

1. Compare only zero sets of scalar determinants.
2. Use a semidefinite metric without reducing its radical.
3. Infer holomorphic multiplicity from \(D^*GD\).
4. Verify only diagonal quadratic energies.
5. Let the comparison maps become singular with cutoff.
6. Prove finite kernel equality without completion spectral exactness.

## Verdict

A complete coercive normal factorization would close bidirectional kernel-set
identification between the boundary cone and the positive Green pencil.

It cannot carry divisor multiplicity. Multiplicity must remain on a
holomorphic first-order comparison pencil related to the boundary cone by
invertible source-derived transformations.

The next gate is therefore the fully polarized first-order factorization, not
another scalar determinant identity.
