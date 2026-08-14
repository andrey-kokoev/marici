# Canonical Peripheral Roof and the Cross-Geometry Purity Gap

## Record

Date: 2026-08-14

Status: proved as a formal theorem for any strict global unlocalized
support--PC filtration, with the integral occurrence/carrier realization
checked exactly. The existence of that global loaded filtration and the
cross-geometry conductor purity map remain conditional. Two proposed
shortcuts are falsified: entry 38 does not itself supply that purity map, and
the half-symbol is not a literal spectral-sequence \(d_2\).

## The peripheral arrow is formal

Assume that an absolute unlocalized facewise support--PC complex \(C\) has
been constructed on the actual scalar filtration

\[
v_+\subset B_{\rm short}\subset K_6
\]

and that its internal normal, Cech, can--var, occurrence, and Cousin
differentials preserve the corresponding closed support subcomplexes. Set

\[
F_0=PC_{\rm supp}(v_+),\qquad
F_1=PC_{\rm supp}(B_{\rm short}),\qquad
F_2=C=PC_{\rm supp}(K_6),
\]

\[
P=F_1/F_0,\qquad E=F_2/F_0,\qquad R=F_2/F_1.
\]

Then the short exact sequence

\[
0\longrightarrow P\longrightarrow E\longrightarrow R\longrightarrow0
\]

already forces the loaded peripheral transgression. It is the off-diagonal
block of the differential on \(E\), equivalently the canonical roof

\[
\boxed{
R\xleftarrow{\sim}\operatorname{Cone}(P\to E)
\longrightarrow P[-1].
}
\]

Thus \(\delta^F:R\to P[-1]\) is not a second geometric arrow to be guessed,
fitted, or inverted. Its chain identity

\[
d_P\delta^F+\delta^F d_R=0
\]

is the square-zero identity for the block differential. The filtration also
canonically supplies the Yoneda two-extension

\[
\boxed{
e_F=
[0\to F_0\to F_1\to F_2/F_0\to F_2/F_1\to0]
\in\operatorname{Ext}^2(R,F_0).
}
\]

No strict global inverse, \(t^{-1}\), normal inverse in the base ring, or
division by three occurs in this construction.

## Exact realization and scope

The occurrence-loaded cellular model realizes the formal theorem over the
unlocalized occurrence ring. On every actual face incidence,

\[
w(S)X_a=w(S\cup\{a\}),
\]

so the weighted differential is a diagonal conjugate of the integral
cellular differential without inverting a normal parameter. The exact face
ranks are

\[
C_*(K_6)=(1,9,21,14),
\]

and the quotient ranks in descending cell degree are

\[
P=(0,6,21,13),\qquad
E=(1,9,21,13),\qquad
R=(1,3,0,0).
\]

The checker verifies the block decomposition, roof, Yoneda extension,
nonnegative Rees shifts, \(D_3\)-covariance, ordered orientations, and the
saturated entry-103 carrier shadow.

The exact certificate is

- `research/voevodsky/check_loaded_peripheral_transgression.rs`

with SHA-256

```text
0668e9335babe2c9e9de1b728bcafb5f1b4fcb5d3d97c540859025e9481a5fc8
```

Reproduce with:

```powershell
$src = "research/voevodsky/check_loaded_peripheral_transgression.rs"
$exe = Join-Path $env:TEMP "check_loaded_peripheral_transgression.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json | Out-Null
```

This does **not** prove that the required absolute unlocalized
\(PC_{\rm supp}(K_6)\) already exists. Entry 38 gives the facewise PC model
only after finite-nonresonant localization of the relevant \(q_E-1\)
factors. Entry 100 gives three local unlocalized packets, but it does not glue
them into the absolute complexes \(F_0\subset F_1\subset F_2\) with all
lower-Cousin maps. The loaded theorem therefore remains conditional exactly
at this global existence step.

## The remaining arrow is purity

Entry 103 formulated a cospan with two apparently missing loaded arrows.
The formal roof removes one of them. What remains is a cross-geometry purity
comparison. Verdier duality applied to \(e_F\) gives

\[
\mathbb D(e_F):\mathbb D(F_0)[-2]\longrightarrow\mathbb D(R).
\]

The minimal source theorem is therefore an independently constructed
equivalence, with all convention-dependent shifts made explicit,

\[
\boxed{
\operatorname{pur}_+:
\mathcal S_+^{\rm cond}\xrightarrow{\sim}\mathbb D(F_0)[-2].
}
\]

