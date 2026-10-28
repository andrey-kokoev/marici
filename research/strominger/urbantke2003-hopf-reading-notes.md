# Urbantke (2003): Hopf geometry and seven physical applications

Source: H. K. Urbantke, **The Hopf fibration—seven times in physics**, *Journal of Geometry and Physics* 46 (2003), 125–150. Local PDF: `references/Urbantke2003.pdf`.

## Search and reading record

Executed the requested `pnpm pdf:reindex`: 5,320 pages from 59 PDFs indexed. Then used:

```sh
pnpm pdf:search 'Hopf' -Book '*Urbantke*' -Limit 25 -Context 200
pnpm pdf:search 'Berry|Maxwell|helicity|monopole|Kustaanheimo|spin bundle|Taub|twistor' -Regex -Book '*Urbantke*' -Limit 24 -Context 240
```

The second query returned 16 matching pages; inclusion of a search term does not imply the paper treats it as an application. In particular, Maxwell/Yang–Mills appears in a cited paper title; it is not one of Urbantke's seven numbered examples.

Read the indexed pages for the overview, qubit/Berry and oscillator sections, Taub–NUT discussion, Robinson congruences, helicity representations, monopole patching, spin/Dirac section, and appendix definitions/group/connection/gauge material. Text extraction has encoding/layout defects, especially in equations. The formulas below are normalized mathematical summaries, not verbatim transcriptions. PDF page n corresponds to printed page n+124.

## 1. Basic construction: what the objects actually are

Sections 2 and A.1: printed pp. 127–128, 141–142; PDF pp. 3–4, 17–18.

Start with a normalized complex pair `z=(z1,z2)`:

```
|z1|^2+|z2|^2=1.
```

Such pairs form S³. Common phase multiplication `z -> exp(i alpha) z` has circle orbits. The quotient is CP¹, identified with S² by

```
R(z) = (2 Re(conj(z1) z2),
        2 Im(conj(z1) z2),
        |z1|^2-|z2|^2).
```

Thus `S¹ -> S³ -> S²`. In the qubit application the base is the space of pure-state projectors `zz†`; it is not physical position. The full Bloch ball describes mixed states, but only its boundary sphere is this pure-state base.

Appendix A.4 (printed p. 145; PDF p. 21) gives the SU(2)/U(1) description, opposite left/right-coset Hopf/anti-Hopf fibrations, and the Hopf invariant as a linking number. For the standard Hopf map that invariant is one. This linking invariant is not the same quantity as a finite comparison-graph cycle count.

## 2. Bundle, connection and gauge are different data

Section 2 and A.6–A.8: printed pp. 128, 147–148; PDF pp. 4, 23–24.

For the canonical connection, a lifted path is horizontal when

```
z† zdot = 0.
```

The connection form is `omega=z†dz` (imaginary-valued); real Berry potentials require a convention such as `A=-i omega`. The canonical horizontal spaces are orthogonal to the circle fibres and respect the full unitary symmetry. Its holonomy produces Berry phase.

A global bundle can exist without a global choice of phase representative. Local sections and transition functions are not defects to eliminate. Also, a consistent connection can have nontrivial loop holonomy; global consistency does not mean every loop phase is one.

The appendix classifies circle bundles over S² using the winding of the equatorial clutching function. Associated line bundles use characters `exp(i alpha) -> exp(i n alpha)`. Tensor powers multiply the corresponding characteristic class; they are extra choices of representation, not extra bundles forced by the number of geometric cells.

## 3. The seven physical examples

| Application | What is being fibred / why Hopf appears | Source location |
|---|---|---|
| **Two-level quantum systems and Berry phase** | Normalized state vectors form S³; forgetting common phase gives pure states S². Horizontal lifting records geometric phase. | §2, printed 127–128; PDF 3–4 |
| **Two-dimensional isotropic harmonic oscillator** | On a nonzero fixed-energy shell, the phase-space variables form S³. The equal-frequency dynamics acts by a common phase, so its trajectories are the Hopf circles. | §3, printed 128–129; PDF 4–5 |
| **Taub–NUT general relativity** | SU(2) spatial geometry with an extra U(1) isometry distinguishes Hopf fibres. They enter horizon generators, NUT regimes and the global topology associated with NUT charge. | §4, printed 129–130; PDF 5–6 |
| **Twistors / Robinson congruences** | Hopf circle tangents determine directions of a special null-geodesic congruence. Opposite twistor sign relates to the anti-Hopf twist. | §5, printed 130–134; PDF 6–10 |
| **Massless helicity representations** | The base is the momentum null cone, topologically S² times a radial factor. Nonzero helicity gives nontrivial associated line bundles; fibre character is `exp(2 i lambda alpha)`. | §6, printed 134–137; PDF 10–13 |
| **Dirac magnetic monopole** | The base is spatial directions surrounding magnetic charge. Local potentials patch by a U(1) transition; quantized winding gives the monopole bundle. Unit winding gives Hopf. | §7, printed 137–140; PDF 13–16 |
| **Spin structure and Dirac operator on S²** | The Hopf bundle double-covers the oriented tangent-frame bundle of S². Its canonical connection is the spin lift of Levi–Civita transport. This enters angular separation of the ordinary Dirac equation in a central electrostatic field. | §8, printed 140–141; PDF 16–17 |

