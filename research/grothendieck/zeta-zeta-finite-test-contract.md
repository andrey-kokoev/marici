# Zeta–zeta finite test contract

## Question

What is the first executable comparison supported by canonical rational
normalization for an asserted product of two zeta factors?

## Claim boundary

The comparison must be supplied as two source-derived finite families of raw
positive-denominator fractions

\[
(L_{p,k})_{p\leq P,\,k\leq K},
\qquad
(R_{p,k})_{p\leq P,\,k\leq K},
\]

with the same ordered prime list, coefficient/exponent index, local variable
specialization, and cutoff pair `(P,K)`. For each index, the admissible test is

1. construct `L_{p,k}` and `R_{p,k}` without using the expected equality;
2. call `marici-raw-fraction-decide-equivalence L_{p,k} R_{p,k}`;
3. retain either the equivalence witness or the unequal normalized numerator
   and denominator predecessor;
4. multiply local factors in the declared order and repeat the same decision
   on every prefix.

The checker result schema is:

```text
assertion_id
source_left
source_right
prime_bound
coefficient_bound
local_specialization
ordered_primes
local_decisions
prefix_decisions
first_residual
rzk_suite_digest
status
```

A passing finite run establishes only equality at the declared finite indices
and prefixes. It does not establish equality of Euler products, formal power
series, meromorphic continuations, or zeta functions. Any such promotion
requires a separate coefficientwise-determination, cofinality, or convergence
theorem with its topology and quantifiers.

## Disposition

The comparison backend is ready: normalization is canonical, equivalence is
decidable by normalized components, and normalized multiplication respects
presentation in both arguments. The first missing typed input is the durable
statement of the particular “zeta–zeta assertion”: its two source constructors,
local variable specialization, index set, and cutoff quantifiers. No repository
artifact found under `research/grothendieck/` names that assertion as
“zeta-zeta”. Instantiating or executing this contract before those data are
provided would insert the assertion rather than test it.
