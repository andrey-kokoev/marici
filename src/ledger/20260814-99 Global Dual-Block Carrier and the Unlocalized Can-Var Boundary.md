# Global Dual-Block Carrier and the Unlocalized Can--Var Boundary

## Record

Date: 2026-08-14

Status: proved integral, based, equivariant carrier theorem and proved local
excess-symbol theorem.  The corresponding unlocalized PC
Beck--Chevalley/can--var kernel remains unconstructed.

Scope: the labelled hexagon associahedron

\[
X=K_6,
\qquad
B=B_{\rm short},
\]

where \(B\) is the union of the six short-diagonal pentagonal facets, together
with the factorization marks, polarity, and orientations fixed in entries
93--98.

This entry refines entry 98.  The six source attachments are not independent:
their carrier grades are the restrictions of two polarity-related global
maps.  What remains missing is one support-filtered lift of those global maps,
not six freely normalized arrows.

## Claim

Let \(v_+\) be the all-odd central triangulation and \(L_+\) its triangular
positive vertex figure.  The suspended augmented carrier is

\[
D_+^{\rm car}=\widetilde C_*(L_+)[1]
\]

with

\[
\mathbb Z\langle f_+\rangle
\xrightarrow{d_3}
\mathbb Z\langle e_1,e_3,e_5\rangle
\xrightarrow{d_2}
\mathbb Z\langle q_0,q_1,q_2\rangle
\xrightarrow{\epsilon}
\mathbb Z,
\]

\[
d_3f_+=e_1+e_3+e_5,
\]

\[
d_2=
\begin{pmatrix}
1&-1&0\\
-1&0&1\\
0&1&-1
\end{pmatrix},
\qquad
\epsilon=(1,1,1).
\]

Entry 98's relative carrier is

\[
C_*(X,B)=
\left[
\mathbb Z\langle K_{\rm rel}\rangle
\xrightarrow{(1,1,1)^T}
\mathbb Z\langle T_0,T_1,T_2\rangle
\longrightarrow0\longrightarrow0
\right].
\]

The labelled pair and its dihedral action give the unique road matching

\[
e_1\longmapsto T_2=F_{14},
\qquad
e_3\longmapsto T_1=F_{03},
\qquad
e_5\longmapsto T_0=F_{25}.
\]

Therefore

\[
\boxed{
A_+^{\rm car}(f_+)=K_{\rm rel},
\qquad
A_+^{\rm car}(e_1,e_3,e_5)=(T_2,T_1,T_0),
}
\]

with the lower two degrees sent to zero, is a strict integral chain map.
The top equation is

\[
A_{+,2}^{\rm car}d_3f_+
=T_0+T_1+T_2
=dK_{\rm rel}.
\]

The three unit road values force the top coefficient to be \(+1\), since the
displayed target differential is injective.  Polarity gives the second global
map

\[
A_-^{\rm car}(f_-)=-K_{\rm rel},
\]

\[
e_0\mapsto-T_1,
\qquad
e_2\mapsto-T_0,
\qquad
e_4\mapsto-T_2.
\]

Thus the six local carrier attachments are restrictions of
\(A_+^{\rm car}\) and \(A_-^{\rm car}\).

## The local excess symbol

For the plus-sheet \(D=03\) restriction, the labelled geometry independently
selects the unique marked path

\[
(x_1,x_3,x_5)
\longrightarrow
(X_{03},x_1,x_3)
\longrightarrow
(X_{03},x_0,x_3).
\]

It retains \(x_3\) and produces

\[
I_+=(u_1,u_3,u_5),
\qquad
I_{03}=(u_0,u_3).
\]

Put

\[
Q=(u_0,u_1,u_3,u_5),
\qquad
\eta=h_3^+-h_3^{03}.
\]

Then the derived intersection has the canonical integral exact sequence

\[
\boxed{
0\longrightarrow K(Q)[1]
\xrightarrow{\eta\wedge-}
K(I_+)\otimes K(I_{03})
\longrightarrow K(Q)
\longrightarrow0.
}
\]

The inclusion is independent of which copy of the shared \(u_3\) is used to
lift the quotient conormal basis.  With the established orders,

\[
\eta\wedge\omega_Q
=
\omega_+\wedge\omega_{03}
\]

has sign \(+1\).  Hence the degree-one shift and excess orientation are
forced rather than fitted.

The exact audit also proves that all invariants visible on the established
boundary agree with entry 97:

- the marked lower-Cousin edge and both endpoints;
- reciprocal-twist regular support versus original-twist locally finite
  support;
- \(u_j^\vee=-q_j^{-1}u_j\), without inverting any \(u_j\);
- the two normalized occurrence values \((1,1)\); and
- the independent positive physical line \([dX_{03}]\).

These equalities determine the unique candidate local excess symbol.  They do
not by themselves construct the full PC chain map.

## The index-three warning

After forgetting the based, support-filtered, and equivariant structure,
\(A_+^{\rm car}\) is null-homotopic.  One integral contraction is

\[
h_2(e_1)=K_{\rm rel},
\qquad
h_2(e_3)=h_2(e_5)=0,
\]

\[
h_1(q_0)=0,
\qquad
h_1(q_1)=T_0+T_1,
\qquad
h_1(q_2)=T_1.
\]

However, an integral \(D_3\)-equivariant contraction would require

