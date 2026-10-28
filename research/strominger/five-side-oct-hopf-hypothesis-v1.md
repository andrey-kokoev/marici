# Hopf hypothesis: a concrete local candidate, not an identification of the current wires

**Result:** the literal global interpretation does not fit the current carrier/wiring. A more relevant **local Hopf lift over native vertex-link spheres** now has concrete geometric support. Its phase/packet binding is still unproved. No routing or renderer was changed.

## 1. Locate the sphere before assuming the fibration

The [comparison-domain calculation](five-side-oct-comparison-domain-v1.md) found 44 residual diagrams per reading. These are not arbitrary N-connected components: they are exactly the stars of the **44 interior native vertices**.

Each star contains:

- four P tetrahedra;
- six N octahedra;
- four E tetrahedra.

Its link of directions is a cuboctahedral two-sphere: 12 vertices, 24 edges and 14 faces (eight triangles and six squares). The 12 radial directions are exactly the normalized permutations of `(±1,±1,0)` in the orthogonal native coordinates.

All six readings identify the **same 44 sites**, not 264 independent objects. For each site the 16 path presentations visit precisely the 14 cells of that star. This is checked by exact cell identities and geometry, not inferred from equal counts.

## 2. The residual comparison cycle sweeps that sphere

A comparison move replaces one native two-interface presentation by another. Its four involved cells surround an actual native edge incident to the star vertex. That edge defines a quadrilateral face in the **dual link**.

The checker maps an oriented comparison cycle to an **integer 2-chain** of these dual faces. It checks the integer boundary, rather than merely reducing modulo two:

- cycles of disjoint substitutions sweep the zero chain;
- the nonzero residual basis cycles sweep all twelve dual quadrilaterals once, with coherent orientations;
- their degrees relative to the first oriented sphere sweep are `+1` or `−1`.

A representative at `-1,-1,2,1` has sweep degrees `0,+1,−1,0,0` for the retained graph-cycle basis. The two nonzero basis sweeps represent opposite choices of the same fundamental sphere class, not two independent residuals.

The construction verifies this at every interior vertex in all six readings. A mutation removing a step from a sphere sweep is rejected because its integer boundary is no longer zero.

**This is the new connection to the Hopf question:** the previously unnamed residual is geometrically a sweep of a native direction sphere. It is not merely an unexplained graph-cycle count. This still does not supply any native phase transport.

## 3. Hopf spinor lift versus ordinary direction frames

For a normalized complex pair `z=(z0,z1)` define

\[
h(z)=(2\operatorname{Re}(z_0\bar z_1),\;2\operatorname{Im}(z_0\bar z_1),\;|z_0|^2-|z_1|^2).
\]

Common phase multiplication leaves `h` unchanged. Its fibres are circles. On the equator `n=(cos φ,sin φ,0)` choose sections

\[
s_N=(1,e^{-i\phi})/\sqrt2,\qquad
s_S=(e^{i\phi},1)/\sqrt2=e^{i\phi}s_N.
\]

The transition has degree **one**. Thus a degree-one native link-sphere sweep is exactly the sort of base sphere on which a Hopf spinor lift would require nontrivial circle transition data.

There is an important alternative. Ordinary oriented direction frames have total space `SO(3)`, not `S³`, and their circle transition has degree **two**. The checker constructs tangent frames from the spinor sections, verifies that `z` and `−z` give the same ordinary frame, and obtains transition degree two. Retaining the spinor sign gives the double-cover lift and degree one.

Therefore the native construction must select and bind **spinor lift versus ordinary frame**, not just exhibit an S². The “double-twist” language alone does not choose between them. The geometric frame test supplies neither native coefficient operations nor a signed-pair interpretation.

In the Hopf long exact sequence, the boundary map `π₂(S²) → π₁(S¹)` is an isomorphism (up to orientation). A once-swept sphere requires a once-wound fibre transition. It cannot be handled by silently setting every phase comparison to identity. For the ordinary frame bundle the corresponding degree is two. Which, if either, describes the retained native comparisons remains the decisive binding question.

