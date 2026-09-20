# Higher-coherence topology iteration 17: Markov normalization confines only when both reciprocal routes share one faithful stationary state

## Candidate topology

Promote the reciprocal CP channels to Markov maps on an ordered operator
system. A state `omega` is stationary for a Heisenberg channel `E` when

\[
\omega(\mathcal E(X))=\omega(X),
\]

and the channel is unital when `E(I)=I`. Markov concatenation then supplies
strict higher coherence, and conditional expectations provide canonical
contractive fillers.

## One-dimensional prime channel

The forward and reciprocal maps are

\[
\mathcal E_+(X)=p^{-2a}X,
\qquad
\mathcal E_-(X)=p^{2a}X,
\qquad a=\operatorname{Re}z.
\]

For any faithful nonzero state `omega`, simultaneous stationarity gives

\[
p^{-2a}\omega(X)=\omega(X),
\qquad
p^{2a}\omega(X)=\omega(X).
\]

Taking one positive `X` with `omega(X)>0` yields

\[
p^{-2a}=p^{2a}=1,
\qquad a=0.
\]

Thus one common faithful stationary state for the two reciprocal routes is
exactly the energy-cycle law.

## Doob normalization

Each branch can be made Markov separately by rescaling or a Doob transform.
For a scalar channel, divide the forward map by `p^(-2a)` and the reciprocal
map by `p^(2a)`. Both normalized maps become the identity for every `a`.

This does not prove confinement. The two transforms use different
normalizations and erase the relative modulus carrying the Haar residual. A
single common Doob weight normalizes both branches only if `a=0`.

Likewise, allowing separate stationary measures makes route equality
vacuous. The argument requires the same source-derived state and the same
normalization on both routes.

## Dilation boundary

A trace-preserving Stinespring dilation can absorb lost mass into an
environment. For an amplifying branch, a larger indefinite or nonunital
reservoir is needed. If separate reservoirs are allowed, both reciprocal maps
can be dilated without constraining `a`; the modulus difference is stored in
the environments.

Confinement follows only if the two dilations share one lossless reservoir and
the environment returns with zero net supply on the Xi cycle. That condition
is another form of the missing Haar energy equality.

## Existing Markov coherence

The repository's Markov fragment supplies complete higher coherence on
uniformly contractive typed paths. It does not provide a source-derived
cross-sector map placing the Evans/prime reciprocal channels in that fragment.
Assigning them Markov normalization independently would assume the contraction
condition being tested.

## Verdict for topology 17

Markov topology gives the clean probabilistic formulation:

> the Xi state is one faithful stationary state for both reciprocal prime
> routes.

This immediately implies the critical line. But separate Doob transforms,
stationary measures, or reservoirs trivialize the condition and lose the
physical relative modulus. A common source normalization is precisely the
terminal theorem, not a consequence of generic Markov completion.

The next nonredundant topology to test is an information-geometric topology
(relative entropy, Fisher metric, or data-processing order), where reciprocal
amplification might be excluded by monotonicity for one common state without
requiring literal trace preservation.