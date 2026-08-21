# The forced Betti map has one remaining boundary commutator

## Obstruction theorem

Under the perfect-pairing hypotheses of Ledger 1312, let `S_q` be the unique
adjoint candidate for Betti pushforward. Define

`Omega_q=partial_H S_q-S_q partial_G`.

Then `S_q` is a map of relative-chain complexes if and only if `Omega_q=0`.
There is no remaining normalization freedom: a nonzero `Omega_q` is the exact
existence obstruction for the forced candidate.

If the chain-level pairings satisfy Stokes adjointness, transposition gives

`Omega_q^T=q^* d_H-d_G q^*`,

up to the fixed grading sign convention. Thus the Betti boundary square is
equivalent to the coefficient pullback being a cochain map at the actual
complex level. A degree-zero deck-label calculation alone cannot establish
this.

## Smallest hostile matrix

For the forced `C4->C2` basis map, identity differentials give `Omega=0`.
A source differential supported only on the even-labelled basis directions,
against the identity target differential, gives

`Omega=[[0,0,0,0],[0,1,0,1]]`.

The generator assignment and pairing adjointness remain fixed, but the map is
not a chain map. The checker verifies that the coefficient commutator is the
transpose of this defect.

## Physical test now required

For the five-site branch quotient, the next admissible calculation is exactly
to construct the actual relative boundary matrices and evaluate `Omega_q`.
Without those matrices, the physical map remains unavailable rather than
false.
