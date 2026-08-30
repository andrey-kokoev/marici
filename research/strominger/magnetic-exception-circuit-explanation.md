# Why the exceptional coefficients are (1,-3,2)

At the genuine exceptional locus `(g,q)=(2,7)`, the three source columns are

\[
(a,m)=(0,-8),(4,2),(6,0).
\]

The locus itself is forced before computing any nullspace.  Put `d=q-g` in
the low-grade odd collision family.  Before specializing the grade, the two
routes carrying the transverse observation `R_2` are

\[
L_{g,d}=-\left(2dg+2d-g^2-11g-4\right)
\frac{(d+g-3)!}{(d-2)!},
\]

and

\[
R_{g,d}=\frac{g(d-4)(d-3)(g-2)(g-1)(g+3)}{2}
\frac{(d+g-3)!}{d!}.
\]

The right route contains the same grade divisor `g-2` that creates the
`q=1` exception.  On that divisor the responses reduce to

\[
R_2(d-1,+)=-6(d-1)(d-5),
\qquad
R_2(d+1,+)=0.
\]

Thus `R_2` is carried by a single source state and disappears exactly at
`d=5` in the admissible odd range.  This immediately predicts

\[
q=g+d=7,
\qquad
(d-1,d+1)=(4,6).
\]

The missing observation is therefore the intersection of two carrier
divisors:

\[
g-2=0,
\qquad
d-5=0.
\]

It is a literal simultaneous loss of both transport routes, not cancellation
between alternative determinant terms.

The grade divisor also has a direct constructor meaning.  The right route is
a `j=3` path contribution, and its multiplicity contains

\[
g(g-1)(g-2)=6\binom g3.
\]

Three fold-step choices are required to transport this observation.  At grade
two that constructor does not exist.  The factors `(d-4)(d-3)` are the
corresponding depth endpoint factors (equivalently `(a-5)(a-4)` for
`a=d+1`).  Thus the full right-route factorization records both capacities:

\[
\text{grade capacity}\times\text{depth capacity}\times
\text{nonzero normalization}.
\]

In system language, `g=2` is not a parameter value at which a working backup
randomly fails.  The backup route requires a three-stage constructor and is
absent from the grade-two architecture.  The left route normally compensates;
`d=5` disables that remaining route.

## Constructor theorem and repairs

In the local row order `(R_1,R_2,R_0)`, the exceptional core is

\[
\begin{pmatrix}
-160&-40&20\\
0&0&0\\
-120&0&60
\end{pmatrix}.
\]

The depth-zero minus column has no `R_2` port.  The other two columns are
exactly the left and right carrier ports.  If their lost entries are restored
as `(ell,rho)`, then

\[
\det
\begin{pmatrix}
-160&-40&20\\
0&\ell&\rho\\
-120&0&60
\end{pmatrix}
=-7200\ell+4800\rho.
\]

Both cofactors are nonzero.  Therefore either independent repair is locally
sufficient:

- a capacity repair `g>=3` restores the right `j=3` route;
- an alignment repair `d!=5` restores the left `j=1` route.

The statement is basis-independent at the level of the two-port route
submodule: changing its generators changes `(ell,rho)` but not the fact that
the determinant pairs nontrivially with both directions.  Hence `R_2` is not
an arbitrarily named matrix row; it is the missing one-dimensional quotient
of the observation space, equipped with two independently constructible
lifts.

## The full interference law

Away from the exceptional fiber, expansion along `R_2` gives

\[
\det C_{g,d}=C_L(g,d)L_{g,d}+C_R(g,d)R_{g,d},
\]

where

\[
C_L=\frac{g(g+3)(dg-2d-5g+4)(g+3)!(d+g-1)!}{6d!},
\]

\[
C_R=\frac{(g+3)!(d+g-1)!}{3(d-2)!}.
\]

Thus the determinantal obstruction has two possible causes:

1. **route loss:** `L=R=0`;
2. **interference:** both routes exist but `C_LL=-C_RR`.

The magnetic Diophantine theorem proves that the second mechanism produces no
additional zero on the admissible integer lattice.  Over complexified
parameters it does occur and accounts for the larger hypersurface `P(g,d)=0`.
This is why route ideals explain the integral exceptions while the Fitting
ideal remains the complete algebraic discriminant.

All their nonzero target data lie on just two rows, `R_0` and `R_1`.  After a
common factor of 20 is removed, their transported boundary states are

\[
v_0=(-6,-8),\qquad v_4=(0,-2),\qquad v_6=(3,1).
\]

Three vectors in a two-dimensional state space possess a canonical signed
Plucker relation.  Its coordinates are

\[
\bigl(\det(v_4,v_6),-\det(v_0,v_6),\det(v_0,v_4)\bigr)
=(6,-18,12).
\]

Dividing by the gcd gives

\[
(1,-3,2).
\]

Thus

\[
v_0-3v_4+2v_6=0,
\]

which lifts directly to

\[
\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}\in\ker M_2.
\]

Every pairwise minor is nonzero, so no two columns are dependent.  The
three-column relation is minimal and its primitive integral coordinate is
unique up to sign.

This supplies the constructor-level explanation.  The factor `d-5` erases
the transverse observation, collapsing the local collision component to a
two-entry boundary state.  Three independently transported source states must
then live in that two-dimensional space, and their coefficients are forced by
the oriented areas between them.  At every other admissible odd `d`, `R_2`
survives and resolves the three states.

Equivalently:

\[
\text{the coefficients }(1,-3,2)\text{ are primitive Plucker coordinates of
the failed boundary reconstruction.}
\]

The checker reconstructs the columns from the lattice path law, verifies the
two-row collapse, computes the minors, and tests minimality exactly.
