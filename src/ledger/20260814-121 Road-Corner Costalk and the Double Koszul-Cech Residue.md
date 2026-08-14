# Road-Corner Costalk and the Double Koszul--Cech Residue

## Record

Date: 2026-08-14

Status: proved finite occurrence--Cousin corner theorem; falsified the
entry-120 comparison with the complete road trace.  The theorem identifies
the supported `v10` corner and its normal residue.  Promotion to the full
ringed PC extraordinary costalk remains unconstructed.

## Claim

Let the entry-97 weighted road square be

\[
Q_2=R\langle F\rangle,
\qquad Q_1=R\langle a,b,c,d\rangle,
\qquad Q_0=R\langle v_{00},v_{10},v_{01},v_{11}\rangle,
\]

with

\[
dF=x_3a-x_4b-x_0c+x_1d.
\]

The opposite path

\[
B_{\rm opp}
=R\langle b,c,v_{00},v_{01},v_{11}\rangle
\subset Q
\]

is a subcomplex.  In the quotient, only the `v10` open-star remains:

\[
dF=x_3a+x_1d,
\qquad da=x_1v_{10},
\qquad dd=-x_3v_{10}.
\]

The map

\[
r:Q\longrightarrow Q/B_{\rm opp},
\qquad
r(a)=Z_3,\qquad r(d)=-Z_1,\qquad r(v_{10})=v
\]

identifies the quotient with the entry-120 occurrence diamond

\[
K_{03}^{\rm occ}:
RF\xrightarrow{(x_3,-x_1)^T}
R\langle Z_3,Z_1\rangle
\xrightarrow{(x_1,x_3)}Rv.
\]

The correct variance is obtained by finite-free duality, not by seeking a
section of \(r\):

\[
0\longrightarrow \mathbb D(Q/B_{\rm opp})
\xrightarrow{\mathbb D(r)}\mathbb D(Q)
\longrightarrow\mathbb D(B_{\rm opp})\longrightarrow0.
\]

On dual bases,

\[
F^\vee\mapsto F^\vee,
\qquad Z_3^\vee\mapsto a^\vee,
\qquad Z_1^\vee\mapsto-d^\vee,
\qquad v^\vee\mapsto v_{10}^\vee.
\]

Thus \(\mathbb D(r)\) is the canonical extension by zero of the corner
cochains.

In cohomological degrees zero through two,

\[
\delta v^*=x_3Z_1^*+x_1Z_3^*,
\qquad
\delta(\alpha Z_1^*+\beta Z_3^*)
=(-x_1\alpha+x_3\beta)F^*.
\]

For the ordered occurrence normals \((x_3,x_1)\), use Cech factor order
\((x_1,x_3)\) and differential \(d(s,t)=s-t\).  The full
Koszul--Cech map is

\[
\begin{aligned}
v^*&\longmapsto1,\\
Z_3^*&\longmapsto(1/x_1,0),\\
Z_1^*&\longmapsto(0,1/x_3),\\
F^*&\longmapsto1/(x_3x_1).
\end{aligned}
\]

Both chain equations hold exactly.  After extension by zero, its forced
one-variable terms are

\[
-d^*/x_3,
\qquad +a^*/x_1.
\]

They may not be discarded in favor of the top Laurent fraction.

Tensoring with the already proved repeated-normal excess trace and the
four-normal Koszul--Cech map gives

\[
\eta_{3,\rm mix}
\longmapsto
\left[\frac1{u_0u_1u_3u_5}\right].
\]

Consequently the corrected entry-120 comparison is the supported corner
identity

\[
\boxed{
(\kappa_{\rm occ}\widehat\otimes\kappa_{\rm norm})
\Theta_{03,\rm flag}^{\rm fil}
=
\operatorname{Res}^{\rm Cousin}_{v_{10}}
(\Theta_{03}^{\rm loc})
}
\]

at finite coefficient/associated-Cousin grade, with value

\[
\boxed{
+\left[
\frac1{x_1x_3u_0u_1u_3u_5}
\right]\otimes[dX_{03}],
\qquad [dX_{03}]=+1.
}
\]

The occurrence factor agrees with the entry-97 tangential coefficient at

