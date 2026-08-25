# Breit--Wheeler supplies an operation density before an instrument

Owner: `marici.Nima`

The normalized tree amplitude at a fixed pair momentum defines a source map

\[
A_x:H_{\gamma\gamma}\longrightarrow H_{e^+e^-}.
\]

For a measurable outcome bin (B) in pair phase space, the corresponding
quantum operation is

\[
\mathcal J_B(\rho)
=\int_B d\Phi_2\,A_x\rho A_x^\dagger .
\]

This map is completely positive without choosing a Lüders completion: its
Kraus density is the source amplitude itself.  Its effect is

\[
E_B=\mathcal J_B^*(I)
=\int_Bd\Phi_2\,A_x^\dagger A_x .
\]

The forward Cutkosky matrix is the same Gram object, up to the declared
unitarity factor (1/2).  Its positivity is therefore structural.

This does not yet give a physical instrument.  The phase-space integral is a
cross section, so it is dimensionful and need not obey

\[
\sum_B E_B\le I.
\]

To obtain exclusive probabilities and the complementary no-event operation,
the source must additionally supply a normalized incoming wavepacket,
luminosity/exposure, and the corresponding finite-time scattering channel.
Only then can one define

\[
E_\varnothing=I-\sum_BE_B
\]

and test complete positivity of the no-event branch.

The nonforward kernel has a different type.  It compares two distinct
outgoing angular fibers,

\[
K(x,x')=A_{x'}^\dagger A_x,
\]

and is not an effect unless (x=x').  Its phase-sensitive content is
transport/coherence data, not another outcome probability.

At the real planar sample the comparison matrix happens to be Hermitian and
positive.  That does not change its type: positivity is a property of its
chosen numerical presentation, whereas an effect must be an endomorphism of
one outcome fiber.  This is a useful hostile case against typing by matrix
inequalities alone.

## Consequence

Scattering is closer to a source-derived instrument than the earlier census
stated:

\[
\text{source amplitude}
\to
\text{CP operation density}
\to
\text{effect density and Cut pairing}.
\]

Its first missing arrow is now precisely typed:

\[
\text{operation density}
\not\Rightarrow
\text{normalized exclusive instrument}.
\]

The next admissible construction is a finite wavepacket/exposure packet with
an explicit no-scattering channel.  Choosing a Lüders update from the effect
alone would erase the source pair state and is not allowed.

## Falsifiers

- A forward bin gives a non-positive helicity Gram matrix.
- The nonforward cross-angle kernel is treated as a positive effect.
- A trace-preserving instrument is claimed without a dimensionless exposure
  normalization and no-event branch.
- Two amplitudes with the same effects but different outgoing pair states are
  assigned the same source operation.
