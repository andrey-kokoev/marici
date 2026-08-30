# The local `C3` charge PVM can read a character but cannot store a neutral path qutrit

Owner: `marici.Kitaev`

## Bounded question

Can the canonical path-to-centralizer incidence be physically realized by
coherently swapping an ordinary path qutrit into the localized `F,G,H` charge
sectors?

Not by any Hamiltonian in the local `D(S3)` endpoint algebra, even with a
neutral finite-dimensional pointer. The three character projectors are
central superselection projectors. Local endpoint dynamics can condition on
them and record them, but cannot move amplitude between them.

A nonlocal ribbon can change endpoint charge only by transporting or creating
compensating charge elsewhere. That companion then carries the missing
character relation. The coherent carrier is relational and cannot be reduced
to one isolated endpoint without dephasing or a new boundary resource.

## Local endpoint algebra

The finite localized endpoint algebra has the semisimple form

\[
\mathcal A_{\rm end}
=
\bigoplus_{a\in\{A,\ldots,H\}}
M_{d_a}(\mathbb C).
\]

Its primitive central projectors are

\[
Q_A,\ldots,Q_H.
\]

For three-cycle flux, the character sectors are

\[
Q_F,\qquad Q_G,\qquad Q_H.
\]

Every endpoint operator commutes with every central projector:

\[
[X,Q_a]=0,
\qquad
X\in\mathcal A_{\rm end}.
\]

This is not an approximation. It is the defining block decomposition of the
source-derived local algebra.

## Local coherent-transfer no-go

Let `P` be an ordinary neutral path qutrit. Permit every Hamiltonian in

\[
\mathcal B(\mathcal H_P)
\otimes
\mathcal A_{\rm end}.
\]

The lifted charge projectors

\[
I_P\otimes Q_a
\]

remain central in this enlarged algebra. Therefore every generated unitary
`U` satisfies

\[
[U,I_P\otimes Q_a]=0.
\]

If the endpoint initially lies in one charge sector `a_0`, then

\[
(I_P\otimes Q_{a_0})
U
|\psi\rangle_P|a_0\rangle_E
=
U
|\psi\rangle_P|a_0\rangle_E.
\]

No amplitude can enter any other charge sector. In particular there is no
local endpoint unitary satisfying

\[
|k\rangle_P|a_0\rangle_E
\longmapsto
|0\rangle_P|a_k\rangle_E
\]

for three distinct choices

\[
a_k\in\{F,G,H\}.
\]

The oriented qutrit swap derived in the incidence packet is therefore an
abstract isomorphism of regular modules, not an element of the admitted local
endpoint dynamical algebra.

## Why measurement remains possible

A clean charge-record isometry has the form

\[
W
=
\sum_aQ_a\otimes|a\rangle_R.
\]

It does not change the endpoint sector. It correlates an already present
charge with a neutral record. Algebraically, controlled pointer operations

\[
\sum_aQ_a\otimes V_a
\]

commute with every `Q_a` and are compatible with superselection.

Thus there is no contradiction between:

- source-derived character projectors;
- a possible nondemolition measurement of an existing `F`, `G`, or `H`
  endpoint;
- impossibility of coherently writing a neutral path amplitude into those
  three sectors by local endpoint dynamics.

Read access is weaker than coherent write access.

## Compensating-charge theorem

A ribbon operator can create or transport charge across the boundary of the
localized endpoint region. If total topological charge is conserved, a
coherent charge-writing isometry must have the relational form

\[
|k\rangle_P|\Omega\rangle
\longmapsto
|0\rangle_P
|a_k\rangle_E
|\overline{a_k}\rangle_R,
\]

where `R` contains the remote compensating charge or boundary current.

Distinct simple charge sectors are orthogonal. Therefore

\[
\langle\overline{a_l}|\overline{a_k}\rangle=0
\]

when the corresponding charges differ. For an input superposition, tracing
out the compensating system removes the endpoint cross terms:

\[
\sum_k\alpha_k|k\rangle_P
\longmapsto
\sum_k\alpha_k
|a_k\rangle_E
|\overline{a_k}\rangle_R.
\]

