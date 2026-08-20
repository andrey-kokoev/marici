---
authors:
  - marici.Nima
---
# Polarity-First Correction to the Deutsch--Popperian Butterfly Conjecture

## Record

Date: 2026-08-15

Status: scoped falsification of entry 151's obstruction order, followed by a
corrected one-bit conjecture. No new coefficient theorem is claimed.

Entry 151 incorrectly promoted the unpointed carrier sequence

\[
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or})\cong\mathbb Z/3
\quad\text{then}\quad
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or})\cong\mathbb Z/2
\]

to the next physical test. Entries 141 and 144 already prove that the
polarity line must be loaded before pointing. This entry supersedes that
ordering statement while preserving entry 151's Deutsch--Popperian
anti-fitting requirements.

## Falsifier

The carrier Tate class in

\[
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or})\cong\mathbb Z/3
\]

is established structural data. It is not the next obstruction to recompute.
The carrier roof has an unpointed \(\mathbb Z/2\)-torsor, but physical polarity
loading transgresses this parity before any point is selected.

The normalization--conductor coefficient sequence is

\[
0\longrightarrow\mathbb Z
\longrightarrow P_{\rm sh}
\longrightarrow\mathbb Z_{\rm or}
\longrightarrow0.
\]

Its Bockstein is the proved isomorphism

\[
\boxed{
\partial_{\rm pol}:
H^1(D_3;\mathbb Z_{\rm or})
\xrightarrow{\sim}
H^2(D_3;\mathbb Z).
}
\]

Both groups are \(\mathbb Z/2\). After the once-relative polarity twist,

\[
H^1(D_3;\mathbb Z)=0,
\qquad
H^2(D_3;\mathbb Z)\cong\mathbb Z/2.
\]

Therefore the loaded problem has no residual parity choice:

\[
\omega_{\rm load}=0
\Longrightarrow
\pi_0\operatorname{Lift}_{\rm load}
\text{ is a singleton},
\]

\[
\omega_{\rm load}=1
\Longrightarrow
\operatorname{Lift}_{\rm load}=\varnothing.
\]

Consequently entry 151's proposed sequence “first compute a vanishing
\(\mathbb Z/3\) obstruction, then choose the nontrivial \(\mathbb Z/2\)
orientation point” is not the correctly typed physical experiment.

## Corrected Deutsch--Popperian conjecture

The missing normalization-sheet correspondence and its two endpoint
connector cells have trivial endpoint/\(Q\) defect parity:

\[
\boxed{
p_{\partial,Q}
=
\bigl[
r_{\partial,Q}(\beta_+,-\beta_-)
\bigr]
=0
\in H^1(D_3;\mathbb Z_{\rm or}).
}
\]

Hence

\[
\boxed{
\omega_{\rm load}
=
\partial_{\rm pol}(p_{\partial,Q})
=0
\in H^2(D_3;\mathbb Z),
}
\]

and the polarity-loaded pointed butterfly exists uniquely up to contractible
choice.

The missing geometric datum remains

\[
\alpha_{\rm sh}^{!,\check C}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\longrightarrow
\mathbb D_{\rm supp}
\left(
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\right)\otimes\chi_N
\]

together with its two endpoint comparison cells. The target endpoint/\(Q\)
object, its nonzero \(Q\)-leg, road inclusion, and Borel--Moore Cech
realization are already fixed.

## Why the corrected explanation is hard to vary

The construction has only one undecided bit:

- the carrier roof is already canonical;
- the carrier \(\mathbb Z/3\) Tate extension is already fixed;
- the normalization--conductor sequence is geometric and nonsplit;
- its Bockstein is already proved to be an isomorphism;
- target-side physical-reflection naturality is already \(+1\);
- restriction to the physical reflection \(f_3\) detects the complete loaded
  obstruction;
- after polarity loading, \(H^1(D_3;\mathbb Z)=0\), so no second choice
  survives.

Thus the source endpoint/\(Q\) connector is either even and produces the
unique loaded lift, or odd and prevents any loaded lift. Extra global
parameters, a preferred strict carrier map, or an outer-octagon sign cannot
alter this dichotomy.

## Decisive test

Construct the single \(f_3\)-paired endpoint/\(Q\) restriction of the two
sheetwise normalization-gallery homotopies. It must retain:

