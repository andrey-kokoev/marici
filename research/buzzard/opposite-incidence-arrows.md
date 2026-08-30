# Opposite incidence arrows packet

## Grothendieck source

This formalizes the finite directional core of
`research/grothendieck/theta-direct-and-dual-tail-systems-carry-opposite-incidence-arrows.md`.

## Formal objects

- `directTailGenerator p` is the upper-triangular forcing-to-endpoint block.
- `dualTailGenerator p` is its transpose and carries the reverse block.
- both generators square to zero.
- `manually_identified_sum_is_bidirectional` shows what happens only after
  placing both matrices on one carrier by hand.
- `TailLocus` distinguishes all four direct/dual endpoint/forcing loci.
- the direct and dual arrows are not composable at those types.
- `reciprocalEndpointSewing` is the smallest explicit arrow that makes their
  chain composable.
- an endpoint observation row retains coefficient one but does not alter the
  missing reverse generator block.

## Assumptions and coefficient types

The matrix identities hold over an arbitrary commutative ring. Directional
typing is finite and coefficient-free.

## Missing interfaces and hostile boundary

The file does not assert that `reciprocalEndpointSewing` exists analytically;
it only types what such a constructor must connect. Fourier--Tate duality must
supply a bounded comparison on the completed carriers before the opposite
arrows can define one boundary-current system. Adding the matrices after an
unjustified carrier identification is the hostile shortcut.

Reachability, observability, and Clark endpoint sensing do not imply dynamic
bidirectionality. Tail decay also blocks a cutoff-uniform pointwise lower
bound; an accumulated Gramian or sewing estimate is still needed. No mixed
supply identity, zero orientation, or RH result is asserted.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
