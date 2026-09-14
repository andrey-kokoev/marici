# A dual-rail encoder exposes coherent null-sector leakage

## Question

Can the channel distinguish coherent superpositions of conductor classes without relying on a number-nonconserving single-rail phase reference?

## Claim boundary

This constructs a number-conserving four-mode code and logical tomography observables. It is an alternative to the three-mode single-rail implementation, not evidence that the physical source prepares the code.

## Dual-rail code

Encode one logical bit by

\[
|0\rangle_L=|1,0\rangle,
\qquad
|1\rangle_L=|0,1\rangle.
\]

For the two syndrome bits define

\[
\mathcal E_D(a,b)
=|1-a,a,1-b,b\rangle.
\]

Every codeword has exactly two photons, one in each rail pair. The four codewords are orthonormal, and linear extension is an isometry from \(\mathbb C[(\mathbb Z/2)^2]\).

## Logical observables

On each single-photon rail pair,

\[
Z_L=N_0-N_1
\]

has eigenvalue \((-1)^a\). Number-resolving detection therefore recovers the same two conductor syndrome bits.

The number-conserving operator

\[
X_L=a_0^\dagger a_1+a_1^\dagger a_0
\]

acts as logical Pauli \(X\) on the code. A balanced beam splitter diagonalizes this operator, so output-port number detection measures \(X_L\).

Adding a relative \(\pi/2\) rail phase before the balanced beam splitter measures logical \(Y\). Separate \(Z\), \(X\), and \(Y\) settings therefore determine the one-bit coherence; their tensor-product settings distinguish two-bit coherent states from diagonal mixtures.

## Site exchange

Exchanging the two rail pairs sends

\[
\mathcal E_D(a,b)\longmapsto\mathcal E_D(b,a)
\]

and swaps the two logical observable triples. Total photon number remains two.

## Relation to the null state

The trivial syndrome is

\[
(0,0)\longmapsto|1,0,1,0\rangle,
\]

not the vacuum. Thus “null syndrome” is representation-independent: it means the identity class in the conductor quotient, not necessarily zero occupation.

## Cost and gate

The construction uses four modes and two photons instead of the single-rail three-mode section. Its benefit is number conservation and phase-sensitive logical tomography using passive linear optics plus number detection.

Physical promotion requires preparation of one photon in each rail pair, calibrated beam-splitter phases, mode-resolved detection, and a source-derived identification of the conductor syndrome with the logical rails.

## Disposition

A number-conserving, site-equivariant encoder and coherence-sensitive readout exist algebraically. The prior claim that diagonal counting cannot distinguish coherence remains correct for the single measurement setting; the dual-rail construction supplies the missing complementary settings rather than extracting phase from diagonal counts alone.
