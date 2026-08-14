# Absolute Support Complex, Shift-Corrected Purity, and the Marked-Correspondence Obstruction

## Record

Date: 2026-08-14

Status: one scoped theorem and one sharp blocker. The absolute unlocalized
original-twist/Borel--Moore support complex exists integrally, and the local
positive-conductor purity shift is forced after fixed-nonzero-\(\beta\),
characteristic-zero Koba--Nielsen completion. The literal \(D03\) pullback of
the resulting filtration class is exactly zero, whereas the established
Cousin trace is nonzero. Consequently the full chain map
\(G_{03}^{\rm Cousin}\) remains unconstructed at one precisely typed marked
ringed-support correspondence.

## The absolute unlocalized complex

Let \(K_6\) be the labelled hexagon associahedron. A generator is a pair
\([S,H]\), where \(S\) is a noncrossing dissection and \(H\subseteq S\)
records the normal-circle directions retained at its boundary face. Work
over the tensor product of the polynomial occurrence ring \(\mathbb Z[X_D]\)
with the universal monodromy ring, writing \(u_D=q_D-1\). Occurrence and
monodromy variables are independent.

With \(\epsilon(S,a)\) the cellular incidence sign and
\(\operatorname{pos}_H(h)\) the ordered-normal sign, define

\[
\boxed{
d[S,H]
=
\sum_{a\ {m addable}}
\epsilon(S,a)X_a[S\cup\{a\},H]
+(-1)^{3-|S|}
\sum_{h\in H}
(-1)^{\operatorname{pos}_H(h)}u_h[S,H\setminus\{h\}].
}
\]

The radial term is the original-twist costandard map
\(\operatorname{var}=1\), with the independent occurrence coefficient
\(X_a\). The normal term is \(\operatorname{can}=u_h\). The two terms
anticommute, so \(d^2=0\) without inverting \(X_D\), \(u_D\), a Rees
parameter, or an integer.

The exact census is

\[
215\ \text{generators},
\qquad
(\operatorname{rk}C_0,\operatorname{rk}C_1,
  \operatorname{rk}C_2,\operatorname{rk}C_3)
=(14,63,93,45).
\]

The actual closed supports give strict \(D_3\)-stable subcomplexes

\[
\boxed{
F_0=PC_{\rm supp}(v_+)
\subset
F_1=PC_{\rm supp}(B_{\rm short})
\subset
F_2=PC_{\rm supp}(K_6),
}
\]

of total ranks \(8\subset208\subset215\). Thus the hypothesis left open in
entry 104 is now realized. Its canonical cone roof and Yoneda class

\[
e_F=
[0\to F_0\to F_1\to F_2/F_0\to F_2/F_1\to0]
\in\operatorname{Ext}^2(F_2/F_1,F_0)
\]

are honest unlocalized objects. After adjoining the relevant \(u_D^{-1}\),
the normal contraction \(p_D\mapsto u_D^{-1}h_D\) recovers the facewise
nonresonant packet of entry 38.

## The local purity shift is forced

The costalk \(F_0\) is exactly one eight-generator original three-normal
packet

\[
F_0=K(u_1,u_3,u_5).
\]

It must not be tensored with a second Boolean carrier. For one normal, the
standard/costandard packets pair perfectly by

\[
K(u)\otimes K(u^\vee)\longrightarrow R[1],
\qquad
\beta(p,\ell^\vee)=1,
\qquad
\beta(\ell,p^\vee)=-q,
\]

where \(u^\vee=q^{-1}-1=-q^{-1}u\). Hence the ordered triple gives

\[
K(I_+^\vee)\simeq\mathbb D(F_0)[3],
\qquad
I_+^\vee=(u_1^\vee,u_3^\vee,u_5^\vee).
\]

Two independent geometric placements fix the remaining shift:

1. codimension-three Thom duality contributes \([-3]\);
2. \(J_+/J_+^2\) is annihilated by \(J_+\), so the first normal symbol is
   supported on \(\widetilde Z_+\), the terminal degree-two term of the
   normalization--Čech total, and contributes \([-2]\).

Therefore, in the stated homological convention,

\[
\boxed{
\mathcal S_{+,\mathrm{loc}}^{\mathrm{cond}}
=K(I_+^\vee)[-5]
\xrightarrow{\sim}
\mathbb D(F_0)[-2].
}
\]

The cross-geometry comparison uses

\[
q_j=\exp(\beta x_j),
\qquad
u_j=\beta x_jv_j(x_j),
\qquad v_j(0)=1,
\]

at fixed nonzero \(\beta\) in a characteristic-zero completed coefficient
ring. This is one base change of one Kummer packet; the occurrence variable
\(x_j\) remains a coefficient. It is not a universal integral purity
theorem.

The tempting double-loaded source is ruled out homologically. The full
entry-99 augmented carrier has a saturated integral contraction, so its
tensor product with the termwise-free reciprocal packet is acyclic. In
contrast,

\[
H_0(F_0)=R/(u_1,u_3,u_5)\ne0.
\]

The mismatch is structural, not merely the corroborating count \(64\ne8\).

## The exact \(D03\) blocker

The absolute complex makes the next comparison decidable. In the literal
\(D03\) road packet, the off-diagonal boundary lands in a strict
\(D03\)-supported subcomplex \(G_{03}\subset F_1\) which is disjoint from
\(F_0\). The first connecting morphism therefore lifts through \(G_{03}\),
and its Yoneda product with
\(0\to F_0\to F_1\to F_1/F_0\to0\) vanishes:

