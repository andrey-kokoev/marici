# Exact coverage of Rees row families

Problem: test exact representatives of the remaining raw-row families and the
interpolation interface.

Bold conjecture: K-multiplication rows, q-multiplication rows, and interpolation
weights have common rational constructions matching three prime fields.

Rivals: the first row-family match was accidental; interpolation introduces a
prime-dependent obstruction; or all source operations admit a rational backend.

Risky consequence: representative rows and coefficient-extraction weights of
degrees one and two must agree coefficientwise after projection at primes 101,
103, and 107.

Strongest falsification attempt: exact K- and q-multiplication representatives
were constructed at ambient degree four. Their modular projections were
compared against the corresponding `raw_relations` rows. Exact Lagrange weights
were independently constructed over the rationals and compared with modular
`interpolation_weights`. Every row residual count is zero and every weight list
matches at all three primes.

Disposition: retained for one representative from each raw-relation family.
Interpolation introduces rational denominators but no prime-dependent data at
the tested primes. This does not construct a full exact iterator or an actual
integral generator. The next test must compare the complete bounded stream,
including stable row labels and order.
