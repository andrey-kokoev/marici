# Carrier state is the authorized-continuation quotient

## Objective

Define the minimal logical state of a protocol actor without retaining complete event history and without collapsing histories that support different future behavior.

The finite optics fixture supplies the first exact instance.

## Histories and continuations

Let \(H\) be the set of admitted event histories and \(\mathcal U\) the declared family of authorized future command sequences. For history \(h\) and continuation \(u\), let

\[
T(h,u)
\]

be the complete typed verdict trace produced by replaying \(h\) and then executing \(u\).

Define

\[
h\sim_{\mathcal U}h'
\quad\Longleftrightarrow\quad
T(h,u)=T(h',u)
\qquad
\forall u\in\mathcal U.
\]

The minimal Carrier state relative to \(\mathcal U\) is the equivalence class

\[
[h]_{\mathcal U}.
\]

This is the actor analogue of a Myhill–Nerode quotient. In dynamic language it is behavioral or coalgebraic trace equivalence over the authorized continuation alphabet.

For a bounded continuation horizon \(h\), the state must be indexed by the remaining resource:

\[
X_h=H/{\sim_{\mathcal U,h}}.
\]

An action consumes one unit of horizon, so the generally well-defined transition is

\[
X_h\longrightarrow X_{h-1}.
\]

A stationary endomap on one quotient need not exist. It emerges only after the Nerode partition stabilizes with horizon, or after an independently justified unbounded continuation completion.

## Why authority indexes the quotient

The quotient changes when the admitted continuation family changes. Two histories indistinguishable by today's commands may separate after a new source-authorized probe is added.

Therefore the minimized state is not an eternal replacement for the source history. It is a sufficient statistic relative to a protocol and authority epoch.

The durable packet must retain:

- the quotient state;
- the continuation alphabet and version;
- the fold and trace semantics;
- a source reference sufficient for authorized replay or future refinement.

## Optical candidate histories

The finite audit compares histories containing:

- a stale decoder frame and the record \((1,2)\);
- a valid same-preparation pilot and route;
- a same-run wrong-preparation pilot;
- a wrong connection route;
- a reverse-direction route;
- a revisionless pilot;
- a history with a redundant repeated frame-binding event.

Authorized continuations include immediate decoding and several pilot/route completions.

## Exact separations

The quotient establishes:

1. the base history and its redundant-frame variant are equivalent;
2. the valid ready history is separated from the wrong-preparation history;
3. it is separated from the wrong-connection history;
4. it is separated from the reverse-route history;
5. it is separated from the revisionless history;
6. all histories retain the same visible residue-pair projection.

Thus complete genealogy is not identity, but the visible record is not a sufficient statistic.

The wrong-connection and reverse-route histories occupy one behavioral class in the current protocol because both produce the same typed route rejection and no admitted continuation distinguishes their diagnostic causes. They would separate only if diagnostic remediation were added to the continuation alphabet.

## Field necessity

A provenance field is necessary relative to \(\mathcal U\) when deleting it merges two histories with different continuation signatures.

In the optics fixture:

- deleting `preparation_id` merges valid and cross-preparation states;
- deleting `connection_id` merges valid and wrong-route states;
- deleting route orientation merges valid and reverse transport;
- deleting revision merges valid and revisionless states;
- retaining the duplicate frame event adds no behavior and is unnecessary.

Field necessity and state-class separation are therefore different tests. A field may be necessary to prevent an invalid history from entering the valid class even when several invalid histories legitimately share one rejected state.

This gives a mechanical minimality test for Carrier schemas.

## Relation to closure and coalgebra

An idempotent closure is one possible transition fragment, not the universal dynamics. The two-state toggle shows why: its behavior alternates forever and its invariant set forgets temporal phase.

Coalgebraic trace semantics supplies the common dynamic layer. Stabilization packets remain useful as typed interfaces inside that layer:

- closure for idempotent completion;
- controlled invariant for safety;
- checkpoint for recovery;
- actor state for protocol continuation;
- behavioral quotient for minimization.

The mathematical Carrier core is therefore active successor capability, not genealogy. Provenance survives in the interface only when its deletion changes a successor transition, its authority, or the admitted continuation alphabet.

At finite horizon this core is a graded coalgebra across residual continuation resources, not necessarily a stationary coalgebra on one state space. The residual horizon or experiment context is an operative port.

## Compiler rule

Given a finite declared history set and continuation suite:

1. replay every history under every continuation;
2. compute each history's typed trace signature;
3. quotient histories by equal signatures;
4. test each proposed state field by deletion;
5. retain a field only when deletion merges distinct signatures;
6. version the quotient by protocol and authority epoch.

For infinite systems, bisimulation, symbolic automata, or coalgebraic minimization may replace enumeration, but the admission principle is unchanged.

## Disposition

The operative identity of a Carrier actor is neither its current bytes nor its complete past. It is its minimal authorized future behavior, together with enough source reference to replay and refine that quotient lawfully.
