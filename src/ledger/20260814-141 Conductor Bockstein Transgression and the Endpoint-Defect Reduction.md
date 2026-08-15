# Conductor Bockstein Transgression and the Endpoint-Defect Reduction

## Record

Date: 2026-08-14

Status: exact coefficient/character theorem and one sharp geometric blocker.
The constant part of the actual normalization--conductor square supplies the
coefficient exact sequence required by the proposed admissible/normal/defect
mapping sequence. Its Bockstein is an isomorphism from the unresolved carrier
reflection parity to the once-polarity-loaded existence obstruction. The
endpoint/\(Q\) defect restriction of the sheetwise gallery lift is still
unconstructed, so the theorem reduces but does not decide the physical
obstruction.

## Claim

Let \(G=D_3^{\rm triad}\), and let
\[
P_{\rm sh}=\mathbb Z\langle e_+,e_-\rangle
\]
be the two-sheet permutation module: rotations preserve each sheet and the
physical reflection \(f_3\) exchanges them. Entry 93's constant conductor
sequence is exactly
\[
\boxed{
0\longrightarrow\mathbb Z
\xrightarrow{\Delta}P_{\rm sh}
\xrightarrow{\operatorname{diff}}\mathbb Z_{\rm or}
\longrightarrow0,
}
\qquad
\Delta(1)=e_++e_-,
\quad
\operatorname{diff}(a e_++b e_-)=a-b .
\]
Thus the coefficient shadow of the desired mapping-complex sequence is
\[
\operatorname{Map}_{\rm adm}:\mathbb Z,\qquad
\operatorname{Map}_{\rm norm}:P_{\rm sh},\qquad
\operatorname{Map}_{\rm defect}:\mathbb Z_{\rm or}.
\]
It is integral and nonsplit equivariantly: a section would have
\(1\mapsto(a,-a)\) and hence \(2a=1\).

The connecting homomorphism is
\[
\boxed{
\partial_{\rm pol}:
H^1(G;\mathbb Z_{\rm or})
\xrightarrow{\sim}
H^2(G;\mathbb Z).
}
\]
Both groups are \(\mathbb Z/2\) by entry 138. The map is nonzero
explicitly. Let
\[
p(g)=
\begin{cases}
0,&g\text{ a rotation},\\
1,&g\text{ a reflection}
\end{cases}
\]
be the sign-valued carrier one-cocycle, and lift it sheetwise by
\(\widetilde p(g)=e_+\) on reflections and zero on rotations. Then
\[
d\widetilde p(g,h)
=\Delta\,c(g,h),
\qquad
c(g,h)
=\frac{p(g)+p(h)-p(gh)}2,
\]
and
\[
c(f_3,f_3)=1.
\]
The source and target classes both have exact order two:
\(2p\) and \(2c\) are integral coboundaries, while their reflection values
are not coboundaries. Hence the Bockstein is an isomorphism.

This corrects the interpretation of entry 138. Once-relative polarity
loading does not discard the carrier \(\mathbb Z/2\) parity. It transgresses
that parity into the loaded \(\mathbb Z/2\) existence obstruction.

## Evidence

Exact certificate:

- research/voevodsky/check_conductor_polarity_bockstein.rs
- SHA-256
  896574dabfe2293274b92593c88a23ef8b9743f93e429dd81170afaf646e29a8

It verifies the \(D_3\)-module exact sequence, equivariance, absence of an
integral equivariant section, the sign-valued one-cocycle, its sheetwise lift,
the connecting two-cocycle on every pair and every cocycle triple, and the
order-two/non-coboundary tests on the physical reflection subgroup.

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses with status=proved
~~~

Dependencies:

- entry 93: the actual two-sheet normalization--conductor sequence;
- entry 136: the canonical unpointed carrier roof;
- entry 138: the sign and loaded coefficient groups;
- entry 139: physical-reflection detection of the loaded class;
- entry 140: strict target-side reflection naturality.

Epistemic-graph admission is pending. The Marici registry advertises the
epistemic-graph surface, but the MCP loader returned Transport closed when
opening the site surface. No graph store, generated graph artifact, or MCP
configuration was edited manually.

## Boundary

This is the coefficient/character shadow of the desired mapping-complex
sequence, not its support-PC construction. In particular, the theorem does
not define
\[
r_{\partial,Q}:
\operatorname{Map}_{\rm norm}
\longrightarrow\operatorname{Map}_{\rm defect}
\]
on the actual sheetwise marked-gallery correspondence. It does not determine
whether that geometric defect has parity zero or one.

