# The Failure Trichotomy Is Superseded by a Failure-Signature Poset

Entry 2053 correctly separated three invariant mechanisms but conjectured too
strongly that every event has exactly one type.  A single source parameter can
activate several mechanisms simultaneously.

Let \(t\) control:

1. the preferred coordinate of a surviving line \((t,1)\);
2. both chords of a four-occurrence support, so \(K_4\) specializes to a
   chordless \(C_4\);
3. the second direction of a transport \(\operatorname{diag}(1,t)\).

At \(t=0\):

- the preferred coordinate vanishes while the line survives;
- clique homology jumps from \(0\) to dimension \(1\);
- the transport determinant vanishes and a kernel is born.

The one event therefore has signature

\[
\sigma=(p,s,d)=(1,1,1).
\]

The exclusive trichotomy is false.  Its surviving content is a system of
three independent invariant tests.  Failures should be typed by the Boolean
poset

\[
\boxed{
\sigma\in\{0,1\}_{\rm presentation}
\times\{0,1\}_{\rm support}
\times\{0,1\}_{\rm degeneration},
}
\]

ordered componentwise.  Higher signatures contain more simultaneous failure
structure; they are not alternative names for the same event.

Sector lenses act after this Carrier-level signature.  They may annihilate or
make a supported coefficient composite, but do not alter the support flag
itself.

The repaired Deutsch–Popperian conjecture is:

> Every source-admissible apparent failure carries a presentation-independent
> finite signature of invariant failure mechanisms, functorial under legal
> transformations.  The three currently established coordinates are chart
> survival, support homology, and exterior-section degeneration.

Its falsifier is a legal transformation that changes any coordinate without
changing the underlying source event, or a fourth recurrent failure mechanism
not determined by these coordinates.

The exact hostile checker passes 6/6 gates.

Artifacts:

- `research/nima/failure-signature-poset.md`
- `research/nima/checkers/check_failure_signature_overlap.py`
- `research/nima/results/failure-signature-overlap.json`

Sequence claim: `seqclaim-01e857b367afbb5097d4c8dc`.
