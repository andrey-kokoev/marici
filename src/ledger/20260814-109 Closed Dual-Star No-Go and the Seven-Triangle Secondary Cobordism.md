# Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism

## Record

Date: 2026-08-14

Status: proved for the carrier-level dual-star no-go, the scoped integral
seven-triangle cobordism, and its ambient relative-chain triviality. A loaded
Morse/conductor comparison and the secondary specialization class remain
unconstructed.

## Claim

Entry 108 proposed the relative closed dual star of the expanded marked
gallery as the smallest kernel that might cross from

\[
\widetilde F_1\subset\widetilde F_2
\]

into the quotient

\[
Q=\widetilde F_2/\widetilde F_1.
\]

That proposal is false as stated. For the natural closed dual-star pair, the
full coface poset has the top cell as a minimum and the \(\widetilde F_1\)
coface poset contracts through the common short facet \(x_3\). Hence both
spaces are contractible and their relative homology vanishes. More
concretely, the natural endpoint-star repair also fails:

\[
N_{\widetilde F_1}\cup N_{\partial G}=N_{\widetilde F_2},
\]

so its proposed relative complex is literally zero.

The exact barycentric census identifies a smaller, useful object, but with a
different interpretation. In the cone-per-gallery-edge ansatz the three
expanded gallery edges have quotient cofaces

\[
e_c:\{\mathrm{top}\},\qquad
h_E:\{\mathrm{top}\},\qquad
e_r:\{\mathrm{top},D03\}.
\]

Thus there are exactly two apex assignments in that ansatz:

\[
(\mathrm{top},\mathrm{top},\mathrm{top}),
\qquad
(\mathrm{top},\mathrm{top},D03).
\]

After stipulating the marked \([\mathrm{top}<D03]\) direction and requiring
radial cancellation, the mixed assignment has a seven-triangle integral
carrier

\[
T_\nu
=
\sum_{r=e_c,h_E,e_r}
\bigl([q_r,r,R_r]-[q_r,r,L_r]\bigr)
-[\mathrm{top},D03,b_D].
\]

Let \(G\) denote its special gallery side and

\[
J_\nu
=-[\mathrm{top},a]
+[\mathrm{top},D03]
+[D03,c]
\]

its generic endpoint-relative side. The exact integral identity is

\[
\boxed{dT_\nu=G-J_\nu,\qquad d^2T_\nu=0.}
\]

Since \(G\subset\widetilde F_1\), this becomes

\[
dT_\nu=-J_\nu
\quad\text{in}\quad
C_*(\widetilde F_2,\widetilde F_1).
\]

Therefore

\[
\boxed{[J_\nu]=0
\text{ in }
H_*(\widetilde F_2,\widetilde F_1).}
\]

The seven-triangle object is a secondary cobordism or chosen
nullhomotopy—not a surviving primitive class of \(Q\).

## Occurrence boundary

On the primal gallery, the established lcm labels force the radial junction
equations

\[
X_{03}c_{e_c}=c_h=x_1c_{e_r}.
\]

Their primitive polynomial solution is

\[
(c_{e_c},c_h,c_{e_r})
=(x_1,X_{03}x_1,X_{03}),
\]

and therefore reproduces

\[
\widetilde\xi
=x_1e_c+X_{03}x_1h_E+X_{03}e_r.
\]

This calculation proves the primitive lcm syzygy on the gallery. It does
not yet prove that a variance-correct pullback of the absolute occurrence
cosheaf to the barycentric carrier has this differential. The current
junction matrix is a necessary coefficient model; the actual loaded
subdivision/Verdier incidence bimodule and its weighted \(d^2=0\) remain to
be constructed.

## Correct secondary formula objective

The vanishing of \([J_\nu]\) does not rule out a secondary boundary
realization. It changes its type.

Work in a dg enhancement. Let

\[
q_J:J\longrightarrow Q,
\qquad
e_F:Q\longrightarrow F_0[2],
\]

and suppose the loaded Morse carrier produces

\[
h_{\rm Morse}\in\operatorname{Hom}^{-1}(J,Q),
\qquad
dh_{\rm Morse}=q_J.
\]

A conductor/Cousin construction must independently produce a second
trivialization

\[
H_{\rm cond}\in\operatorname{Hom}^{1}(J,F_0),
\qquad
dH_{\rm cond}=e_Fq_J.
\]

Only then is the difference

\[
\boxed{
\Delta_J
=H_{\rm cond}-e_Fh_{\rm Morse}
}
\]

closed, with

\[
[\Delta_J]\in\operatorname{Ext}^1(J,F_0).
\]

Equivalently, the pullback \(q_J^*e_F\) is the zero two-extension and the
Morse and conductor constructions are two proposed splittings; their Baer
difference is the secondary class. If the choices are not fixed, its exact
indeterminacy is

\[
e_{F*}\operatorname{Ext}^{-1}(J,Q)+I_{\rm cond}
\subseteq\operatorname{Ext}^1(J,F_0).
\]

To compare this class with entry 108's local generator requires an
independently constructed purity map

\[
\boxed{
\Phi_{J,+}:
R\!\operatorname{Hom}(J,F_0)
\longrightarrow
C_{03}^{\rm exit}
=[R\xrightarrow{U_{03}}R].
}
\]

