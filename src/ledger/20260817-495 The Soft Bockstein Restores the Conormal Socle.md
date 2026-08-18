# Entry 495 — The Soft Bockstein Restores the Conormal Socle

Entry 494 identifies the class lost by ordinary soft specialization as the
top conormal socle \(a^3\).  The connecting morphism can now be computed
directly.

Let \(c=1-b^2\), and work generically over

\[
R_0=\mathbb Q(b)[a]/(a^4).
\]

Before specialization the Euler vector is

\[
E=(a/4,0,u/2).
\]

Multiplying by the lost source class \(a^3\), using
\(a^4=-ua^2c\), and dividing by \(u\) gives the connecting cycle

\[
\beta(a^3)=(-a^2c/4,0,a^3/2).
\]

At \(u=0\), the three retained gradients are

\[
(K_a,K_b,K_u)=(4a^3,0,a^2c).
\]

The Koszul boundary of \((1/4)e_a\wedge e_u\) is

\[
(-a^2c/4,0,a^3).
\]

Therefore the Bockstein has the normal form

\[
\boxed{
\beta(a^3)\equiv-{1\over2}a^3e_u
\quad\text{in }H_1(K_a,K_b,K_u;R_0).
}
\]

This class is nonzero.  A boundary with zero \(e_a\)-component would require
its \(e_a\wedge e_u\) coefficient to annihilate \(a^2c\), hence to lie in
\((a^2)\); multiplying such a coefficient by \(4a^3\) produces zero, not
\(a^3e_u\).

## Consequence

The falsifier in Entry 494 is passed: derived \(u\)-specialization restores
exactly the missing one-dimensional Cartier socle, and does so in the
deformation-gradient direction.  Thus the generic even comparison has the
length decomposition

\[
\operatorname{im}(a/4)\ \text{of length }3
\quad\oplus_{\rm derived}\quad
\mathbb Q(b)\langle a^3e_u\rangle\ \text{of length }1.
\]

Together these reconstruct the length-four principal conormal module.  The
extra \(K_u\) direction is therefore not a second conormal generator; it is
the Bockstein carrier of the top layer of the original one.

## Next gate

Restore the \(b\)-dependence at the endpoints \(c=1-b^2=0\).  Determine
whether the normal form \(a^3e_u\) extends across both endpoint charts or
acquires a residue/extension class there.  This is the remaining passage
from the generic conormal reconstruction to the global filtered defect of
Entry 473.

The exact finite calculation is
`research/voevodsky/check_soft_axis_conormal_bockstein.py`.
