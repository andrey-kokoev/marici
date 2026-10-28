# New PDF clues for Su-32's comparison law

## Search scope

Operator request: rebuild the PDF index, then search the PDFs added today for clues relevant to the Hopf/Su-32 investigation.

`pnpm pdf:reindex` completed: **5,672 pages from 69 PDFs**, up from 5,320/59 in the preceding run. Ten PDFs with October 27 modification dates were searched individually, in addition to the already reviewed Urbantke PDF. Modification dates identify the search cohort; they are not asserted to be download timestamps.

The ten files contain eight distinct works: Cayssol–Fuchs and Barnich–Smoes each appear in preprint and published versions. This is a search and targeted reading, not a complete review of all 352 additional pages. Page references below are PDF page numbers; extracted printed-page labels are sometimes incorrect. The indexed text has encoding/layout defects, so formulas below use normalized notation rather than verbatim extraction.

| File(s) | Work | Reading emphasis |
|---|---|---|
| `1908.04029v2.pdf` | Nikolai Mnëv, *Minimal triangulations of circle bundles, circular permutations and binary Chern cocycle* | pp. 1–3, 14–17 |
| `1009.4789v1.pdf` | Chang, Markina, Vasil'ev, *Hopf fibration: geodesics and distances* | pp. 1, 3–4, 6 |
| `2012.11941v4.pdf`; `Cayssol_2021_J._Phys._Mater._4_034007.pdf` | Cayssol–Fuchs, *Topological and geometrical aspects of band theory* | Preprint pp. 10–11, 17; published title/abstract checked |
| `2502.20267v3.pdf`; `JHEP10(2025)056.pdf` | Barnich–Smoes, *Model spaces as constrained Hamiltonian systems. Part I. Application to SU(2)* | Published pp. 14, 16; both title/abstract pages checked |
| `2107.10810v1.pdf` | Sugic et al., *Particle-like topologies in light* | pp. 1–2 |
| `1512.08981v1.pdf` | Hall et al., *Tying Quantum Knots* | p. 1 and targeted search hits |
| `1302.0342v1.pdf` | Kedia et al., *Tying knots in light fields* | pp. 1–2 |
| `0907.2394v1.pdf` | McRae, *Clifford Fibrations and Possible Kinematics* | p. 1 and targeted search hits |

## 1. Highest-priority clue: cyclic orders on our four comparison triples

Mnëv's Theorem 1 (p. 2) classifies when a circle bundle can be triangulated over a fixed finite semi-simplicial base using a binary, integer-valued Chern cocycle. Sections 5–6 (pp. 14–17) give the explicit local construction: minimally triangulated circle bundles are encoded by compatible circular permutations of simplex vertices. The cyclic order on a triangle has two possibilities, assigned values 0 and 1.

On the boundary of an ordered tetrahedron with vertices 0,1,2,3, let f_i be the value on the face omitting i. Table 1 (p. 17) computes

```
c = f_0 - f_1 + f_2 - f_3.
```

Its sixteen assignments have:

- six cases with c=0: trivial circle bundle;
- eight cases with |c|=1: Hopf/anti-Hopf;
- two cases with |c|=2: oriented tangent-frame circle-bundle topology.

The zero cases extend to a single circular order over the tetrahedron. The nonzero classes on its boundary do not. On the two-dimensional boundary, all these 2-cochains are cocycles; the alternating-sum condition is the extra extension condition across the 3-simplex. This distinction matters when reading the paper's terminology.

### Direct match to the layer-4 record subsets

Our tested comparison outputs are

```
{P+,P-,E+}, {P+,P-,E-}, {P+,E+,E-}, {P-,E+,E-}.
```

These are exactly the four three-element subsets of the four signed labels: the abstract tetrahedron boundary. Our current reference join retains their membership and overlap values, but not a source-derived circular order on each triple.

**New test:** recover any cyclic order carried by each actual comparison operation, check its restriction to shared subsets, and evaluate the alternating face sum. Keep both orientation conventions and all unresolved order choices. The lexical sorting in our fixture/checkers is not source cyclic-order evidence.

This changes the priority: we do not have to start by guessing complex amplitudes or a differential phase law. A source-derived system of cyclic orders could already construct a combinatorial circle bundle. The abstract record tetrahedron still needs a comparison map to the native vertex-link sphere if their characteristic classes are to be identified. Their both being spheres is not that map.

The theorem concerns semi-simplicial triangulations. Its condition is not automatically sufficient for an ordinary simplicial triangulation. Requiring one globally extending order would select c=0 and exclude the nontrivial bundles; that requirement should not be built into the test by default.

## 2. A concrete phase-sensitive comparison: overlaps and loop products

Cayssol–Fuchs preprint p. 10, equations (22)–(27), derives a connection from the phases of inner products of neighbouring states and distinguishes open-path gauge dependence from closed-loop phase. Page 17, equations (47)–(52), separates the phase and modulus of the overlap: connection/curvature versus quantum metric.

For supplied nonorthogonal normalized states at our four comparison vertices, a proposed discrete test is

