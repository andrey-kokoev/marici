# The Pearson Ladder Is the Mellin Shadow of a Relative de Rham Boundary

## Question

Can the analytic regular Mellin strip and the polar Gysin sequence be attached
without fitting a boundary correction?

Yes. The complete Pearson ladder is the Mellin transform of one exact
source-level derivative identity. Its wall current is the Stokes boundary of
that identity.

## Source germs

Put \(x=ce^y\), \(a=3/2\), and

\[
f_j(y)=x^{j+5/4}(x-a)e^{-x}.
\]

Define the shifted source

\[
g_j(y)=f_{j+1}(y)-a f_j(y)
=x^{j+5/4}(x-a)^2e^{-x}.
\]

Direct differentiation gives

\[
-\partial_yg_j
=f_{j+2}
-\left(j+\frac{19}{4}\right)f_{j+1}
+\frac32\left(j+\frac54\right)f_j.
\]

Every coefficient in the width-two Pearson recurrence is therefore forced by
one relative de Rham boundary.

## Mellin pushforward

Let

\[
I_{j,q}=\int_0^\infty y^qf_j(y)\,dy,
\qquad
K_j(q)=I_{j+1,q}-\frac32I_{j,q}.
\]

For positive real part of \(q\), Stokes integration gives

\[
\int_0^\infty y^q(-\partial_yg_j)\,dy
=q\int_0^\infty y^{q-1}g_j(y)\,dy
=qK_j(q-1).
\]

This is exactly the meromorphic Pearson identity.

At \(q=0\), the ordinary boundary term is

\[
g_j(0)
=c^{j+5/4}(c-3/2)^2e^{-c}
=W_j.
\]

In the meromorphic formula, the same value appears as

\[
\lim_{q\to0}qK_j(q-1)
=\operatorname*{Res}_{q=0}K_j(q-1)
=W_j.
\]

Thus the regular shifted bulk and the polar wall current are not separate
repairs. They are the interior and boundary terms of one Stokes identity.

## The totalized correspondence

The source diagram now contains:

1. multiplication by \(y\), which raises the Rees grade;
2. the de Rham derivative \(\partial_y\), which lowers it;
3. evaluation at \(y=0\), which records the Gysin quotient;
4. Mellin pushforward, which converts their adjunction into exponent shift.

On untruncated germs,

\[
[\partial_y,y]=1.
\]

This Weyl relation is the source-derived chain homotopy behind the factor
\(q\) in the Pearson ladder.

## Finite-jet anomaly

On the square truncated jet space \(A_N\), the derivative and truncated
multiplication satisfy

\[
[\partial_y,y]_N
=1-(N+1)P_N,
\]

where \(P_N\) projects to the terminal jet \(y^N\). The last term is a cutoff
anomaly created by deleting grade \(N+1\). It is not the physical wall
residue.

For every fixed finite jet, the projector moves beyond that jet as the cutoff
increases. The formal germ limit restores the exact Weyl relation. A finite
checker that silently wraps the terminal jet back to the residue would mix a
cutoff anomaly with the Gysin boundary and is inadmissible.

## Relation to the five-channel pairing

The wall quotient and its dual comparison port now arise from the relative
de Rham sequence. The tail determinant and its dual comparison port arise
from the invertible Pearson degree block. The five-channel carrier is
therefore the finite value-level shadow of a larger differential
correspondence, not an arbitrary spectral completion.

The remaining question is no longer whether a boundary constructor exists.
It is whether the degree-global quadratic form lifts to a bilinear pairing on
this de Rham–Rees correspondence and whether its cutoff anomaly is exact in
the total complex.

## Sharp falsifier

Compute the bilinear concomitant of the five-channel form with
\(\partial_y\) and multiplication by \(y\). Any residual not supported on
the declared wall evaluation or terminal cutoff projector is a genuine typed
anomaly and closes the metric-lift route.

## Verification

The checker
`research/grothendieck/checkers/pearson_relative_derham_boundary.py`
verifies the source derivative identity, wall value, hostile coefficient
residual, and the exact finite-jet Weyl anomaly through order twelve.
