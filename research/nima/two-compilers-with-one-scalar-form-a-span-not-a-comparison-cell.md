# Two Compilers with One Scalar Form a Span, Not a Comparison Cell

## Correction

Aspect's ordered-projector loop and cyclic-permutation compiler calculate the
same Bargmann invariant on their ideal algebraic domains:

\[
\operatorname{Tr}(P_iP_jP_k)
=
\operatorname{Tr}\left(V_3(P_i\otimes P_j\otimes P_k)\right).
\]

This gives a commutative span into a common scalar readout:

\[
L\longrightarrow\mathbb C\longleftarrow S.
\]

It does not yet give a comparison cell between the physical compilers.

The loop compiler \(L\) carries one-copy sequential-filter structure,
reference-branch calibration, loss ports, rejection ports, and filter order.
The shift compiler \(S\) carries three-copy preparation, mode
indistinguishability, coherent permutation control, and shared-control fault
structure.

Their resource objects and complete records are different.

## Finite nonfaithfulness witness

Let a loop record be

\[
\ell=(B,a),
\]

where \(B\) is the retained Bargmann amplitude and \(a\) is unmatched
attenuation or rejected-environment data. Let a shift record be

\[
s=(B,d),
\]

where \(d\) records copy distinguishability or control coherence.

Both scalar projections forget the second coordinate:

\[
\pi_L(B,a)=B,
\qquad
\pi_S(B,d)=B.
\]

Records \((B,a_1)\) and \((B,a_2)\) with \(a_1\ne a_2\) have the same scalar
image. The same holds for distinct \(d\). Therefore neither scalar map is
faithful on the complete compiler record, and equality of scalar outputs
cannot reconstruct a relation between the omitted coordinates.

## Required comparison structures

Any of the following would be stronger than the current span:

1. a source-authorized common refinement \(R\) with maps to both compiler
   records;
2. a resource-preserving simulation from one compiler to the other;
3. a bisimulation identifying complete operational traces;
4. a fault translation mapping every admitted hostile and residual between
   the two implementations;
5. a universal realization theorem showing both are initial or terminal
   realizations of the same instrument specification.

No such structure is currently supplied.

## What cross-compiler agreement does establish

Agreement remains valuable because the two implementations have different
failure modes. On independently admitted ideal domains, matching complex
amplitudes and conjugation under reversal provide strong evidence that both
implement the same abstract oriented invariant.

The correct claim is:

> Two independent realizations agree after projection to one abstract
> invariant.

The stronger claim is not yet admitted:

> The two physical compilers are equivalent, comparable, or mutually
> translatable instruments.

## DPC

A claimed comparison cell between compilers is accepted only if:

1. the compared domains and resource packets are typed;
2. the complete records, not only selected scalar outputs, are related;
3. the relation preserves admitted composition and orientation reversal;
4. copy, loss, rejection, and control resources are accounted for;
5. hostile faults have a declared translation or common refinement;
6. the relation survives the declared completion and uncertainty model.

Scalar agreement alone receives the verdict
\`common_readout_span_only\`.

## Cross-sector consequence

This corrects a recurring Marici inference. Two source mechanisms producing
the same scalar value need not be two factorizations of one authority-bearing
constructor. They may only meet after a lossy readout. The distinction applies
to Flavor source and physical CP cycles, theta/Tate scalar factorizations, and
software implementations sharing output bytes.