The aspirational equality is now

\[
\boxed{
\Phi_{J,+}([\Delta_J])
\stackrel{?}{=}
[1]\in R/(U_{03}).
}
\]

This is a design specification, not a construction. At present the ordinary
conductor contraction and the seven-triangle carrier solve different
equations in different categories. Subtracting them before building the
common loaded mapping complex would merely rename the missing
specialization map.

## Evidence

Exact certificates:

- `research/voevodsky/check_d03_relative_dual_star_carrier.rs`
- `research/voevodsky/check_d03_endpoint_relative_morse_sector_triads.rs`

SHA-256:

```text
0e50675e63d1bf34c518d3f00112b3b7ded2be1e3ffca852f7899aa1f3f74a0d
906f3dc9e23d4a75196edf562e32424c5fff577abba8a74ef7cadaf78f32f66a
```

The first certificate compares three natural meanings of the relative dual
star and proves that none simultaneously supplies full gallery support,
intrinsic \(D03\) typing, and the lcm boundary. The second constructs the
scoped mixed carrier and verifies the integral identities
\(dT_\nu=G-J_\nu\) and \(d^2T_\nu=0\), while explicitly reporting the
ambient derived \(Q\)-class as zero and all loaded/purity claims as open.

## Boundary

- The phrase “dual star of a subcomplex” is not a canonical kernel. The
  strict \(D03\) star sees only the final gallery edge; the common top cone
  loses \(D03\) typing; the full closed star is too large and acyclic.
- The mixed carrier is unique only in the stipulated cone-per-edge ansatz
  after requiring the marked \([\mathrm{top}<D03]\) edge and radial
  cancellation. This is not yet uniqueness among stratified Morse sectors.
- Containment of \([\mathrm{top}<D03]\) is a marked-edge predicate, not yet a
  comparison with the independently ordered physical \(D03\) normal.
- The unweighted carrier differential is proved. A variance-correct loaded
  pullback of \(\mathcal P_{\rm abs}\), its weighted \(d^2=0\), and its
  subdivision counit are not.
- The isolated path has \(H_1(J,\{a,c\})\simeq\mathbb Z\), but its image in
  the ambient relative complex is exact. These statements are compatible;
  confusing them caused the discarded positive claim.
- No conductor trivialization \(H_{\rm cond}\), common mapping complex, or
  purity quasi-isomorphism \(\Phi_{J,+}\) has been constructed.

## Next experiment

Construct the variance-correct loaded Morse cobordism before attempting the
secondary comparison. The required theorem is

\[
\boxed{
dH_{\rm Morse}^{\rm abs}
=q_J^{\rm abs}-\widetilde\xi^{\rm abs},
\qquad
d^2=0,
}
\]

where every coefficient comes from the pullback of the 215-generator
absolute occurrence complex through an explicit barycentric
incidence/Verdier kernel. The same construction must compare the marked
\([\mathrm{top}<D03]\) edge with the ordered physical normal.

If this succeeds, define one common mapping complex

\[
M=R\!\operatorname{Hom}(J,F_0)
\]

with all occurrence-dual, support, and localization shifts retained. Only
then construct \(H_{\rm cond}\), verify that both homotopies have differential
\(e_Fq_J\), compute the indeterminacy, and evaluate their difference.

## Outcome contract

```json
{
  "claim": "The natural relative closed-dual-star kernel is acyclic. A marked mixed seven-triangle carrier exists as an integral secondary cobordism with dT=G-J and d2=0, but its generic path is exact in the ambient Q complex. The desired scalar half-symbol must therefore arise, if at all, as a loaded secondary difference of two independently constructed trivializations rather than as ordinary Q restriction.",
  "status": "proved",
  "assumptions": [
    "The corrected D03 stellar subdivision and filtration are those of entries 105-108.",
    "The seven-triangle uniqueness claim is restricted to the cone-per-gallery-edge ansatz with a stipulated marked D03 edge and radial-cancellation condition.",
    "The occurrence lcm equations are presently the primal-gallery coefficient model, not a proved barycentric Verdier pullback."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_relative_dual_star_carrier.rs",
    "research/voevodsky/check_d03_endpoint_relative_morse_sector_triads.rs",
    "ledger entries 105-108"
  ],
  "factorization_test": {
    "natural_closed_dual_star": "falsified: relative acyclic",
    "natural_endpoint_star_repair": "falsified: relative complex zero",
    "seven_triangle_integral_cobordism": "passed",
    "ambient_Q_class_of_generic_path": "falsified: exact",
    "loaded_barycentric_occurrence_pullback": "unconstructed",
    "secondary_Toda_Baer_class": "well-typed objective only",
    "evaluation_to_local_unit": "unconstructed"
  },
  "counterevidence": [
    "The full and F1 closed coface stars are contractible.",
    "The seven-triangle identity itself gives dT=-J modulo F1.",
    "The conductor and Morse homotopies are not yet elements of one mapping complex."
  ],
  "next_experiment": "Construct the actual P_abs-loaded barycentric Morse differential and ordered-normal comparison; prove dH_Morse=q_J-xi_tilde and d2=0 without fitted coefficients."
}
```
