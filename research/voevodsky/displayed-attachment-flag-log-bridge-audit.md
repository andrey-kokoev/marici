# Displayed attachment audit for the flag/log bridge

## Question

Does the formal comparison cell over the bounded flag/log bridge define a displayed univalent attachment category, and what is the first obstruction?

## Claim boundary

This packet tests one proposed attachment only: a nullhomotopy of the distinguished degree-two class on the minimal logarithmic and flag complexes. It does not classify other Marici attachments, construct a global displayed category, or infer a readout.

## Base bridge

Let

\[
A_{\min}=\mathbb Z[-2],\qquad B_{\min}=\mathbb Z[-2]
\]

with distinguished generators \(\Xi\) and \(\sigma\). The checked residue comparison is

\[
\operatorname{Res}:A_{\min}\xrightarrow{\cong}B_{\min},
\qquad \Xi\longmapsto\sigma.
\]

It is inverted by source localization and becomes an identity path after univalent completion.

## Candidate attachment fiber

For a cochain complex \((X,\xi_X)\) with distinguished cocycle \(\xi_X\in Z^2X\), define the nullhomotopy fiber

\[
\operatorname{Null}(X,\xi_X)
=
\{h\in X^1\mid dh=\xi_X\}.
\]

This is the homotopy fiber of \(d:X^1\to Z^2X\) over \(\xi_X\), not an untyped set of auxiliary labels.

For the two minimal complexes,

\[
A_{\min}^1=B_{\min}^1=0,
\]

while \(\Xi\) and \(\sigma\) are nonzero. Therefore

\[
\operatorname{Null}(A_{\min},\Xi)
=
\operatorname{Null}(B_{\min},\sigma)
=
\varnothing.
\]

The formal cell \(\tau\) with

\[
d\tau=(\Xi,-\sigma)
\]

exists only after replacing the bridge by its signed comparison cone. It is not an object in either base fiber.

## Variance audit

A chain map \(f:(X,\xi_X)\to(Y,\xi_Y)\) satisfying \(f(\xi_X)=\xi_Y\) sends a nullhomotopy \(h\) to \(f(h)\). Thus the displayed nullhomotopy construction is covariant:

\[
\operatorname{Null}(X,\xi_X)
\longrightarrow
\operatorname{Null}(Y,\xi_Y).
\]

It does not instantiate the proposed contravariant attachment fibration

\[
\operatorname{Att}:\widehat{\mathcal C}^{op}\to\mathbf{Cat}_{\rm univ}.
\]

Contravariance could arise from a separately defined category of extensions and pullback squares, but no such extension object, cartesian lift, or cleavage is materialized here.

## Displayed-univalence test

Displayed univalence cannot yet fail or pass for the proposed attachment because the required displayed category has not been constructed. The exact first obstruction is earlier:

1. the candidate nullhomotopy fibers over the two base objects are empty;
2. the cone cell belongs to a new target complex, not either fiber;
3. nullhomotopies transport covariantly, whereas the proposed attachment fibration is contravariant.

A proof that \(\operatorname{Res}\) is an equivalence does not repair any of these typing failures.

## Strongest falsification attempt

Adjoin degree-one generators \(a\) and \(b\) with \(da=\Xi\) and \(db=\sigma\). The extended fibers become inhabited, and \(\operatorname{Res}\) can be extended by choosing \(a\mapsto b\). This construction demonstrates consistency but not provenance: it is the universal cell attachment that kills the distinguished classes. The choice is extra structure and is not induced by the original bridge.

## Disposition

The Grothendieck-total-category architecture remains a viable programme, but the formal comparison cell is not its first displayed attachment. For this bridge, the first obstruction is the absence of a typed contravariant extension fibration. The next admissible construction is a category whose objects are source-derived extensions over a base complex and whose cartesian morphisms are pullback squares; only then can displayed univalence be tested.

## Verification

- `research/voevodsky/checkers/check_displayed_attachment_flag_log_bridge.py`
- `research/voevodsky/check_cosmology_comparison_cone_definition.py`
- `research/voevodsky/check_cosmology_cone_to_source_lift.py`
- `research/voevodsky/aspect-univalent-coherence-handoff-audit.md`
