# Multifrequency KMS coherence instrument

Owner: `marici.Aspect`

Strength: finite-frequency KMS coherence theorem.

## Bounded question

Can individually valid thermal sideband records at several frequencies be
assembled into one common-temperature bath, or is an additional coherence law
required across frequency bins?

## Source, frame, and ports

The source is three oscillator transitions at frequency labels 1, 2, and 3,
declared to share one thermal parameter \(q\). Each transition has separate
upward and downward Markov ports. The detector uses calibrated sideband
asymmetry in every bin. Frequency units, sideband ordering, bandwidth, gain,
and the common reference clock are fixed before the ratios are compared.

Constructor order is: declare the common bath parameter, generate each
frequency-labelled rate pair, measure both sidebands, form each ratio, then
test cross-frequency coherence. Independent per-bin fitting is a different
source constructor.

## Finite coherence law

For integer frequency label \(j\), common-temperature detailed balance gives

\[
R_j=\frac{\Gamma_{\uparrow,j}}{\Gamma_{\downarrow,j}}=q^j.
\]

With \(q=1/2\), the exact ratio packet is \((1/2,1/4,1/8)\). It obeys

\[
R_2=R_1^2,\qquad R_3=R_1^3=R_1R_2.
\]

These are coherence cells across detector bins. Positivity and stability of
each rate pair do not imply them.

## Smallest locally valid hostile

The packet \((1/2,1/3,1/8)\) preserves the first and third ratios and admits
positive stable upward/downward rates in every bin. Nevertheless it has
nonzero residuals against the common-parameter laws. It is therefore three
locally thermal-looking records without one global thermal source.

This parallels a general completion warning: compatible finite pieces do not
automatically descend from one global trivialization. The common parameter is
reconstructed from the fundamental ratio only after the cross-frequency
coherence tests pass.

## Conservation and detector boundary

Each complete oscillator-bath channel preserves its canonical commutator and
has positive record probabilities. The sideband instrument identifies rate
ratios; it does not select a temperature or prove that all transitions share
one bath. That sharing is source authority.

## Completion gate

Three integer frequencies give a finite coherence theorem, not an unbounded
KMS condition. Completion requires arbitrary-frequency detailed balance,
analytic continuation in a thermal strip, continuum convergence independent
of bin exhaustion, and a microscopic bath coupling. No finite sideband packet
alone supplies those claims.

Run:

```powershell
python research/aspect/checkers/multifrequency_kms_coherence_instrument.py
```
