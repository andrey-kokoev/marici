# Support-Directed Can--Var Packet and Three Local Cousin Traces

## Record

Date: 2026-08-14

Status: proved one-normal coefficient theorem; proved three labelled local
derived road traces; falsified a strict degree-zero finite-free lift.  The
global augmented \(D_3\)-equivariant Cousin coherence remains untyped, not
disproved.

Scope: the universal monodromy ring

\[
R_0=\mathbb Z[q_0^{\pm1},\ldots,q_5^{\pm1}],
\qquad u_j=q_j-1,
\]

the plus normalization branch, and the three marked roads
\(F_{03},F_{25},F_{14}\) of entries 97--99.  Scalar occurrence variables,
monodromy variables, physical normal lines, and support directions remain
distinct.

This entry refines the immediate objective of entry 99.  The missing object
cannot be a strict map between finite Koszul stalks.  Its canonical local
pieces are bivariant excess correspondences followed by Koszul--Cech local
duality.

## The support-directed one-normal packet

Put

\[
q^\vee=q^{-1},
\qquad
u^\vee=q^{-1}-1=-q^{-1}u.
\]

The original-twist locally finite/Borel--Moore road and its reciprocal-twist
regular Verdier dual use different, paired can--var conventions.

For the costandard road object,

\[
Rj_*\mathscr L[1]:
\qquad
\Psi=R\langle\ell\rangle
\mathop{\rightleftarrows}^{\operatorname{can}=u}_{\operatorname{var}=1}
\Phi=R\langle p\rangle .
\]

For the reciprocal standard object,

\[
j_!\mathscr L^\vee[1]:
\qquad
\Psi^\vee=R\langle p^\vee\rangle
\mathop{\rightleftarrows}^{\operatorname{can}^\vee=1}_{
\operatorname{var}^\vee=u^\vee}
\Phi^\vee=R\langle\ell^\vee\rangle .
\]

In both cases the two composites are the appropriate monodromy difference.
The support-directed finite complexes are

\[
K(u)=[R\langle\ell\rangle\xrightarrow{u}R\langle p\rangle],
\qquad
K(u^\vee)=[R\langle\ell^\vee\rangle
\xrightarrow{u^\vee}R\langle p^\vee\rangle].
\]

The complementary-degree pairing

\[
\boxed{
\beta:K(u)\otimes K(u^\vee)\longrightarrow R[1]
}
\]

is fixed by

\[
\beta(p,\ell^\vee)=1,
\qquad
\beta(\ell,p^\vee)=-q.
\]

It is a chain pairing because

\[
u+q u^\vee=0,
\]

and it is perfect because its antidiagonal determinant is the Laurent unit
\(q\).  This is the integral one-normal source of entry 97's bivariant
pairing.

The finite complex is only the logarithmic/simple-pole stage.  The honest
supported Cousin object is the extended Cech complex

\[
C_u^\bullet=
[R\xrightarrow{\rm loc}R[u^{-1}]],
\qquad
H^1(C_u)=R[u^{-1}]/R.
\]

There is a canonical comparison

\[
\boxed{
\kappa_u:
[R\xrightarrow{u}R]
\longrightarrow
[R\xrightarrow{\rm loc}R[u^{-1}]],
\qquad
\kappa_u=(1,u^{-1}).
}
\]

On cohomology it sends

\[
\bar r\longmapsto r/u.
\]

Thus entry 38's \(\ell/u\) is the Koszul-to-Cech image of the integral
generator.  Keeping \(R[u^{-1}]\) as one Cousin term is not global inversion.
Tensoring the whole theory with \(R[u^{-1}]\) instead contracts \(K(u)\) and
erases the supported class.  No single finite-free complex is both the full
local-cohomology object and the literal holder of \(\ell/u\).

## The twist-aware repeated-normal excess

At the plus/\(D03\) intersection, order the reciprocal plus factor before the
original road factor.  The repeated normal is

\[
D_3=K(u_3^\vee)\otimes K(u_3),
\]

with

