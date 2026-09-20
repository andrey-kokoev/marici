# Higher-coherence topology iteration 43: tau-adic completion forces vanishing only after compatible lifts through every formal neighborhood

## Candidate topology

At a Xi zero work over the local analytic ring `O` with ideal

\[
I=(\tau).
\]

Replace labelled and common-history modules by their formal completions

\[
\widehat K=\varprojlim_n K/I^nK,
\qquad
\widehat H=\varprojlim_n H/I^nH.
\]

The successive thickenings remember all normal jets to the Xi divisor.

## Potential vanishing mechanism

If higher coherencers prove

\[
R\in I^nK
\qquad\text{for every }n,
\]

then separatedness gives

\[
R\in\bigcap_{n\ge1}I^nK=0.
\]

This is the divisor-adic version of the separated Rees mechanism from
iteration 10. It would be genuinely noncircular if the `n`th cone supplied the
next divisibility lift from source data.

## What the bordered identity supplies

The current equation

\[
C(R)=\tau H_{\rm border}
\]

provides only first-order divisibility after applying `C`. It does not imply
`R in IK`; its failure is the `Tor_1` class identified in iteration 42.

Passing to the completion does not kill this torsion. For example, the module
`O/(tau)` is already complete and its `tau`-torsion survives unchanged.

## Compatible formal lifts

A sufficient formal criterion is a compatible family `S_n` satisfying

\[
H_{\rm border}-C(S_n)\in I^nH,
\qquad
S_{n+1}\equiv S_n\pmod{I^nK}.
\]

Completeness produces `S in widehat K` with

\[
C(S)=H_{\rm border}.
\]

Then

\[
C(R-\tau S)=0,
\]

and completed injectivity yields `R=tau S`.

To obtain infinite-order vanishing of `R`, rather than just vanishing on the
divisor, one would need to repeat this division compatibly at every order.

## Strictness requirements

The inverse-limit argument requires:

1. `K` is `I`-adically complete and separated;
2. the induced map `widehat C` is injective;
3. the image of `C` is `I`-adically closed/strict;
4. inverse limits have no `lim^1` defect;
5. the formal lift algebraizes or converges in the analytic Köthe topology if a
   neighborhood statement is required.

Projective Köthe closedness does not automatically imply `I`-adic strictness.

## Higher-coherence interpretation

The tower of cones would be useful if its `n`th stage solved the extension
problem from the `n`th to the `(n+1)`st Xi thickening. Mere existence of one
additional homotopy at every rung, without this compatibility and order raise,
does not enter the Krull intersection.

The known positive first Haar normal jet also warns that no tower can claim
flatness in the critical-line normal coordinate. Xi-divisor order and
critical-line normal order are distinct and must not be conflated.

## Verdict for topology 43

`tau`-adic topology provides a valid forcing mechanism: compatible sourced
lifts through every formal Xi neighborhood, together with strict separated
completion, would kill the residual. The present bordered identity supplies
only the first codiagonal divisibility equation, and completion preserves its
torsion obstruction.

The next nonredundant topology to test is a crystalline/connection topology on
the formal Xi neighborhood, asking whether a flat source connection can
canonically propagate a first divisor lift through all higher thickenings.