- both sheets and their conductor difference;
- the based nonzero \(q_\Sigma\) and \(Q\) leg;
- both endpoint connector cells;
- reciprocal-regular versus Borel--Moore variance;
- occurrence and independent multi-Rees filtrations;
- both repeated-normal Tor grades;
- the established \(x_3/x_4\) edge purity and physical normal.

Read

\[
p_{\partial,Q}(f_3)\in\mathbb Z/2
\]

before evaluating \(K_{\rm alt}\), the Cousin residue, or any desired target
class. Apply the already-proved Bockstein only afterward.

## Outcome matrix

- \(p_{\partial,Q}=0\): the corrected carrier/loaded synthesis passes locally,
  and the loaded pointing is unique.
- \(p_{\partial,Q}=1\): the conjecture is falsified and no polarity-loaded
  butterfly exists.
- An undefined parity because the endpoint connector is untyped leaves the
  conjecture open; it is not evidence for either outcome.
- A rank-one answer obtained only after imposing the residue, \(K_{\rm alt}\),
  or a chosen carrier lift is inadmissible.

## Prohibited repairs

Do not:

- choose a point in the carrier \(\mathbb Z/2\)-torsor before loading polarity;
- recompute the carrier \(\mathbb Z/3\) Tate class as if it were the physical
  obstruction;
- select one of the affine rank-nine strict lifts;
- divide by \(2\) or \(3\);
- infer the bit from the outer octagon;
- discard the Tor-one copy;
- define the connector from its desired residue.

## Evidence

No new executable calculation is required for the ordering falsifier. It is
the direct conjunction of the exact results in:

- entry 135: canonical carrier roof, strict-map no-go, and rank-nine
  unpointed lift family;
- entry 141: conductor Bockstein
  \(H^1(D_3;\mathbb Z_{\rm or})\simeq H^2(D_3;\mathbb Z)\);
- entry 144: polarity-first endpoint/\(Q\) formulation and binary loaded
  existence test;
- entry 151: the superseded carrier-first conjecture.

The existing exact certificate for the decisive coefficient map is

- research/voevodsky/check_conductor_polarity_bockstein.rs
- SHA-256
  896574dabfe2293274b92593c88a23ef8b9743f93e429dd81170afaf646e29a8.

## Boundary

This entry does not compute \(p_{\partial,Q}\), construct
\(\alpha_{\rm sh}^{!,\check C}\), or prove existence of the loaded half-object.
It corrects the experiment so that those constructions are tested in the
right order.

It does not weaken the canonical carrier roof or the integral augmented
triangle. It changes only their physical use: polarity loading precedes
pointing.

## Outcome contract

~~~json
{
  "claim": "The carrier-first Z/3-then-Z/2 experiment of entry 151 is mistyped physically. The correct conjecture is that the endpoint/Q defect parity vanishes; its conductor Bockstein is then zero and the once-polarity-loaded butterfly exists uniquely.",
  "status": "falsified",
  "assumptions": [
    "The polarity line is loaded relatively exactly once.",
    "The coefficient Bockstein and physical-reflection detection retain their proved scopes.",
    "The endpoint/Q target and road inclusion remain fixed as in entry 144."
  ],
  "evidence_refs": [
    "ledger entry 135",
    "ledger entry 141",
    "ledger entry 144",
    "ledger entry 151",
    "research/voevodsky/check_conductor_polarity_bockstein.rs"
  ],
  "factorization_test": {
    "entry151_carrier_first_order": "falsified",
    "carrier_Tate_Z3": "fixed structural class, not the next physical obstruction",
    "carrier_endpoint_parity": "H1(D3,Z_or)=Z/2",
    "conductor_Bockstein": "isomorphism to H2(D3,Z)=Z/2",
    "loaded_choice_space_if_unobstructed": "singleton",
    "endpoint_Q_defect_parity": "uncomputed",
    "next_test": "one physical-reflection endpoint/Q connector"
  },
  "counterevidence": [
    "The missing normalization-sheet kernel and endpoint connector cells remain unconstructed.",
    "Target-side closure cannot determine the source defect bit.",
    "A carrier pointing chosen before polarity loading is not the physical lift."
  ],
  "next_experiment": "Construct the f3-paired endpoint/Q defect restriction, read its parity before target evaluation, and apply the proved conductor Bockstein."
}
~~~
