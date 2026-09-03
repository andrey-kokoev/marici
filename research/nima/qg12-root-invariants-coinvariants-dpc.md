# Invariants versus coinvariants: new cycle 3

## Problem

“Unordered root target” can mean either the invariant submodule or the coinvariant quotient. These constructions have different parity content.

## Bold conjecture

Mere descent to the unordered-root quotient excludes odd single-root projection maps.

## Named rivals

1. quotient descent forces the even diagonal class;
2. quotient descent identifies the two roots and therefore admits either single-root lift;
3. only the invariant norm/transfer target forces evenness.

## Risky consequences

If quotient descent forces evenness, the primitive coinvariant generator cannot have a lift of odd total parity.

## Strongest falsification attempt and residual

Let `M=Z e_- direct-sum Z e_+` with root transposition. Then

\[
M^{S_2}=\mathbb Z(e_-+e_+),
\qquad
M_{S_2}=M/\langle e_--e_+\rangle\cong\mathbb Z.
\]

Execution `structured_command_execution:e_31668_1788304260546334300_6` verifies that both `(1,0)` and `(0,1)` lift the primitive coinvariant generator. They have odd total parity. Thus descent to coinvariants does not exclude projection maps and the quotient has no canonical section back to the ordered-root lattice. The bold conjecture is falsified.

## Disposition and residual conjecture

Evenness requires factorization through the invariant class, not merely the unordered quotient. There is a canonical norm/transfer from coinvariants to invariants,

\[
N([e_-])=e_-+e_+.
\]

The norm is an integral isomorphism in the natural generators; it is not a section of the quotient, since quotient after norm multiplies the coinvariant generator by two. The residual conjecture is that the physical specialization is typed as source to coinvariants followed by this norm. This would force evenness, but the target comparison alone does not select norm-like rather than projection-like source correspondence.

The next falsifier is to test the norm/transfer composition and determine whether existing conductor coefficients supply the required factor of two or instead obstruct the factorization.

## Evidence

- `research/nima/checkers/check_qg12_root_invariants_coinvariants.py`
- `research/nima/qg12-source-occurrence-exchange-dpc.md`
- `research/benincasa/results/qg12_root_pair_invariant_target_dpc.json`