The connecting formula must therefore be written
\[
\boxed{
[\alpha_{\rm nc,abs}]_{\rm adm}
=
\partial_{\rm map}
\bigl[r_{\partial,Q}(\beta_+,-\beta_-)\bigr],
}
\]
after the endpoint/two-extension shift. Writing
\(\partial[\beta_+,-\beta_-]\) without the defect restriction is
imprecise: the sheetwise pair belongs to the normalization term, while the
connecting input is its endpoint/\(Q\) descent defect.

Here \(\partial_{\rm map}\) is the still-to-be-constructed connecting map of
the loaded mapping-complex sequence. The theorem identifies only its
coefficient/character shadow:
\[
\operatorname{gr}_{\chi}(\partial_{\rm map})
=\partial_{\rm pol}.
\]

The ring-level conductor difference alone is insufficient. Coefficientwise
the gallery homotopy is ordinary exact, as entry 133 proves. The missing
restriction must retain the based nonzero \(Q\)-leg, both endpoint connector
cells, the full Tate window, support variance, and the once-relative polarity
line. Defining it from \(K_{\rm alt}\), \(q_\Sigma\), the edge residue, or a
desired parity would be circular.

## Consequence

The next decision is now one bit before any loaded two-cocycle calculation.
Define the endpoint defect class
\[
p_{\partial,Q}
=
\bigl[r_{\partial,Q}(\beta_+,-\beta_-)\bigr]
\in H^1(G;\mathbb Z_{\rm or}).
\]
Then
\[
\boxed{
\omega_{\rm load}
=\partial_{\rm pol}(p_{\partial,Q}).
}
\]
Because \(\partial_{\rm pol}\) is an isomorphism and the target reflection
square is already \(+1\):

- \(p_{\partial,Q}=0\) gives \(\omega_{\rm load}=0\) and the unique loaded
  lift component;
- \(p_{\partial,Q}=1\) gives the nonzero obstruction and no loaded lift.

The smallest next experiment is therefore not another full \(D_3\) bar
calculation. Construct one \(f_3\)-paired endpoint/\(Q\) restriction of the
two sheetwise gallery homotopies, including its two connector cells, and
read its sign parity before applying the conductor Bockstein.

## Outcome contract

~~~json
{
  "claim": "The constant normalization-conductor sequence is 0 -> Z -> Z{+,-} -> Z_or -> 0, and its Bockstein is an isomorphism H1(D3,Z_or)=Z/2 -> H2(D3,Z)=Z/2. Once-relative polarity loading therefore transgresses carrier endpoint parity into the loaded existence obstruction.",
  "status": "proved",
  "assumptions": [
    "The physical D3 rotation preserves the two normalization sheets and f3 exchanges them.",
    "The low-degree cohomology orders are those proved independently in entry 138.",
    "The theorem is scoped to the coefficient/character shadow and does not assert a support-PC defect map."
  ],
  "evidence_refs": [
    "research/voevodsky/check_conductor_polarity_bockstein.rs",
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260814-138 Physical Polarity Loading and the Shifted Butterfly Obstruction.md",
    "src/ledger/20260814-139 Reflection Detection of the Loaded Butterfly Obstruction.md",
    "src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md"
  ],
  "factorization_test": {
    "coefficient_sequence": "exact and D3-equivariant",
    "integral_equivariant_section": "absent; would require 2a=1",
    "carrier_parity": "generator of H1(D3,Z_or)",
    "connecting_cocycle": "c(g,h)=(eps(g)+eps(h)-eps(gh))/2",
    "reflection_value": "c(f3,f3)=1",
    "bockstein": "isomorphism Z/2 -> Z/2",
    "target_reflection_square": "+1 by entry 140",
    "endpoint_Q_defect_class": "unconstructed"
  },
  "counterevidence": [
    "The module sequence does not select the endpoint/Q defect class of the geometric sheetwise gallery lift.",
    "Ordinary coefficient descent makes beta_gal removable and cannot supply the physical class.",
    "The connecting input is the defect restriction r(beta), not beta itself."
  ],
  "next_experiment": "Construct the f3-paired endpoint/Q defect restriction of the two sheetwise gallery homotopies and determine its sign parity. Apply the proved Bockstein only afterward."
}
~~~