## 4. Why the literal global carrier interpretation fails

The unmodified carrier is a solid octahedron with boundary, not the Hopf total space `S³`. Independent cellular homology over F₂ gives:

| Complex | Betti numbers | Euler characteristic |
|---|---|---:|
| Solid carrier | `(1,0,0,0)` | 1 |
| Boundary | `(1,0,1)` | 2 |
| Relative carrier/boundary | `(0,0,0,1)` | −1 |

The chain matrices satisfy boundary-squared-zero. Deleting a cell face is rejected. A compact circle bundle cannot have the carrier's Euler characteristic one.

One can **add** the quotient `B³/∂B³ ≅ S³` and place a standard Hopf fibration on it. The probe does this explicitly, rather than implying it is already the native model. In orthogonal coordinates the octahedron is `|x|₁ ≤ R`, with `R=5`. Set `d=R−|x|₁` and

\[
q(x)=\frac{(2dx_1,2dx_2,2dx_3,|x|^2-d^2)}{|x|^2+d^2}.
\]

Every boundary point maps to `(0,0,0,1)`. The interior map is radial compactification followed by inverse stereographic projection. The reference common-phase action moves that collapsed boundary class into the interior; it is not a boundary-preserving action on the original 3-ball.

Eighty arbitrarily selected reference fibres pass phase-invariance, chart round-trip, and section tests, with errors below `2×10⁻¹⁴`. The number eighty is just the number sampled; Hopf topology did not select it. This reference is a positive control, not a new realization of the retained 80 fibres.

The current unvalidated port candidate has 320 open slot paths and no closed slot paths. Under the explicitly stated global reference projection, **all 340 displayed N channels change base point**; minimum measured drift is about `0.089`. They are not Hopf fibres of that map. This does not exclude another source-justified map, and it does not test or refute the local frame-bundle hypothesis of sections 1–3.

## 5. A naive signed-pair binding also fails

If the four native direction pairings are interpreted as literal complex signs, common phase identifies

```
++ with --
+- with -+
```

at the Hopf base. For generic nonzero coordinates there are only two distinct base values, not four. The phase coordinate can retain distinctions along a fibre, but then these four records are not four distinct base fibres.

The operator's signs denote directions, not established complex-amplitude signs. This is a conditional test rejecting a tempting identification—not a contradiction in the operator's specification.

## 6. What remains to establish

The promising hypothesis is now precise:

> Do the retained native comparison maps on each vertex star realize the degree-one spinor lift of its direction sphere, and do those lifts agree on overlapping stars?

Required work:

1. Identify the actual native state/packet coordinates and their context maps. The names P and E do not alone supply two complex scalar coordinates.
2. Determine whether native transport retains a spinor sign and a common circle action, or only ordinary frames, or neither.
3. Evaluate the actual comparison loop against the integer sphere-sweep witness; recover its transition winding without inserting the reference phase by hand.
4. Verify compatible lifts and histories across all overlapping stars, entry/exit presentations and the boundary.
5. Bind that result to the 80 retained fibres. Neither 44 vertex stars nor the reference's 80 sampled circles supplies this binding by count.

The eta-squared notes (`the-first-irreducible-five-point-residue-is-eta-squared.md` and `the-eta-squared-moore-cycle-is-explicit-before-artin-expansion.md`) concern a specified class in `π₄(S²)`. They do not identify this native sphere sweep or supply its phase lift. No inference from GF(2) counts to eta-squared is made.

## Reproduce

```sh
node --test tests/five-side-oct-hopf-probe.test.mjs
node research/strominger/checkers/check_five_side_oct_hopf_hypothesis.mjs --record
```

Implementation: `five-side-oct-hopf-probe.mjs`.
Receipt: `results/five-side-oct-hopf-hypothesis-v1/verification.json`.

Eight tests check carrier homology, chart/boundary behavior, phase orbits, patch transitions, the spin/frame distinction, native link geometry, exact integer sphere sweeps and rejection of the current channels under the declared reference projection. The receipt retains `constructionAdmitted: false` and `nativeHopfBinding: not established`.
