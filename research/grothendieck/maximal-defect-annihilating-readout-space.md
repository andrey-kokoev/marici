# Defect annihilation defines a maximal cocycle-level readout space

Epistemic-graph event: 1340.

## Maximality theorem

For a graded Betti candidate `S:C(G)->C(H)`, define

`A^n(S)={ell in Z^n(H) : ell Omega_(n+1)=0}`.

Then `A^n(S)` is the unique maximal linear subspace of target degree-`n`
cocycles whose pullbacks by `S_n` are source cocycles.  Equivalently,

`A^n(S)=Z^n(H) intersect ker(Omega_(n+1)^*)`.

Ledger 1323 gives the proof: for every target cocycle `ell`,

`d_G(S^*ell)=-ell Omega_(n+1)`.

Thus `S^*` restricts canonically to

`A^n(S) -> Z^n(G)`.

If `S` is a chain map, `A^n(S)=Z^n(H)`.  A nonzero defect can still leave a
large admissible readout space equal to its cocycle annihilator.

## Cohomology-representative anomaly

Without `Omega=0`, this construction need not descend from target cocycles
to target cohomology classes.  Adding an exact target cocycle can change both
admissibility and the induced source cohomology class.

For the target complex

`Z^2 --[1 0]--> Z`,

the degree-one cocycle `ell=[1 0]` is exact.  Map the generator of a source
complex `Z -> 0` to `(1,1)`.  There is no source degree-two group, so `ell` is
admissible, but `S^*ell=1` is a nonzero source cohomology class.  Hence the
zero target cohomology class can acquire a nonzero selected source readout
under a defective graded map.

This is not functorial cohomological pullback; it is representative-dependent
pairing data.

## Physical consequence

The maximal readout space is useful only when the physical cocycle
representative, including regulator and endpoint normalization, is frozen.
If the observable is claimed to depend only on a target cohomology class,
one needs the stronger requirement that exact representative changes pull
back to exact source changes.  Strict chain compatibility guarantees this;
mere defect annihilation by one selector does not.
