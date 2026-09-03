# Falsification attempt on the universal transfer chain

## Question

Does every legitimate transfer admit the linear certificate order source typing, descent, faithfulness, coherent composition, completion, physical readout, with a unique first failure?

## Claim boundary

This packet tests the proposed order, not the weaker claim that every transfer needs typed certificates. It supplies ordinary functional-analytic counterexamples; it does not settle the sourced analytic closure theorem for the coherence pyramid.

## Bold conjecture under test

Every legitimate cross-sector identification factors through the stated linear chain, and every failure localizes to its unique first failed certificate.

## Named rivals

- The certificates form a dependency partial order rather than a chain.
- Completion is presentation-relative, so it can precede or erase a finite-stage descent question.
- Global higher obstructions require an unbounded family of coherence conditions rather than one finite checklist.

## Falsification 1: descent without completion

Let `c_00` be the finite real sequences with the `l2` norm and let

\[
F(x)=\sum_n x_n.
\]

Take the trivial quotient, so descent is automatic, and finite truncations are well-defined. For

\[
x^{(N)}=N^{-1/2}(1,\ldots,1,0,\ldots),
\]

we have norm one but `F(x^(N))=sqrt(N)`. Thus `F` has no continuous extension to `l2`. Descent passes while completion fails.

## Falsification 2: completion without descent

Let `F:l2->R` be `F(x)=x_1`. This is bounded and complete. Quotient `l2` by `span(e_1)`. Since `F(e_1)=1`, the functional does not descend. Completion passes while descent fails.

These examples show that descent and completion are logically independent predicates. A chosen workflow can test descent first, but that order is not an intrinsic factorization theorem.

## Falsification 3: nonunique first failure

For the unbounded sum functional, additionally quotient `c_00` by `span(e_1)`. The same proposed expression both fails descent and lacks continuous completion. Calling descent the first failure reflects checklist order, not a canonical mathematical obstruction. Reversing the audit order identifies completion first without changing the object.

## Strongest residual

The original conjecture is falsified at two claims: the certificate stages do not form a universal chain, and a unique first failure is not intrinsic when independent defects coexist.

The surviving conjecture is weaker: admissible transfers are classified by a dependency diagram of certificate predicates. Each claimed strength declares the subset it requires; failures record the full minimal antichain of violated prerequisites. Downstream interpretations are refused whenever any prerequisite fails.

## Disposition

Revise. Preserve source typing as a universal gate for interpretation, but replace the linear strength lattice and unique-first-failure rule by a finite dependency poset with potentially multiple minimal residuals. The completion pseudofunctoriality question remains separate: these examples establish logical independence, not a failure of any sourced completion constructor.
