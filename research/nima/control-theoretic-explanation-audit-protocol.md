# Control-theoretic explanation audit protocol

## Purpose

This protocol distinguishes accurate shadows, identifiable realizations, and
source explanations without demanding an ultimate theory. It is relative to a
frozen problem situation and reports the first failed gate.

## Required packet

Before auditing a candidate, freeze:

1. source objects and their nonidentity transformations;
2. source-authorized atoms, relations, and global attachments;
3. admitted interventions and probes;
4. ordered state type and domain;
5. authorized realization gauge;
6. Sum and Product readout maps;
7. completion or operating regime;
8. hostile variations admitted by the same source grammar.

If one of these is absent, the audit reports unresolved typing rather than
silently selecting it from the candidate.

## Gate 1: lower-lens adequacy

The candidate Endo realization \(E\) must reproduce every frozen Product and
Sum readout:

\[
E\xrightarrow{\Pi_{\mathrm{prod}}}\Delta,
\qquad
\Delta\xrightarrow{\Pi_{\mathrm{sum}}}j.
\]

Failure rejects the candidate. Passage establishes consistency only.

## Gate 2: ordered intervention closure

Every admitted intervention generator must act on the declared state space,
and every frozen source relation must hold before scalar projection.

For generators \(g_i\) and relations \(r_k\), require

\[
E(r_k)=I.
\]

Scalar cancellation of a nonzero ordered residual fails this gate.

## Gate 3: behavioural minimality

Compute the future-equivalence quotient or the corresponding controllability
and observability reduction. Remove unreachable and unobservable dark state.

For a finite linear system, require full controllability and observability
rank on the claimed realization state. A nonminimal state may still be a
valid implementation, but its dark directions have no explanatory authority
for the frozen problem.

## Gate 4: realization identifiability

Let \(\mathcal Q\) be the hostile-closed realization moduli after authorized
gauge. The complete behaviour map

\[
\overline\Sigma:\mathcal Q\longrightarrow\mathcal Y
\]

must be injective for global structural identifiability.

At the infinitesimal level, the behavioral derivative may have only gauge
kernel. A non-gauge invisible deformation rejects hard-to-vary status.

## Gate 5: source derivation

Require a checkable derivation

\[
S\xrightarrow{\pi}E
\]

of state types, intervention ports, transition constructors, and lower-lens
readouts.

A backward fit from \(\mathcal Y\) to \(E\), followed by relabelling the state
coordinates with source nouns, fails this gate.

## Gate 6: generator density and presentation invariance

The full constructor must be reconstructed from a proper source-atomic packet
through declared composition, gluing, anomaly, and boundary laws.

Equivalent source presentations must yield equivalent explanatory verdicts.
A mega-generator containing the complete fitted realization fails.

## Gate 7: family naturality

For every admitted source transformation \(f:S\to S'\), require a typed
realization map \(F(f)\) and commuting intervention/readout squares.

At least one nonidentity, prospectively selected source transformation must be
tested. Naturality on a discrete collection of fitted instances is vacuous.

## Gate 8: stable completion or regime control

The moduli-to-behaviour map must remain an embedding in the declared
completion. Metric observability or identifiability lower bounds may certify
this when source-derived norms exist.

A sequence of normalized realization states or parameters whose outputs
vanish in the limit is a completion-escape witness.

## Gate 9: prospective hostile

Freeze a composite intervention, neighbouring source instance, perturbation,
or regime boundary before evaluating the candidate. The same constructor law
must predict the outcome without adding a new generator or correction.

This is the Popperian gate that prevents a complete retrospective encoding
from passing as explanation.

## Classification

| Highest passed gate | Classification |
|---|---|
| 1 | accurate Sum/Product shadow |
| 2 | coherent ordered model |
| 3 | minimal predictive realization |
| 4 | identifiable behaviour-relative realization |
| 5 | source-derived realization |
| 6 | generative source explanation |
| 7 | family-natural explanation |
| 8 | completion-stable explanation |
| 9 | prospectively tested explanation |

These are scoped achievements, not metaphysical ranks.

## Pinned examples

### Pauli and toric code

The one-qubit Pauli packet passes ordered closure:

\[
P(v)P(w)=\omega(v,w)P(v+w).
\]

Additive labels plus the central cocycle identify the Pauli group law up to
section gauge. The lattice family derives these actions from cell incidence,
primal--dual intersection, and periodic attachment. Translations and lattice
symmetries supply nonidentity naturality tests.

Status: generative family-level algebraic explanation of syndrome and logical
operator structure. Physical actuator construction is a deeper problem
packet. Decoder selection fails source derivation unless noise or dynamics
supplies it.

### Ho--Kalman realization

Full-rank Hankel data reconstructs a minimal fixed-order linear realization up
to similarity.

Status: identifiable behaviour-relative realization. It becomes a source
explanation only if linearity, ports, and state order are independently
derived for the plant.

### Compiled software table

A transition table compiled from a source state machine retains explanatory
authority when the compiler correctness map and source derivation remain
available.

The identical table without that record is an executable predictive
realization, not a source explanation.

### Scalar-shadow hostile

A determinant or completed scalar section can pass lower-lens adequacy while
trace-zero shears and commutator dynamics remain invisible.

Status: accurate diagnostic shadow; fails realization identifiability unless
an independently typed full characteristic-transfer theorem applies.

## Machine-readable disposition schema

    {
      "candidate": "...",
      "problem_packet": "...",
      "highest_gate_passed": 0,
      "classification": "...",
      "first_failed_gate": "...",
      "witness": "...",
      "authorized_gauge": ["..."],
      "unresolved_typing": ["..."],
      "completion_stable": false,
      "prospective_hostile_passed": false
    }

## Decision rule

Do not call a lower classification false merely because it is not yet an
explanation. Report exactly what it establishes and the first additional
constructor needed for the next gate.
