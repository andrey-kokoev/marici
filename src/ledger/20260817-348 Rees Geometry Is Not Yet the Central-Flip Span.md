# Rees Geometry Is Not Yet the Central-Flip Span

## Result

The source-side candidate geometry is explicit, but it does not yet define
the central-flip six-functor correspondence.

For ordered adjacent branch sections \((a,b)\) and complementary road
section \(c\), entry 216 constructs

\[
Y=\operatorname{Bl}_{(ab,c)}\operatorname{Spec}\mathbb Z[a,b,c].
\]

Its two charts are

\[
\mathbb Z[a,b,t],\quad c=abt,
\qquad
\mathbb Z[a,b,c,s]/(cs-ab).
\]

The center \((ab,c)\) is a regular sequence, the second chart is normal,
the exceptional fiber over \(ab=c=0\) is \(\mathbb P^1\), and the derived
self-intersection has ranks \((1,2,1)\). The blowdown is proper. Entries 249
and 315 additionally supply the oriented \(dP_6\) KN carrier and the local
labelled log-node orientation line.

These facts construct a Rees/log carrier. They do not construct a span.
The blowdown has not been identified with either projection required by

\[
\operatorname{Tr}_{Z}\bigl(p^*(-)\otimes q^!(-)\bigr).
\]

Moreover, the entry-143 object is an explicit support/BM--Cech complex, not
the realization of a ringed space or stack to which a morphism \(q\) can be
given. No relative dualizing complex or oriented trace for such a span is
defined.

## Refined construction order

The previous missing block d_central_flip_ringed_span therefore separates
into three prerequisites:

1. d_central_flip_target_geometrization: realize the literal entry-143
   support complex as the relevant functorial costalks of a ringed/log target;
2. d_central_flip_projections: construct a normalization-provenanced space
   or stack \(Z\) and actual maps \(p,q\) to the source and geometrized target,
   with the required proper/lci hypotheses;
3. d_central_flip_dualizing_trace: construct and orient the relative
   dualizing/Thom line and its extraordinary trace.

Only afterward can d_central_flip_pc_purity compare the already-proved
finite corner

\[
\mathbb D(Q/B_{\rm opp})\widehat\otimes
\mathcal C_{Q_{03}}^{\rm norm}\otimes[dX_{03}]
\]

with the actual PC extraordinary costalk.

A standard Cartier closed-immersion purity theorem closes entry 131's
scoped edge because its target and perfect normal line are defined. It does
not supply any of the three central-flip prerequisites above.

Delegation evidence: run-22a77e2761b8459aae1ccc5bbc3be9b3 and
run-e5e0d3baf46649be8033eaf9e2e6f6de.