### Especially explicit example: oscillator

In the author's scaled equal-mass/equal-frequency system,

```
H = (p1^2+p2^2+q1^2+q2^2)/2,
a_k=q_k+i p_k,
a_k(t)=exp(-it) a_k(0).
```

At fixed positive H, `z_k=a_k/sqrt(2H)` lies on S³ and the physical flow is precisely the common-phase circle action. Unlike an analogy based only on an S² picture, this example identifies the total space, the fibre action and the dynamical law explicitly. Unequal oscillator frequencies do not supply this same common-phase action by that argument.

### Especially important warning: twistor circles are not light paths

Printed p. 133, PDF p. 9, explicitly distinguishes two orders of projection. Minkowski null geodesics are straight null lines, not the stereographically displayed Hopf circles. The tangent of a Hopf circle at an initial point supplies the direction used to construct the corresponding null line. This warns directly against interpreting a fibration drawing as a physical wire trajectory.

### Monopole patching does not follow merely from a Hopf picture

Printed pp. 138–140, PDF pp. 14–16, supply a magnetic field, local potentials, charged-particle covariant derivatives, and smooth transition functions. These are substantive physical inputs. Nonzero flux forbids a global potential on the surrounding sphere; it does not make the patched bundle inconsistent.

Urbantke distinguishes the transition winding n from the Chern number, which is `-n` in his stated convention. His Hopf example has transition winding one and Chern number minus one. These signs must be compared only after aligning base orientation, connection convention and associated-bundle action.

## 4. The factor of two is geometrically explicit

Printed p. 128 and pp. 140–141; PDF pp. 4, 16–17.

A phase-sensitive tangent frame is constructed from bilinear spinor expressions. Changing the spinor phase by alpha rotates that tangent frame by **2 alpha**. Consequently z and -z have the same ordinary tangent frame, while the spinor retains their distinction. The Hopf bundle is the spin bundle of S², double-covering its SO(2) frame bundle.

This gives a precise candidate meaning for a doubled twist. It does **not** prove that the operator's N-tube “double-twist” is this map. Such an identification would need an actual state/frame correspondence and an operation intertwiner, not the phrase alone.

## 5. Consequences for our Sulfur/Hopf investigation

### Supported directions

- Keep internal state, its phase-sensitive lift and the geometric presentation separate. The qubit and spin-bundle examples fit this distinction directly.
- Treat phase/frame transition records as potentially essential retained data. Nontrivial holonomy need not be erased for global consistency.
- Use the oscillator example as a template for what a convincing identification requires: explicit state space, action, projection and dynamics/operation law.
- The source-bound electron spinor bridge and complementary-frame calculations are closer to §§2 and 8 than to the magnetic-monopole interpretation.

### Corrections and boundaries

- Our `five-side-oct-hopf-probe.mjs` uses `2 Im(z0 conj(z1))` for its second base coordinate; Urbantke uses `2 Im(conj(z1) z2)` with one-based indexing. After matching variable names, these differ by reflection of the second Bloch coordinate. Sign comparisons require this orientation change to be included.
- A native vertex-link S² does not identify whether the base is state space, momentum directions, spatial directions or a tangent-frame geometry. The physical examples deliberately make different identifications.
- Neither one monopole per interior vertex nor multiplication of 44 identical-charge factors follows from this paper. Our 44-source field remains an additional reference hypothesis.
- The paired SU(2) frame does not create two independent source records. Opposite character weights or determinant cancellation alone do not identify native P/E contents.
- Nothing in these passages assigns additive, multiplicative and quartic Sulfur stages. The Hopf map is quadratic in spinor coordinates, and its norm identity is quartic, but that algebraic fact is not a quartic interaction law or a layer schedule.

## 6. Useful next reading/application question

For each proposed Sulfur interpretation, fill in the same four entries that are explicit in Urbantke's examples:

1. What is the total retained state space?
2. Which operation generates the U(1) fibres?
3. What does the base point retain and what does projection forget?
4. Which source operation supplies transport/connection, and what observes its holonomy?

The three best-supported candidates to compare are an internal two-level state, a spin lift of a directional frame, and a shared-phase dynamical orbit. The paper gives no reason to prefer spatial monopoles merely because the carrier is three-dimensional.

These are literature findings and proposed comparison criteria, not new native operation or construction admissions. No routing code was changed.
