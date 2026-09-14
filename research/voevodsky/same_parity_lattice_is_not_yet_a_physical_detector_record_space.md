# The same-parity lattice is not yet a physical detector record space

## Question

Do Aspect's detector packets authorize interpreting the repaired same-parity lattice as the actual physical record space?

## Claim boundary

This tests compatibility with existing Aspect detector semantics without changing Aspect-owned artifacts. It does not rule out an apparatus specifically engineered to encode the same-parity lattice.

## Two distinct readout types

The relative Čech–de Rham contract uses the linear map

\[
(a,b)\longmapsto(a-b,a+b).
\]

Its outputs are algebraic dark-port and complementary phase-sensitive coordinates. The contract is explicitly a simulation-only structural classifier.

Aspect's calibrated photon-counting packet instead defines physical records through POVM effects and count probabilities. Number-resolving records are nonnegative count labels; efficiency produces a binomial distribution, dark counts convolve the distribution, and phase-sensitive recovery requires a local oscillator or another coherent phase reference.

These are different typed maps:

\[
\text{route coefficients}\longrightarrow\text{linear amplitude coordinates}
\]

versus

\[
\text{quantum state}\longrightarrow\text{probability distribution on count records}.
\]

No existing arrow identifies them.

## Same-parity restriction

The algebraic image lattice

\[
L_{\rm rec}=\{(u,v)\in\mathbb Z^2:u=v\pmod2\}
\]

excludes the elementary records

\[
(1,0),\qquad(0,1).
\]

The photon-counting packet explicitly treats these ordered pairs as admissible records in two resolved bins, although those bins are temporal rather than the two algebraic output coordinates. Therefore standard resolved counting does not impose same parity merely from having two channels.

Transporting that observation from time bins to dark/complementary ports would require a detector-mode map. Without it, the examples are a falsifier of automatic parity authority, not a contradiction.

## Phase-sensitive apparatus status

The connected-route coherent-control packet records ideal deterministic means of control \(X\) and \(Y\), not raw detector counts. It requires any physical packet to replace those means with trial counts while retaining route, compiler, phase, bypass, environment, and reset fields.

Thus the available phase-sensitive object is not yet a physical record lattice. A local oscillator, calibration, and stochastic observation model must intervene before integer-lattice claims can be tested.

## Consequence

Typing the codomain as \(L_{\rm rec}\) repairs the abstract linear map, but cannot be promoted to detector semantics. The physical alternatives are:

1. derive an encoder whose allowed joint records genuinely satisfy equal parity;
2. treat \((a-b,a+b)\) as calibrated real-valued estimators reconstructed from many trials rather than individual integer records;
3. use two wall-labelled raw count channels and postpone linear aggregation until after the parity-sensitive source test.

Only the first alternative would make \(L_{\rm rec}\) the literal record lattice.

## Disposition

No current Aspect artifact authorizes the same-parity lattice as a physical detector record space. The strongest supported reading of the complementary readout is a characteristic-zero structural or estimator map. Raw-trial and detector-mode maps remain missing.