\[
D_{3,2}=R
\xrightarrow{(-u_3,u_3^\vee)^T}
D_{3,1}=R^2
\xrightarrow{(u_3^\vee,u_3)}
D_{3,0}=R.
\]

Define

\[
\pi_0=1,
\qquad
\pi_1=(1,-q_3),
\qquad
\pi_2=0.
\]

The oriented kernel generator is

\[
\boxed{
\eta_{3,\rm mix}
=-q_3\,\ell_3^{+,\vee}\otimes p_3^{03}
-p_3^{+,\vee}\otimes\ell_3^{03}.
}
\]

It gives the integral exact sequence

\[
\boxed{
0\longrightarrow K(u_3^\vee)[1]
\longrightarrow K(u_3^\vee)\otimes K(u_3)
\xrightarrow{\pi}K(u_3^\vee)
\longrightarrow0.
}
\]

The entry-97 twist normalization

\[
p^\vee\longmapsto-q p,
\qquad
\ell^\vee\longmapsto\ell
\]

sends the complete sequence to entry 99's sequence with

\[
\eta_3=\ell_3^+-\ell_3^{03},
\]

up to the same forced Laurent unit \(-q_3\) on source and image.  The top
coefficient and determinant orientation remain \(+1\).  Hence twist reversal
does not alter the carrier sign and requires no \(u_3^{-1}\) or numerical
denominator.

## Three local derived road traces

For the plus branch

\[
I_+^\vee=(u_1^\vee,u_3^\vee,u_5^\vee)
\]

and the three opposite road pairs

\[
I_{03}=(u_0,u_3),
\qquad
I_{25}=(u_2,u_5),
\qquad
I_{14}=(u_4,u_1),
\]

let \(Q_i\) be the union of the corresponding branch and road normal
sequences.  The actual marked paths of entry 99 distinguish the two copies of
the shared normal and select a labelled excess retraction

\[
\operatorname{tr}^{\rm ex}_i:
K(I_+^\vee)\otimes K(I_i)
\longrightarrow K(Q_i)[1]
\]

whose shifted primitive generator maps to \(1\).  Composing with the
multi-normal Koszul--Cech comparison gives

\[
\boxed{
\Theta_i^{\rm loc}:
K(I_+^\vee)\otimes K(I_i)
\longrightarrow C_{Q_i}[1],
\qquad
\eta_{i,\rm mix}\longmapsto
\left[\frac{1}{\prod_{j\in Q_i}u_j}\right].
}
\]

For all three roads, the exact certificate checks every Koszul degree, the
actual two-flip marked path, the full road Cousin square, occurrence weights,
and support twists.  Each local map:

- gives the two normalized occurrence endpoint values \((+1,+1)\);
- kills the marked lower-Cousin interval boundary;
- uses inverses only inside the indicated Cech localization summands; and
- retains the positive physical normal line separately.

This is a local derived-correspondence theorem.  Independence of the labelled
retraction and compatibility among the three representatives still require a
global Cousin coherence.

## Strict finite-free lift no-go

There is no degree-zero \(R_0\)-linear chain map

\[
K(I_+)\longrightarrow K(I_i)
\]

whose degree-zero multiplier specializes to the carrier unit.  For an
unshared branch normal \(u_a\), the degree-one chain equation would force

\[
a u_a\in I_i.
\]

Modulo \(I_i\), \(u_a\) is a non-zero-divisor, so \(\bar a=0\).  This
contradicts the required identity augmentation \(a(1,\ldots,1)=1\).  The
same argument holds on \(F_{03},F_{25},F_{14}\).

Equivalently, the checked Hom complex has

\[
\operatorname{Ext}^0=\operatorname{Ext}^1=0,
\qquad
\operatorname{Ext}^2\cong\operatorname{Ext}^3
\cong R_0/(I_++I_i).
\]

The no-go is therefore exactly for a strict ordinary stalk map.  It is
positive evidence for the derived excess correspondence, not evidence that a
global kernel cannot exist.

## Evidence

Exact certificates:

- `research/voevodsky/check_one_normal_can_var_cousin.rs`
- `research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs`

SHA-256:

