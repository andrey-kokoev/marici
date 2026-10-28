# Reference-covariant Ramsey certificates

## Result and stratum

The complete **mathematical certificate relation** is covariant under signed coordinate permutations, lattice translations and bijections of the color alphabet, when the region, template and optional reference are transported together. The inverse and composition laws hold on the full records, not only on a scalar color or shape.

There is a distinct native-geometry boundary: all 48 signed coordinate permutation matrices preserve the unrefined tetrahedral–octahedral carrier, but only **16** preserve the actual source's fixed octahedral primitive subdivision. Full geometric certificate covariance is not full native primitive/particle covariance.

Verification level: written all-input algebraic proof, exact Python record controls and bounded replay of the actual source macro/primitive neighbor routines. No new proof-assistant theorem, native coefficient/phase/PN/NE covariance, physical evolution or canonical witness selector is claimed.

## Frames and verification without changing the old interface

A framed instance carries a complete coloring of

$$
\Omega=z+L_N,\qquad z\in L,
$$

with globally labelled template points S, color count r and an explicit `reference` field. The reference may be absent (`null`), a labelled point with no direction, or a labelled point with a nonzero lattice direction. These are declared geometric context fields, not a physical proton or a calibrated momentum. No reference is inferred from a color or a silhouette.

To reuse the existing strict verifier, subtract z from the coloring points, witness image and translation parameter a, **but not from S**:

$$
(a-z)+mS=(a+mS)-z.
$$

The old verifier then checks the complete centered coloring, exact labels, positive integer scale, containment and homogeneity. A translated finite region is not clipped back to an origin-centered box. Reference validation and source-to-target comparison remain explicit additional checks.

## Correct action when the template also moves

Let g(v)=Qv+b, where Q is a signed coordinate permutation and b is in L. Let pi be a bijection of the r colors. Transport

$$
S'=QS+b,\qquad z'=Qz+b,
\qquad \kappa'(g(v))=\pi(\kappa(v)).
$$

Q preserves the even-sum lattice and the infinity norm. Hence g maps the entire region z+L_N bijectively onto z'+L_N, with N unchanged.

For a certificate a+mS in color q, the transformed certificate is

$$
a'=Qa+(1-m)b,\qquad m'=m,\qquad q'=\pi(q).
$$

Indeed,

$$
a'+m(Qs+b)=Q(a+ms)+b.
$$

The offset a is therefore **not generally a point transported by g**. Applying a'=g(a) while also translating S would add an erroneous extra mb to every predicted image. For m=2 and nonzero b this is already visible. If one chose the different convention S'=QS (template vectors, not transported template points), then a'=g(a) would instead be correct. This result freezes the first convention and does not mix the two.

A reference point transforms as p'=Qp+b; a direction transforms as d'=Qd, without the translation. A label remains the same label. Optional null reference/direction values remain null. The direction's role is not exchanged with the offset or with a point.

## Soundness, inverse and composition

The affine identity gives exact containment and homogeneous color of the transported labelled image. Label bijections and m>0 preserve distinctness. Complete coloring coverage follows from the region bijection and color permutation. Thus the map sends every valid source record to a valid target record.

Its inverse uses Q transpose, translation -Q transpose times b and inverse palette permutation. Substitution recovers each source point, image, reference and offset exactly, so it is a bijection of certificate relations.

For outer (Q2,b2,pi2) after inner (Q1,b1,pi1), the composite is

$$
(Q_2Q_1,\ Q_2b_1+b_2,\ \pi_2\circ\pi_1).
$$

Applying the offset formula twice yields

$$
Q_2Q_1a+(1-m)(Q_2b_1+b_2),
$$

exactly the direct composite offset. Point, direction, template, region and palette formulas compose by the same respective laws. Identity maps fix the entire supplied record. No selection of a preferred witness is needed: this is covariance of the **relation**, not an equivariant deterministic search policy.

Validity alone does not certify a particular transport. Two instances with different legitimate references can have the same geometric witness. `check_transport` therefore compares the whole target instance and certificate against the specified source/map before accepting the transport. A wrong but well-typed reference is not silently accepted as that map's result.

## Actual source subdivision boundary

`makeLatticeItem` uses a fixed four-tetrahedron subdivision of each octahedron. Its retained diagonal has physical direction (0,1,0). A signed coordinate permutation preserves that diagonal choice precisely when it sends this axis to itself up to sign. There are 2 permutations of the other axes and 8 sign choices: 16 matrices. The condition is closed under composition and inverse. Lattice translations preserve the choice as well.

The remaining 32 matrices still carry macro cells and macro-face adjacency correctly, but change the internal primitive subdivision. They are not admitted as symmetries of the fixed primitive presentation. Transporting a refinement index could support a broader comparison family; this packet does not adopt a new native subdivision or supply its coefficient histories.

The actual-source checker compares transformed macro vertices and `acrossFace` neighbors for all 48 matrices. For the 16 subdivision-preserving matrices it additionally checks `LocalPrimitiveGeometry.neighbor` on all source primitive faces of representative upright/inverted tetrahedra and an octahedron. This is geometric primitive covariance, not proof that native reader roles, coefficients or phase witnesses also transform.

## Evidence and scope

- Implementation: `research/voevodsky/ramsey_transport.py`.
- Prospective scope: `research/voevodsky/contracts/ramsey-reference-covariance-attempt.v1.json`.
- Python/combined checker: `research/voevodsky/checkers/check_ramsey_reference_covariance.py`.
- Actual geometry checker: `research/voevodsky/checkers/check_ramsey_transport_geometry.mjs`.
- Receipt: `research/voevodsky/results/ramsey-reference-covariance-v1.json`.
- Source geometry receipt: `research/voevodsky/results/ramsey-transport-geometry-v1.json`.

Finite controls supplement the algebraic all-input proof. Existing source subdivision work (`research/strominger/fcc-toroidal-field-v1.md`) already distinguished macro actions from fixed primitive actions; this packet reuses that warning and freshly checks the larger declared signed-permutation family. No old proof outcome is silently imported, and no production source is modified.

The certificate-layer covariance node can close at this scope. Stronger native-process transport, a faithful forcing realization and common-witness assembly remain separate obligations. Nothing here derives a physical law from coordinate transport.
