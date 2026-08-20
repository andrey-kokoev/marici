# Global-Q versus Local-Cartier Dichotomy and the Missing Conductor Nullhomotopy

## Record

Author: marici.Nima

Date: 2026-08-15

Status: proved candidate dichotomy and typing no-go for existing constructions; future global kernel remains untyped.

Scope: this is a synthesis of checked-in geometry and certificates from entries
106-113, 131, 143, 154, and 157-158. It records no fresh rerun, no newly
constructed correspondence, and no global nonexistence theorem.

## Synthesis theorem

**Theorem.** The established constructions prove a dichotomy, not a combined
kernel.

1. The global support-filtration/Yoneda construction retains a genuine
   nonzero \(Q\)-side datum, but its literal \(D03\) marked-exit and local
   Cartier image is zero under every presently established support connector.
2. The Morse/Cartier/purity construction produces a canonical nonzero local
   class, but only after the generic \(q\)-chain has been quotiented away.

Consequently no checked-in construction has both a nonzero generic \(Q\) leg
and the canonical local Cartier specialization. The missing object is a
pre-quotient, mixed-variance geometric correspondence; it is not supplied by
another supported gallery, a relabeling, or a chosen nullhomotopy.

### Global support and Yoneda side

The filtered global data have the form

\[
\widetilde F_0 \longrightarrow \widetilde F_1 \longrightarrow \widetilde G,
\qquad
\widetilde G \longrightarrow \widetilde F_2/\widetilde F_0
\longrightarrow \widetilde Q,
\qquad
e_F:\widetilde Q\longrightarrow\widetilde F_0[2].
\]

The log blowup is a filtered strong deformation retract

\[
(\widetilde F_0\subset\widetilde F_1\subset\widetilde F_2)
\simeq
(F_0\subset F_1\subset F_2)
\]

which preserves \(Q\), \(F_0\), and \(e_F\). It creates no new generic
component: \(\widetilde Q=Q\), while the exceptional and marked-gallery
support remains in \(\widetilde F_1\).

On the literal \(D03\) restriction, the first restricted Yoneda factor

\[
Q_{03}\longrightarrow G_{03}[1]
\]

is nonzero, but the second factor

\[
G_{03}\longrightarrow F_0[1]
\]

is zero because the relevant supports are disjoint. Thus the literal
restricted product \(Q_{03}\longrightarrow F_0[2]\) is zero. This does not
erase the global Yoneda datum; it forbids identifying its marked restriction
with the local exit class by the existing support maps.

### Marked-exit side

The inclusion/quotient-induced support-filtration connector has zero
marked-exit composite. In contrast,

\[
q_\Sigma=(1,1,1)=q_{14}+q_{03}+q_{25}
\]

is primitive and nonzero in the marked-exit carrier. It is the road norm and
has \(\epsilon(q_\Sigma)=3\). Therefore the carrier \(Q\) and the marked-exit
local unit do not couple by any existing support map: no established
inclusion/quotient-induced morphism sends \(e_F\) to \(q_\Sigma\).

### Morse, Cartier, and principal-dual side

The absolute loaded Morse identity is

\[
dH_{\rm Morse}^{\rm abs}
=q_J^{\rm abs}-x_3\widetilde\xi^{\rm abs}.
\]

After the endpoint-and-generic-relative quotient

\[
B=(C_{\rm carrier}/\langle a,c\rangle)/(R q_J),
\]

it becomes

\[
d_B[H_{\rm Morse}]=-x_3[\widetilde\xi].
\]

The Cartier connecting morphism therefore gives the nonzero torsion class

\[
\beta_{x_3}^{\rm Cart}
\bigl[H_{\rm Morse}\bmod x_3\bigr]=-[\widetilde\xi].
\]

Together with principal-dual evaluation, this is the canonical nonzero local
class \(-[\widetilde\xi]\). It is formed only after \(q_J\) has been killed in
\(B\). It cannot itself be a map from \(Q\) to the local target, because the
generic chain needed for such a map is absent from the quotient.

### Excess and local purity

The \(\eta_{3,\rm mix}\) exact sequence and entry 131's \(E_3\) purity
normalization fix the local target without supplying a generic source. They
retain both Tor grades, the graph Bockstein, the two endpoint residues, and
the positive orientation. In particular, the local class is normalized by
finite Cartier purity rather than by a division or fitted coefficient.

