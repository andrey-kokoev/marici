# Exact QTDS and Jordan Lift Audit

## Record

Date: 2026-08-12

Status: all implemented exact checks pass. They verify the order-relative tree lift through eight
points, complete six-point PT-basis reconstruction, six/eight-point cut products, one nested
eight-point residue, and the special rectangular Jordan identity. They do not construct the
missing twisted half-chain augmentation.

## Reproducible artifact

Run:

```text
python research/nima/check_qtds_lift.py
```

The script uses only Python's standard library and exact rational arithmetic. Its Mandelstam data
are generic points of the formal Gram-free massless space

\[
s_{ij}=s_{ji},
\qquad
s_{ii}=0,
\qquad
\sum_j s_{ij}=0.
\]

It imports the independently audited scalar associated-grade implementation from
`check_j_reconstruction.py`.

## Quartic recursion

Rooting a planar quartic tree on the last external leg turns it into an ordered ternary tree. Each
off-shell current contains an odd consecutive block, and every nontrivial current is assembled
from three odd blocks. The recursion uses only:

- the alternating \(+,-,+,-\) assignment;
- the propagator \(1/K^2\);
- the vertex \(-2K_1\cdot K_3\), with the momentum-crossing sign handled when the root slot has
  positive polarity.

The resulting tree counts are

\[
N_4=1,
\quad
N_6=3,
\quad
N_8=12,
\quad
N_{10}=55,
\quad
N_{12}=273,
\]

in agreement with the quartic-tree sequence quoted in the QTDS source.

## Period comparison

For both global polarity assignments, the script verifies

\[
A_n^{\rm QTDS}(\alpha,\varepsilon)
=
A_n^{\rm QTDS}(\alpha,-\varepsilon)
=
(-1)^{n/2-1}a_{R,n}(\alpha)
\]

at:

| Multiplicity | Exact ordering samples | Result |
| --- | ---: | --- |
| 4 | 1 | pass |
| 6 | 2 | pass |
| 8 | 2 | pass |

Each of the six- and eight-point sets includes a noncanonical label ordering. The alternating sign
is only the relative convention between the paper's quartic vertex and the scalar-shift grade; it
can be absorbed into the quartic coupling convention.

At six points the recursion also reproduces equation (6) of the QTDS paper exactly. The three
individual tree contributions are not invariant under the global polarity flip, while their exact
sum is invariant. This is direct evidence that polarity flip is an equivalence of the evaluated
tree presentation, not a diagram-by-diagram redundancy.

## Missing-choice audit

For a bare set of \(n\) labels, the number of unordered balanced bipartitions is

\[
\frac12\binom{n}{n/2}.
\]

The script records

\[
3,
\quad
10,
\quad
35
\]

at \(n=4,6,8\). None is a permutation-invariant distinguished choice. QTDS does not use an
arbitrary balanced bipartition: a cyclic order selects its alternating double cover. The count is
included only to expose how much coloring data the bare class has forgotten.

## Rectangular Jordan audit

For exact rational matrices

\[
x\in\operatorname{Mat}_{2\times3},
\qquad
y,z\in\operatorname{Mat}_{3\times2},
\]

the script implements

\[
Q_x(y)=xyx
\]

and checks the typed fundamental formula

\[
Q_{Q_x y}(z)
=
Q_x\bigl(Q_y(Q_x(z))\bigr)
\]

entry by entry. The equality is exact.

## Interpretation

The checks establish five useful facts:

1. one finite quartic grammar evaluates to the scalar-derived ordered period at low multiplicity;
2. the two fibers of the alternating cyclic cover have the same tree evaluation but different
   internal decompositions;
3. the matrix QTDS realization obeys the Jordan coherence identity expected of its target algebra.
4. both six-point polarity families reconstruct the same half-class from all six independent
   Parke--Taylor periods;
5. audited cut residues split as products of lower QTDS periods, including an eight-point
   codimension-two corner.

They do not establish:

- a canonical choice of order, polarity, or Jordan pair from \(\mathsf J\);
- a chain map into twisted cohomology before PT pairing;
- a sewing-stable quotient of presentation differences;
- the all-Jordan-pair strictifiability classification;
- an exact arbitrary-topology representative rather than a cut-equivalence class.

## Next executable extension

The complete-basis and presentation-level residue tests are now implemented here. Entry 19 and
`check_qtds_descent.py` construct the six-point local flip flow and the exact eight-point
coherence complex. The remaining executable target is the generic Jordan-valued solution of its
24 local edge equations and the four square curvatures, followed by an augmentation into a
scalar-normal twisted-chain model.
