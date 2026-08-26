# Minimal two-path interferometer

Owner: `marici.Aspect`

## Bounded question

Can a two-path interferometer be factored from source preparation through
ordered propagation, phase calibration, recombination, loss, and detector
projection without identifying a dark detector amplitude with annihilation of
the pre-readout route state?

## Typed factorization

The source prepares one normalized input mode. The first balanced splitter
embeds it into the ordered route space with basis `(upper, lower)`. Propagation
is diagonal in that route basis. A calibrated relative phase is attached to
the lower route only after the path convention and reference arm have been
fixed. The second splitter recombines routes into the ordered detector ports
`(bright, dark)`. Detection is a final coordinate projection, not an inverse
claim about the route state.

With the real Hadamard convention, the internal state after the first splitter
is `(1, 1)/sqrt(2)`. A relative phase `phi` gives
`(1, exp(i phi))/sqrt(2)`. Recombination yields detector amplitudes
`((1 + exp(i phi))/2, (1 - exp(i phi))/2)`. At `phi = 0`, the dark amplitude is
zero while the route-state norm immediately before recombination is one.

Constructor order is part of the type. A phase shifter on a named route and a
splitter generally do not commute. Moving the phase across the splitter
without transporting its basis changes the apparatus.

## Loss completion

Attenuation on one route is not a two-route unitary. It is represented by an
isometry into an enlarged space containing an environmental loss port. The
detector probabilities may sum to less than one only after that environment
is omitted from the readout. The full enlarged state retains unit norm.

## Smallest hostile falsifiers

1. Dark-port erasure: assert that zero dark amplitude makes the internal
   route vector zero. The checker requires internal norm one and therefore
   rejects the assertion.
2. Order erasure: commute a nontrivial route phase through the balanced
   splitter without a basis transport. The checker records a nonzero matrix
   commutator.
3. Loss erasure: attenuate a route but omit the environmental port while
   claiming closed norm preservation. The checker records the missing norm as
   the environmental probability.

## Claim boundary

This is a finite-dimensional, monochromatic, perfectly calibrated apparatus
model. It does not establish polarization transport, temporal coherence,
continuum-mode completion, detector back-action, nonreciprocity, or cavity
feedback. Those require successor packets.

## Verification

Run:

`python research/aspect/checkers/minimal_two_path_interferometer.py`

The checker is dependency-free and writes
`research/aspect/results/minimal_two_path_interferometer.json`.
