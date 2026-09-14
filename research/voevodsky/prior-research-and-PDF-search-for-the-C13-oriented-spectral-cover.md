# Prior-research and PDF search rejects a C13 oriented-cover identification

## Repository findings

### C13 already moved to a square-root cover

`research/voevodsky/C13_moves_from_the_conductor_to_its_elliptic_square_root_cover.md` rejects direct realization of C13 as a theta characteristic on the conductor and replaces it by

\[
\Sigma_g:\quad \xi^2=g(m).
\]

The four simple zeros of \(g\) make this an elliptic double cover. Its deck exchange is exactly the kind of branch datum needed for an oriented two-channel lift. However, the recorded conjecture concerns Bunch--Davies orientation, two-torsion, and Picard parity; it does not provide a map to the RH Schwarz observation square.

### A2 has a canonical rational eigensplitting

`research/benincasa/a2-integral-eigensplitting.json` records:

- canonical rational plus/minus eigenlines;
- a quadratic base change \(\lambda=\mu^2\);
- a deck action separating the two eigencharacters;
- a forced integral \(\mathbb Z/2\) defect.

This is structurally close to the required oriented spectral cover. It also warns that rational branch splitting need not give an integral labeled splitting.

### The RH A2/associahedron packet remains conditional

`research/nima/rh-finite-operator-geometry-is-type-a2-and-its-coherence-shadow-is-pentagonal.md` proves the \(A_2\) root census but explicitly does not construct source mutation charts, exchange maps, or a positive chamber. It states that orientation remains extra.

`research/nima/rh-five-is-the-associahedron-of-a-four-stage-pure-spinor-comparison.md` likewise identifies the pentagonal coherence shape but leaves theta smoothing and the transversality/positive-seam theorem open.

### The positive-geometry source embedding is explicitly missing

`research/nima/canonical-form-source-embedding-interface.md` requires a source-derived tuple

\[
(K_n,\iota_n,\{X_c\},P_n,\nu_n).
\]

At five points, affine positive geometries exist, but no source arrow selects one. Positivity and recursion do not substitute for \(\iota_n\).

## PDF search

Executed `pnpm pdf:search` for:

- `C13`;
- `kinematic associahedron`;
- `positive source`;
- `spectral cover`;
- `associahed`;
- `kinematic space`;
- `positive geometry`;
- `eigenline`.

No indexed PDF matched `C13`, `kinematic associahedron`, `positive source`, `spectral cover`, or `eigenline`.

The broader searches found only background references:

- generalized associahedra in `1212.3563v1.pdf`;
- associahedra and positive geometries mentioned in `Cosmological Polytopes and the Wavefunction of the Universe - 1709.02813.pdf`;
- generic kinematic-space and positive-geometry discussions in the cosmology PDFs.

None supplies the missing RH comparison from the C13 double cover or A2 eigenlines to the primitive/prime-prime Schwarz square.

## Revised frontier and erratum

The conductor `C13` is a conjecture identifier, whereas the scattering \(C_{13}\) is a kinematic source coordinate. They are not the same object. The conductor double cover and its deck exchange therefore cannot be used as ingredients for the RH Schwarz comparison without an independently sourced cross-program map.

The repository and PDF search reveal no such map. The correct frontier remains a direct source-derived comparison from the RH primitive/prime-prime observation square to the kinematic coordinates \(X_{13},X_{24},C_{13}\). See `research/voevodsky/erratum-the-conductor-C13-candidate-is-not-the-kinematic-C13-coordinate.md`.
