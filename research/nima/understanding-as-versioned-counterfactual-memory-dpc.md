# Deutsch--Popperian conjecture: understanding is versioned counterfactual memory

## Deterministic sufficiency theorem

Let \(\mathcal H\) be a history set, \(\mathcal W\) a frozen future
intervention family, and \(\mathcal R\) a frozen probe family. Define

\[
h_1\sim_{\mathcal W,\mathcal R}h_2
\]

when

\[
r(h_1w)=r(h_2w)
\qquad
\forall\,w\in\mathcal W,\ r\in\mathcal R.
\]

The minimal future-sufficient state is

\[
X_{\mathcal W,\mathcal R}
=
\mathcal H/{\sim_{\mathcal W,\mathcal R}}.
\]

A record map

\[
\rho:\mathcal H\longrightarrow D
\]

is sufficient exactly when

\[
\rho(h_1)=\rho(h_2)
\quad\Longrightarrow\quad
h_1\sim_{\mathcal W,\mathcal R}h_2.
\]

Equivalently, the quotient map to \(X_{\mathcal W,\mathcal R}\) factors
through \(D\). This is a theorem from the definitions, not a physical
conjecture.

## Refinement under new futures

If

\[
\mathcal W_1\subseteq\mathcal W_2,
\qquad
\mathcal R_1\subseteq\mathcal R_2,
\]

then

\[
\sim_{\mathcal W_2,\mathcal R_2}
\;\subseteq\;
\sim_{\mathcal W_1,\mathcal R_1}.
\]

Hence the richer interface has a finer minimal state and a canonical
forgetful map

\[
X_{\mathcal W_2,\mathcal R_2}
\longrightarrow
X_{\mathcal W_1,\mathcal R_1}.
\]

Minimal records therefore form a refinement system indexed by intervention
and probe capability. A state description can be sufficient at one interface
version and insufficient at a later one without having been incorrect on its
original scope.

## Classical capacity bound

If \(X_{\mathcal W,\mathcal R}\) has \(N\) elements, any perfectly faithful
classical record requires at least

\[
\left\lceil\log_2N\right\rceil
\]

bits.

This is a lower bound on distinguishable record states. It does not include
fault tolerance, synchronization, provenance, or access-control overhead.

For the smallest torus, local syndrome leaves four logical classes modulo
local repair. Two loop bits are therefore both sufficient and classically
minimal for the logical future interface.

## Causal shielding

The record is not merely an inscription. It is a state through which future
behaviour factors:

\[
r(hw)=\widehat r(\rho(h),w).
\]

The present record causally shields the admitted future from irrelevant past
detail. A failure of such factorization is a non-Markovian witness for the
declared state description.

## Quantum correction

The set quotient is not the universal record type. In a quantum sector,
incompatible future probes may require retention of a noncommutative state or
observable algebra. A classical serialization can destroy distinctions that a
later quantum intervention would expose.

The adequate memory type may be:

- a density operator;
- an operator system or algebra;
- a quantum channel;
- a phase torsor;
- a hybrid classical--quantum record.

The coefficient lens determines which memory composition law is admissible.
Sum, Product, and Endo memories should not be coerced into one classical
field.

## Source-update boundary

Physical interaction can update a data-plane record, turning an interaction
into persistent memory.

Turning that memory into a new source claim requires a separate control-plane
step: the typed record undergoes criticism and admission before entering a
revised source packet.

The record does not authorize its own schema, interpretation, or theory
revision.

## Snapshot and event-log consequence

An event log retains raw history. A snapshot retains a compressed state. The
snapshot is safe for a declared future interface exactly when its equality
implies future equivalence.

When a software version adds a new query or command, an old snapshot may cease
to be sufficient. Migration then requires either:

- a retained event log;
- an auxiliary reference port;
- proof that the new operation factors through the old snapshot;
- or an explicit statement that historical distinctions are unrecoverable.

## Deutsch--Popperian conjecture

For every bounded problem situation, adequate understanding consists of a
source-typed memory object that:

1. is sufficient for the admitted future interventions and probes;
2. discards only distinctions declared future-inoperative;
3. updates compositionally under new interactions;
4. exposes its record type through the correct coefficient lens;
5. remains stable in the declared regime or completion;
6. versions the interface under which its compression is valid;
7. predicts the first interface extension that would require refinement.

Human understanding advances by constructing and criticizing such memory
objects for increasingly powerful counterfactual vocabularies.

## Critics

### Ontic critic

Future indistinguishability does not prove ontic identity. The conjecture
concerns adequate memory and understanding, not what exists independently of
all interfaces.

### Accessibility critic

Information may persist only in inaccessible environmental correlations. A
physical record need not be a source-facing record.

### Quantum critic

No single classical record need be faithful for incompatible future probes.
The record category must be coefficient-sensitive.

### Resource critic

Persistent memory requires capacity, stability, error correction, and
maintenance. Abstract closure does not construct those resources.

### Moving-interface critic

No finite record is guaranteed sufficient under arbitrary future enlargement.
Sufficiency must be scoped and versioned.

### Trivial-history critic

Keeping the whole history is always sufficient but supplies no minimal
counterfactual compression. The conjecture requires comparison with the
future-equivalence quotient.

## Finite falsifier

A claimed sufficient record fails at the first witness

\[
\rho(h_1)=\rho(h_2)
\]

for which there exist \(w\in\mathcal W\) and \(r\in\mathcal R\) satisfying

\[
r(h_1w)\ne r(h_2w).
\]

The repair is not automatically to retain the full histories. It is to adjoin
the smallest source-authorized port separating the exposed kernel, or to
restrict the interface claim.
