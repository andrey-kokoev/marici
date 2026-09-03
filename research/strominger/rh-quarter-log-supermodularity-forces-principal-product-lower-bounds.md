# Quarter log-supermodularity forces principal-product lower bounds

## Question

Does reverse Hadamard–Fischer structure itself explain every positive principal minor?

## Claim boundary

The general implication is algebraic: a positive diagonal and log-supermodular principal-minor map force the product lower bound. The exact matrix test covers the order-eight transfer; it does not prove log-supermodularity for arbitrary Hurwitz size.

## Disposition

For every subset \(S\),

\[
p(S)\geq\prod_{i\in S}p(\{i\}),
\]

with equality only at sizes zero and one and strict inequality for all 247 larger subsets. Apply reverse Hadamard–Fischer to a current subset \(T\) and a disjoint singleton \(\{i\}\):

\[
p(T)p(\{i\})\leq p(T\cup\{i\})p(\varnothing).
\]

Since \(p(\varnothing)=1\), iteration gives the bound. Therefore positive diagonal plus log-supermodularity is sufficient for all P-matrix signs; fixed signs of individual almost-principal minors are unnecessary. The next leaf is `quarter-transfer-anti-sign-symmetric-induction`, formalizing the Desnanot–Jacobi induction that reduces all principal positivity to opposite paired almost-principal products.
