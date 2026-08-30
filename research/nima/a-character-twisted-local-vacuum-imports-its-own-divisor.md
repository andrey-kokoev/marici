# A character-twisted local vacuum imports its own divisor

## Local normalization

Fix a prime \(p\). Let the additive character \(\psi_p\) be trivial on \(\mathbb Z_p\) and nontrivial on \(p^{-1}\mathbb Z_p\). Normalize multiplicative Haar measure by

\[
\operatorname{vol}_{d^\times x}(\mathbb Z_p^\times)=1.
\]

For the spherical vacuum

\[
f_0=\mathbf 1_{\mathbb Z_p},
\]

the local Tate integral is

\[
Z_p(f_0,s)
=
\int_{\mathbb Q_p^\times}
f_0(x)|x|^s\,d^\times x
=
\sum_{k\ge0}p^{-ks}
=
\frac1{1-p^{-s}}.
\]

## First nonspherical family

Choose

\[
\eta=p^{-m}u,
\qquad
m\ge1,
\qquad
u\in\mathbb Z_p^\times,
\]

and define the character-twisted vacuum

\[
f_\eta(x)
=
\psi_p(\eta x)\mathbf 1_{\mathbb Z_p}(x).
\]

Its shell integral is controlled by the unit average

\[
A_{m,k}
=
\int_{\mathbb Z_p^\times}
\psi_p(\eta p^kv)\,d^\times v.
\]

The three cases are exact:

\[
A_{m,k}
=
\begin{cases}
0,&k\le m-2,\\
-\dfrac1{p-1},&k=m-1,\\
1,&k\ge m.
\end{cases}
\]

The middle value is the normalized sum of a nontrivial additive character over the nonzero residue classes.

## Exact local Tate factor

Therefore

\[
Z_p(f_\eta,s)
=
-\frac{p^{-(m-1)s}}{p-1}
+
\sum_{k\ge m}p^{-ks}.
\]

Hence

\[
Z_p(f_\eta,s)
=
\frac{p^{-ms}}{1-p^{-s}}
-
\frac{p^{-(m-1)s}}{p-1}.
\]

Relative to the unramified factor,

\[
R_{\eta,p}(s)
=
\frac{Z_p(f_\eta,s)}{Z_p(f_0,s)}
=
p^{-(m-1)s}
\frac{p^{1-s}-1}{p-1}.
\]

This is an explicit source comparison, not a qualitative ramification warning.

## Divisor consequence

The factor \(p^{-(m-1)s}\) is entire and nowhere zero. The remaining factor vanishes when

\[
p^{1-s}=1.
\]

Equivalently,

\[
s
=
1-\frac{2\pi i n}{\log p},
\qquad
n\in\mathbb Z.
\]

Thus the simplest finite character-twisted vacuum introduces its own vertical divisor on \(\operatorname{Re}s=1\).

It is not related to the spherical zeta vacuum by a nowhere-zero local frame.

## Consequence for RH feedback

The nonspherical Weyl direction does carry the additive phase missing from valuation projection. But its local Tate section is not a harmless enlargement of the unramified Euler factor.

If it is inserted into a determinant or boundary feedback system, its divisor must be retained and separated. Silently identifying it with the distinguished zeta line would import spurious spectral zeros.

Therefore the ramified enlargement route requires more than a relative scalar normalization. It needs a typed complex in which the extra local divisor is canceled by a source-derived acyclic pair or is confined to a declared auxiliary determinant line.

Dividing by \(p^{1-s}-1\) after the calculation would be circular unless that inverse arises from an independently authorized constructor.

## First-conductor case

For \(m=1\),

\[
R_{\eta,p}(s)
=
\frac{p^{1-s}-1}{p-1}.
\]

This is the smallest phase-sensitive local port. It already fails the nowhere-zero comparison test.

Hence increasing conductor is not the source of the obstruction. The obstruction appears at the first nonspherical Weyl excitation.

## Spherical-route implication

The distinguished zeta determinant should remain on the spherical local carrier unless the auxiliary ramified divisor is explicitly resolved.

The odd orientation required for the RH feedback therefore cannot be obtained merely by replacing one spherical local vacuum with a character twist.

A lawful use of the twist must keep two determinant lines separate:

\[
\text{unramified zeta line}
\quad\text{and}\quad
\text{ramified phase line}.
\]

Only a source-derived comparison complex may combine them.

## Hostiles

1. Declare the character twist to be a nowhere-zero change of local frame.
2. Remove \(p^{1-s}-1\) by scalar division without a constructor.
3. Attribute the imported \(\operatorname{Re}s=1\) zeros to the completed zeta section.
4. Sum ramified ports over primes before recording their separate local divisors.
5. Use the correct Weyl phase but forget that the local Tate factor changed.

## Verdict

The first explicit ramified additive port supplies the missing finite Weyl phase, but it also supplies an unavoidable local divisor:

\[
R_{\eta,p}(s)
=
p^{-(m-1)s}
\frac{p^{1-s}-1}{p-1}.
\]

So ramified phase directions cannot be added as invisible boundary coordinates. Their divisor must be resolved by a separate source-derived complex before they can participate in an RH determinant.
