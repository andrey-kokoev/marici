# A microscopic `F/R` coherence fragment in the electric `Rep(S3)` sector

Owner: `marici.Kitaev`

## Bounded question

Can any channel-wise `F` and `R` data be derived from explicit microscopic
intertwiners, rather than inferred from the modular matrix?

Yes for the pure-electric subcategory.  Electric excitations of `D(S3)` have
trivial flux and form `Rep(S3)`.  Freeze the real standard representation
`C` with a 120-degree rotation and a reflection, then solve the intertwiner
equations exactly for

\[
C\otimes C=A\oplus B\oplus C.
\]

Every Clebsch--Gordan embedding is normalized and its sign is fixed by making
the first nonzero matrix entry positive.  This is the declared gauge.

## Exact recoupling matrix

The total-`C` subspace of `C tensor C tensor C` has three multiplicity
channels, indexed by intermediate charge `A,B,C`.  Overlap of the left- and
right-associated orthonormal embeddings gives

\[
F^{C}_{CCC}=
\begin{pmatrix}
1/2&1/2&1/\sqrt2\\
-1/2&-1/2&1/\sqrt2\\
1/\sqrt2&-1/\sqrt2&0
\end{pmatrix}.
\]

It is exactly orthogonal.  This is not reconstructed from `S,T`; it is
computed from explicit representation matrices and Clebsch--Gordan maps.

## Channel braiding

The electric subcategory is symmetric, so microscopic braiding is tensor
factor exchange.  Projecting the flip onto the three `C tensor C` channels
gives

\[
(R^{CC}_A,R^{CC}_B,R^{CC}_C)=(1,-1,1).
\]

The minus sign occurs precisely in the antisymmetric sign channel `B`.
On the total-`C` multiplicity space,

\[
B_{12}=\operatorname{diag}(1,-1,1),\qquad
B_{23}=F B_{12}F^T.
\]

The checker verifies exactly

\[
B_{12}B_{23}B_{12}=B_{23}B_{12}B_{23},
\qquad B_{12}^2=B_{23}^2=1.
\]

This is a microscopic braid/coherence fragment rather than a scalar modular
invariant.

## Carrier and coefficient allocation

Carrier geometry supplies the binary fusion tree, its left/right association,
ordered leaves, and exchange path.  The quantum coefficient lens supplies the
representation matrices, normalized intertwiners, fusion-space inner product,
recoupling coefficients, and channel braid action.  A fusion tree without
coefficient intertwiners does not determine `F`.

## Verification

`uv run --with sympy python -u research/kitaev/checkers/check_s3_electric_recoupling.py`
passes eight aggregate gates.  It solves every intertwiner equation rather
than inserting a tabulated `F` matrix, proves the `A+B+C` decomposition is
orthogonal and complete, constructs all six association embeddings, and
checks orthogonality and the braid relation symbolically.

## Claim boundary

Only the full subcategory on electric charges `A,B,C` is represented, and
only the displayed nontrivial `C,C,C -> C` recoupling is frozen.  The packet
does not compute flux or dyon intertwiners, mixed-sector `F` symbols,
non-symmetric `R` symbols, or the complete pentagon/hexagon family.  The
ambient tensor product of vector spaces is strictly associative, but that
fact is not substituted for an exhaustive simple-channel pentagon audit.

The electric-sector identification follows the finite-group quantum-double
representation theory in [Kitaev](https://arxiv.org/abs/quant-ph/9707021) and
the explicit `D(G)` representation/ribbon account of
[Cowtan and Majid](https://arxiv.org/abs/2107.04411).

## Falsifiers

Failure of the representation intertwiner equations, incomplete or
nonorthogonal `C tensor C` decomposition, nonorthogonal `F`, channel flip
eigenvalues other than `(1,-1,1)`, or failure of the braid relation falsifies
the fragment.
