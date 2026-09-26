# Explicit binders for the proposed Sigma/Pi comparison

## First interpretation: repeated fixed-index operations

Choose a universe U, a small index type I, and Q:U. Define endofunctors

S_I(X) := Sigma(i:I). X,
P_I(X) := Pi(i:I). X.

The proposed left and right sides are now well-typed:

L(Q) := Pi(i:I). Sigma(j:I). Sigma(k:I). Pi(l:I). Q,
R(Q) := Sigma(i:I). Pi(j:I). Pi(k:I). Sigma(l:I). Q.

The binders are independent in this particular interpretation. Full chains, innermost first:

Q -> P_I(Q) -> S_I(P_I(Q)) -> S_I(S_I(P_I(Q))) -> P_I(S_I(S_I(P_I(Q))));
Q -> S_I(Q) -> P_I(S_I(Q)) -> P_I(P_I(S_I(Q))) -> S_I(P_I(P_I(S_I(Q)))).

This is not a universal equivalence. For I=Bool and Q=Unit, the left has 16 inhabitants and the right 32. Both are sets, so no HoTT equivalence exists between them. A higher coherence witness cannot repair unequal cardinalities of these particular types. This refutes this interpretation as a universal law, not the user's broader closure-preserving structural proposal.

## The genuine dependent distributivity law

Given I:U, J:I->U, and B:Pi(i:I).J(i)->U, there is a standard equivalence

Pi(i:I). Sigma(j:J(i)). B(i,j)
  ~=
Sigma(f:Pi(i:I).J(i)). Pi(i:I). B(i,f(i)).

Forward: g maps to (lambda i. fst(g(i)), lambda i. snd(g(i))).
Backward: (f,h) maps to lambda i. (f(i),h(i)).

The inverse laws use Sigma eta and function extensionality as appropriate. This constructive type-theoretic equivalence retains an explicit selection function f; it is not a principle extracting witnesses from propositionally truncated existence. The latter would be a separate choice question.

Crucially, exchanging product and sum changes the indexing: the outer sum is now over complete dependent functions, not merely over the old individual index j. Omitting that index change creates the false generic commutation law.

## Relation to the table and tower

A lossless row/column transpose naturally uses Pi/Pi exchange for a full table, or Sigma/Sigma exchange for a type of incidences. It does not by itself identify the mixed Sigma/Pi construction above. To proceed with the proposed observer tower, either:

1. make productization a precisely specified reindexing operation, not necessarily literal dependent product; or
2. use the dependent distributivity law and retain its function-valued indices at every stage; or
3. impose extra restrictions under which the desired endofunctors genuinely commute, proving rather than presupposing the comparison.

No automatic C tower is built yet. The next closure obligation is to specify how the resulting indexed families and full comparison chains again form legitimate inputs.

Checker: `research/nima/checkers/check_sigma_pi_interchange_typing.py`.
Result: `research/nima/results/sigma-pi-interchange-typing.json`.
