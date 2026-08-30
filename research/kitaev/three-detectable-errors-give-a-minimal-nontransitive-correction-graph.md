# Three detectable errors give a minimal nontransitive correction graph

Owner: \`marici.Kitaev\`

## Question

What is the smallest explicit coherent-error fixture in which lower detection
passes, pairwise correction compatibility is nontransitive, and quotient
materialization therefore fails?

## Claim boundary

This is an exact four-dimensional linear-algebra witness. It does not assert a
microscopic noise process, recovery implementation, or fault-tolerance bound.

## Code and ambient space

Let the code be \(\mathcal C=\mathbb C^2\), and take the ambient space

\[
\mathcal H=\mathbb C^2\oplus\mathbb C^2.
\]

Let \(P\) project onto the first summand. Write \(I\) and \(Z\) for the identity
and Pauli \(Z\) on the code.

Define three isometries from the code into the ambient space:

\[
V_1
=
\frac{1}{\sqrt2}
\begin{pmatrix}
I\\
I
\end{pmatrix},
\qquad
V_2
=
\begin{pmatrix}
I\\
0
\end{pmatrix},
\qquad
V_3
=
\frac{1}{\sqrt2}
\begin{pmatrix}
I\\
Z
\end{pmatrix}.
\]

Let \(E_iP=V_i\). Their action away from the code is irrelevant to the
compressed witness.

## Lower detection passes

Compression back to the code gives

\[
P E_1 P=\frac{1}{\sqrt2}P,
\qquad
P E_2 P=P,
\qquad
P E_3 P=\frac{1}{\sqrt2}P.
\]

Each error is individually detectable: no \(E_i\) has a non-scalar logical
action inside the code under this compression.

This validates the lower detector interaction. The later failure does not
retroactively invalidate it.

## Pairwise overlaps

The compressed relative errors are

\[
P E_1^\dagger E_2 P
=
\frac{1}{\sqrt2}P,
\]

\[
P E_2^\dagger E_3 P
=
\frac{1}{\sqrt2}P,
\]

but

\[
P E_1^\dagger E_3 P
=
\frac12(I+Z)
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]

The last matrix is not scalar on the two-dimensional code.

Therefore:

- \(E_1\) is correction-compatible with \(E_2\);
- \(E_2\) is correction-compatible with \(E_3\);
- \(E_1\) is not correction-compatible with \(E_3\).

Pairwise Knill–Laflamme compatibility is not transitive.

## Minimality

Two errors cannot witness nontransitivity; three vertices are necessary.

A one-dimensional code cannot witness non-scalar compression because every
operator on it is scalar. Thus code dimension two is necessary.

The displayed construction uses one auxiliary copy of the code, so ambient
dimension four suffices. It is minimal under the requirement that the middle
isometry share scalar overlap with two distinct code isometries while the outer
pair retain a non-scalar relative overlap.

The last ambient-minimality sentence is a structural dimension argument for
this isometric block construction, not a classification of every possible
non-isometric error model.

## Channel normalization

If the three labels must appear as Kraus branches on the code, set

\[
F_i=\frac{1}{\sqrt3}E_i.
\]

Then

\[
\sum_i P F_i^\dagger F_i P=P.
\]

The scalar versus non-scalar pattern is unchanged by the common normalization.
A completion outside the code can be added independently.

## Why no quotient exists

Define a compatibility edge when

\[
P E_a^\dagger E_b P
\]

is scalar on the code. The fixture gives the path graph

\[
E_1\;-\;E_2\;-\;E_3
\]

without the edge \(E_1-E_3\).

This graph is not a disjoint union of cliques, so it cannot be the graph of an
equivalence relation. Any SCC step that takes connected components would merge
all three errors and falsely certify their coherent span as correctable.

The correctable subsets are cliques:

\[
\{E_1,E_2\},
\qquad
\{E_2,E_3\},
\]

but not \(\{E_1,E_2,E_3\}\).

## Exact higher-cell failure

For the full error family, no scalar matrix \(\alpha\) can satisfy

\[
P E_a^\dagger E_b P=\alpha_{ab}P
\]

for every pair because the \((1,3)\) entry is non-scalar. Hence no single
recovery channel corrects the coherent span of all three errors.

The first failed higher cell is the missing \((1,3)\) scalar-compression cell.
The individual detector cells and the two compatible pair cells remain valid.

## Optical interpretation

The two summands can be read as two spatial rails. The middle route occupies
only the first rail. The outer routes share the same first-rail component, so
each has scalar overlap with the middle route. Their second-rail components
differ by \(Z\), retaining logical-polarization information in their mutual
overlap.

Direct lower detection can therefore pass while recombining the two outer
routes reveals a logical-state-dependent fringe. The hostile requires coherent
comparison of the outer pair; separate intensity records cannot expose the
non-scalar cross term.

## SCC schema consequence

Before materializing compatibility classes, SCC must verify:

- reflexivity;
- symmetry;
- transitivity;
- contextual congruence.

If transitivity fails, retain a compatibility graph or hypergraph. A connected
component is not a quotient class.

For coherent correction, store each compressed matrix
\(P E_a^\dagger E_b P\), not only a boolean edge. Scalar values must assemble
into one positive-semidefinite Gram matrix on every claimed correctable span.

## Deutschian explanation

The obstruction is not “insufficient detection.” Each error passes the lower
test. The obstruction is that compatibility with a common intermediary does
not erase the logical information stored in the outer pair's relative
environmental component.

The graph shape explains why local pair checks cannot be transitively closed:
the missing cross term is independent information.

## Falsifiers

- Compatibility edges are transitively closed without calculating the missing
  pair.
- Connected components are treated as correctable classes.
- Individual detectability is promoted to joint correctability.
- Scalar pair flags are stored without their coherent Gram values.
- The non-scalar \((1,3)\) block is averaged into a scalar.
- The higher-cell failure is reported as failure of the lower detector.

## Disposition

Three errors on a two-dimensional code embedded in four dimensions give an
exact minimal nontransitivity witness. The lower detector interaction passes;
the higher correction cell fails at one explicit cross term.

No checker, build, or Git operation was run for this research-only packet.
