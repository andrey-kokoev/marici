# The primitive theta profile already carries the first cubic flux

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: directed mechanism audit and interpretation correction

## Question

The four-moment certificate proves that the completed theta source has
positive adjacent variance flux at the first hostile cubic interface.  A
natural first explanation was that cross-label modular completion reverses
the negative local seam tendency.  That explanation predicts that the
primitive label alone should not already have the observed orientation.

## Directed primitive test

Retain only the $n=1$ source profile on the canonical positive chamber and
repeat the same directed moment calculation.  Its cross-multiplied flux gap
satisfies

\[
5.88134757514609\times10^{-17}
<D_1<
5.88134803467998\times10^{-17}.
\]

In particular,

\[
D_1>0.
\]

For the full completed positive-chamber source, the corresponding gap is

\[
5.88147833916049\times10^{-17}
<D<
5.88147833918077\times10^{-17}.
\]

Directed division gives

\[
0.9999777668084242
<\frac{D_1}{D}<
0.9999778449442455.
\]

This ratio is a comparison of two nonlinear flux gaps, not an additive
percentage decomposition.  It proves that higher-label cross terms are not
needed to create the sign and alter the primitive gap by less than one part
in ten thousand.

## Interpretation correction

The positive orientation is therefore not produced by cancellation among
many theta labels.  It is already present in the primitive positive-chamber
profile.  Arithmetic completion still has an essential role, but a different
one:

1. reciprocal Poisson sewing selects the canonical seam at $u=0$;
2. the positive chamber then has overwhelming primitive-label dominance;
3. the wall-truncated primitive profile carries the cubic flux orientation;
4. higher labels perturb its magnitude without changing its sign.

Thus the earlier phrase “global completion reverses the local sign” was too
coarse.  Completion defines the physical chamber and its boundary.  The
actual bulk sign at this interface is a primitive seam-profile phenomenon,
not a many-label cancellation phenomenon.

## Exact incomplete-gamma reduction

Write the primitive profile as

\[
\phi_1(u)=
2\pi e^{5u/2}
\left(2\pi e^{2u}-3\right)
e^{-\pi e^{2u}},
\qquad u\ge0.
\]

Put

\[
A(a)=\pi^{-a}\Gamma(a,\pi).
\]

After $x=\pi e^{2u}$, direct substitution and the incomplete-gamma
recurrence give, for $t\ge1$,

\[
Z_t^{(1)}
=\frac{\pi}{2^{2t}}
\left(
4tA^{(2t-1)}(5/4)-\frac12A^{(2t)}(5/4)
\right).
\]

The endpoint term in

\[
A(a+1)=\frac a\pi A(a)+\frac{e^{-\pi}}\pi
\]

vanishes after differentiation.  Thus the primitive problem is an exact
one-parameter incomplete-gamma derivative inequality, not an uncontrolled
theta-label sum.

## Endpoint-hostility audit

Replace the lower endpoint $\pi$ by $c>3/2$, retaining the positive
primitive family obtained from $x=ce^{2u}$.  A bounded Simpson sweep over

\[
c\in
\{1.51,1.6,2,2.5,3,\pi,3.5,4,5,6,8,10,20\}
\]

finds positive normalized flux at every point, increasing from about
$0.0509$ to $0.1356$.  This sweep is diagnostic rather than directed, but
it falsifies the idea that the numerical value $c=\pi$ is visibly tuned to
the sign.

The revised theorem target is the gamma-tail family itself: prove that its
adjacent normalized moment flux is positive for every $c>3/2$, or return
the first counterexample.  Such a theorem would explain the theta sign by
the primitive profile's superexponential stiffness.  Modular arithmetic
would select the physical member $c=\pi$ and control the higher-label
perturbation, but would not manufacture the orientation.

If that reduction succeeds, theta arithmetic will enter through the
source-derived endpoint $\pi$, while positivity will be explained by a
single boundary recurrence rather than a hidden label census.

## Falsifier

The new interpretation fails if the gamma-tail family has any
$c>3/2$ with nonpositive flux, or if a source with the same derived
one-lobe stiffness properties has negative flux.  The latter would show that
an additional, more rigid property of the incomplete-gamma recurrence is
still missing.
