# 3262 — Identity-Labelled Kummer Shifts Do Not Type the Quarter Recurrence

## Question

Entries 3256 and 3258 showed that the quarter defects belong to order-four Kummer sectors but are not invariants of those sectors. Can an integral shift in the exponent be represented by keeping the 36 labelled low generators fixed and comparing their relation spaces directly?

The two same-character comparisons are

\[
-\frac54\longrightarrow-\frac14
\]

in the \(-i\) sector and

\[
-\frac74\longrightarrow-\frac34
\]

in the \(+i\) sector.

## Exact two-prime result

For each exponent, reduce the 36 labelled low rows modulo the 720-row high exact sector and compute their relation kernel. In the fixed monomial basis (a^ib^j), (i+j\le7), the results at both primes are:

\[
\begin{array}{c|c|c|c|c|c}
\text{sector}&\dim R_{\rm res}&\dim R_{\rm reg}&
\dim(R_{\rm res}\cap R_{\rm reg})&
\dim(R_{\rm res}/\cap)&\dim(R_{\rm reg}/\cap)\\
\hline
-i&15&10&5&10&5\\
+i&17&10&5&12&5.
\end{array}
\]

Neither relation space contains the other. The labelled identity map therefore does not descend to a map between the two reduced complexes.

The relative-rank differences are still the observed quarter defects:

\[
15-10=5,
\qquad
17-10=7.
\]

But those integers are Euler differences, not yet ranks of a constructed boundary map.

## Narrow conclusion

Multiplication by an integral power of (K) preserves Kummer inertia, but it does not act as identity transport on the selected low-generator quotient. The lost and gained relation directions are transverse enough that a boundary correction cannot be represented by adjoining only the numerical defect dimensions.

A typed recurrence must provide a source-derived chain map that mixes:

- the 36 low labelled generators;
- the 720-row high exact sector;
- the relative boundary costalk.

The frozen exponent-pencil packet contains the fibers of this comparison but not that cross-fiber chain map. Consequently the quarter recurrence remains unconstructed rather than failed.

## Programme consequence

Do not infer a dimensional recurrence from shared Kummer character, equal labels, or relative-rank differences. The next admissible input is the pre-specialization source identity implementing multiplication by (K), together with its Stokes boundary term. If that identity is unavailable, the quarter branch remains closed under the current source packet.

## Artifacts

- `research/benincasa/checkers/exponent_adapter_integral_recurrence_obstruction.py`
- `research/benincasa/results/exponent_adapter_integral_recurrence_obstruction.json`
