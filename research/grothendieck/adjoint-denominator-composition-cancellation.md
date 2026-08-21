# Adjoint denominators are submultiplicative but can cancel in a composite

Epistemic-graph event: 1355.

## Composition theorem

For composable rationally nondegenerate pairing data, uniqueness of adjoints
gives

`S_(r q)=S_r S_q`.

Let `L_q,L_r,L_(r q)` be the least positive denominator-clearing integers of
the three adjoint matrices.  Since `L_q S_q` and `L_r S_r` are integral,

`L_q L_r S_(r q)`

is integral.  Therefore

`L_(r q) divides L_q L_r`,

and the localization-prime support of the composite is contained in the
union of the two stage supports.

Equality need not hold.  Matrix multiplication can cancel denominators, so
an integral composite does not imply integral stage adjoints.

## Small consistent cancellation

Take rank-one pairing lattices

`P_G=[2]`, `P_H=[3]`, `P_J=[2]`

and identity coefficient pullbacks at both stages.  Adjunction forces

`S_q=2/3`, `S_r=3/2`, but `S_(r q)=1`.

Thus `L_q=3`, `L_r=2`, and `L_(r q)=1`.  The terminal transfer is integral
while neither stage is.

## Double blindness of terminal tests

Ledger 1317 showed that boundary defects can cancel in a composite.  This
result shows that pairing-lattice denominators can cancel independently.
Consequently a terminal multi-bit quotient can simultaneously hide
nonintegral intermediate adjoints and nonzero intermediate boundary defects.

Every one-bit five-site specialization must therefore publish and test its
own Smith adjunction data and its own `Omega`; terminal integrality and
terminal chain compatibility are only consistency checks.
