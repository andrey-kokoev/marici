# Theta off-seam anomaly lines require two inequivalent metrics

## Question

Packet 174 constructs the primitive anomaly as a unitary direct-limit line on
the critical seam.  Can the same cutoff lines be completed off the seam in a
single Hilbert metric uniformly equivalent to the seam trivialization?

The nonoscillatory displacement already gives a decisive no.

## Exact local ratio

Let

\[
 s={1\over2}+\delta,
 \qquad 0<\delta<{1\over2},
\]

and use the local Tate transition

\[
 \gamma_p(s)
 ={1-p^{-s}\over1-p^{s-1}}.
\]

Both numerator and denominator are positive, and

\[
 \gamma_p\left({1\over2}+\delta\right)
 ={1-p^{-1/2-\delta}\over1-p^{-1/2+\delta}}>1.
\]

Moreover, since

\[
 \log(1-a)-\log(1-b)
 =\int_a^b{du\over1-u}\ge b-a
 \qquad(0<a<b<1),
\]

we obtain

\[
 \log\gamma_p\left({1\over2}+\delta\right)
 \ge p^{-1/2+\delta}-p^{-1/2-\delta}.
\]

The prime sum on the right diverges.  Hence

\[
 \boxed{
 \prod_{p\le X}\gamma_p\left({1\over2}+\delta\right)
 \longrightarrow+\infty.}
\]

By reciprocal reflection,

\[
 \gamma_p\left({1\over2}-\delta\right)
 =\gamma_p\left({1\over2}+\delta\right)^{-1},
\]

so the corresponding product tends to zero.

## Fixed-metric no-go

Give each cutoff line \(L_X\simeq\mathbb C\) a norm

\[
 \|z\|_X^2=m_X|z|^2.
\]

Suppose these metrics remain uniformly equivalent to one fixed scalar
trivialization:

\[
 0<c\le m_X\le C<\infty.
\]

Then the norm of transport from the initial line to cutoff \(X\) differs from
the raw Euler product by at most the fixed factor \(\sqrt{C/c}\).  It is
therefore unbounded for \(\delta>0\), while its reciprocal is unbounded for
\(-\delta\).

Thus:

\[
 \boxed{
 \text{no single cutoff-independent Hilbert metric, uniformly equivalent to
 the seam metric, controls both off-seam orientations}.}
\]

## The legal two-metric completion

There is no obstruction to transporting the metric itself.  Setting

\[
 m_Y=m_X|U_{X,Y}(s)|^{-2}
\]

makes every bonding map an isometry.  But for \(\delta\ne0\) these transported
metrics escape every uniformly equivalent fixed-metric class.  The two open
half-sectors therefore carry reciprocal metric polarizations, whereas the
critical seam is exactly the locus on which the two polarizations share one
unitary metric.

This is a metric statement, not a scalar-product convergence statement.  The
line-valued directed system still exists on either side.

## Consequence for the seam return problem

The seam return operator cannot be defined by putting both valuation sectors
inside one fixed Hilbert line and multiplying their scalar Euler coordinates.
It must compare two transported metric systems through a relative pairing or
dual-line correspondence.  Any proposed off-seam Green identity that silently
uses the seam norm on both sides has erased precisely the exponential anomaly
carried by the primitive current.

This gives a source-derived meaning to the two half-planes:

\[
 \boxed{
 \text{they are reciprocal metric polarizations of one anomaly line, not two
 regions of one fixed scalar Hilbert geometry}.}
\]

## Scope and falsifier

The theorem is proved on the real displacement \(t=0\).  It is sufficient to
falsify a universal fixed-metric completion, but it does not classify the
oscillatory product at every \(t\), construct the relative pairing, or exclude
unit return eigenvalues.

The next gate is exact: derive the archimedean-normalized pairing between the
two transported metric lines and test whether its Green boundary current is
cutoff invariant.  A residual factor depending on \(X\) is the finite
falsifier.
