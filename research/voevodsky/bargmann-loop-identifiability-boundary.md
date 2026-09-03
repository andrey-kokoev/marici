# Bargmann-loop identifiability boundary

## Question

Does the ordered four-projector Bargmann invariant separate the underlying labelled rank-one projector configurations?

## Claim boundary

This packet proves global noninjectivity on labelled rank-one projector quadruples. It does not prove noninjectivity on Kitaev's smaller frozen electric associator family; that requires an explicit parameterization of that family and its gauge quotient.

## Observable

For normalized rays \(v_1,\ldots,v_4\) with projectors \(P_i=v_iv_i^*\), the four-copy observable is

\[
B(P_1,P_2,P_3,P_4)
=\operatorname{Tr}(P_1P_2P_3P_4)
=\langle v_1,v_2\rangle
 \langle v_2,v_3\rangle
 \langle v_3,v_4\rangle
 \langle v_4,v_1\rangle.
\]

It is invariant under ray phases and simultaneous unitary conjugation. It is therefore a valid quotient coordinate, but validity does not imply faithfulness.

## Exact collision

In \(\mathbb R^2\), let \(e_1,e_2\) be the standard rays. Compare the labelled quadruples

\[
A=(e_1,e_2,e_1,e_2)
\]

and

\[
B=(e_1,e_2,e_1,(e_1+e_2)/\sqrt2).
\]

Both ordered Bargmann invariants vanish because the first adjacent overlap is zero. Yet their labelled pairwise transition data differ: the fourth ray in \(A\) is orthogonal to the first, while the fourth ray in \(B\) has squared overlap \(1/2\) with it. No simultaneous unitary preserving the first three labelled projectors can identify the quadruples.

Thus the observable fiber over zero contains inequivalent configurations. Repetition and reversed orientation do not resolve this collision because zero is its own conjugate.

## Relevance to the nonzero frozen value

The collision proves that the Bargmann map is not globally monic. It does not determine the fiber over \(-1/8\) inside the frozen `D(S3)` source family. That narrower question needs:

1. the exact parameter space of admissible labelled projector quadruples;
2. the declared gauge action;
3. the map from parameters to all admitted quadrature settings;
4. an injectivity or finite-fiber computation at the target point.

Without these objects, the demonstrated claim remains the exact scalar loop invariant, not reconstruction of associator data.

## Stronger probe design

Pairwise transition magnitudes together with an oriented Bargmann phase can reduce ambiguity, but their joint coordinate must be tested on the declared quotient. Pairwise magnitudes alone lose phase; one Bargmann invariant does not fix all pairwise geometry. A candidate faithful family should include enough independent labelled overlaps or higher cyclic invariants to pass an exact quotient-fiber test.

## Disposition

The four-copy Bargmann observable is gauge-invariant but globally nonfaithful. Faithfulness on Kitaev's frozen electric family is unresolved at the first missing typed object: an explicit admissible-family quotient parameterization. The acceptance test is injectivity, or an exact residual fiber, for the complete admitted probe map at \(-1/8\).

## Verification

- `research/voevodsky/checkers/check_bargmann_loop_identifiability.py`
- `research/voevodsky/results/bargmann_loop_identifiability.json`
