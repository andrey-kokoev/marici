# Toric four-port Pfaffian is an unframed emergent logical volume

## Question

Does the pinned four-port toric logical packet instantiate the Pfaffian emergent-volume claim, and what survives when the marked loop basis is removed?

## Claim boundary

Order the logical defect coordinates as

\[
(Z_1,Z_2,X_1,X_2).
\]

The primal–dual intersection form has matrix over \(\mathbf F_2\)

\[
J=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
\]

In characteristic two this matrix is alternating even though its displayed transpose equals itself. Its Pfaffian is

\[
\operatorname{Pf}(J)
=
0-(1)(1)+0
=
1\pmod2.
\]

Equivalently, choose the real skew lift

\[
J_{\mathbb R}=
\begin{pmatrix}
0&I_2\\
-I_2&0
\end{pmatrix},
\]

whose Pfaffian is a nonzero unit up to the chosen orientation convention.

Thus the four logical ports generate nonzero top exterior volume:

\[
\frac12\omega\wedge\omega\ne0.
\]

This is an exact pinned instance of emergent relational volume.

### What the nonzero volume means

The result says more than pairwise anticommutation. It says the two matched primal–dual pairs jointly span the entire four-dimensional logical phase space with no residual radical.

Every three-port restriction is alternating on an odd-dimensional space and therefore degenerate. Restoring the fourth matched port is the minimal operation that closes the symplectic volume.

This agrees with the recorded finite theorem that four binary logical probes are required for joint faithfulness on the full Pauli quotient, while only two probes classify one primal homology class.

### Unframed descent

A change of marked primal basis acts by

\[
z\longmapsto Az,\qquad
x\longmapsto A^{-T}x.
\]

The total transformation on \(H_1\oplus H^1\) preserves \(J\). Its determinant is

\[
\det A\,\det A^{-T}=1.
\]

Hence the top symplectic volume is invariant under simultaneous primal–dual frame transport.

This gives a strong separation:

- an individual loop coordinate does not descend without a marked basis;
- zero versus nonzero homology descends only coarsely;
- the full symplectic pairing and its Pfaffian volume descend canonically.

The emergent relational volume is therefore more canonical than its component coordinates.

### Bridge to the ordered algebra

Nondegeneracy of \(J\) makes the twisted logical group algebra simple:

\[
\mathbf C^\omega[\mathbf F_2^4]
\cong
M_4(\mathbf C).
\]

The four-dimensional irreducible logical Hilbert module is connected to the four-dimensional symplectic phase space through the finite Heisenberg representation. They are not the same vector space:

- \(\mathbf F_2^4\) labels projective logical Pauli operators;
- \(\mathbf C^4\) carries their irreducible representation.

The matching dimensions are a consequence of the nondegenerate two-qubit Heisenberg algebra, not an identification of Carrier and Hilbert coordinates.

### Self-closure attack

The ordered tower introduces no independent triple or quadruple phase.

Associativity of the Weyl cocycle enforces triangle coherence. Centrality of all commutators makes every nested commutator trivial. Therefore any four-word relative phase reduces to the sum of pairwise intersection parities over the required inversions.

The four-port Pfaffian does not contradict this closure. It is a global nondegeneracy invariant of the bilinear relation field, not a new higher commutator.

This is important: emergent volume can be new as an aggregate invariant while still being completely determined by lower pairwise data.

### Lens separation

The three coefficient lenses see different shadows:

- additive Carrier lens: the nondegenerate alternating form on \(H_1\oplus H^1\);
- determinant-line lens: its oriented Pfaffian volume;
- ordered quantum lens: the Weyl commutator algebra and the simple matrix algebra it generates.

The determinant of the represented Pauli commutator is not the Pfaffian. Indeed the central commutator \(-I_4\) has determinant one. Matrix determinant erases the ordered phase, whereas the Pfaffian belongs to the logical pairing space before representation.

Conflating those two determinants is a falsifier.

### Hostile cases

The emergent-volume conclusion fails if:

- the primal–dual intersection pairing becomes degenerate;
- one logical port is duplicated or omitted;
- primal and dual bases are transported inconsistently;
- a coordinate determinant is substituted for the Pfaffian line;
- leakage or non-Pauli operations are included while class-two closure is claimed;
- algebraic volume is used to infer executable measurement or reset capability.

The existing deliberate broken-face fixture attacks the common source bridge. The existing missing-reset result attacks physical source closure. Neither falsifies the ideal unframed Pfaffian theorem.

## Disposition

The toric logical packet is a complete positive instance of Pfaffian emergent relational volume. Four source-derived logical ports generate a nonzero symplectic top form; every three-port restriction is degenerate; and the volume survives removal of the marked basis even though individual logical bits do not.

It also validates the self-closure criterion: the volume is genuinely collective but contains no independent higher commutator information. It is forced by the pairwise intersection form, while associativity and centrality close the ordered tower.