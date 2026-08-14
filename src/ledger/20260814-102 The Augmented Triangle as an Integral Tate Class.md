# The Augmented Triangle as an Integral Tate Class

## Record

Date: 2026-08-14

Status: proved an exact integral representation-theoretic identification of
the augmented triangle from entries 94 and 99; proved that the weighted
normal packet of entry 101 is **not** an unlocalized realization of that Tate
window. This does not construct the filtered comparison \(\alpha_+\) or a
full PC half-object.

## Claim

Let \(C_3=\langle r\mid r^3=1\rangle\) and
\(D_3=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle\). With road basis
\((1,r,r^2)\), tag basis \((r,r^2,1)\), and the reflection/orientation actions
fixed in entry 94, the augmented triangle is the based exact sequence

\[
\boxed{
0\longrightarrow\mathbb Z_{\rm or}
\xrightarrow{N}P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}
\xrightarrow{\epsilon}\mathbb Z
\longrightarrow0,
\qquad N=1+r+r^2.
}
\]

Here \(P_{\rm road}\simeq\mathbb Z[C_3]\), the road reflection is inversion,
the tag reflection is \(-r^{-1}s\), the left endpoint is reflection odd, and
the right endpoint is reflection even. Entry 99 uses the same complex after
reversing the three tag columns. Thus the primitive/contact resolution is a
finite, orientation-twisted window of the complete \(C_3\)-Tate resolution,
not an ad hoc triangle.

The sequence represents the generator

\[
\boxed{
\beta_\triangle\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\rm or})
\cong\mathbb Z/3.
}
\]

Restriction to \(C_3\) gives the usual norm/augmentation two-extension. In
the Lyndon--Hochschild--Serre calculation for
\(1\to C_3\to D_3\to C_2\to1\), inversion negates the generator of
\(H^2(C_3;\mathbb Z)\), while the orientation coefficient contributes a
second minus sign. Their product is invariant, giving the displayed
\(\mathbb Z/3\) class. The checker verifies the corresponding based
\(D_3\)-chain actions directly.

This simultaneously explains

\[
\Delta^\vee=\epsilon,
\qquad
\partial_\triangle^\vee=-\partial_\triangle,
\qquad
\epsilon N=3,
\]

and the Smith factors

\[
\operatorname{SNF}(\Delta^\vee,\partial_\triangle)=(1,1,3).
\]

The contact lattice is the augmentation ideal

\[
A_2=\operatorname{im}(1-r)=\ker\epsilon,
\]

while the primitive is the coinvariant quotient

\[
\operatorname{coker}(1-r)\simeq\mathbb Z.
\]

They are the two ends of one integral periodicity window. An invariant
section of the primitive quotient would send \(1\) to \(N/3\); its failure
integrally is exactly \(\beta_\triangle\), not missing normalization data.

## Evidence

The extended exact certificate is

- `research/voevodsky/check_weighted_three_road_star.rs`

with SHA-256

```text
92bfd8b2b2bc058fa70c49af4c69ca80f460b175882211621928c3d93377e008
```

It verifies:

- entry 94's triangle matrix as multiplication by \(1-r\);
- entry 99's column-reversed based form;
- integral exactness and the middle Smith factors \((1,1,0)\);
- \(\Delta^\vee=\epsilon\) and
  \(\partial_\triangle^T=-\partial_\triangle\);
- the full \(D_3\) chain actions, orientation twist, and group relations;
- the Smith index three;
- the induced cochain pattern \(1-r\mapsto0\), \(N\mapsto3\), hence
  \(\widehat H^{\rm even}(C_3;\mathbb Z)=\mathbb Z/3\) and adjacent odd
  Tate group zero;
- the negative comparison with the unlocalized weighted Koszul packet.

Reproduce with:

```powershell
$src = "research/voevodsky/check_weighted_three_road_star.rs"
$exe = Join-Path $env:TEMP "check_weighted_three_road_star.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json | Out-Null
```

The earlier checker version recorded by entry 101 remains reproducible at
commit `ac6756d`; this entry records the extended source as a new immutable
version rather than rewriting entry 101's admitted evidence.

