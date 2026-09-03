# Actual Rees row exact-lift interface

Problem: determine whether current modular Rees rows lift to exact labelled
source rows.

Bold conjecture: `raw_relations` preserves prime-independent row labels and
exact coefficients, including the half twist.

Rivals: current modular rows suffice; source formulas must be rerun over an
exact coefficient ring; or cross-prime reconstruction works without row
identities.

Risky consequence: each receipt must retain a stable source-row label and
coefficients prior to modular reduction, with one rational half-twist
normalization.

Strongest falsification attempt: column labels are structural tuples and row
loop order is deterministic. Rows carry no explicit source label. Coefficients
are reduced modulo the active prime during construction, fiber polynomials
already inhabit that prime field, and the half twist is inserted separately as
the modular inverse of two at each prime.

Disposition: falsified for the current interface. Existing receipts do not
define exact rows. The source formulas can support a new rational backend with
explicit row labels, coefficient-ring abstraction, half twist `-1/2`, an exact
input digest, and projection tests. The next leaf constructs a bounded exact
row and compares its projections at three primes.