\[
h_2(e_1)=h_2(e_3)=h_2(e_5)=aK_{\rm rel}
\]

and the top homotopy equation becomes

\[
3a=1.
\]

It exists only after adjoining \(1/3\).  This is the same index-three
phenomenon already seen in the augmented triangle resolution.  It is not an
invitation to rationally split the object: it shows that the integral
equivariant and support-filtered category is essential.

## Evidence

Exact certificates:

- `research/voevodsky/check_d03_global_dual_block_carrier.rs`
- `research/voevodsky/check_d03_plus_excess_beck_chevalley.rs`

SHA-256:

```text
9ab22bf4332fad1ad430a4cde755aa8c76c2ff5f37afe2e72241415eaab179e6
b0cd887960b9a0809618fd9e36dbf1fbfb05f7792da7be0d828d61c1d037d0e4
```

The first checker verifies both polarity-related carrier maps, the forced top
coefficient, dihedral covariance, the explicit ordinary null-homotopy, and
the integral equivariant obstruction \(3a=1\).  The second enumerates the
fourteen labelled triangulations, proves uniqueness of the marked \(D03\)
path, verifies the complete excess Koszul exact sequence and its determinant
sign, and compares every already-typed boundary invariant.

Reproduce with:

```powershell
$sources = @(
  "research/voevodsky/check_d03_global_dual_block_carrier.rs",
  "research/voevodsky/check_d03_plus_excess_beck_chevalley.rs"
)
foreach ($src in $sources) {
  $exe = Join-Path $env:TEMP ((Split-Path $src -LeafBase) + ".exe")
  rustfmt --edition 2021 --check $src
  rustc --edition=2021 -D warnings -O $src -o $exe
  & $exe | ConvertFrom-Json | Out-Null
}
```

Inherited inputs are entries 38 and 93--98.

## Boundary

The following stronger statement is not proved:

\[
A_+^{\rm Cous,PC}:
\mathcal D_+^{\rm Cous,PC}
\longrightarrow
\mathbb D\operatorname{PC}(K_6,B_{\rm short}).
\]

In particular:

1. Entry 38 constructs face tubes for actual associahedral faces.  It does
   not construct an augmented vertex-figure dual-block map to the relative
   complex.
2. The local \(\eta\)-wedge sequence is the canonical top-
   \(\operatorname{Tor}_1\) symbol, not the missing global can/var kernel.
3. The ordinary excess Euler class vanishes for the trivial coordinate
   excess line.  The desired map must retain the secondary derived class.
4. Nonresonant inversion contracts the supported Koszul complexes and erases
   precisely the class that must define the lift.
5. Equality of carrier signs, occurrence values, and endpoint periods is
   necessary but insufficient for a filtered chain map.

The first missing datum is therefore one unlocalized, support-preserving
augmented dual-block/Cousin kernel.  It must contain the scalar occurrence and
normal layers separately, realize can/var before \(u_j\) is inverted, and
restrict on each road to the entry-97 bivariant trace including all lower
Cousin terms.

## Consequence

Replace the six-map objective of entry 98 by two global maps.  The next
formula is

\[
\boxed{
A_\pm^{\rm Cous,PC}:
\mathcal D_\pm^{\rm Cous,reg,\vee}
\longrightarrow
\mathbb D\operatorname{PC}(K_6,B_{\rm short})\otimes\chi_N
}
\]

over the unlocalized universal monodromy ring, with

\[
\operatorname{gr}A_\pm^{\rm Cous,PC}=A_\pm^{\rm car}
\]

and, for the three roads,

\[
\boxed{
\rho_iA_\pm^{\rm Cous,PC}
\simeq
\operatorname{Tr}_{i,\partial}^{\rm PC}
\partial_{\pm i}^{\rm ex}.
}
\]

One global construction proves all six local comparisons by restriction and
polarity.  A failure to construct its unlocalized can/var component is the
first canonical failure of the current scalar master enhancement.

## Outcome contract

```json
{
  "claim": "The labelled relative hexagon supplies two polarity-related integral equivariant carrier maps, and the plus/D03 restriction has a canonical eta-wedge top-Tor excess symbol with all established boundary invariants fixed.",
  "status": "proved",
  "assumptions": [
    "The carrier retains the labelled bases, orientations, integral dihedral action, and polarity line.",
    "The local excess calculation is performed before inverting the independent u_j=q_j-1 normals.",
    "The PC Beck-Chevalley statement is not inferred from agreement of boundary invariants."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_global_dual_block_carrier.rs",
    "research/voevodsky/check_d03_plus_excess_beck_chevalley.rs",
    "ledger entries 38 and 93-98"
  ],
  "factorization_test": {
    "global_carrier": "passed for both polarity sheets",
    "plus_D03_excess_symbol": "passed integrally",
    "forced_boundary_invariants": "passed",
    "unlocalized_can_var_kernel": "untyped",
    "full_PC_Beck_Chevalley": "inconclusive"
  },
  "counterevidence": [
    "The carrier map is null-homotopic after forgetting integral equivariance and support filtration.",
    "An equivariant contraction requires division by three.",
    "Entry 38 does not supply the augmented dual-block/can-var lift."
  ],
  "next_experiment": "Construct the unlocalized augmented dual-block/Cousin kernel globally for the plus vertex figure and test that its D03 restriction is the eta-wedge excess class and entry-97 road trace."
}
```
