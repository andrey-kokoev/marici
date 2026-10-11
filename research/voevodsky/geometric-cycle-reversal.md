# Return to the generating operation: triangle-cycle reversal

## What the retained proton model actually does

The source of the 1836 coefficients is `research/nima/checkers/check_twelve_triangle_positive_geometry.py`, using the cyclic-coordinate primitives in `check_triangle_half_phase.py`.

It does not obtain those coefficients by contracting a tetrahedron radially. It:

1. Generates twelve face-centroid/edge triangles using the twelve proper tetrahedral rotations.
2. Selects a complex cyclic mode in each triangle.
3. Averages the twelve real rotation transports to align those modes.
4. Supplies dense feedback through their assembled rank-one projector.

The selected mode, the averaging, and the feedback are source construction choices. The count 1836 records the nonzero transfers in this three-stage realization; it is not the number of radial incidence arrows.

## Reconstruction, not substitution

For the reference triangle `(F_ABC,A,B)`, let X have its three position vectors as columns. The source uses

```text
C = [[0,1,0], [0,0,1], [1,0,0]],
omega = (-1 + sqrt(-3))/2,
c = (1, omega, omega^2),
v = X c,
A = X C X^(-1).
```

Exactly A v = omega v. Its orthogonal mode projector is

```text
P = v v* / (v* v).
```

Transport the same recipe to the other eleven triangles. Their projectors form block-diagonal L. Averaging the real inter-triangle rotations gives G. Stacking their vectors gives the assembled projector N.

The new checker reconstructs every entry of L, G, and N from this geometry and matches the retained coefficient source exactly. Thus the next reversal operates on the actual generator, not an independently supplied replacement matrix.

## Reverse the cycle, retaining the same character

Replace C by C^(-1), while retaining the source's selected eigenvalue omega. Then

```text
c_reverse = (1, omega^2, omega) = conjugate(c),
v_reverse = X c_reverse = conjugate(v),
A_reverse v_reverse = omega v_reverse.
```

X is real, so this derives conjugation of the generated mode. Consequently:

```text
L_reverse = conjugate(L),
G_reverse = G,
N_reverse = conjugate(N) = N^T.
```

The reversed generation still satisfies G L_reverse = N_reverse and closes its own feedback protocol. It is not the original selected mode.

This is different from taking the Hermitian adjoint of an already constructed projector: that operation leaves a Hermitian projector unchanged. Reversing the generating cycle selects its opposite complex mode instead.

Reversing both C and the selected character omega restores the original line. Therefore what is held fixed during reversal matters; the calculation explicitly keeps omega fixed.

## Connection to the outward tetrahedron

Each of the twelve source triangles splits into two barycentric boundary triangles. Coning them to the body center gives exactly the 24 flag tetrahedra already used in the outward incidence construction. The checker verifies the complete correspondence, including shared labels.

But two operations remain distinct:

- **Radial incidence reversal:** body → face → edge → vertex.
- **Cyclic traversal reversal:** C → C^(-1) within the triangle coordinates.

Changing the radial reveal order preserves the cells and their coordinates. It does not by itself prescribe the cyclic traversal. The new result derives coefficients from cyclic reversal; it does not prove that outward growth forces cyclic reversal.

A concrete electron candidate can now be stated as: build outward on the new tetrahedron and use reversed local cyclic traversal with the same selected character. The second clause is still a conjectured construction rule, not a consequence of the first clause.

## Higher-level outcome

We have identified an operation in the actual proton generator whose reversal determines new coefficients. This replaces the previous choice between finished-matrix transpose and adjoint with a generator-level question.

It does not yet produce hydrogen or deuterium. Under the previously tested rigid attachment contract, its assembled mode is exactly the transpose candidate that failed direct closure. Reconstructing its origin does not remove that failure or justify inserting the phase repair automatically.

The remaining task is an attachment law for this generated complex, including which direction, cycle orientation, and character data survive at its barycenter. That law must be specified before attempting a two-isotope comparison.

## Verification

```text
python research/voevodsky/checkers/check_geometric_cycle_reversal.py
```

Seventeen exact checks pass. `results/geometric_cycle_reversal.json` records source and generator hashes, both seed coefficient vectors, reconstruction checks, eigenvector identities, transport identities, and the 12-to-24 flag correspondence. Existing sources and visualizations are unchanged.
