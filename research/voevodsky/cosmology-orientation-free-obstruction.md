# Orientation-free obstruction

## Question

What is canonical before choosing which primitive generator is positive?

## Claim boundary

The canonical object is the determinant line of the rank-two torus character lattice, with its Tate realization. It is a free rank-one integral lattice. Normalized de Rham classes, Betti top classes, Parshin cycles, and character residues give compatible integral realizations of this line. Milnor symbols do so after rationalization or projection to the regulator-visible quotient; integral monomial changes may add diagonal 2-torsion symbols, audited separately.

Its two primitive generators form a torsor under `{+1,-1}`. A signed generator is selected by any equivalent orientation datum: an ordered torus basis modulo `SL(2,Z)`, an oriented Betti torus, or a cyclic orientation of the boundary triangle.

A `GL(2,Z)` coordinate change acts on every signed realization by its determinant. Determinant-one changes preserve the generator; determinant-minus-one changes reverse it.

The horn obstruction uses only nonvanishing and primitivity, so it is independent of this sign choice. A signed physical value would require separate orientation authority.

## Disposition

The orientation-free result is the nonzero primitive determinant/Tate line. A numerical `+1` always means this line together with an explicit orientation. The next leaf verifies the determinant transformation law for general monomial coordinate changes across all faithful realizations.

## Verification

- `research/voevodsky/check_cosmology_orientation_free_obstruction.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
