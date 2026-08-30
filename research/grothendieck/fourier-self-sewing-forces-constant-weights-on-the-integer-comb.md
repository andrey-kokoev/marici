# Fourier self-sewing forces constant weights on the integer comb

## Weighted hostile family

Consider a tempered measure supported on the fixed integer lattice,

\[
\mu_w=\sum_{n\in\mathbb Z}w_n\delta_n,
\]

where the weights have at most polynomial growth. This preserves the support
selected by the affine-lattice theorem while altering the label-amplitude
channel.

Because every support point is integral, its Fourier transform is
1-periodic:

\[
\widehat\mu_w(\xi+1)=\widehat\mu_w(\xi).
\]

This statement is distributional and requires no convergence of the formal
Fourier series as an ordinary function.

## Same-object eigenmeasure rigidity

Assume the weighted comb closes on itself under Fourier transport:

\[
\widehat\mu_w=\lambda\mu_w,
\qquad \lambda\neq0.
\]

Since the left-hand side is 1-periodic, so is \(\mu_w\). Translation by one
acts on its atoms as

\[
\tau_1\mu_w
=\sum_{n\in\mathbb Z}w_n\delta_{n+1}
=\sum_{n\in\mathbb Z}w_{n-1}\delta_n.
\]

Equality with \(\mu_w\) forces

\[
w_{n-1}=w_n
\]

for every integer (n). Hence (w_n=c) is constant and

\[
\mu_w=c\Delta_{\mathbb Z}.
\]

The ordinary comb is Fourier-fixed, so any nonzero constant solution has
eigenphase \(\lambda=1\). There is no nonconstant same-support Fourier
eigenmeasure in this class.

## Where nonconstant weights go

Nonconstant periodic weights do not disappear; they create additional dual
support. For example, weights of period (q) decompose into characters of
\(\mathbb Z/q\mathbb Z\), and Fourier transport produces a union of rational
cosets in \(q^{-1}\mathbb Z\).

Thus a weighted comb can remain Fourier-closed only after enlarging its type
to include multiple support cosets and their finite Fourier-transform matrix.
It is not a scalar deformation of the original one-port comb.

This is the amplitude analogue of the shift theorem:

- a spatial shift becomes a dual character;
- a weight character becomes a dual spatial coset.

Position and amplitude are reciprocal comparison towers.

## Completion fixes the remaining scalar

Fourier self-sewing determines the weights only up to the common scalar (c).
The original theta constructor fixes (c=1) through its unit multiplicity at
every integer label. The same normalization is detected by the Haar
comparison: changing (c) changes the continuum asymptotics and destroys the
exact cancellation with the fixed completion carrier.

Hence support coherence, amplitude coherence, and boundary normalization
together select

\[
\Delta_{\mathbb Z}=\sum_{n\in\mathbb Z}\delta_n
\]

without fitting any zero data.

## Source-rigidity consequence

Combining the affine and weighted classifications gives:

> Among tempered measures consisting of one affine lattice with scalar atom
> weights and closing on the same labelled object under Fourier transport,
> the completed source is uniquely the unit-weight integer comb, up to the
> scalar already fixed by the boundary carrier.

This is a substantial canonical-source theorem. It rules out shifts, scale
changes, and nonconstant label amplitudes before scalar aggregation.

It still does not prove RH. The unique canonical comb can possess a completed
scalar section with zeros, and source uniqueness alone does not locate them.
The remaining force must concern the transform of the canonical
quantization-current packet, not the admissibility of alternative one-comb
sources.

## Next hostile class

The smallest surviving extension is a finite union of rational cosets with a
finite Fourier matrix. This is the first setting in which nonconstant weights
and displaced supports close together under Fourier transport.

The next audit should classify its irreducible Fourier eigenpackets and ask
which admit:

- positive one-sided quantization currents;
- the same scalar completion boundary;
- no extra character or coset readout;
- an off-seam completed zero.

If every nontrivial packet exposes an additional finite port, then the scalar
integer theta source is isolated within the entire finite-coset category.

## Operator stimulus

The operator asked whether another comparison channel was missing. Weighted
combs show that label amplitude is such a channel: Fourier transport exchanges
amplitude characters with spatial cosets. Treating them as one scalar source
would erase precisely the port that distinguishes a hostile weighted comb.
