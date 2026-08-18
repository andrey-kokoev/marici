# Entry 473 — Orbit Completion Localizes the First-Order Defect in the Odd Character

Entry 471 identifies the smallest deck-equivariant first-order exact complex:
the sum of the \(L_2^-=a-u/2\) lattice and its conjugate
\(L_2^+=a+u/2\).  Entry 470 then permits taking the two monodromy
idempotents before computing the cokernel.

## Characterwise census

Work over \(\mathbb Q[u]/(u^2)\), retain all four exact sectors and both exact
columns, and use the same total \((a,b)\)-degree filtration as Entry 450.  For
each source column in the minus lattice, its deck conjugate is included and
the target and image are projected to the \(+\) and \(-\) eigenspaces.

At cutoffs \(D=16,20,24,28\), the frozen cokernel dimensions are exactly

\[
\dim C_{D,+}=2D+1,
\qquad
\dim C_{D,-}=2D-1,
\]

whose sum is the established \(4D\).  The orbit-completed dual-number
dimensions are

\[
\dim C^{(1)}_{D,+}=4D+1,
\qquad
\dim C^{(1)}_{D,-}=3D.
\]

Therefore the first-order flatness defects split as

\[
\delta_+(D)=2(2D+1)-(4D+1)=1,
\]

\[
\delta_-(D)=2(2D-1)-3D=D-2.
\]

The total orbit-completed defect is \(D-1\).

## Interpretation

Deck completion does not restore flatness.  It localizes its growth.  The
invariant block has only a single cutoff-independent failure, compatible in
size with the one conormal relation cell typed in Benincasa Entry 472.  This
dimension match is not yet an identification: it requires the actual map to
\(I/I^2\).

Every cutoff-growing contribution lies in the anti-invariant block.  Thus the
remaining infinite obstruction is not an even--odd extension and is not
hidden in the invariant quartic tail.  It is same-character mixing between
the odd resonance and the odd quartic tail \(\langle a,a^3\rangle\).

The defect \(D-1\) is larger than the one-sided value \(D-6\) of Entry 450
because orbit completion enlarges the exact image by the conjugate lattice;
the two cokernels are different filtered objects.  The comparison should not
be read as deterioration of one fixed module.

## Next gate

The plus and minus problems are now qualitatively different.

1. Construct the invariant carrier-reduction map and test whether its unique
   finite defect is precisely the conormal class \(I/I^2\).
2. Determine the stable presentation of the anti-invariant image.  Its linear
   defect shows that comparison only with the reduced line \(R/(z)\) cannot
   be an isomorphism before an odd-tail subcomplex is retained or removed by
   a geometrically derived relative-support operation.

No additional carrier component is indicated.  The obstruction is in the
anti-invariant coefficient complex.

The executable audit is
`research/voevodsky/check_soft_axis_orbit_character_cokernel.py`.
