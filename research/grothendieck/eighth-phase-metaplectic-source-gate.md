# The missing one-eighth is archimedean and not supplied by pi_0 symmetry

Epistemic-graph event: 1400.

## Exact source of the smooth constant

Define the Riemann--Siegel phase

`vartheta(t)=Im log Gamma(1/4+i t/2)-(t/2)log pi`.

Stirling expansion gives

`vartheta(t)=t/2 log(t/(2 pi))-t/2-pi/8+1/(48t)+O(t^(-3))`.

The smooth zero count is `vartheta(t)/pi+1`, hence

`N_smooth(t)=t/(2 pi)log(t/(2 pi))-t/(2 pi)+7/8`

` +1/(48 pi t)+O(t^(-3))`.

Ledger 1370's raw phase volume has constant `1`.  The entire constant defect
is therefore the archimedean phase

`(-pi/8)/pi=-1/8`.

## Metaplectic temptation

A quarter rotation of a symplectic plane has an order-eight metaplectic lift,
so the source `D4` quarter rotation appears at first to be a possible origin
of an eighth phase.

That inference fails on the conditional rank-one arithmetic object.  Every
mapping-class automorphism of the connected generator preserves its component
class `U`; therefore the full `D4` action on

`L=Gr(pi_0)`

is the identity.  Its dual action on `L_dual` is also identity, so its image
in the symplectic group of `L direct_sum L_dual` is trivial.  The metaplectic
preimage of the identity supplies at most the central sign, not a canonical
quarter-rotation phase.

Thus the source `D4` symmetry does not derive the missing `-pi/8` on the
rank-one phase plane.  Importing the gamma phase repairs the count but remains
the archimedean input already isolated in Ledger 1362.

## Remaining route

A nontrivial metaplectic correction would require a source action on a richer
coefficient--Betti symplectic fiber that:

1. descends to the selected physical quotient;
2. contains a canonical symplectic quarter rotation rather than a relabeling;
3. fixes a metaplectic lift and half-form line; and
4. yields the gamma phase without consulting `Gamma`, `xi`, or zero counts.

No admitted object currently satisfies these requirements.

## Scope

This is an exact constant-term and representation-typing audit.  It does not
exclude a metaplectic correction on a future higher-rank physical fiber.
