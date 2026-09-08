# Physical conductor–Morse difference: endpoint-support audit

## Outcome

No value for the physical class

\[
\Delta_J=H_{\mathrm{cond}}-e_Fh_{\mathrm{Morse}}
\]

is assigned by this calculation. It proves a specific obstruction to using the
constructed native first-jet readout to obtain that value: **the readout
annihilates the whole literal endpoint target of the physical mapping
complex**. It does not merely fail on a chosen representative.

The nonzero native class previously denoted `b` remains nonzero, but it is not
in the image of endpoint-valued cohomology under the literal inclusion. A
support-changing extraordinary comparison would be additional data; it is
not provided by principal parts, by an orientation choice, or by a scalar
normalization.

## 1. Actual domains

Use the previous native complex \(\widetilde E\), its complete endpoint
subcomplex \(V=V_+\oplus V_-\), and the sixteen-generator source
\(Q_f=K(f)\otimes P\). Each endpoint packet has all eight normal subsets.
The positive endpoint has face \(\{13,15,35\}\); the negative endpoint has
face \(\{02,04,24\}\). The physical support called \(F_0\) in the original
secondary-class formulation is the positive endpoint; the two-sheet version
embeds it in \(V\).

Retain the original coefficient ring \(\mathcal B\), its conductor ideal
\(\mathcal I\), the specified spectator subring
\(\mathcal C=\mathcal B/\mathcal I\), and

\[
u=u_{03},\qquad s=t_{04},\qquad t=t_{35},\qquad
D=\mathcal C/(u,s,t).
\]

In words: the exceptional normal and the two spectator Rees parameters stay
independent until the supported residue is taken.

The constructed first-principal-parts operation is

\[
\mathcal J^1_{\mathcal C}(M)
=W_{\mathcal C}\otimes^L_{\mathcal B}M,
\qquad W_{\mathcal C}\cong\mathcal B/\mathcal I^2.
\]

In words: its right coefficient action retains the six first conductor
symbols; its left coefficient action is through the spectator ring. The
result has seven coefficient components. This is the specific bimodule of
the preceding calculation, not a claim of arbitrary base-change exactness
for principal parts on singular rings.

Set

\[
\mathcal A_E=\mathcal J^1_{\mathcal C}
\operatorname{Hom}_{\mathcal B}(Q_f,\widetilde E),\qquad
\mathcal A_V=\mathcal J^1_{\mathcal C}
\operatorname{Hom}_{\mathcal B}(Q_f,V).
\]

The first has 27,440 basis elements. The second has 1,792, with ranks

\[
(42,224,490,560,350,112,14)
\]

in cohomological degrees \(-3,-2,-1,0,1,2,3\). One endpoint alone contributes
896 basis elements. These include every source generator and every first
conductor symbol.

## 2. Complete endpoint restriction

The existing corrected readout is

\[
\Xi_{\mathrm{jet}}=V_{\mathrm{read}}+h_s Z_{04}-h_t Z_{35}.
\]

Its support consists of exactly four native rows:

| row | face | marks | coefficient operation |
|---:|---|---|---|
| 162 | 03,04,E | 03,E | first X04 coefficient, with minus sign |
| 164 | 03,04,E | 03,04,E | constant coefficient, Koszul correction |
| 170 | 03,35,E | 03,E | first X35 coefficient, with plus sign |
| 172 | 03,35,E | 03,35,E | constant coefficient, Koszul correction |

None is an endpoint face. The correction homotopies act on the target
sixteen-state supported dual complex; they do not introduce an endpoint
input row.

Consequently the actual matrix satisfies

\[
\Xi_{\mathrm{jet}}|_{\mathcal A_V}=0.
\]

In words: every endpoint-valued cochain is killed, before imposing
\(u=s=t=0\). This is not merely zero after passing to cohomology.

The verifier checks all 1,792 columns and their differentials. It also
constructs the induced cochain map

\[
\overline\Xi_{\mathrm{jet}}:
\mathcal J^1_{\mathcal C}
\operatorname{Hom}_{\mathcal B}(Q_f,\widetilde E/V)
\longrightarrow\mathcal M_{\mathrm{loc}}.
\]

In words: the existing readout factors through the quotient by the entire
physical endpoint packet. The quotient domain has 25,648 basis elements;
the induced comparison has 48 nonzero columns with 52 polynomial terms.

This factorization is valid because the endpoint sequence is split in every
graded term, \(Q_f\) is bounded free, and all the complexes in this calculation
are explicitly represented. Hom and the displayed principal-parts tensor
preserve this termwise-split short exact sequence. No flatness assumption on
\(W_{\mathcal C}\) is needed.

## 3. Consequence for any literal realization of the physical expression

Let \(i_0:F_0\to\widetilde E\) be the literal endpoint inclusion. For any
source chain map \(a:Q_f\to J\) in compatible shifts and any cochain
\(A:J\to F_0\), the composite \(i_0 A a\) still has endpoint-valued columns.
Therefore

\[
\Xi_{\mathrm{jet}}\bigl(j^1(i_0 A a)\bigr)=0.
\]

In words: neither changing the source comparison nor changing coefficients
can move this literal target out of endpoint support.

In particular, whenever the physical difference has been constructed as an
actual cochain of \(\operatorname{Hom}(J,F_0)\), its image through this literal
route obeys

\[
\Xi_{\mathrm{jet}}
\bigl(j^1(i_0\Delta_J a)\bigr)=0.
\]