The candidate half-symbol is the secondary composite

\[
\boxed{
A_+^{\rm sec}=\mathbb D(e_F)\circ\operatorname{pur}_+:
\mathcal S_+^{\rm cond}\longrightarrow\mathbb D(R).
}
\]

Equivalently, once the source leg \(\alpha_+\) and the formal peripheral leg
are both present, the unsplit chain object is

\[
\operatorname{holim}
(\mathcal S_+^{\rm cond}\to P\leftarrow R)
\simeq\operatorname{Cone}(\alpha_+-\delta^F)[-1].
\]

This is a Verdier-dual Yoneda two-extension, or a Toda shadow after choices.
It is not a literal differential in the spectral sequence of the carrier
filtration: entry 103 proves that

\[
d_1:H_2(K_6,B_{\rm short})
\xrightarrow{\sim}H_1(B_{\rm short},v_+)
\]

is already an isomorphism, so the relevant \(p=2\) class does not survive to
an \(E_2\)-page on which such a \(d_2\) could act.

## Two type corrections

First, entry 38 does not construct \(\operatorname{pur}_+\). Its worldsheet
normal-torus coefficient and the scalar normalization--conductor occurrence
coefficient are independent layers. A proof of purity needs an actual
formal-support map, a dualizing orientation, and an extraordinary-pullback
comparison; analytic nonresonant localization cannot substitute for them.

Second, the local traces of entry 100 are not literal restrictions of
\(\delta^F\). A road restriction of \(\delta^F\) starts from \(K(I_i)\), while
the local trace starts from

\[
K(I_+^\vee)\otimes K(I_i),
\]

including a reciprocal conductor factor and a repeated-normal excess line.
The correct comparison is a derived Beck--Chevalley two-cell after both legs
of the correspondence have been constructed.

## Smallest next experiment

Construct the absolute loaded costalk of \(v_+\) on its eight-cell Boolean
coface block and one actual formal-support purity square over the marked
\(D=03\) face. Its derived pullback must produce, without fitting,

\[
\eta_{3,\rm mix}
=-q_3\ell_3^{+,\vee}\otimes p_3^{03}
-p_3^{+,\vee}\otimes\ell_3^{03},
\]

followed by the residue

\[
[1/(u_0u_1u_3u_5)],
\]

the two unit endpoints \((1,1)\), and the independently oriented positive
physical line \([dX_{03}]\). Only after this one square passes should it be
rotated through the other roads and inserted into
\(\operatorname{Cone}(\alpha_+-\delta^F)[-1]\).

## Outcome contract

```json
{
  "claim": "For any strict global unlocalized facewise support-PC loading of v+ subset B_short subset K6, the peripheral transgression is canonically forced by the quotient filtration as a cone roof and Yoneda two-extension; the occurrence/carrier realization is exact. The global loaded support complex and the conductor purity equivalence remain unconstructed.",
  "status": "conditional",
  "assumptions": [
    "A global unlocalized PC_supp(K6) exists and its normal, Cech, can-var, occurrence, and Cousin differentials preserve the actual closed support filtration.",
    "Occurrence variables and monodromy variables remain independent.",
    "Verdier shifts and determinant lines are retained explicitly."
  ],
  "evidence_refs": [
    "research/voevodsky/check_loaded_peripheral_transgression.rs",
    "research/voevodsky/conductor_vertex_purity_audit.md",
    "ledger entries 38, 100, and 103"
  ],
  "factorization_test": {
    "formal_roof_and_chain_identity": "passed",
    "Yoneda_two_extension": "passed",
    "occurrence_realization": "passed unlocalized",
    "integral_carrier_and_D3_covariance": "passed",
    "global_unlocalized_support_PC": "unconstructed",
    "conductor_vertex_purity": "unconstructed",
    "local_excess_compatibility": "requires a Beck-Chevalley two-cell"
  },
  "counterevidence": [
    "Entry 38 works only in the finite-nonresonant facewise model and does not identify the scalar conductor with the worldsheet vertex costalk.",
    "A literal restriction of the peripheral arrow is source-mistyped relative to the entry-100 trace.",
    "The carrier d1 is an isomorphism, so the candidate is not a literal spectral-sequence d2."
  ],
  "next_experiment": "Construct the v+ absolute loaded costalk and one D03 formal-support purity square; verify eta_3,mix, the simple-pole residue, endpoints (1,1), and the positive physical normal line before D3 rotation."
}
```