```text
f2342969a0623742846fa538ef32e307d5efbf479b232389c307e9800144f401
e0cfc26031c78ae2c9050ac96cbc672a0de59f11b547e683d6d93aa56d57d448
```

Reproduce with:

```powershell
$sources = @(
  "research/voevodsky/check_one_normal_can_var_cousin.rs",
  "research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs"
)
foreach ($src in $sources) {
  $exe = Join-Path $env:TEMP ((Split-Path $src -LeafBase) + ".exe")
  rustfmt --edition 2021 --check $src
  rustc --edition=2021 -D warnings -O $src -o $exe
  & $exe | ConvertFrom-Json | Out-Null
}
```

Inherited inputs are entries 38 and 93--99.

## Boundary

This entry does not prove a global map

\[
A_+^{\rm Cous,PC}:
\mathcal D_+^{\rm Cous,reg,\vee}
\longrightarrow
\mathbb D\operatorname{PC}(K_6,B_{\rm short})\otimes\chi_N.
\]

In particular:

1. the three local Cech targets are not yet glued through the lower
   \(q\)-vertices and augmentation;
2. Cech localization terms are not finite free over \(R_0\);
3. the labelled local excess retractions have not been proved independent of
   representative;
4. no \(D_3\)-equivariant homotopy coherence has been constructed; and
5. absence of that coherence in the present audit is not a nonexistence
   theorem.

Calling the localization arrow itself `can` is also invalid:

\[
\operatorname{Hom}_{R_0}(R_0[u^{-1}],R_0)=0,
\]

so no reverse `var` can make both composites \(u\).  Can--var belongs to the
finite perfect stage; the Cech comparison realizes its supported Cousin
class.

## Consequence and next formula

The global objective should be formulated as a bivariant kernel on the marked
flag correspondence, not as a strict map of finite stalk complexes.  The
first unresolved coherence occurs at the lower source vertex \(q_2\), shared
by the \(F_{03}\) and \(F_{25}\) incidence terms.  After passing both local
traces to their common Cech refinement, construct or falsify

\[
\boxed{
\rho_{q_2}^{03}\Theta_{03}^{\rm loc}
-\rho_{q_2}^{25}\Theta_{25}^{\rm loc}
=d_{\rm Cous}H_{q_2}+H_{q_2}d.
}
\]

The occurrence pullbacks, reciprocal/Borel--Moore twist, and all localization
summands must be fixed before solving for \(H_{q_2}\).  If this homotopy
exists, rotate it to the other two lower vertices and test the remaining top
coherence.  If it does not, its nonzero class is the first intrinsic
obstruction to the global half-object lift.

## Outcome contract

```json
{
  "claim": "The support-directed one-normal can-var packet and its Koszul-to-Cech realization canonically produce the twist-aware repeated-normal excess line and three labelled local derived road traces; no strict degree-zero finite-free Koszul lift can carry the unit road coefficient.",
  "status": "proved",
  "assumptions": [
    "The original BM and reciprocal regular support directions use their paired, not identical, can-var conventions.",
    "C_Q is the support Cech complex, with inverses only in its localization summands.",
    "The local trace retains the marked occurrence path, twist reversal, and physical normal line."
  ],
  "evidence_refs": [
    "research/voevodsky/check_one_normal_can_var_cousin.rs",
    "research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs",
    "ledger entries 38 and 93-99"
  ],
  "factorization_test": {
    "one_normal_can_var": "passed",
    "twist_pairing": "passed and perfect",
    "mixed_repeated_normal": "passed integrally",
    "three_local_Cech_traces": "passed",
    "strict_finite_free_lift": "falsified on all three roads",
    "global_D3_Cousin_coherence": "untyped, not disproved"
  },
  "counterevidence": [
    "The local-cohomology realization is not a bounded finite-free R0 complex.",
    "The three labelled representatives are not yet connected through lower-vertex homotopies.",
    "Globally inverting u would erase the supported excess class."
  ],
  "next_experiment": "Compare the F03 and F25 labelled Cech residues at their shared q2 vertex and solve the first support- and twist-compatible chain homotopy."
}
```
