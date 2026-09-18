# Coherent Resolution code-interpretation audit

## Question

Does Nima's finite type-A Coherent Resolution supply a genuine chain-complex or subsystem-code interpretation, and what is the signed exchange defect under that interpretation?

## Evidence boundary

This audit uses the exact complexes and ranks in `research/nima/a3-coherent-resolution.md`, `a3-physical-weight-resolution-gate.md`, and `arbitrary-m-coherent-resolution.md`. It does not add a history-to-positroid map, physical coefficient transport, or quantum Hamiltonian.

## Exact chain-complex result

Yes: the A3 object is a genuine integral augmented chain complex

\[
0\to \mathbb Z\xrightarrow{d_3}\mathbb Z^9\xrightarrow{d_2}\mathbb Z^{21}\xrightarrow{d_1}\mathbb Z^{14}\xrightarrow{\varepsilon}\mathbb Z\to0,
\]

with `d1 d2=0`, `d2 d3=0`, and zero augmented homology. The arbitrary-rank `CR_m` is also a genuine simplicial chain complex with an explicit contraction `dh+hd=id` at every finite rank.

## Canonical CSS shadow

Reducing A3 modulo two and placing qubits on `C1` gives the standard CSS incidence assignment

- X-check matrix `H_X=d_1`;
- Z-check matrix `H_Z=d_2^T`.

Commutation is exact because

\[
H_XH_Z^T=d_1d_2=0.
\]

Its encoded dimension is

\[
k=\dim\ker d_1-\operatorname{rank}d_2=\dim H_1=0.
\]

Thus the canonical code shadow is a valid finite stabilizer state with no logical qubits. It is not evidence of protected global capability. Logical classes and a nontrivial logical pairing are absent because the complex is contractible.

## Checks, boundaries, cycles, and transport

Under this shadow:

- local X syndromes are vertex incidences of edge errors;
- Z stabilizers are face boundaries;
- cycles are edge chains in `ker d1`;
- boundaries are `im d2`;
- logical edge classes would be `H1`, which is zero;
- adding a face boundary preserves the sole logical sector;
- a transport operator is code-trivial only when its edge chain is a boundary.

The finite A3 checks have bounded support inherited from edges and square/pentagon faces. The arbitrary-rank barycentric complexes are finite at each rank, but the present packets do not prove a uniform bounded-weight LDPC family, a geometric interaction metric, or a uniform distance statement. With `k=0`, logical distance is undefined or vacuous rather than a growing protection parameter.

## Signed exchange defect

The signed physical exchange residual is not presently a code syndrome. A syndrome requires a typed error-chain map into a binary or declared coefficient check space. The residual is a scalar coefficient-transport defect, while 14 of 21 A3 mutation-edge ratios still depend on missing negative-simple coordinates. No source-derived map sends that residual to `C0`, `C2`, or a subsystem gauge-check module.

It is therefore not yet a logical operation either: there are no nonzero canonical logical classes, and no physical-to-chain transport has been supplied. The strongest current classification is an untyped coefficient-transport obstruction. Calling it an unprotected perturbation would additionally require a Hamiltonian or noise model, which is absent.

## First missing typed map

The first missing map is the physical lift

\[
H_n\longrightarrow CR_{n-5}
\]

from labelled history or positroid cells to the chain complex, together with source-derived edge coefficient transport commuting with the differential. For a code interpretation one further needs an error alphabet and map from physical perturbations to chain errors. Without these maps, syndrome, correctability, and logical-action claims are notation-level analogies.

## Disposition

- genuine chain complex: admitted;
- canonical binary CSS shadow: admitted, with `k=0`;
- subsystem-code interpretation: unsupported;
- nontrivial protected logical sector: refuted for the canonical exact complex;
- signed exchange defect as syndrome or logical operator: unsupported at the missing physical-to-chain map;
- local cancellation or finite rank as global protection: prohibited.
