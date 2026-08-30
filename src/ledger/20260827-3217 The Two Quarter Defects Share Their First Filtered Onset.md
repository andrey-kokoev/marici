# 3217 — The Two Quarter Defects Share Their First Filtered Onset

## Question

Do the multiplicities five and seven in Entries 3210 and 3213 arise as an evident static decomposition of the labelled low-readout space?

## Frozen filtration

Use the 36 source-labelled numerator monomials

\[
a^i b^j,
\qquad i+j\leq7,
\]

with the total-degree filtration.  At each exponent value, reduce these low rows modulo the 720 source relations and compute the relation kernel in this same fixed basis.

No transport or fitted identification between exponent fibers is inserted.

## Result

At both primes 32003 and 32009, the cumulative relation dimensions from degrees zero through seven are:

\[
\begin{array}{c|c}
\gamma&\dim K_{\leq d},\quad d=0,\ldots,7\\
\hline
17&(0,0,0,0,0,0,3,10)\\
-5/4&(0,0,0,0,0,2,9,15)\\
-7/4&(0,0,0,0,0,2,9,17)
\end{array}
\]

Thus both quarter defects first appear through two degree-five relations and remain indistinguishable by cumulative dimension through degree six.  Their difference occurs only in the top degree-seven grade.

In the fixed low basis, the generic relation kernel intersects each quarter kernel in dimension five.  The two quarter kernels intersect each other in dimension six.  These intersection dimensions replicate at both primes.

## Interpretation

The five-versus-seven distinction is not visible as five common marked directions with two additional directions already split off at the first filtered onset.  The two supports have the same first onset and the same degree-six closure; the extra distinction is delayed to degree seven.

Moreover, neither quarter relation kernel contains the generic relation kernel.  Relations rotate inside the fixed low basis as \(\gamma\) changes.  Therefore a canonical defect comparison requires source-derived exponent transport or a local Smith specialization map.  Static subtraction of relation spaces is not intrinsic.

## Narrow conclusion

The naive mechanism hypothesis

\[
7=5\text{ marked directions}+2\text{ base directions}
\]

is unsupported as a static filtered direct sum and should be retired in that form.  A transported or extension-theoretic version remains possible, but it must derive its comparison map independently.

## Next falsifier

Construct the local specialization maps from the generic lattice into each reduced quarter fiber.  Compute their associated graded maps at degrees five, six, and seven.  Only then test whether the resulting cokernels carry marked-occurrence and base-normal representations.

## Evidence

- `research/benincasa/checkers/exponent_adapter_defect_filtration.py`
- `research/benincasa/results/exponent_adapter_defect_filtration.json`
- the frozen sparse pencils cited in Entry 3210.

Ledger number authority: `seqclaim-407e83c237facb4ce4ac3935`.
