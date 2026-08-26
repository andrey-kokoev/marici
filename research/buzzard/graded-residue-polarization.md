# Graded residue polarization packet

## Grothendieck source

This formalizes the local convention-fixed theorem in
`research/grothendieck/graded-residue-jet-polarization.md`.

## Formal objects

- `Fin m` indexes the jet basis `e_0,...,e_(m-1)`.
- `residueJetForm uInv` pairs complementary degrees through `Fin.rev`.
- `degreeReverse u` is the source-defined reversal scaled by the leading
  coefficient.
- `polarizedJetForm` is multiplicity times the residue pairing after degree
  reversal.
- `polarizedJetForm_eq_scaled_dot` proves exact cancellation of `u^(-1)u`
  and gives `m` times the ordinary coordinate pairing.
- the real nonnegative and positive theorems establish positive definiteness
  for `m>0` and a nonzero jet vector.

## Assumptions and coefficient types

The algebraic identity holds over an arbitrary field with `u != 0`.
Positivity is stated separately over the real numbers. This preserves the
distinction between coefficient cancellation and ordered-field positivity.

## Hostile and global gate

`imaginary_scalar_not_conjugation_fixed` records the smallest nonreal
obstruction: a nonreal scalar cannot be a one-dimensional self-adjoint
eigenvalue. Local degree reversal does not change that scalar.

The global direct sum, density of the original Mellin test-family image,
compact resolvent, Hilbert--Schmidt inverse, regularized determinant, and the
claim that every source zero is real remain outside this theorem. The final
self-adjoint boundary is conditional on the RH-equivalent reality premise;
that premise is not assumed to manufacture an unconditional conclusion.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