**This does not prove \([\Delta_J]=0\).** It proves that the current readout
cannot detect a nonzero class by the literal inclusion. The theorem does not
apply to a new extraordinary correspondence that changes the spatial support,
or to an independently constructed Verdier-duality comparison with another
target. Such a correspondence must itself be specified.

## 4. The native nonzero class is not an endpoint class

The previously constructed native representatives are

\[
b_+=j^1\mathfrak a_{35},\qquad
b_-=-j^1\mathfrak a_{04}.
\]

They satisfy the exact cochain identities

\[
\Xi_{\mathrm{jet}}(b_+)=\tau,
\qquad \Xi_{\mathrm{jet}}(b_-)=\tau,
\qquad
b_+-b_-=\delta(j^1\widetilde\Theta).
\]

The image of \(j^1\widetilde\Theta\) under the readout is zero.
Thus the two positively normalized native sheet sections have zero secondary
difference, with the displayed primitive. Their individual nonzero class does
not change this conclusion. They have not been identified with the physical
conductor and Morse homotopies.

The class \([\tau]\) generates

\[
H^1(\mathcal M_{\mathrm{loc}})=D[\tau]\ne0.
\]

Suppose \([b_+]\) were in the image of \(H^1(\mathcal A_V)\). Then
\(b_+-i v=\delta K\) for an endpoint cocycle \(v\). Applying the readout gives
\(\tau=\delta\Xi_{\mathrm{jet}}K\), contradicting the computed nonzero
supported class. Hence

\[
[b_+]\notin\operatorname{im}
\bigl(H^1(\mathcal A_V)\to H^1(\mathcal A_E)\bigr).
\]

In words: the native primitive is not an endpoint-valued physical class under
this inclusion. It remains detected in the endpoint quotient, and the
supported section of the readout remains there as well.

## 5. What the existing Morse construction actually supplies

The independently specified source identity is

\[
dH=q_J-X_3\widetilde\xi,
\qquad dq_J=X_3d\widetilde\xi.
\]

It is not \(dH=q_J\) in the full endpoint-resolved complex. This identity is
explicit in the repository's loaded Morse implementation.

Retain a separate occurrence Koszul factor with \(dh_{\mathrm{occ}}=X_3p\).
Using the usual tensor-product differential gives

\[
\widehat h_{\mathrm M}
=H\otimes p-\widetilde\xi\otimes h_{\mathrm{occ}},
\]

\[
d\widehat h_{\mathrm M}
=q_J\otimes p-(d\widetilde\xi)\otimes h_{\mathrm{occ}}
=\widehat q_J.
\]

In words: this is an endpoint-corrected Morse trivialization. The second
summand of \(\widehat q_J\) must remain. The occurrence factor is not identified
with the monodromy normal \(u_{03}\).

The checker verifies this full tensor identity. It does not call the corrected
source the physical common source or assign an extension map to it. An actual
transport of \(e_F\) and an independently defined \(H_{\mathrm{cond}}\) on this
same source are still required to form the requested physical difference.

## 6. Why boundary data alone cannot supply the missing homotopy

Within the native first-jet mapping complex, \(b_+\) is closed and has zero
endpoint and Q components; the original, pre-jet endpoint connecting maps
vanish on its native representative as well. Thus adding \(m b_+\) to a
candidate degree-one cochain does not change its differential or those target
boundary values, but changes its supported readout by \(m[\tau]\).

This is a statement about the explicitly checked native model. It does not
assert that such a perturbation preserves a physical source-support condition
that has not yet been supplied. In fact, Section 4 proves that this
perturbation is not an endpoint-valued one. It shows why the native frame alone
cannot be used to identify or choose the physical input.

## 7. Scope and source evidence

The original secondary formulation requires, in one dg enhancement,

\[
\delta h_{\mathrm{Morse}}=q_J,
\quad \delta e_F=0,
\quad \delta H_{\mathrm{cond}}=e_Fq_J.
\]

The first-jet readout and its native test classes do not construct these three
maps or an identification of their domains. The inspected implementation of
the global transform compares a boundary-signature dictionary with its copy;
it does not produce the missing conductor homotopy. No claim is made that no
physical construction could exist elsewhere or be constructed in the future.

The completed results here are the full endpoint restriction, the exact
quotient factorization, the non-image theorem for the native primitive, the
zero difference of the two existing positively normalized sheet sections, and
the endpoint-corrected Morse identity. They rule out the direct native-jet
identification, not the existence of the intended physical invariant.

## Reproduction

Run `python check_physical_delta.py` in this directory with Python 3.10 or
later. No external Python packages or network access are needed. The script
extracts the supplied dependency archive, replays its 275,708 checks, and
performs 109,849 additional exact checks. Most new checks verify the quotient
factorization on every basis column. These counts verify the finite matrices;
the coefficient-uniform conclusions follow from the support and cochain
arguments above.

Sources, pinned at `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`.
- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: actual F0
  endpoint support and all normal-state differentials.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: the loaded Morse
  identity and its occurrence-Koszul endpoint correction.
- `research/voevodsky/check_global_mixed_variance_transform.py`: scope of the
  inspected implementation.
- Supplied `conductor_jet_comparison_package.zip`: exact native first-jet
  map, source resolution, native retraction, and coefficient operations.
- Stacks Project, Tags 0A8H and 0A8X: Hom-complex differential and composition;
  Tag 09CH: principal parts and differential operators; Tag 06XP: extension
  classes and derived Hom.
