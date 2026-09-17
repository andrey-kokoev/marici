# Tate-torus cofiber and octahedral realization

The remaining exactness relations admit a canonical model using coordinate-support filtrations of the channel lattice.

Let the four selected tetrahedral channel coordinates span

\[
L^{tet}=\mathbb Z\langle e_{d_0},e_{d_1},e_{d_2},e_{d_3}\rangle.
\]

For each face-coordinate subset `S subset {0,1,2,3}`, define

\[
V_S=\mathbb C[\mathbb Z^S],
\]

the algebraic span of lattice deltas whose support uses only coordinates in `S`. If `A subset B`, extension by zero gives a monomorphism

\[
V_A\hookrightarrow V_B.
\]

Define the oriented edge object by its cofiber

\[
C_{B/A}=V_B/V_A.
\]

For every nested triple `A subset B subset C`, there is a canonical short exact sequence

\[
0\longrightarrow V_B/V_A
\longrightarrow V_C/V_A
\longrightarrow V_C/V_B
\longrightarrow0.
\]

In the derived/stable target this is the distinguished cofiber triangle

\[
C_{B/A}\longrightarrow C_{C/A}
\longrightarrow C_{C/B}\longrightarrow\Sigma C_{B/A}.
\]

For a four-stage filtration, the quotient triangles produced by its nested triples form the standard octahedron. No extra coherence choice is needed: it is the canonical octahedron of composable inclusions.

## Fourier and rotation compatibility

Pontryagin Fourier identifies `V_S` with trigonometric polynomials on the dual torus depending only on the coordinates in `S`. It carries inclusions, quotient sequences, and their derived cofiber triangles to the corresponding pointwise-product chart.

Tetrahedral rotation sends

\[
V_S\longmapsto V_{\rho S}
\]

and preserves every short exact sequence. Combined with the graded Fourier lift, this makes the cofiber and octahedral data compatible with both the semidirect relation and `q^4=Sigma`.

Reciprocal reflection `v -> -v` preserves every `V_S`. Derived duality reverses the quotient triangles and obeys

\[
\mathbb D\Sigma\simeq\Sigma^{-1}\mathbb D.
\]

## Result and boundary

This gives nonzero analytic objects for the standard tetrahedral face-poset generators and realizes:

1. zero and vertex objects;
2. incidence maps;
3. triangular cofiber relations;
4. tetrahedral octahedral compatibility;
5. the graded Fourier helix;
6. reciprocal derived duality.

Consequently it is a candidate nonzero exact realization of the tetrahedral/channel subcategory of the universal eight-lattice category. Extending the claim to the entire declared source still requires matching every named eight-lattice generator and its orientation convention with the corresponding coordinate subset and quotient map.

`check_tate_torus_cofiber_octahedra.py` checks all 256 nested triples in the four-coordinate Boolean tetrahedron on a finite lattice window. The identities are dimension-independent because they arise from literal quotient short exact sequences.
