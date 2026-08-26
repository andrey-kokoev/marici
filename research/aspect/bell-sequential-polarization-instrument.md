# Bell Correlations Need a Sequential Polarization Instrument

## Question

What is the smallest optical instrument extension of Nima's static Bell/Carrier table that types local records, conditional continuation, and the classical-comparison boundary without introducing signalling or a hidden pointer?

## Construction

Use a polarization-entangled photon pair in the singlet state. At Alice's port, a selectable polarizing analyzer implements the two-outcome Lüders instrument

\[
\mathcal I_{a,r}(\rho)=K_{a,r}\rho K_{a,r}^{\dagger},
\qquad
K_{a,r}=P_{a,r}\otimes I.
\]

The trace of the subnormalized state is the local record probability. Its normalized value, when nonzero, is the joint continuation state conditional on that record. The nonselective local operation is

\[
\mathcal E_a(\rho)=\sum_r\mathcal I_{a,r}(\rho).
\]

This is the missing type in a static state--effect table: an effect gives a probability, whereas an instrument also gives the continuation on which a later interaction acts.

## Exact finite audit

Take the two analyzer bases to be horizontal/vertical, denoted Z, and diagonal/antidiagonal, denoted X. The dependency-free checker verifies:

- the first Z record is unbiased;
- conditioned on Alice's Z record, Bob's same-basis record is opposite with probability one;
- without Alice's record, Bob's reduced state remains maximally mixed after Alice's nonselective Z measurement;
- Z followed by Z repeats the first record with probability one;
- Z followed by X followed by Z retains the first Z record with probability one half.

The last two statements distinguish an effect-only table from a continuation law. They witness local measurement disturbance but do not by themselves violate a temporal hidden-state model.

## Reconstruction and comparison boundary

One port can reconstruct its own instrument statistics by time-tagging its setting and record stream. It can estimate local probabilities, repeatability, and sequential disturbance. It cannot reconstruct the joint Bell correlators, infer the remote record on an individual trial, or distinguish the entangled source from a locally maximally mixed source using local data alone.

The joint law is reconstructed only after the two stations compare setting labels, record labels, trial identifiers, and clock-alignment metadata through an ordinary classical channel. Conditional remote predictions are retrospective subensemble statements defined by that comparison. They are not locally readable pointers and cannot carry a controllable signal.

## Cheapest optical realization

The minimal hostile experiment needs an entangled-pair source, fast selectable polarization analyzers at both ports, time-tagging detectors, and a classical coincidence join. The sequential extension adds a second analyzer at Alice's port, with a bypass choice implementing either Z--Z or Z--X--Z. A delayed-choice setting is useful for closing memory and setting-predictability loopholes, but it is not required for the finite typing calculation.

The decisive data products are kept separate:

1. Alice-local transition counts test the instrument continuation law.
2. Spacelike-separated four-context coincidence counts test Bell factorization.
3. Singles counts indexed by the remote setting test no-signalling.

No one of these substitutes for the other two.

## Hostile dispositions

A renamed hidden variable that supplies independently evaluable responses at both ports is still rejected by Nima's CHSH checker. A classical invasive local memory can reproduce the sequential disturbance test, so that test is not advertised as a Bell witness. Conversely, CHSH data without a typed update rule do not specify what survives into a later measurement. The useful extension is therefore compositional: Bell nonfactorization constrains the two-port joint law, while the sequential analyzer constrains local continuation.

Decoherence is typed as insertion of a channel between preparation and instrument. Complete dephasing in a named basis removes off-diagonal continuation terms in that basis; it is not merely a reduction in coincidence visibility. A future audit should vary a calibrated dephasing strength and test the same channel against local sequential transitions, joint correlators, and singles invariance.

## Claim boundary

This is a finite instrument-level construction for two polarization bases. It does not derive the Lüders rule from Carrier, select a measurement interpretation, exclude every contextual hidden-variable theory, or establish an unbounded compositional calculus.

## Verification

Run:

```text
python research/aspect/checkers/check_bell_sequential_polarization_instrument.py
```

The checker is dependency-free and uses exact rational matrix arithmetic.

The compositional checker additionally runs the optimal four-setting CHSH
experiment in exact arithmetic over \(\mathbb Q(\sqrt2)\):

```text
python research/aspect/checkers/check_combined_bell_instrument.py
```

It constructs every joint record as an instrument continuation, applies the
forget-continuation map by taking its trace, and verifies equality with the
static Bell table. It then checks normalization, no-signalling, all sixteen
deterministic Bell-local strategies, the CHSH bound, the singlet violation,
and the earlier sequential Z--Z and Z--X--Z transition probabilities in one
calculation.
