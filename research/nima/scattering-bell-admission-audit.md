# Scattering-to-Bell admission audit

## Question

Do the admitted scattering objects already define a minimal Bell experiment,
or do they merely provide the amplitude-level ingredients from which one
could build one after adding physical detector data?

## Strongest existing packet

Entries 42, 45, 53, and 54 establish four relevant structures:

1. multilinearity in external polarization data;
2. Ward reduction to physical polarization classes;
3. factorization under a physical cut;
4. coherent closure of two open polarization pairs by metric trace.

This is enough to type a candidate bipartite amplitude.  It is not yet enough
to type a Bell probability table.

## The first missing map

For settings \(x,y\) and outcomes \(a,b\), Bell requires a positive normalized
readout such as

\[
P(a,b\mid x,y)
=
\operatorname{Tr}\!\left[
\rho\,(E^A_{a\mid x}\otimes E^B_{b\mid y})
\right],
\qquad
\sum_a E^A_{a\mid x}=1,
\quad
\sum_b E^B_{b\mid y}=1.
\]

Nothing in the admitted scattering packet declares \(\rho\), the four local
instruments, their exclusive effects, or the amplitude--conjugate-amplitude
pairing and phase-space normalization that would realize this formula.
External polarization vectors are state/amplitude inputs; changing them is not
automatically a local detector choice.  The transmutation trace is an
amplitude counit; it is not a binary measurement outcome.

## Result

The bounded gate vector is

\[
(1,0,0,0,0,0),
\]

for bipartite kinematics, local settings/outcomes, normalized probabilities,
no-signalling, CHSH survival, and Tsirelson respectively.  The first failure is
therefore the detector-instrument gate, before any numerical Bell inequality
is meaningful.

This is a useful localization, not a negative verdict on scattering.  The
amplitude/cut packet supplies the process kernel.  The missing object is the
sector-specific experimental lens-plus-readout: a polarized preparation,
local analyzers, exclusive outcomes, and a positive normalized pairing.

## Next bounded construction

Locate or construct one source-derived polarized \(2\to2\) packet with:

1. a normalized incoming preparation;
2. two analyzer settings on each outgoing wing;
3. two exhaustive outcomes for each analyzer;
4. a conjugate-amplitude and phase-space readout;
5. independence of each marginal from the remote setting.

Only after those checks pass should the CHSH correlators be formed.  This
prevents the Carrier's polarization grammar from being mistaken for an
already physical measurement protocol.
