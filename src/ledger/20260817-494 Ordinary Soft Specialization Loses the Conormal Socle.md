# Entry 494 — Ordinary Soft Specialization Loses the Conormal Socle

Entry 493 supplies the global Euler bridge

\[
K={a\over4}K_a+{u\over2}K_u
\]

from the principal hypersurface resolution to the three-gradient complex.
Ordinary restriction to \(u=0\) does not preserve the whole bridge.

At a generic point of the \(b\)-line, the special carrier algebra is

\[
R_0=\mathbb Q(b)[a]/(a^4).
\]

The conormal module \(I/I^2\cong R_0\) has basis

\[
1,a,a^2,a^3.
\]

But the Euler vector specializes from \((a/4,0,u/2)\) to
\((a/4,0,0)\).  Its induced coefficient map is multiplication by \(a/4\):

\[
R_0\xrightarrow{a/4}R_0.
\]

This map has rank three and kernel

\[
\boxed{\operatorname{ker}(a/4)=\mathbb Q(b)\langle a^3\rangle.}
\]

Hence the naively specialized Euler cycle sees only
\(R_0/(a^3)\); it loses the top Cartier layer of the length-four conormal
module.  The missing direction is precisely the layer carried before
specialization by the \(uK_u/2\) component.

## Consequence

The three-gradient correction is necessary but ordinary base change is still
too early.  The conormal comparison must be specialized derivedly in the
\(u\)-direction.  Its \(\operatorname{Tor}_1\) or Bockstein term is expected
to restore the missing \(a^3\) socle.

This gives a concrete meaning to the extra Kodaira--Spencer direction:

\[
\text{ordinary Euler image of length }3
\quad+\quad
\text{derived }u\text{-Bockstein of length }1
\quad=\quad
I/I^2\text{ of length }4.
\]

This length decomposition is established; the identification of the
Bockstein arrow with the missing socle remains to be computed explicitly.

## Next gate

Represent specialization by the two-term resolution
\([S\xrightarrow u S]\), totalize it with the Euler comparison, and compute
the connecting morphism on the class killed by multiplication by \(a\).
The falsifier is any Bockstein image other than a nonzero multiple of
\(a^3\).

The finite rank audit is
`research/voevodsky/check_soft_axis_naive_specialization_loss.py`.
