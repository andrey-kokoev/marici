# 3265 — The Rank-Twelve Candidate Uses Only the Existing Pole Lattice

## Exact factorization

Factor all 24 denominator polynomials of the reconstructed final (4\times3) marked-extension blocks over \(\mathbb Q[u,v]\). Every irreducible factor belongs to the pre-existing source support inventory:

\[
\begin{gathered}
u, v, u-1, u-2, v-2, u-v, u-v+2, u+v-2,\\
2u^2+u+v-2,
\quad 2u^2-u-v+2,\\
4u^2v-9u^2-6uv+12u-v^2+4v-4,\\
u^3-u^2v+2uv-3u+v-2.
\end{gathered}
\]

No denominator contains the homogeneous quartic \(\mathcal Q\), an undeclared carrier divisor, or an additional irreducible factor.

Eleven factors occur with maximal exponent one. The sole higher exponent is

\[
u^2
\]

in one component. The maximum denominator degree of an individual entry is 16. The least common multiple of all 24 denominators has total degree 19.

## Meaning

The formal source Cramer denominator bound 1063 is overwhelmingly nonminimal for this candidate. The candidate lies in a small meromorphic lattice supported entirely on already established walls.

This does not yet prove that every source-consistent extension lies in the same pole lattice. Therefore degree 19 cannot yet replace the Cramer bound in a global source certificate.

## Next gate

Derive, from the source Laurent complexes and indicial data, the maximal pole order of the canonical final-coordinate projection along each of the twelve factors. If the source forces precisely the displayed lattice, then mixed flatness and finitely many exact normalizations become a finite cocycle-rigidity problem. If the source admits larger poles, retain the larger source lattice rather than fitting the candidate.

## Artifacts

- `research/benincasa/checkers/audit_marked_extension_candidate_pole_lattice.py`
- `research/benincasa/results/marked_extension_candidate_pole_lattice.json`
