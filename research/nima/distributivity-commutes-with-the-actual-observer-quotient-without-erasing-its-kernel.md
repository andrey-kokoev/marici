# Distributivity commutes with the actual observer quotient without erasing its kernel

## Result

The oppositely directed source presentations are now tested through the actual seven-reading to two-vacuum comparison, not merely through arbitrary coordinate frames.

The bridge preserves:

- all seven physical-row values;
- the two retained vacuum values;
- the five actual residual coordinates;
- the complete affine source fibers;
- the depth-compatible coarse tower;
- the conditional inverse on the admitted reachable history.

It does **not** make the ambient noninvertible observer invertible. Its kernel still has dimension five and inherited dimensions `(5,2,0)`.

The owning comparison is `../voevodsky/an-actual-noninvertible-observer-square-preserves-fibers-and-history-relative-retention.md`.

## 1. Two presentations of the declared source

The source is the seven-dimensional ideal slice of the forgotten cube. Path coordinates are

`u=(a1,...,a7)`, with `a0=-sum u`.

Interaction coordinates are the seven nonempty moments m. They are coefficients of ordered P/H products, with **H=Q-P**. Let

`m=Z u`, `u=X m`, `XZ=ZX=identity`.

These are inverse coordinate maps on the stated source domain. They are not an exchange of addition and multiplication, and neither map reconstructs arbitrary expression provenance.

The actual seven-reading matrix E is rebuilt using the independent ordered-cut recorder. Its interaction-coordinate version is `Em=EX`. If P selects the two vacuum readings, the quotient square is

`W=PE`, `Wm=WX`.

The checker verifies these as exact matrices, so the identities hold on the entire declared rational slice, not just the displayed fixtures.

## 2. Explicit AST transport through the receiver

The checker extends the typed rewrite rules with the definition

`H -> Q + (-1)*P`.

It normalizes each tested factor presentation by two different strategies, expands the corresponding P/Q path presentation, and compares their collected **ordered formal monomials**.

Every local step checks its rule and address, preserves typed endpoints, preserves the source value and interaction value, and is evaluated against all seven actual observer rows. The quotient and residual values are checked at the same step.

The run covers 1,437 local AST steps and 10,059 physical-row checks. The 15 source cases include the seven-dimensional path basis, five filtration-adapted kernel generators, zero, a mixed source and the pure cubic interaction.

A selected complete rewrite witness is serialized as an initial AST and a sequence of rule/address/hash records, then replayed. It does not store every intermediate before/after tree.

The opposite direction is tested independently: recover the interaction coordinates from the expanded path coefficients and construct the canonical P/H presentation. This does not rely on replaying an archived original AST. It recovers the canonical presentation, not an arbitrary original construction history.

These are explicit normalization tests, not a proof of unrestricted rewrite confluence.

## 3. The same residual, not merely the same visible answer

Use the owning filtered linear section S, kernel inclusion N and residual extraction R on the seven readings. Their checked identities include

`PS=identity`, `RN=identity`, `PN=0`, `RS=0`,

`SP+NR=identity`.

Consequently both source presentations give the same residual:

`REX m = REm m`.

The wire payload retains labelled vacuum values and all five residual values, bound to the reading model and section. Reconstructing the seven readings and invoking the standalone source decoder recovers all eight path coefficients. Fifteen serialized roundtrips pass.

Changing presentation does not permit forgetting a residual, changing the section silently, or replacing an unknown residual by zero.

## 4. Complete fibers agree

Let

`K=E^(-1)N`.

The columns of K span the actual five-dimensional quotient kernel in path coordinates; the same kernel is `ZK` in interaction coordinates.

For **any** vacuum pair c, the entire compatible source fiber is

`E^(-1)S c + K r`, for arbitrary `r in Q^5`.

Regrouping gives

`Z E^(-1)S c + ZK r`.

The matrix identities establish this parameterization for every c. Four exact rational affine-system comparisons additionally test the implementations. Filtration-adapted kernel sources are checked against the actual Fox vanishing orders, yielding `(5,2,0)`.

No preferred point of this fiber is asserted to be the unknown source.

## 5. Depth compatibility is conditional on descent

The coarse row-space intersections with jets of orders zero through three have dimensions

`(0,0,1,2)`.

At order two the available row is the **sum** of the canonical and reversed vacuum readings. The individual rows depend on the hidden cubic interaction.

The presentation bridge commutes with each of these actual coarse views. All ten depth-transition squares are checked, including

`(u,v) -> u+v`.

The pure top interaction has zero order-two jet and vacuum pair `(-1,1)`. The checker also solves the covector-factorization problem and verifies that neither individual vacuum row descends to order two. This is an obstruction, not a missing coordinate-change trick.

## 6. Reachable history supplies a different inverse contract

For the prescribed history, append **P-Q** in the second and third blocks. This sign convention is the negative of H above; two appended factors cancel those two signs.

The source map T20 satisfies

`W T20 = identity_2`,

and its image intersects K trivially. On this admitted history, the vacuum pair reconstructs the source. Actual marked-source multiplication verifies the history map.

In the owning illustrative section, the residual values on that history are forced to be

`(0,-u-v,0,u+v,0)`.

They are not generally zero. The history section differs from the illustrative section by exactly the corresponding kernel-valued map.

The test demonstrates three distinctions:

1. The same vacuum pair has distinct ambient ideal-source preimages.
2. The prescribed history picks a unique one, conditional on externally admitted dynamics and support.
3. Setting the illustrative section's residual to zero can select a different source with the same visible pair.

A history-only inverse is rejected unless its declared history contract is explicitly admitted by the caller. A matching digest binds the contract; it does not prove that the physical history occurred.

## Verification

`python research/nima/checkers/check_distributivity_with_actual_observer_quotient.py`

All checks pass. Missing residuals, untracked section changes and unadmitted history inversion are rejected. The actual matrices, residual data, history map and a replayable AST witness are exported to

`research/nima/results/distributivity-with-actual-observer-quotient.json`.

This is stronger than the earlier standalone distributivity experiment: it tests the bridge against a genuinely lossy, source-derived observer and its retention contract. It remains a finite exact-domain result, not a physical acquisition certificate, global source-bimodule splitting, or general AST confluence theorem.
