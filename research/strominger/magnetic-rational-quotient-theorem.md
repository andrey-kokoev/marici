# Rational quotient of the classified magnetic kernel

Let `g>=2`, let `A` be any finite admitted set of nonnegative even pole
depths, and impose any Laurent cutoff.  Start from the complete combinatorial
classification in `parity-kernel-master-theorem.md`.

For every visible positive-depth tower

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)},\qquad a>0,
\]

the `z`-component of its folded one-form has residues

\[
\operatorname{Res}_{z=0}f_{g,a}
=-g(g+1)C_{g+1}a^{\overline{g-1}},
\]

\[
\operatorname{Res}_{z=-1/\bar z}f_{g,a}
=g(g+1)C_{g+1}a^{\overline{g-1}},
\]

where `C_n` is the Catalan number.  This character is nonzero throughout the
admissible range, so no positive-depth tower has a rational primitive.

## Residue transport proof

Writing `u=z*bar(z)`, direct conversion of the covariant chain gives

\[
f_{g,a}=\bar z\,T_{g+1}T_g\cdots T_2u^{-a},
\qquad
T_s=\partial_u+\frac{2s}{1+u}.
\]

For the formal residue pairing, integration by parts gives the exact adjoint
step

\[
\operatorname{Res}_{u=0}(1+u)^{-r}T_sH\,du
=(r+2s)\operatorname{Res}_{u=0}(1+u)^{-r-1}H\,du.
\]

Moving all `g` transport factors across therefore yields

\[
\operatorname{Res}_{z=0}f_{g,a}\,dz
=\frac{(2g+2)!}{(g+2)!}
[u^{a-1}](1+u)^{-g}.
\]

All admitted positive depths are even, so

\[
[u^{a-1}](1+u)^{-g}
=-\binom{g+a-2}{a-1}.
\]

Factoring the product proves

\[
-\frac{(2g+2)!}{(g+2)!}
\binom{g+a-2}{a-1}
=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

The second residue is its opposite because the rational one-form has no
residue at infinity.  This proves the all-grade, all-depth assertion without
interpolation.

The depth-zero tower is rational-exact, with primitive

\[
\Phi_{g,0}=-\frac{(g+3)!}{6(g-1)(1+z\bar z)^{g-1}}.
\]

Both exceptional grade-two circuits

\[
E_1^-=1-\bar z^{-2},
\qquad
E_2^-=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}
\]

are rational-exact as well.  A primitive for the previously untreated second
circuit is

\[
\Phi_2=
-\frac{4(-2\bar z^8z+3\bar z^7+5z^7)}{\bar z^7z^7(1+z\bar z)}
+8\bar z^{-7}.
\]

All positive-depth residue vectors lie on the same unlabelled line: their two
entries are `(r,-r)` at the same divisors.  Therefore combinations of distinct
towers can cancel their residues.  If `K_g` is the visible magnetic kernel and
`K_g^rat` its rational-exact subspace, then the ordinary rational de Rham
quotient is

\[
\boxed{
\dim(K_g/K_g^{rat})
=\mathbf 1_{\{a\in A:a>0,\ m_{min}\le -(g+a-1)\le m_{max}\}\ne\varnothing}.
}
\]

More precisely, introduce the universal logarithmic form

\[
\eta=d\log\frac{u}{1+u}
=\frac{dz}{z(1+u)}+\frac{d\bar z}{\bar z(1+u)}.
\]

Hermite reduction of the folded tower form gives the cohomological normal
form

\[
\boxed{\omega_{g,a}=d\Phi_{g,a}+r_{g,a}\eta,}
\]

with rational `Phi_{g,a}` and the residue character `r_{g,a}` above.  Hence
every positive-depth tower is a different rational representative of the same
one-dimensional logarithmic class.  The Catalan coefficient is its change of
representative, not a new cohomology generator.

Choose one visible positive depth `a_0` and write

\[
r_{g,a}=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

Then `K_g^rat` is spanned by the visible depth-zero tower, the visible
exceptional circuits, and

\[
r_{g,a_0}D_{g,a}-r_{g,a}D_{g,a_0}
\qquad(a>0,\ a\ne a_0).
\]

Thus the ordinary quotient forgets every boundary circuit and every relative
difference between positive depths.  It retains one common residue class.

A depth-labelled associated grade may instead place each residue in a separate
summand indexed by `a`; that refined object has one line per positive depth.
It is not the ordinary rational de Rham quotient, because its constructor
forbids cancellations between independently labelled depths.  The distinction
between these two objects must remain explicit.

The checker verifies the residue character on grades `2<=g<=8` and depths
`2<=a<=12`, verifies rational primitives for the two exceptional circuits and
depth-zero towers, hostile-tests cross-depth residue-cancelling combinations,
and checks the universal logarithmic normal form.  The residue-transport
calculation above supplies the unbounded residue formula; the finite grid
independently audits the exact reductions.
