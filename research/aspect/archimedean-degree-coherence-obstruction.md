# Archimedean degree coherence obstruction

## Result

The obvious archimedean candidate does not complete the six-port boundary.
For the Gaussian label operator

`Q e_m = m^2 e_m`,

the heat degree is

`(1/2) log(Q) e_m = log(m) e_m`.

The complete prime-power incidence family gives the same value:

`sum_(p^k divides m) log(p) = log(m)`.

Therefore the heat-degree row is exactly the arithmetic-incidence row. It is
an arithmetic--archimedean coherence equation, not an independent
countercurrent. Adding it leaves the boundary rank at five.

## Hostile witnesses

The equality survives both kinds of small hostile packet:

- repeated primes: `m=8` requires three incidences and gives `3 log(2)`;
- mixed primes: `m=12` gives `2 log(2)+log(3)`.

A bare-prime or prime-square-only observer fails these packets. The completed
incidence tower passes them, but precisely because it already contains the
same logarithmic degree as the Gaussian heat scale.

## Consequence for the operator

The proposed six-type completion cannot use heat degree as its sixth type.
Doing so would count one law twice and manufacture rank by naming.

The missing archimedean datum must be transverse to label degree. Nima's
source gives the natural next candidate: the support-compressed conductor
operator with symbol

`-log(pi) + Re psi(1/4 + i tau/2)`.

Its meaningful information is not its diagonal logarithmic growth. It is the
support-domain boundary form, especially the near-critical even secular
channel at the prime-two boundary. A genuine sixth current now requires:

1. a source-defined domain or boundary trace for that conductor form;
2. an orientation under the seam involution;
3. a coefficient fixed before observing the residual;
4. a witness annihilated by the five existing records but detected by this
   boundary trace.

Until those four items are constructed, the completed packet has five
independent boundary types plus one exact arithmetic--archimedean coherence
constraint. That is a stronger architecture than a fictitious rank-six
completion because it says exactly where the new law must live.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_archimedean_degree_coherence_obstruction.py
```
