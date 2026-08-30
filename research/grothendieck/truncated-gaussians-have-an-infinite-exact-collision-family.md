# Truncated Gaussians have an infinite exact collision family

## Question

The exponential hostile violates the smooth even seam condition
\(f'(0)=0\).  Can smooth modular evenness combined with strict log-concavity
exclude finite cosine tangencies?

## Gaussian half-source

On \([0,1]\), take

\[
f_A(u)=e^{-Au^2},
\qquad
A>0.
\]

This is the positive half of a smooth even Gaussian source.  It is strictly
decreasing for \(u>0\), satisfies \(f_A'(0)=0\), and is strictly log-concave:

\[
(\log f_A)''=-2A<0.
\]

Define

\[
C_A(y)=\int_0^1f_A(u)\cos(yu)\,du,
\]

\[
M_A(y)=\int_0^1u f_A(u)\sin(yu)\,du.
\]

## Exact integer-frequency dependence

Since

\[
f_A'(u)=-2Au f_A(u),
\]

integration by parts gives

\[
M_A(y)
=-rac1{2A}\int_0^1f_A'(u)\sin(yu)\,du
\]

and hence

\[
M_A(y)
=
-\frac{f_A(1)\sin y}{2A}
+\frac{y}{2A}C_A(y).
\]

At every integer Fourier frequency

\[
y=2\pi k,
\qquad
k\ge1,
\]

the boundary sine vanishes and

\[
M_A(2\pi k)
=
\frac{\pi k}{A}C_A(2\pi k).
\]

Therefore every zero of \(C_A(2\pi k)\) as a function of \(A\) is
automatically a double zero of the cosine transform as a function of frequency.

## Existence for every winding frequency

At \(A=0\),

\[
C_0(2\pi k)=0.
\]

Differentiating with respect to \(A\) at zero gives

\[
\left.\partial_AC_A(2\pi k)\right|_{A=0}
=-int_0^1u^2\cos(2\pi ku)\,du
=-rac1{2\pi^2k^2}<0.
\]

Thus \(C_A(2\pi k)<0\) for all sufficiently small positive \(A\).

As \(A\to\infty\), the Gaussian mass concentrates near \(u=0\), where the
cosine is positive.  After the rescaling \(v=\sqrt A u\), dominated
convergence gives

\[
\sqrt A\,C_A(2\pi k)
\longrightarrow
\int_0^\infty e^{-v^2}\,dv>0.
\]

Continuity therefore supplies at least one \(A_k>0\) satisfying

\[
C_{A_k}(2\pi k)=M_{A_k}(2\pi k)=0
\]

for every \(k\ge1\).

The first collision parameter is numerically

\[
A_1\approx2.32123509554598.
\]

This decimal only locates the exact intermediate-value root; existence is
analytic.

## Strength of the hostile source

The Gaussian hostile possesses every unlabelled archimedean property proposed
so far:

- positivity;
- smoothness;
- even seam extension;
- vanishing first seam derivative;
- strict decrease on the positive chamber;
- strict log-concavity;
- minimum phase of the one-sided transform;
- positive sine orientation;
- explicit endpoint-current retention;
- a self-Fourier carrier before hard support truncation.

Yet its finite support flow has infinitely many exact collision parameters.

## Explanation of the collision

At the integer frequencies \(2\pi k\), the support endpoint is phase-aligned:
the boundary sine term vanishes.  Gaussian differentiation converts position
weighting into the source derivative, so the tangent channel becomes a scalar
multiple of the value channel.  The two collision equations lose rank.

This is a post-factum-obvious mechanism:

> Phase-aligned support plus Gaussian differential closure identifies value
> and tangent ports, making tangency unavoidable when the value crosses zero.

The actual completed theta source must escape this mechanism through structure
not possessed by a single Gaussian—namely its polynomial Gaussian current,
integral winding tower, and modularly coupled label sum.

## Consequence

No theorem formulated solely in terms of a smooth even strictly log-concave
aggregate source can exclude the RH support-flow collision.  Even Gaussian
differential closure makes the problem worse by forcing exact rank loss at
integer frequencies.

The sole viable lane is now the labelled one.  Before codiagonalization, theta
labels carry distinct polynomial-Gaussian scores and square-separated winding
parameters.  A successful theorem must prove that their modular coupling
prevents the Gaussian value--tangent identification from surviving the full
sum.

## Falsifier for the labelled theorem

At \(xL=2\pi k\), compute the labelled value and tangent vectors before
summation.  If the theta differential recurrences make their codiagonal sums
proportional as in the Gaussian hostile, the collision route remains open.  A
genuine advance is an exact labelled residual transverse to that proportional
channel.

## Result

Smooth even Gaussian geometry admits an infinite exact family of finite
support collisions.  This closes the entire unlabelled archimedean-shape lane
and isolates labelled polynomial-Gaussian modular coherence as the remaining
candidate mechanism.
