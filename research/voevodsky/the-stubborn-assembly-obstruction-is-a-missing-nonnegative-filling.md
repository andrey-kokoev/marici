# The stubborn assembly obstruction is a missing nonnegative filling

## Source-filling formulation

The owning three-bin moment carrier has atom caps and prefix budgets. Its pairwise restrictions are exact and their coordinate overlaps are strict equalities. The stubborn failure is a boundary triple whose individual pair restrictions lift but whose common source fiber is empty.

Express the total-budget relation through a witness:

    W(x1,x2,x3) = {lambda >= 0 : x1+x2+x3+lambda=B3},

together with the other source constraints. The pairwise projections retain all non-total source inequalities. The omitted source condition is exactly existence of this nonnegative slack witness.

## Actual obstruction

For the owning candidate

    (x1,x2,x3)=(B2/2,B2/2,B3-B2/2),

every coordinate pair has an admitted zero-extended full-carrier lift. The proposed common filling forces

    lambda=B3-(x1+x2+x3)=-B2/2<0.

Thus its filling fiber is empty. The previously verified robust signed-objective gap remains hash-bound in the input packet: this failure changes the owning block bound, not merely a redundant source distinction.

## Exact completion criterion

For this particular source, pairwise admissibility plus nonnegative total slack is equivalent to global source admissibility. The checker verifies every original non-total row occurs in a pair projection; all pair rows are implied by original nonnegative-coefficient rows and mass nonnegativity. Adding the total row therefore restores exactly the full source carrier.

This does not infer the missing budget from the local marginals. Its source-authorized equation is additional retained higher-arity information.

All coordinate orientations give the same slack: solving the equation for any xi yields the same deficit. Across the cut after two bins, s=x1+x2 and r=B3-s, and the third mass is compatible iff x3<=r (with the other caps). This is the cut presentation of the same filling relation, without a privileged causal reading.

## Structural outcome

The overlap maps were already coherent. Their failure was incomplete filling information. The source-filling formulation identifies an exact obstruction value and a necessary-and-sufficient extra witness relation for this carrier.

The witness is unique whenever it exists, because the masses determine lambda. This is different from the coupled observer's ambiguous origin fibers: there the missing boundary distinction selects between multiple admitted fillings; here the proposed boundary has no filling at all.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_stubborn_gluing_filling_space.py

Artifacts:

- `results/stubborn-gluing-filling-space-contract.json`
- `results/stubborn-gluing-filling-space.json`

The owning independent ternary-budget verifier is freshly replayed. Scope is the declared analytical moment relaxation, not exact prime realizability.