\[
\boxed{
\operatorname{pb}^{\mathrm{lit}}_{03}(e_F)=0.
}
\]

But entry 100's independently constructed local Cousin trace obeys

\[
\boxed{
\Theta_{03}^{\mathrm{loc}}(\eta_{3,\mathrm{mix}})
=
\left[\frac{1}{u_0u_1u_3u_5}\right]\ne0.
}
\]

Thus the local trace is not a literal road restriction of the filtration
class. This falsifies that shortcut, not a derived factorization
correspondence.

The first missing arrow is now exact. The marked road endpoint
\(\{D03,x_1,x_3\}\) and the central conductor vertex
\(v_+=\{x_1,x_3,x_5\}\) are related by removing \(D03\); they are not joined
by a face inclusion in the absolute complex. One must construct a marked,
ringed support correspondence across this central flip. Neither the support
filtration nor the one-normal perfect pairing supplies it automatically.

## Consequence for the formula objective

The absolute scalar differential and the local source placement are now
fixed. The remaining formula is not a new differential but a correspondence
component

\[
\boxed{
\Gamma_{+;03}^{\mathrm{mark}}:
\mathcal S_{+,\mathrm{loc}}^{\mathrm{cond}}
\dashrightarrow
\mathbb D(F_2/F_1)
}
\]

whose composition with the canonical Yoneda class must induce

\[
\eta_{3,\mathrm{mix}}
\longmapsto
[1/(u_0u_1u_3u_5)],
\]

the two endpoint values \((1,1)\), and the separate positive physical normal
line \([dX_{03}]\). It must arise from the marked normalization--conductor
and central-flip geometry, not be defined by these required values.

Only after this one correspondence and its Beck--Chevalley two-cell exist can
one assemble the full

\[
G_{03}^{\rm Cousin}:
(\mathcal S_F^{\rm sp},d_{\rm sp,sc})
\longrightarrow
(\mathcal R_{03}^{\rm circ,PC},d_{\rm circ}^{\rm PC})
\]

and test factorization naturality. The north-star objective remains open,
but its first unconstructed datum is now singular and geometric.

## Evidence

Exact certificates:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, SHA-256
  `55234ea577d528838bf91d7a641947ee79c51f24fa48c0915221a8e168cb9d2d`;
- `research/voevodsky/check_d03_formal_support_purity.rs`, SHA-256
  `f3a585c5a2091f2b500b9c76f878be83e4e48f676f648acde64ab828ed2be0d1`.

The entry-104 certificate remains unchanged at
`0668e9335babe2c9e9de1b728bcafb5f1b4fcb5d3d97c540859025e9481a5fc8`.

Reproduce with:

```powershell
$sources = @(
  "research/voevodsky/check_absolute_unlocalized_support_pc.rs",
  "research/voevodsky/check_d03_formal_support_purity.rs"
)
foreach ($src in $sources) {
  rustfmt --edition 2021 --check $src
  $exe = Join-Path $env:TEMP ((Split-Path $src -LeafBase) + ".exe")
  rustc --edition=2021 -D warnings -O $src -o $exe
  & $exe | ConvertFrom-Json | Out-Null
}
```

## Outcome contract

```json
{
  "claim": "The n=6 scalar target has a canonical 215-generator integral unlocalized original-twist/Borel--Moore support-PC complex with strict F0 subset F1 subset F2. At fixed nonzero beta in characteristic-zero Koba--Nielsen completion, its positive-conductor source has the forced placement K(I_plus^vee)[-5] equivalent to D(F0)[-2]. The literal D03 pullback of the filtration Yoneda class is zero and therefore cannot equal the nonzero entry-100 Cousin trace.",
  "status": "proved",
  "assumptions": [
    "The positive real chamber fixes the radial basepoint on every oriented normal circle.",
    "Occurrence coefficients and universal monodromy variables are independent.",
    "The cross-geometry purity comparison is restricted to fixed nonzero beta in a characteristic-zero completed coefficient ring.",
    "Complexes use the homological shift convention stated above."
  ],
  "evidence_refs": [
    "research/voevodsky/check_absolute_unlocalized_support_pc.rs",
    "research/voevodsky/check_d03_formal_support_purity.rs",
    "ledger entries 93, 99, 100, and 104"
  ],
  "factorization_test": {
    "absolute_unlocalized_d_squared": "passed on 215 generators",
    "strict_support_filtration": "passed with ranks 8 subset 208 subset 215",
    "D3_covariance": "passed",
    "local_purity_shift": "passed as [-3] Thom plus [-2] terminal conductor placement",
    "double_loading": "falsified by homology",
    "literal_D03_Yoneda_pullback": "zero",
    "entry100_local_trace": "nonzero",
    "full_marked_Beck_Chevalley_map": "unconstructed"
  },
  "counterevidence": [
    "The local purity statement is not a universal integral cross-geometry theorem.",
    "The literal road pullback cannot produce the required Cousin trace.",
    "No marked ringed support correspondence across the central flip has yet been constructed."
  ],
  "next_experiment": "Construct one marked D03 ringed support correspondence across {D03,x1,x3} to v_plus={x1,x3,x5}; test its canonical Beck--Chevalley composite against eta_mix, the four-normal residue, endpoints (1,1), and the separate [dX03] line."
}
```
