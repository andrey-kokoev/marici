# The arithmetic representation is the Weil form before it is a GNS space

Event 10286 constructed the always-positive curvature GNS

\[
L^2(\mu_\Xi).
\]

The arithmetic side cannot be assumed to be another positive GNS before RH.
Its source-native object is the explicit-formula sesquilinear form.

Let \(f\) be an authorized Mellin test packet and write \(\widehat f(s)\) for
its transform. Define the reciprocal involution by

\[
\widehat{f^\#}(s)
=
\overline{\widehat f(1-\bar s)}.
\]

The divisor-side Weil form is schematically

\[
Q_\Xi(f,g)
=
\sum_\rho
\widehat f(\rho)
\overline{\widehat g(1-\bar\rho)},
\]

with the standard convergence regularization and endpoint terms fixed by the
declared test class.

The explicit formula transports this same form to prime, archimedean, and
endpoint data. Thus \(Q_\Xi\) exists as a typed Hermitian form before any
claim of positivity.

## RH specialization

If RH holds, then

\[
1-\bar\rho=\rho,
\]

and therefore

\[
Q_\Xi(f,f)
=
\sum_\rho|\widehat f(\rho)|^2
\ge0.
\]

After quotienting the radical and completing, this is precisely the
multiplicity-resolved divisor GNS.

If an off-seam reciprocal pair exists, the two evaluation coordinates are
paired across distinct points rather than with themselves. On a sufficiently
rich authorized test class, interpolation separates those coordinates and
produces a negative direction. This is the content of the Weil positivity
criterion.

Hence, with the exact test-space hypotheses stated,

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
Q_\Xi(f,f)\ge0
\ \text{for every authorized }f.
\]

## Categorical consequence

The correct arrow is

\[
\text{prime/gamma constructor}
\to
\text{Hermitian Weil form}
\to
\begin{cases}
\text{Hilbert GNS},&Q_\Xi\ge0,\\
\text{indefinite/Krein geometry},&Q_\Xi\not\ge0.
\end{cases}
\]

It is circular to start with a positive arithmetic Hilbert space and then
deduce RH from its positivity. Positivity is the theorem.

This returns exactly to Kitaev’s first warning: off the seam, the natural
geometry may be a generalized eigenvalue pencil or Krein form rather than a
positive Birman–Schwinger contraction.

## Relation to the five margins

The five-margin constructor programme now has a precise terminal target. It
must prove positivity of the complete source-derived Weil form, not merely
positivity of a scalar shadow or of the analytic curvature measure.

The hierarchy is

\[
\text{constructor coherence}
\to
\text{five uniform source margins}
\to
Q_\Xi\ge0
\to
\text{Weil criterion}
\to
\mathrm{RH}.
\]

The spectral-identification theorem is the proof that the form produced by
the constructors is exactly \(Q_\Xi\), including prime, gamma, seam,
endpoint, and mixed terms.

The smallest hostile is an incomplete explicit form that omits one endpoint
or mixed port. It may remain positive while no longer being the Weil form;
such positivity says nothing about RH.

This identifies the categorical resolution sharply: build the complete Weil
form from source constructors and prove its positivity without assuming the
divisor Hilbert representation that positivity would create.
