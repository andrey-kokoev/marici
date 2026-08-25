# The joint electric/magnetic observer is faithful

Write the full folded sheet packet as

\[
T_{\mathrm{sheet}}(D)=(A(D),B(D)),
\]

with complementary readouts

\[
E=A+B,
\qquad
M=A-B.
\]

Over characteristic zero, `(E,M)` and `(A,B)` determine one another.  Hence

\[
\ker E\cap\ker M=\ker T_{\mathrm{sheet}}.
\]

The unbarred sheet map `A` alone is injective for arbitrary grade, finite even
pole-depth set, and Laurent cutoff.  The exact sparse audit supplies the
following cross-check coverage:

\[
2\le g\le10,
\qquad
0\le k\le6,
\]

with two independently varied sufficient Laurent cutoffs at every `(g,k)`:
126 matrices and 9,072 source columns in total.

Therefore no tested nonzero source state is erased from the full sheet packet
or from the joint `(E,M)` observer.

Every tested tower also has a nonzero sheet for

\[
2\le g\le30,
\qquad
0\le a\le20,
\]

and both exceptional circuits have nonzero cleared sheets.  In particular,

\[
A(E_1)=40\bigl(z+\bar z\bigr)
\]

after the common denominator is cleared, while

\[
A(E_2)=-120z^{-7}-160z^{-6}\bar z
-120\bar z^{-7}-160z\bar z^{-6}
\]

in the sparse cleared numerator convention.

A wider componentwise stress test uses pole cutoff `k=20` on every signed
diagonal `-30<=h=a+m<=15` for grades `2<=g<=8`.  All 322 additional branch
matrices are injective.

Thus, without a bounded qualifier,

\[
\boxed{
\text{magnetic kernel}
=
\text{nonzero information routed entirely to the reflection-even sheet
sector}.
}
\]

## Unbounded proof

The unbarred sheet matrix has an even simpler component law than the magnetic
matrix.  Every target of a source `(a,m)` has fixed signed exponent difference

\[
r-t=1-g-(a+m).
\]

Hence `A` decomposes by the signed diagonal `a+m`, without identifying it with
its reflected negative.  Magnetic antisymmetrization is precisely the later
operation that joins the two signed branches.

Joint faithfulness reduces to injectivity of each one-branch weighted path
matrix.  Reflection pairing, not the fold itself, is therefore the sole source
of magnetic kernel classes.

There is also an exact one-variable reduction.  On a signed component write

\[
D=\bar z^hF(u),
\qquad
F(u)=\sum_{a\text{ even}}c_a u^{-a}.
\]

Then

\[
A(D)=\bar z^{h+g-1}
\left(u\partial_u+h+g\right)\mathcal L_gF,
\]

where

\[
\mathcal L_g=prod_{s=2}^{g+1}
\left(\partial_u+\frac{2s}{1+u}\right).
\]

Thus a sheet-kernel vector would require

\[
\mathcal L_gF=c\,u^{-(h+g)}.
\]

Let `u^-a` be the highest pole of nonzero `F`, with `a>0`.  Direct induction
through the factors of `L_g` gives

\[
\mathcal L_gu^{-a}
=(-1)^g a^{\overline g}u^{-a-g}
+(-1)^{g+1}g(g+3)a^{\overline{g-1}}u^{-a-g+1}
+O(u^{-a-g+2}).
\]

Both displayed coefficients are nonzero.  The first forces `h=a` if the
right-hand monomial is nonzero.  But the right-hand side has no
`u^{-a-g+1}` term.  No lower admitted pole can cancel it, because the next
even depth is at most `a-2` and begins only at order `u^{-a-g+2}`.  This is a
contradiction.

If the right-hand constant `c` is zero, the nonzero leading coefficient
already gives a contradiction.  The remaining case `a=0` means `F` is
constant.  Here

\[
\mathcal L_g1=4^{\overline g}(1+u)^{-g},
\]

and

\[
(u\partial_u+h+g)\mathcal L_g1
=4^{\overline g}(1+u)^{-g-1}\bigl((h+g)+hu\bigr),
\]

which cannot vanish for `g>=2`.

Therefore `F=0`, proving

\[
\boxed{\ker A=0.}
\]

Since `(E,M)` is an invertible linear recombination of `(A,B)`, the joint
electric/magnetic observer is faithful as well.
