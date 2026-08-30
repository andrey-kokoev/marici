# Flat-comb completion escape

## Hostile cutoff sequence

At every finite label cutoff, the normalized augmentation comb and the
control pulse have a well-conditioned rank-two Gram matrix. That does not make
them a compatible pair of state vectors in the completion.

Embed the `N`-label flat comb into an `M`-label space by zero padding. For
`N<=M`, their overlap is

`sqrt(N/M)`.

Hence

`||omega_N-omega_M||^2 = 2-2 sqrt(N/M)`.

Taking `M=4N` makes this distance squared equal to one at every scale. The
flat comb is not Cauchy in the square Hilbert grade.

The failure is stronger in the primitive rigging. At weight `delta=1/2`, the
squared primitive norm of the normalized first-`N` prime comb grows at least
as `(N+1)/2`. It therefore cannot define a test state in any positive
primitive grade.

## Retyping

The control pulse `e_0` is cutoff-compatible. The augmentation comb is not.
Its infinite object is the augmentation row, which Grothendieck has already
placed in the continuous dual of the rapid-decay arithmetic test space.

Therefore the finite graph--anti-graph calculation remains correct at each
cutoff, but its second anchor cannot be promoted to a state-valued normal
frame. The completed seam must be a rigged state--covector graph or another
typed correspondence, not an ordinary two-state normal bundle.

## Optical falsifier

Prepare normalized flat combs at cutoffs `N` and `M` and measure their coherent
overlap. The exact source prediction is `sqrt(N/M)`. In particular, quadrupling
the cutoff must give overlap one half and fixed distance one.

This is an unusually useful failure signal: the apparatus can demonstrate
directly why every finite rank test passes while the proposed state completion
does not exist.

## Correction to earlier interpretation

The uniform finite Gram floor proves only finite separation. It does not
remove completion escape as a possibility. The finite anti-graph normal is an
exact diagnostic packet, but the completed augmentation direction must be
represented in the dual.

## Next constructor

Construct a rigged seam correspondence pairing the compatible control state
with the augmentation current, and test whether the sewing involution extends
as an adjoint mate between state and dual grades. That is the correctly typed
replacement for a two-state normal bundle.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_flat_comb_completion_escape.py
```
