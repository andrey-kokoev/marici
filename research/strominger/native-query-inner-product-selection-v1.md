# Beyond diagonal measures: joint transport/query compatibility

## Conjecture and scope correction

The preceding repair was proved only for positive DIAGONAL measure pairings on R^A4. A natural stronger conjecture is that the two native triangle actions being isometries selects the pairing without this restriction. That stronger conjecture is false; this does not contradict the preceding scoped theorem.

## Falsification

Let J be the twelve-by-twelve all-ones matrix. Keep the SAME transition features f_ab(g)=[g(a)=b], source group, common AB-record preparation, six exchange ports and record reader. Set

    H_lambda=(I+lambda J)/(3+9lambda), lambda>=0.

This pairing is strictly positive: before the positive normalization, its quadratic form is sum x_g^2 + lambda (sum x_g)^2. Every permutation of group coordinates preserves it, so in particular BOTH native triangle left actions are isometries. Every selected feature has three ones and therefore unit squared norm.

Nevertheless, AB and BA have one common support element, giving

    <f_AB,f_BA>_lambda=(1+9lambda)/(3+9lambda).

The SAME exchange law has the SAME first state after AB but gives BA-record readings

    lambda=0:   1/3,
    lambda=1/9: 1/2.

Both complete exchange systems retain involution, positive budget, matched-state fixing, locality relative to their own selected orthogonal component, and all-word ordered composition. The checker verifies involution and isometry over the complete eighteen-coordinate domain, not just the displayed preparation.

Thus transport isometry alone does not authorize diagonal measure pairing. This is a second kind of ambiguity: unlike the previous weighted-diagonal countermodel, BOTH of these models already have left-invariant budgets.

## Repair: ask for joint compatibility with the native queries

Define the linear multiplication operator of each of the SIX existing query functions:

    (P_e x)(g)=f_e(g)x(g).

These are idempotents independently of the pairing. Add the requirement that they are SELF-ADJOINT for the same positive pairing that the two triangle left actions preserve.

This extra condition has a clear mathematical meaning: query-accepted and query-rejected amplitudes are orthogonal. It is not a consequence of a Boolean truth table, nor an automatic physical measurement implementation.

### Finite classification

Write H for an arbitrary positive symmetric twelve-by-twelve matrix, not assumed diagonal.

Self-adjointness of P_e says

    (f_e(g)-f_e(k)) H[g,k]=0.

Transport isometry gives H[hg,hk]=H[g,k]. Therefore if any translated query separates g and k, their matrix entry must vanish.

The six queries alone distinguish only ten of the twelve group elements: one class has three members. However, their LEFT TRANSLATES separate EVERY distinct pair. This follows generally because the six edges include a query from each source vertex: if g != k, choose a with g(a)!=k(a), an available edge a->b, and h sending g(a) to b. Then h k(a)!=b. The generated A4 action is transitive on vertices.

The checker independently verifies a separating translated query for all 132 ordered distinct pairs. Thus every off-diagonal entry of H vanishes. Triangle isometry then equates all twelve diagonal entries. Hence

    H=cI, c>0.

Unit feature normalization removes c. With the separately stated local exchange assumptions and supplied preparation, all finite-word responses are uniquely determined.

This proves a conditional classification of ALL positive inner products on this fixed carrier, not merely diagonal pairings.

## Remaining authority boundary

The improvement is real but conditional. The exact missing premise is now a JOINT source-to-response interpretation:

- native triangle transports act by the specified left actions;
- their actions preserve one fixed response pairing;
- native Boolean queries act as the stated multiplication projections;
- those projections are self-adjoint for that SAME pairing.

The native module supplies transport and query semantics, not their amplitude linearization or a physical orthogonality law. Calling a Boolean test a physical orthogonal measurement would assume this new premise. Query filtering is also not the exchange operation and does not supply a pointer, resource return, or reset cycle.

One possible mathematical realization is the counting-space linearization with its usual inner product. Its existence is straightforward; its physical or source-selected authority is precisely what remains to justify. The proof gives a uniqueness certificate IF that joint interface is independently admitted, not evidence that nature admits it.

## Verification

    python research/strominger/checkers/check_native_query_inner_product_selection.py

Exact standard-library rational arithmetic verifies both positive invariant pairing examples, all six full-domain exchange involutions/isometries, the two continuation readings, and all translated-query separating witnesses. The uniqueness classification is the written argument above. No new Agda compilation or physical experiment was performed.

Receipt: `results/native-query-pairing-selection/general-inner-product.json`.
