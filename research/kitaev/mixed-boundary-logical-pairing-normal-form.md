# Mixed boundaries change logical representatives, not the Pauli normal form

Owner: `marici.Kitaev`

## Bounded question

How does the perfect relative intersection pairing decompose into loop and arc
coordinates, and which logical information is lost by a loop-only probe family?

## Coordinate decomposition

Let \(R\) contain \(r>0\) rough boundary components and \(S\) contain
\(s>0\) smooth components, with \(r+s=b\). The long exact sequence gives a
noncanonical vector-space splitting

\[
H_1(\Sigma,R)
\simeq
\mathbf F_2^{2g}
\oplus
\mathbf F_2^{s-1}
\oplus
\mathbf F_2^{r-1}.
\]

The three summands may be represented by handle cycles, surviving smooth
boundary loops, and arcs joining rough components. Dually,

\[
H_1(\Sigma,S)
\simeq
\mathbf F_2^{2g}
\oplus
\mathbf F_2^{r-1}
\oplus
\mathbf F_2^{s-1},
\]

represented by dual handle cycles, surviving rough boundary loops, and arcs
joining smooth components.

The splittings are basis choices, not canonical source identifications. Their
dimensions and exact-sequence provenance are canonical.

## Pairing normal form

Poincare--Lefschetz duality gives a perfect pairing

\[
H_1(\Sigma,R)\times H_1(\Sigma,S)\longrightarrow\mathbf F_2.
\]

Dual bases can be chosen so its matrix is the identity. With the coordinate
types above, the blocks pair as follows:

- primal handle cycles with dual handle cycles;
- primal smooth-boundary loops with dual smooth-boundary arcs;
- primal rough-boundary arcs with dual rough-boundary loops.

Thus the boundary part is intrinsically loop--arc, not loop--loop. Boundary
exchange swaps the two loop--arc blocks.

If \(Z(v)\) and \(X(w)\) are the corresponding logical string operators, the
quantum coefficient law is

\[
Z(v)X(w)=(-1)^{\langle v,w\rangle}X(w)Z(v).
\]

The direct sum of primal and dual logical coordinates therefore has the
standard symplectic matrix

\[
\Omega=
\begin{pmatrix}
0&I_k\\
I_k&0
\end{pmatrix},
\qquad
k=2g+b-2.
\]

The abstract logical Pauli algebra depends only on \(k\), not on the size of
the rough/smooth partition. The partition changes which operators are loops,
which are boundary-to-boundary arcs, and which excitations may condense.

## Readout consequence

A probe family containing only closed boundary and handle loops omits the
\((r-1)\)-dimensional primal rough-arc sector. Its common kernel therefore has
dimension at least \(r-1\). The dual loop-only family similarly misses the
\((s-1)\)-dimensional smooth-arc sector.

Joint faithfulness requires one independent probe for every relative arc
coordinate as well as the surviving loop and handle coordinates. Counting
only closed Wilson loops is complete for a one-component rough set, but not
for multiple condensing components.

## Pair-of-pants witness

For \(g=0,b=3,r=2,s=1\), the primal logical generator is a rough-to-rough arc
and the dual generator is a rough boundary loop. They intersect once and
anticommute. There is no surviving primal boundary-loop coordinate, so a
primal closed-loop census alone reports rank zero even though the code encodes
one qubit.

## Shared versus quantum structure

Carrier geometry supplies the exact-sequence decomposition, relative arcs,
and perfect intersection pairing. The quantum coefficient lens supplies the
phase \((-1)^{\langle v,w\rangle}\), operator incompatibility, and Pauli
algebra. A marked dual basis rigidifies coordinates but is not selected by the
Hamiltonian alone.

## Falsifiers

- a decomposition whose dimensions do not total \(2g+b-2\);
- a degenerate primal--dual pairing;
- pairing a relative arc with no dual boundary-loop coordinate;
- a loop-only probe claimed faithful when \(r>1\) or \(s>1\);
- treating the chosen dual bases as canonical without source framing.

## Disposition

Mixed boundaries preserve the standard logical Pauli normal form while
changing the geometric species of its generators. The additional logical
coordinates produced by disconnected condensing boundary are relative arcs,
and they require arc-sensitive readout ports.

## Claim strength

Exact finite topological and logical-algebra theorem over \(\mathbf F_2\).

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_pairing_normal_form.py`.
The result is written to
`research/kitaev/results/mixed-boundary-pairing-normal-form.json`.