## Boundary

The Tate identification does **not** identify the weighted residual-normal
complex

\[
K_E=K(u_4,u_0,u_2)
\]

with the exact augmented triangle over the unlocalized base ring. Indeed,

\[
H_0(K_E)=R_0/(u_4,u_0,u_2),
\]

whereas the Tate window is exact. Diagonal conjugation to unit incidence
requires simultaneous inversion of \(u_4,u_0,u_2\), which removes the
supported fibre that the scalar specialization must retain. The formal
unit-incidence control \(u_4=u_0=u_2=1\) also sends \(q_j=1+u_j\) to \(2\),
so it belongs only after the corresponding base change; it is not an
integral geometric specialization of the original Laurent-monodromy base.

Entry 101's legal Cech star avoids global inversion by placing each
\(1/u_j\) in its named localization summand and by sending the lower
\(q\)- and augmentation cells to zero. Consequently it is a conditional
top/road half-map, not the complete Tate window.

In particular, the following inferences are prohibited:

- replacing the supported normal/Rees complex by the constant Tate
  resolution;
- applying a Tate construction and declaring \(\alpha_+\) thereby built;
- globally inverting the even normals to obtain unit incidence;
- interpreting the order-three class as physical torsion in an amplitude;
- using the rational projector \(N/3\) as an integral descent map.

The Tate class controls the cyclic symmetry and nonsplitting of the carrier.
It does not supply the normal weights, can--var maps, Cech poles,
normalization--conductor occurrence filtration, repeated-normal excess,
physical normal lines, or the intrinsic supported top arrow
\(f_+\mapsto\tau_AK_{\rm rel}\).

## Consequence

The clean architecture is now **Rees first, Tate shadow second**. A future
filtered comparison must retain two distinct and compatible shadows:

1. its integral carrier/incidence shadow must be the class
   \(\beta_\triangle\);
2. its supported coefficient shadow must be entry 101's weighted Cech star.

These shadows are not chain-isomorphic over \(R_0\), and no such
identification is required. They should arise from different forgetful or
associated-grade functors applied to one geometric comparison

\[
\boxed{
\alpha_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}
R\Gamma_{v_+}^{F}(P_{\rm abs}).
}
\]

The immediate falsifier is unchanged but sharpened: construct \(\alpha_+\)
without inverting \(t\), any \(u_j\), or \(3\), and verify simultaneously
that its carrier incidence is the norm/\((1-r)\)/augmentation window and its
supported normal grade is the weighted star with the three established local
excess traces. Failure of either shadow to arise from the same filtered
specialization object falsifies the proposed source geometry.

## Outcome contract

```json
{
  "claim": "The augmented triangle of entries 94 and 99 is the orientation-twisted integral C3 Tate periodicity window representing the order-three class in Ext^2_{Z[D3]}(Z,Z_or); the weighted normal packet is not an unlocalized realization of that window.",
  "status": "proved",
  "assumptions": [
    "The D3 road, tag, and endpoint actions are those fixed in entries 94 and 99.",
    "The Ext interpretation uses the standard Lyndon-Hochschild-Serre identification for C3 normal in D3."
  ],
  "evidence_refs": [
    "research/voevodsky/check_weighted_three_road_star.rs",
    "ledger entries 94, 99, and 101"
  ],
  "factorization_test": {
    "based_Tate_window": "passed",
    "D3_orientation_covariance": "passed",
    "self_duality": "passed",
    "order_three_Ext_class": "passed",
    "unlocalized_weighted_realization": "falsified",
    "intrinsic_filtered_alpha_plus": "unconstructed"
  },
  "counterevidence": [
    "K(u4,u0,u2) has supported H0=R0/(u4,u0,u2), while the Tate window is exact.",
    "Making the weighted incidence unit requires unsupported simultaneous normal localization.",
    "The legal Cech star retains only a top/road half-map and does not construct alpha_plus."
  ],
  "next_experiment": "Construct alpha_plus in the integral D3-stable Rees category and test that one object has both the Tate carrier shadow and the weighted supported-Cech shadow without identifying them over the base ring."
}
```
