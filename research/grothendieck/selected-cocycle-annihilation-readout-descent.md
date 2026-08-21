# A selected cocycle can descend without a Betti homology map

Epistemic-graph event: 1339.

## Paired-readout theorem

Let `S_n:C_n(G)->C_n(H)` be a graded Betti candidate, not assumed to be a
chain map, and let `ell` be a target degree-`n` cocycle:

`ell D_H,n+1=0`.

The selected scalar readout `ell S_n` descends to a functional on
`H_n(C(G))` exactly when

`ell Omega_(n+1)=0`,

where `Omega_(n+1)=D_H,n+1 S_(n+1)-S_n D_G,n+1`.  Indeed,

`ell Omega_(n+1)=-ell S_n D_G,n+1`.

Thus the selected pairing is insensitive to source boundaries precisely
when the selected cocycle annihilates the next-degree boundary defect.
Neither `Omega=0` nor the existence of a full map `H_n(G)->H_n(H)` is
necessary.

## Strict separation from homology descent

Take a source complex with `C_1(G)=Z`, `C_0(G)=0`, and a target complex

`C_1(H)=Z^2 -> C_0(H)=Z`, `D_H=[1 0]`.

Let `S_1(1)=(1,1)` and choose `ell=[0 1]`.  The source generator is a cycle,
but its image is not: `D_H S_1(1)=1`.  Hence `S` does not induce a target
homology map.  Nevertheless `ell S_1(1)=1`, and there are no source
boundaries, so the nonzero scalar readout is perfectly well-defined on
source homology.

## Hierarchy

The physical conclusions therefore form a strict hierarchy:

1. `Omega=0`: strict relative-chain pushforward;
2. cycle/boundary conditions of Ledger 1318: induced homology map;
3. `ell Omega_(n+1)=0`: one selected scalar readout descends.

Each lower condition can survive failure of the condition above it.  The
third is the natural endpoint for a paired coefficient--Betti observable,
but it certifies only that selected observable.  It must not be promoted to
a physical Mackey correspondence.

## Five-site gate

Once the source-derived boundary packet exists, the frozen selector should
be tested directly against `Omega` before demanding full vanishing.  This
could admit a scalar cosmological readout even if the complete relative-chain
pushforward fails.  At present both `Omega` and this contraction remain
unavailable because the physical boundary matrices are missing.
