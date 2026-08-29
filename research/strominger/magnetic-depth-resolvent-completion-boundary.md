# Depth resolvent fixes the magnetic completion boundary

Let

\[
F_a(t,x)=(1+t)^{-a}(1-xt)^{a-\beta}.
\]

The exact source transfer is

\[
F_{a+1}=U F_a,
\qquad
U(t,x)=\frac{1-xt}{1+t}.
\]

Introduce a depth-generating variable \(y\). Summing the orbit before grade
truncation gives the exact resolvent identity

\[
\sum_{a\ge0}y^a F_a(t,x)
=
\frac{(1-xt)^{-\beta}}{1-yU(t,x)}.
\]

This is the source-side generating function requested by the completion
problem. No Hall basis or fitted norm enters its derivation.

## Truncated-jet singularity

On the grade-\(g\) jet,

\[
U=I+N,
\qquad
N^{g+1}=0.
\]

Hence

\[
(I-yU)^{-1}
=
\frac{1}{1-y}
\sum_{j=0}^{g}
\left(\frac{y}{1-y}\right)^jN^j.
\]

The depth resolvent has one finite singular locus,

\[
y=1,
\]

and pole order at most \(g+1\). Therefore every coefficient sequence obtained
by a fixed source-side linear observation has polynomial growth of degree at
most \(g\). On any circle \(|y|=r<1\), equivalently any coefficient weight
\(\rho^a\) with \(\rho=r^{-1}>1\), the source resolvent is analytic and its
coefficient kernel is exponentially summable.

This identifies the candidate completion boundary without selecting \(\rho\)
from successful trials:

\[
\rho_c=1.
\]

## Quotient prediction

The right Euler boundary operator contains the displacement \(x^Q\), with

\[
Q=q+2.
\]

After descent to the preferred Hall carrier, this becomes the observed delay:
the moving minus tail of a deep plus relation begins at depth offset \(Q\).
The quotient should therefore be a finite plus-cap correction followed by a
delayed lower-triangular kernel.

One cancellation is expected when passing from the full source jet to a single
relation column. This predicts:

\[
\max_a\|c_a\|_1\asymp N^{g-1}
\]

for the unweighted column maximum through cutoff \(N\), while accumulating
columns at a fixed observer coordinate predicts

\[
\max_d\sum_a|c_{a;d}|\asymp N^g.
\]

## Exact bounded evidence

At \(q=3\), exact rational Hall relations were computed through cutoff \(120\).
Effective exponents between cutoffs \(80\) and \(120\) were:

| \(g\) | column exponent | row exponent | predicted |
|---:|---:|---:|---:|
| 3 | 1.986 | 2.960 | \(2,3\) |
| 4 | 2.969 | 3.938 | \(3,4\) |
| 5 | 3.940 | 4.900 | \(4,5\) |
| 6 | 4.900 | 5.851 | \(5,6\) |
| 7 | 5.851 | 6.793 | \(6,7\) |
| 8 | 6.793 | 7.726 | \(7,8\) |

The convergence from below is uniform with increasing grade and matches the
finite-cutoff signature of the predicted powers.

## Status and remaining theorem

The source resolvent identity and its unit singular locus are exact theorems.
The identification of the descended Hall projection with a delayed rational
kernel having the one-degree cancellation remains a conjecture supported by
exact bounded evidence.

The missing proof is now local:

1. express \(x^QH_a\) as the \(Q\)-step source transfer of \(H_{a-Q}\);
2. descend the identity through \(A_-\) and \(A_+\);
3. isolate the finite plus-cap boundary term;
4. prove the remaining kernel has denominator dividing
   \((1-y)^g\);
5. apply two-sided Schur estimates for every \(\rho>1\);
6. show the nonzero leading Laurent coefficient forces failure at \(\rho=1\).

This would establish both the quotient-operator norm and the adjoint-observer
norm on the same source-authorized depth-generating space.

## Exact pole-drop lemma

The branch-alignment mismatch itself already has the required principal part.
Since \(U=I+N\),

\[
U^Q-I
=
\sum_{k=1}^{g}\binom{Q}{k}N^k
=
N\,V_Q(N),
\qquad
V_Q(0)=Q.
\]

Multiplying the exact resolvent gives

\[
(U^Q-I)(I-yU)^{-1}
=
\sum_{k=1}^{g}\binom{Q}{k}N^k
\sum_{j=0}^{g}\frac{y^jN^j}{(1-y)^{j+1}}.
\]

The order-\((g+1)\) term is annihilated because it contains \(N^{g+k}\)
with \(k\ge1\). The unique surviving order-\(g\) term is

\[
\frac{Q\,y^{g-1}N^g}{(1-y)^g}.
\]

It is nonzero in the native source jet. Indeed,

\[
N=-\frac{(1+x)t}{1+t},
\]

so modulo \(t^{g+1}\),

\[
N^g(1-xt)^{-\beta}
=
(-1)^g(1+x)^g t^g.
\]

Thus grade extraction gives the nonzero principal coefficient

\[
(-1)^gQ\,g!(1+x)^g.
\]

This proves, before Euler descent, that branch alignment cancels exactly one
depth pole and no more. The adjoint mismatch has the transposed principal
coefficient \(Q(N^\ast)^g\), hence retains the same pole order \(g\).

Any finite plus-cap correction is a polynomial in \(y\). It is holomorphic at
\(y=1\) and therefore cannot create, cancel, or modify this principal part.
Cap dependence can affect finite constants and charts but not the completion
boundary or pole order.

The Euler action on the top class is also explicit. Set

\[
\phi_a=x^{-a-g}(1+x)^g.
\]

Direct substitution into the universal boundary operators gives

\[
A_-\phi_a
=
(1+x)(1-Q-a-g)\phi_a,
\]

and

\[
A_+\phi_a
=
(1+x)(1+Q-a-g)\phi_a.
\]

Thus neither boundary operator annihilates the stable top-jet tail. Each can
vanish only at an isolated initialization depth. Such depths belong to the
finite cap and cannot change the Laurent principal part of the infinite depth
resolvent.

Consequently the source mismatch loses exactly one pole before descent, the
stable Euler maps preserve its top direction, and inversion along the minus
spine divides only by the displayed affine depth factor. The remaining formal
task is to write this inversion as a depth-generating multiplier and verify
that its finite initialization terms are precisely the observed cap.
