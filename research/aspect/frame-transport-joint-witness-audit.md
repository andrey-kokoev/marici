# Frame-transport joint-witness audit

## Result

The corrected optical invariant distinguishes a presentation change from an object mutation. A certified modulo-5 phase shift has a coherent invertible record transport across all twenty source classes. Replacing rate 5 by rate 6 destroys injectivity and cannot be treated as a frame isomorphism.

The sufficient evidence composition is one common run plus either a common context or a source-derived coherent context transport. This packet specifies the acceptance signature; it does not establish that current Marici lacks or implements that composition.

## Source, ports, and transport

For the two labelled clocks, let

\[
H_\delta(f)=(f\bmod4,f+\delta\bmod5).
\]

The certified transport

\[
T_\delta(a,b)=(a,b-\delta\bmod5)
\]

satisfies

\[
T_\delta H_\delta=H_0
\]

on every source in the declared band. The epoch-0 decoder consequently satisfies (D_0T_\delta H_\delta(f)=f). This is a source-derived change of readout frame.

## Object mutation

Replacing the second rate by 6 gives records ((f\bmod4,f\bmod6)). Sources 0 and 12 collide, so the observer is not injective on the twenty-class band. No invertible record relabelling can turn a noninjective observer into the original injective one. Rate mutation therefore changes the instrument object rather than its presentation.

## Encoding audit

- Marginal schema validation accepts the splice.
- A content-hash bundle binds bytes but not their common physical realization.
- An untyped causal chain records order without enforcing run or frame coherence.
- Literal epoch equality rejects the splice but also rejects valid transported observations.
- Common run plus an authorized coherent frame transport has the required signature: reject the splice and accept the transported same-run packet.

## Smallest hostile

Bind individually valid evidence into one immutable bundle without checking whether its run-scoped contexts are equal or connected by an authorized transport. The bundle preserves every byte and still admits the false spliced claim.

## Conserved information and detector

The phase transport preserves the full joint-observer information and the decoded source class. The rate mutation does not. The prospective detector is therefore two-sided: it must reject the known cross-run splice and accept a source-certified same-run phase transport.

## Completion and authority boundary

This exact audit defines the semantic invariant that a candidate composition must realize. Determining whether existing Marici relations already enforce it requires a capability-level execution audit. Failure of an encoding would identify a missing invariant, not by itself a missing primitive.

## Reproduction

Run:

    python research/aspect/checkers/frame_transport_joint_witness_audit.py
