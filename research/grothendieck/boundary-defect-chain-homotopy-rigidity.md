# The boundary defect is invariant under chain-homotopy changes

Epistemic-graph event: 1344.

## Rigidity theorem

Let `S:C(G)->C(H)` be a graded map with

`Omega=D_H S-S D_G`.

For any degree-raising map `K`, make the ordinary chain-homotopy change

`S'=S+D_H K+K D_G`.

Then

`D_H S'-S'D_G=Omega`.

All correction terms cancel because `D_H^2=D_G^2=0`.  Thus the boundary
commutator is constant on the entire chain-homotopy class of `S`.  A nonzero
defect cannot be repaired by changing representatives within that class.

## Selected readout invariance

If `ell` is a target cocycle and `x` a source cycle, then

`ell S'x=ell Sx`.

Indeed, `ell D_H Kx=0` and `ell K D_Gx=0`.  Hence the scalar readout on
cycles is also chain-homotopy invariant whenever defined.  This matches the
rigidity of the anomaly tests in Ledgers 1323--1325.

## What a repair would require

An actual repair must replace `S` by `S+C` with

`D_H C-C D_G=-Omega`.

Such a correction is not an ordinary chain-homotopy adjustment.  In the
paired lane, perfect-pairing uniqueness already fixes `S` degreewise, so a
nonzero `C` generally changes the adjunction or the frozen generator
pairings.  It therefore requires new physical data, not a regulator
reparametrization disguised as homotopy.

## Five-site consequence

If the eventual source-derived five-site matrices produce nonzero `Omega`,
endpoint or overlap homotopies cannot erase it while retaining the same
forced Betti map.  They may prove equality between presentations, but the
commutator itself is presentation- and homotopy-rigid.