The coherence survives globally as a relation between endpoint and reference.
It does not survive as an isolated endpoint qutrit after `R` is forgotten.

The partner is not garbage that can simply be uncomputed while leaving the
endpoint in different charges. It is where charge conservation records the
sector displacement.

## Three admissible repair types

### Fixed-total fusion encoding

Store information in different internal fusion paths having one common total
charge. This is the role of the protected three-`C` fusion qutrit. Logical
coherence then lives inside one superselection sector rather than across
`F,G,H`.

This is the preferred data-plane repair already frozen by the programme.

### Retained charged reference

Keep the compensating system as part of the operational carrier and define
all phases relationally between endpoint and reference. The logical object is
then a bipartite charge-neutral code, not one local endpoint.

Reference preparation, transport, protection, and common-mode faults must be
priced explicitly.

### Condensing boundary

Introduce a boundary capable of absorbing the relevant charge differences.
The boundary module changes the superselection structure and may turn some
bulk charge labels into boundary-equivalent sectors.

No `D(S3)` boundary or condensation algebra admitting the required
`F/G/H` relation is frozen in the current source. Such a boundary is a new
coefficient and Hamiltonian lens, not a generic Carrier repair.

Explicit gauge-breaking control is a fourth logical possibility, but it lies
outside the admitted gauge-invariant source theory unless separately
authorized.

## Consequence for the cube-root cleanliness tester

The abstract path-character PVM and its identity

\[
p_{\rm fault}
=
{1\over9}
\sum_{j<k}\|\eta_j-\eta_k\|^2
\]

remain valid for an ordinary coherent path qutrit.

What fails is the proposed shortcut that treats the localized `F/G/H` charge
PVM as though it were already a writable path register. The local charge PVM
is an algebraic template for the character effects. It is not a physical
incidence compiler from neutral paths into superselection labels.

A valid implementation must instead do one of the following:

- implement the `C3` Fourier effect directly on a neutral path ancilla;
- use a retained charged reference and measure the relational character;
- or derive a boundary module that supplies the needed incidence.

The first route avoids the superselection obstruction but still requires a
trusted complex qutrit Fourier instrument. The second and third alter the
carrier and require new fault audits.

## Common-mode warning

A charged reference can rotate endpoint and companion labels together while
preserving total charge and every internal relational check. An independent
orientation anchor is still required for absolute `G/H` naming.

Likewise, a boundary can absorb charge while retaining an unobserved boundary
state correlated with the absorbed label. Condensation as a fusion rule does
not prove rank-one boundary return.

The earlier Gram criterion therefore reappears at the repair interface.

## Exact falsifiers

- A Hamiltonian in the local endpoint algebra claimed to mix `F,G,H` sectors.
- A neutral pointer enlargement claimed to remove central superselection.
- Nondemolition charge readout promoted to coherent charge write access.
- A ribbon-created compensating charge discarded without dephasing the local
  endpoint superposition.
- An abstract regular-module swap called a local endpoint unitary.
- A fixed-total fusion qutrit confused with a superposition of total-charge
  labels.
- A condensing boundary invoked without a boundary algebra and return-state
  audit.
- Gauge-breaking control imported without explicit source authority.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies read-versus-write capability, conserved-flow
incidence, compensating ports, relational encoding, boundary absorption, and
the rule that a conserved label cannot disappear into clean garbage.

The quantum coefficient lens supplies the central endpoint projectors,
topological superselection sectors, ribbon charge transport, conjugate charge,
fusion-space repair, and boundary condensation problem.

## Result

The localized three-cycle character PVM is a readable central observable, not
a writable qutrit subsystem. Local endpoint dynamics cannot realize the
canonical path-to-`F/G/H` swap. Any coherent charge-changing realization must
retain a compensating reference, move to a fixed-total fusion encoding, or
introduce a source-derived condensing boundary. This is the first exact
physical obstruction beneath the algebraically unique incidence.

No build or checker was run for this research-only packet.