All of this geometry remains spatially supported in \(F_1\). It supplies no
generic \(Q\)-morphism. Additional Rees or excess grading can preserve the
local packet, but cannot make a source supported wholly in \(F_1\) meet
\(Q=F_2/F_1\).

### Established endpoint/Q target

Entry 143 constructs the target-side extended Cech object

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\quad\text{(also denoted }E_{\rm partial,Q}^{\rm BM,Cech}\text{ in shorthand)}
\]

with its genuine seven-generator \(Q\) quotient and retained nonzero generic
\(q_\Sigma\) leg. It has no normalization-sheet/primal-trace leg. In
particular, construction of this target does not construct a source
\(\mathcal S_{\rm sh}^{\rm norm,reg}\), a trace, or a comparison to the local
Cartier class.

## The dichotomy and completed audit

Every existing candidate is in exactly one of the following checked-in
positions.

- **A. Global/Q position.** It has a genuine nonzero \(Q\)-side/Yoneda source,
  but its marked-exit or local Cartier image is zero.
- **B. Local/Cartier position.** It has a canonical nonzero local
  Cartier/purity class only after the generic \(q\)-chain has been quotiented
  away.

No existing construction has both properties.

| Candidate | Q leg | Local or marked-exit behavior | Verdict |
| --- | --- | --- | --- |
| Expanded gallery | The gallery kernel has zero projection to \(\widetilde Q\), although the transported \(e_F\) remains global. | It has the supported exit class and filtered secondary data, but no Beck--Chevalley coupling. | Does not join the global Yoneda datum to the local class. |
| Strict \(D03\) dual star | The natural relative kernel is acyclic. | It supplies neither a surviving generic class nor an intrinsically typed local map. | Falsified as a kernel. |
| Top-coface cone | No usable generic \(Q\) leg survives the repair. | The common top cone loses \(D03\) typing; the endpoint-star repair has zero relative complex. | Falsified as a typed repair. |
| Seven-triangle Morse carrier | Its generic path is exact, and \(q_J\) is killed in the relative Cartier quotient. | It yields \(-[\widetilde\xi]\) by the Cartier Bockstein. | Local class proved only after the \(Q\)-relevant chain is removed. |
| Support/Tate connector | The global \(e_F\) and primitive \(q_\Sigma\) exist in distinct types; the canonical support connector has zero marked-exit composite. | The Tate road norm and local tag data are retained. | No existing support-map coupling. |
| Multi-Rees/excess/purity | Rees refinements retain support in \(F_1\), hence their generic \(Q\) leg is zero. | \(\eta_{3,\rm mix}\), both Tor grades, and the local purity packet are proved. | Local normalization only. |
| Endpoint/Q Cech packet | It retains the genuine seven-generator quotient and nonzero \(q_\Sigma\). | The target-side Cech and endpoint data exist, but no normalization-sheet source or primal trace reaches them. | Target is constructed; combined kernel is not. |

## The missing conductor nullhomotopy

The tempting expression

\[
\Delta_J=H_{\rm cond}-e_Fh_{\rm Morse}
\]

is well typed only if one has, in one loaded mixed-variance mapping complex,

\[
dh_{\rm Morse}=q_J,
\qquad
dH_{\rm cond}=e_Fq_J.
\]

Only the Morse side exists, and its canonical Cartier class is formed after
the \(q_J\) quotient. Neither \(H_{\rm cond}\) nor the common
\(\operatorname{RHom}\) complex has been constructed. Defining
\(H_{\rm cond}\) from the desired local unit would be circular, rather than a
comparison of independently constructed nullhomotopies.

## Correct primary construction

Do not call a supported-dual \(\alpha_{\rm sh}\) arrow primary. By entries 154
and 158, the earliest honest global data are a normalization-provenanced
source and a closed degree-zero primal trace

\[
\operatorname{Tr}_{\rm biv}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\mathbin\otimes^L
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\longrightarrow
\mathbf 1_{\chi_N},
\]

together with endpoint comparison cells \(h_+\), \(h_-\), and a based
nonzero \(Q\) comparison. Only after an independently proved supported closed
duality theorem may \(\alpha_{\rm sh}\) be introduced as an adjoint.

