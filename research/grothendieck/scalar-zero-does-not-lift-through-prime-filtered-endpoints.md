# Scalar Zero Does Not Lift Through Prime-Filtered Endpoints

## Labelled endpoint packet

Write the completed source as a sum of labelled source components,

\[
\Phi=\sum_{n\geq 1}\Phi_n,
\]

and let

\[
a_n(z)=\int_{\mathbb R}\Phi_n(v)e^{zv}\,dv.
\]

The scalar completed transform is the augmentation

\[
X(z)=\sum_{n\geq1}a_n(z).
\]

For a prime \(p\), retain the valuation-zero and positive-valuation
projections

\[
X_{p,0}(z)=\sum_{p\nmid n}a_n(z),
\qquad
X_{p,+}(z)=\sum_{p\mid n}a_n(z).
\]

Then

\[
X=X_{p,0}+X_{p,+}.
\]

The primitive-current regulator acts on these filtered packets before their
augmentation.

## Exact obstruction

A scalar zero gives only

\[
X_{p,0}(z)=-X_{p,+}(z).
\]

It does not give either filtered endpoint condition separately.

This is already forced by the smallest two-label packet. Take one label outside
the \(p\)-divisible sector and one label inside it, with amplitudes

\[
a_1=1,
\qquad
a_p=-1.
\]

Then

\[
a_1+a_p=0,
\]

while

\[
X_{p,0}=1,
\qquad
X_{p,+}=-1.
\]

Thus cancellation after augmentation can hide a nonzero primitive endpoint
current.

## Categorical form

Let \(V\) be the labelled coefficient module, let

\[
\varepsilon:V\longrightarrow\mathbb C
\]

be total augmentation, and let

\[
P_{p,0}:V\longrightarrow V_{p,0}
\]

be the primitive \(p\)-free projection. The two-label witness proves

\[
\ker\varepsilon
\not\subseteq
\ker P_{p,0}.
\]

Therefore there is no universal implication from scalar nullity to
prime-filtered nullity. Such an implication, if true for the completed theta
source, must come from an additional source coherence law. It cannot come from
linearity, reciprocal symmetry, or the zero equation alone.

## Consequence for seam selection

The common primitive regulator domain collapses to the critical seam because
it retains all prime-filtered currents. The aggregate zero-tail bridge cannot
access that collapse: it sees only \(\varepsilon(a)=0\).

The missing RH-bearing statement can now be typed precisely:

> A zero of the completed theta augmentation canonically lifts to a labelled
> boundary state on which every primitive-current operation is defined,
> coherently across all primes and both reciprocal sectors.

This does not require the filtered endpoints to vanish. It requires their
entire family to inhabit the common source domain. The present theorem shows
that scalar nullity supplies none of that compatibility by itself.

## Hostile falsifier

Any proposed zero-to-labelled-state theorem must reject the two-label packet
above by naming the theta constructor it violates. If it accepts the packet
and uses only its zero augmentation, it cannot transmit the prime-current
seam threshold and supplies no RH information.

## Explanatory status

The apparent zero-to-kernel bridge was one thing only after compression.
Before compression it is two distinct structures:

- cancellation in the augmentation channel;
- admissibility in the family of prime-filtered channels.

Their conflation was hiding the missing wall. RH requires a coherence cell
from the first structure to the second, not another scalar positivity
statement.