```
W = product_cycle [ <u_i,u_(i+1)> / |<u_i,u_(i+1)>| ].
```

Local phase changes cancel in W. Its orientation/sign convention must be stated: the review uses `A=i<u|du>`, whereas some of our prior notes use the opposite convention. A zero overlap must be reported as a failure of this phase chart, not replaced by a chosen phase.

This tests something the lossless record join does not: two comparison routes can recover the same projectors or records while retaining different transport phases. The necessary additional input is a source-defined Hermitian state encoding and comparison pairing. The paper does not identify the four signed records with four kets.

## 3. Two comparison directions can generate the missing fibre direction

Chang–Markina–Vasil'ev p. 1 identifies the S3 horizontal distribution with two SU(2) vector fields whose commutator supplies the missing Hopf-fibre direction. Page 6 gives the horizontal condition `<gamma_dot,gamma>=0`; p. 4 separates geometric and dynamical phase.

This suggests a second operation-level discriminator: if the two Su-32 comparison directions have a source-defined continuous lift, does their commutator have a vertical component while the projected comparison closes? Our set-valued joins alone have no such differential structure. The finite coefficient permutations are not automatically horizontal vector fields.

### Another Hopf possibility worth keeping distinct

Page 3 also discusses the quaternionic fibration `S3 -> S7 -> S4` for two two-level systems. Therefore the observation that four complex amplitudes give CP3 after a common U(1) quotient does not eliminate every Hopf construction. A quaternionic Hopf interpretation uses a larger SU(2) fibre action, not the same U(1) quotient. It needs that action to be supplied by the source; no entanglement or quaternionic structure is assigned merely from four record names.

## 4. Retained constraints versus premature gauge fixing

Barnich–Smoes formulate coadjoint-orbit/model spaces as constrained Hamiltonian systems. Published pp. 14–16 show explicitly that the Hopf bundle forbids a global gauge condition: an Euler-angle gauge valid on the overlap fails at the poles, where appropriate local combinations of angles must be used.

For our work this supports retaining local representatives and their transition data instead of enforcing one globally chosen frame. It does not select Su-32's constraint surface: the Hamiltonian/Poisson structure is additional data in their construction. This is more useful after a native cyclic-order or phase-comparison candidate is identified than as the first test.

## 5. Physical realization clues

- **Sugic et al., pp. 1–2:** two complex polarization components, including their phase, define a normalized S3 field; Stokes data give the S2 polarization projection. Their experiment reconstructs the full field and reports Skyrme number 0.945. This gives a concrete distinction between polarization-only and full phase-sensitive reconstruction.
- **Hall et al., p. 1:** linked preimages of a nematic direction field provide an experimental Hopf-texture example. The order parameter and imposed magnetic-field protocol, rather than wire incidence, define the map.
- **Kedia et al., p. 2:** the electromagnetic construction supplies actual field equations: Bateman scalars obey a differential compatibility condition, and `F=grad(alpha) cross grad(beta)` gives `F=E+iB` with `E dot B=0` and `|E|=|B|`. It is a candidate physical target only if corresponding field variables and operations exist. The paper explicitly distinguishes field-line geometry from the straight null trajectories carrying the field.
- **McRae, p. 1:** quaternionic flows in three generator directions give different fibrations with different base interpretations. This is a reminder to identify which action and base are intended; its kinematical parameters are not derived from Su-32.

## Decision

Prioritize **Mnëv's four-face cyclic-order test**. It matches the record-subset structure already produced by our actual layer-4 incidence adapter and supplies a sixteen-case classifier with distinct trivial/Hopf/frame results. Follow with overlap-loop phases only if the native data provide a Hermitian pairing. The continuous horizontal-commutator and physical-field constructions are later tests with additional source requirements.

No native cyclic orders or Chern class were computed in this reading pass. The change is a source-supported test proposal, not a promotion of the reference join to a Hopf bundle.

## Search reproduction

Initial query, separately for every file pattern in the cohort:

```sh
pnpm pdf:reindex
pnpm pdf:search 'Hopf|phase|spinor|comparison|intertwiner' -Regex -Book '*1908.04029*' -Limit 5 -Context 160
```

Targeted queries:

```sh
pnpm pdf:search 'cyclic order|circular permutation|transitivity|cocycle' -Regex -Book '*1908.04029*' -Limit 18 -Context 170
pnpm pdf:search 'Pancharatnam|Bargmann|overlap|Wilson|parallel transport' -Regex -Book '*2012.11941*' -Limit 12 -Context 220
pnpm pdf:search 'commutator|horizontal|holonomy' -Regex -Book '*1009.4789*' -Limit 9 -Context 180
pnpm pdf:search 'Gribov|second class|oscillator|Schwinger|quaternion' -Regex -Book '*JHEP10*' -Limit 12 -Context 170
```

Reindex execution: `structured_command_execution:e_29164_1793123720187528700_29`. Initial per-file searches: executions ending `_30` through `_39` in the same structured-command process. Page texts were then read directly from `references/extractions/pdf-search-all/`. No scientific checker, native operation or routing code was changed.