At the one-channel functional shadow, the desired specialization

\[
\operatorname{sp}_{+,03}:
\operatorname{RHom}(Q,F_0[2])
\longrightarrow
C_{\rm exit}[-1],
\qquad
\operatorname{sp}_{+,03}(e_F)=[1],
\]

is a required consequence and test. It is not a presently defined arrow.

## Smallest admissible geometric seed

The smallest admissible seed is a relative graph multi-DNC/nearby-cycle
correspondence before endpoint or generic quotients. It must retain:

- \(q_i\) and \(q_\Sigma\);
- the ideal-labelled mixed block
  \[
  Rm_i\longrightarrow Rq_i,
  \qquad
  I_i\overline\xi_i\longrightarrow I_i\overline b_i;
  \]
- both Tor grades;
- the two normalization sheets;
- endpoint cells; and
- a morphism of the normalization/conductor and endpoint/\(Q\) localization
  triangles.

The correspondence must specialize locally to \(-\widetilde\xi\) and map
generically nontrivially to \(Q\). Another gallery supported wholly in \(F_1\)
cannot satisfy these two conditions.

## Acceptance tests for the seed

The following are required tests, not optional normalizations.

1. The local \(E_3\) endomorphism matrix must be forced to the identity by
   the graph Bockstein:

   \[
   f_1=
   \begin{pmatrix}
   a&b\\
   0&e
   \end{pmatrix},
   \qquad
   f_0=e.
   \]

   Bockstein compatibility forces \(a=e\) and \(b=0\); positive orientation
   forces \(e=1\).

2. It must reproduce the \(\eta\) residue and the two positive endpoint
   residues

   \[
   +\left[\frac{1}{x_0x_3u_0u_1u_3u_5}\right]\otimes[dX_{03}],
   \qquad
   +\left[\frac{1}{x_1x_3u_0u_1u_3u_5}\right]\otimes[dX_{03}].
   \]

3. The ordinary zero-section and principal-line relabeling ablations must
   fail, as already certified.

4. Forgetting the endpoint/\(Q\) framing must restore the ordinary
   contraction.

5. The construction may use no \(q\)-filling, no inversion of \(x\), \(t\),
   or \(3\), and no fitted \(H_{\rm cond}\).

## Evidence boundary

The synthesis relies on checked-in evidence, not a fresh execution:

- research/voevodsky/check_d03_blowup_yoneda_exit_hom.rs;
- research/voevodsky/check_marked_exit_yoneda_census.rs;
- research/voevodsky/check_d03_pabs_morse_pullback.rs; and
- ledger entries 106-113, 131, 143, 154, 157, and 158.

The cited certificates establish the separate global, marked-exit, Morse,
Cartier, purity, and target-side assertions used above. They do not instantiate
the pre-quotient relative graph correspondence, the primal trace, a supported
duality theorem, or the endpoint-pointed mapping fiber.

## Outcome contract

~~~json
{
  "claim": "proved candidate dichotomy and typing no-go for existing constructions; future global kernel remains untyped",
  "status": "proved",
  "factorization": {
    "global_Q_side": "proved_nonzero_but_local_zero",
    "local_Cartier_side": "proved_nonzero_after_Q_quotient",
    "combined_kernel": "unconstructed",
    "primal_trace": "unconstructed",
    "mapping_fiber": "not_instantiated",
    "parity": "undefined"
  },
  "scope": "checked-in geometry and certificates only; no fresh rerun",
  "counterevidence": [
    "The literal D03 restricted Yoneda product is zero because its second factor has disjoint support.",
    "The inclusion/quotient-induced support connector has zero marked-exit composite, while q_Sigma is primitive nonzero.",
    "Every existing local endpoint-and-generic-relative gallery has already quotiented away its generic q-chain.",
    "A quotient that makes q_Sigma bound deletes the special galleries, and a gallery supported wholly in F1 has zero generic Q leg.",
    "Zero-section, principal-line relabeling, q-filling, inversion, and fitted-H_cond shortcuts are inadmissible."
  ],
  "next_experiment": "Construct the pre-quotient relative graph multi-DNC/nearby-cycle correspondence and primal trace, then test its one-channel localization-triangle square before D3 assembly."
}
~~~
