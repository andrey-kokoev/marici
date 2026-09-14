# Two pairwise photon parities realize the complementary syndrome probe

## Question

Can Aspect's existing number-resolving detector semantics realize the two binary wall syndromes without requiring same-parity raw count records?

## Claim boundary

This constructs observables on three labelled count channels. It does not identify those channels with the three conductor lattice coordinates or supply physical acquisition data.

## Number-resolving record space

Let a raw three-channel record be

\[
n=(n_1,n_2,n_3)\in\mathbb N^3.
\]

Define pairwise parity observables

\[
O_1(n)=(-1)^{n_1+n_3},
\qquad
O_2(n)=(-1)^{n_2+n_3}.
\]

Their binary syndrome values are

\[
s_i(n)=\frac{1-O_i(n)}2\in\{0,1\}.
\]

Equivalently,

\[
s(n)=
\bigl(n_1+n_3,\ n_2+n_3\bigr)\pmod2.
\]

These are exactly the conductor characters

\[
\ell_1=(1,0,1),
\qquad
\ell_2=(0,1,1).
\]

## Detector effects

For ideal number-resolving detectors, each count triple has the joint projector

\[
\Pi_n=|n_1,n_2,n_3\rangle\langle n_1,n_2,n_3|.
\]

The four syndrome effects are

\[
E_{ab}=
\sum_{s(n)=(a,b)}\Pi_n,
\qquad(a,b)\in(\mathbb Z/2)^2.
\]

They are positive, mutually orthogonal, and sum to the identity on the declared three-mode Fock space. Thus the syndrome pair is an ordinary coarse-graining of number-resolving photon counts.

## Faithfulness on the conductor quotient

For integer conductor coordinates \(v\in\mathbb Z^3\), the same formula has kernel equal to \(\operatorname{im}J\). Hence it descends to an isomorphism

\[
\operatorname{coker}J\xrightarrow{\sim}(\mathbb Z/2)^2.
\]

The two photon-parity outputs therefore implement the minimal complementary probe if a source-derived encoder identifies the conductor coordinates with the three count-channel occupation coordinates modulo two.

## Site exchange

Exchanging detector channels one and two fixes channel three and swaps

\[
O_1\leftrightarrow O_2.
\]

This matches the conductor site exchange and removes the prior identity-versus-swap ambiguity once hardware channel labels are fixed.

## Noise and calibration

Finite efficiency and dark counts do not preserve raw parity deterministically. They define a stochastic response matrix from source occupations to measured syndromes. The response must be calibrated and shown invertible on the declared finite photon-number class before inferred parities can be treated as estimators of the source syndromes.

No same-parity constraint is imposed on raw records. Records \((1,0,0)\) and \((0,1,0)\) are admissible and yield distinct syndromes.

## Disposition

The two complementary binary observables now have a standard physical detector realization as pairwise photon-count parities. The remaining missing arrow is an encoder from the three conductor coordinates to three labelled optical occupation channels, followed by detector-response calibration and raw data.
