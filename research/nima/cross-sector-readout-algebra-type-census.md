# The first readout-algebra census finds objects but no cross-sector morphisms

## Bounded census

The four candidate sectors currently supply different algebraic types.

### Radiative memory

The standard \(D_3\) directional-memory plane has the graded polynomial
invariant algebra

\[
R_{\rm mem}=\mathbb Q[q_2,q_3],
\qquad \deg(q_2,q_3)=(2,3).
\]

### Source-normalized string disk readout

On the one-dimensional disk-period character line,

\[
R_{{\rm str},n}=
\begin{cases}
\mathbb Q[x^2],&n\text{ odd},\\
\mathbb Q[x],&n\text{ even}.
\end{cases}
\]

This is the invariant algebra of the displayed character line, not of the
full Koba--Nielsen or exceptional coefficient system.

### Five-site cosmology

For diagonal deck translation of \(G=(C_2)^5\) on the coefficient--Betti
label pair \(G\times G\), the orbit is classified by \(g\oplus h\).  Hence

\[
R_{\rm cos}=\operatorname{Fun}(G,\mathbb Q)\simeq\mathbb Q^{32}.
\]

The physical delta pairing is one primitive idempotent of this algebra, not
the entire invariant quotient.

### Flavor

The current exact packet supplies an audited observable subalgebra generated
by sector traces/determinants, selected mixed traces, and the commutator
determinant.  It does not supply a presentation of the complete weak-basis
invariant algebra.  Treating the finite observable list as that complete ring
would be untyped.

## Result

The sector objects are valid but heterogeneous:

\[
\text{graded polynomial ring},
\quad
\text{character-invariant polynomial ring},
\quad
\text{finite reduced idempotent algebra},
\quad
\text{partial observable subalgebra}.
\]

No audited source artifact currently supplies a constructor map between any
two of these algebras.  Therefore there is not yet a typed composable
cross-sector readout-algebra system, and the conditional \(\pi_0\) arithmetic
cannot be claimed natural on it.

This is an absence-of-map result, not an incompatibility theorem.  The exact
missing datum is a sector constructor

\[
F:(V,G,\text{physical resources})
\longrightarrow
(W,H,\text{physical resources})
\]

with declared equivariance and selection compatibility, inducing

\[
F^*:A[W]^H\longrightarrow A[V]^G.
\]

An arbitrary algebra homomorphism does not qualify.

## Verification

The checker verifies the string invariant degrees through degree 24, derives
all 32 cosmological diagonal orbits, and checks all 1024 products of their
primitive idempotents.  The memory and flavor typings are pinned to their
existing exact packets.

Evidence:

- `research/nima/check_cross_sector_readout_algebra_types.py`;
- `research/nima/results/cross-sector-readout-algebra-types.json`;
- Ledger Entries 1056 and 1225;
- the source-normalized string disk-period and flavor exact-audit packets.
