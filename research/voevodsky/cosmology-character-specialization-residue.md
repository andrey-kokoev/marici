# Character-specialization residue

## Question

Does the singular specialization of twisted coefficients contain new information beyond the existing unit obstruction?

## Claim boundary

No. Near the trivial character, set `x=a-1` and `y=b-1`. These form a regular sequence. The top Koszul cokernel is `R/(x,y)`, of length one, and the normalized local residue is

`Res dx wedge dy/(x y)=1`.

Successive connecting maps in the `x` and `y` directions produce this unit top class; reversing their order changes the sign. The same unit and sign law already occur in double logarithmic monodromy, the normalized torus period, ordered Parshin residues, and the primitive triangle orientation.

This is a codimension-two, double-connecting residue. It reconstructs the degree-two obstruction and cannot be replaced by one regular degree-one precycle at the trivial character.

## Disposition

Character specialization supplies no independent filler datum. The next leaf unifies the algebraic, Betti, Deligne, character, and incidence realizations and freezes the remaining source boundary.

## Verification

- `research/voevodsky/check_cosmology_character_specialization_residue.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