\[
v_{10}=x_1x_3,
\qquad
\Theta_{\rm tan}(v_{10})=(x_1x_3)^{-1}.
\]

## Evidence

Exact certificate:

- `research/voevodsky/check_d03_corner_residue_comparison.rs`, SHA-256
  `e0d1f07c7700caf1314a384bb1eebd560c94b8347d8be8411bb90c8933ecf40e`.

The certificate verifies the full road-square differential, closure of
\(B_{\rm opp}\), the quotient and dual chain maps, the sign in
\(\mathbb D(r)\), the strict-section ideal obstruction, all lower and top
Koszul--Cech equations, the normal excess residue, the physical orientation,
and the localization negative control.

Reproduce with `rustfmt --edition 2021 --check`, compile the certificate with
`rustc --edition=2021 -D warnings -O`, and execute the resulting binary.  Its
stdout is the structured outcome packet.

## Boundary

The stronger formula proposed as entry 120's next experiment is false:

\[
\kappa_{Q_{03}}\Theta_{03,\rm flag}^{\rm fil}
\not\simeq\Theta_{03}^{\rm loc}
\]

when the right side denotes the complete road trace.  Indeed:

- \(\mathbb D(r)\) vanishes on \(b,c,v_{00},v_{01},v_{11}\), while the
  normalized entry-97 trace is nonzero on every road vertex;
- after inverting \(x_1,x_3\), the corner quotient is a contractible Koszul
  complex and its supported class dies;
- the complete normalized road trace remains its nonzero rank-one
  augmentation class.

This does not kill the corner residue.  Its inverses occur only inside the
target Cech summands, while the source and its occurrence, endpoint, and
excess supports remain unlocalized.  Equality after Laurent base change is
therefore equality of one residue representative, not equality of the two
supported objects.

The finite cellular dual map also does not by itself prove that
\(\mathbb D(Q/B_{\rm opp})\) is the actual ringed PC extraordinary costalk.
That promotion still requires the occurrence-loaded Cousin purity or
subdivision counit attached to the marked gallery.

## Consequence

The target-side problem is smaller and correctly typed.  Entry 120 already
constructs the filtered source trace; this entry identifies exactly one of
its target Cousin components.  The global road trace should no longer be
used as the immediate codomain.

The next discriminating experiment is to form the four corner quotients of
the road square and their edge-overlap Cech diagram.  Test whether its
totalization reconstructs the complete entry-97 trace, with no extra
cohomology or torsion, and whether the `v10` component is the ringed
six-functor costalk constructed here at coefficient level.  Failure of the
corner cover to glue, or a nontrivial overlap obstruction, would show that
additional PC Cousin coherence is required.

## Outcome contract

```json
{
  "claim": "The entry-120 road-flag trace has a canonical variance-correct extension into the full road dual through the quotient Q/B_opp. Its target Koszul-Cech image is the positive v10 corner residue of the entry-97/100 trace, not the complete road trace.",
  "status": "proved",
  "assumptions": [
    "The statement is scoped to the finite occurrence-Cousin and established normal-excess coefficient model.",
    "The source, endpoint, and excess supports remain unlocalized; inverses occur only in target Cech terms.",
    "The ringed PC extraordinary-costalk identification is not included in the theorem."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_corner_residue_comparison.rs",
    "ledger entries 97, 100, and 120"
  ],
  "factorization_test": {
    "road_quotient": "passed",
    "dual_extension_by_zero": "passed with forced sign",
    "occurrence_Koszul_Cech": "passed including lower terms",
    "normal_excess_residue": "passed",
    "combined_corner_value": "+1/(x1*x3*u0*u1*u3*u5) times [dX03]",
    "full_road_equality": "falsified",
    "ringed_PC_purity": "unconstructed"
  },
  "counterevidence": [
    "The supported quotient becomes contractible after global occurrence localization.",
    "The extension-by-zero class vanishes on the opposite road path, whereas the full trace is nonzero at all four vertices.",
    "Keeping only the top Laurent fraction violates the Cech chain equation."
  ],
  "next_experiment": "Construct the four-corner occurrence-Cousin cover of the road square, compute its overlap totalization, and test reconstruction of the full entry-97 trace together with ringed PC costalk provenance."
}
```
