# 1801 — Singleton Intersections Convert the Five-Site Logarithm into Kummer Quotients

## Question

After Entry 1800's typing correction, what is the actual coefficient object
at an intersection of the physical threshold with a further singleton wall?

## Exact gates

For each relative label

\[
d=j-i=1,2,3,4\pmod5
\]

and both reflected physical sheets:

1. restrict the added singleton gradient to the \(q_e\)-residue sphere;
2. certify its squared norm by rational interval arithmetic;
3. impose \(g_j=0\) with a source-energy compensator preserving \(E_T\) and
   \(g_i=0\);
4. remove exactly \(g_i\), \(g_j\), and \(q_e\) from the complete 26-term
   source sum;
5. certify all thirteen remaining walls and the resulting residue coefficient
   as nonzero.

All eight labelled-sheet tests pass.

## Local residue

After positive-definite Morse normalization, write the added wall as

\[
g_j=h+\lambda u+\cdots,
\qquad
\lambda\neq0.
\]

The local three-wall germ is

\[
\int
\frac{du\,dv}
{(\tau+u^2+v^2)(h+\lambda u)}.
\]

Taking the added-wall residue first gives

\[
\boxed{
\operatorname{Res}_{g_j}
=
\frac{\pi}
{\lambda\sqrt{\tau+h^2/\lambda^2}}.
}
\]

Its discriminant is

\[
\boxed{
h^2+\lambda^2\tau=0.
}
\]

## Result

Each of the four relative-label orbits carries a rank-one Kummer quotient:

\[
T_s=-1,
\qquad
N=0.
\]

Thus an added singleton does not produce a second logarithmic extension. It
converts the wall-residue quotient of the threshold logarithm into a
square-root coefficient system.

The four quadratic discriminants are derived from the existing
singleton-threshold incidence and the source Morse Hessian. They are
coefficient support, not new carrier generators.

## Architectural consequence

This is a direct five-site example of

\[
\text{existing marked carrier incidence}
+
\text{sector-specific change of coefficient type}
\]

from unipotent logarithmic variation to semisimple Kummer variation.

## Next falsifier

Assemble each Kummer quotient through its free \(C_5\)-orbit and compare its
deck character with the occurrence and soft characters. Then pass to
non-singleton region walls, whose restricted gradients can have different
incidence rank.

## Evidence

- research/benincasa/checkers/five_site_g5_singleton_tangent_gradients.py
- research/benincasa/results/five-site-g5-singleton-tangent-gradients.json
- research/benincasa/checkers/five_site_g5_singleton_source_coefficients.py
- research/benincasa/results/five-site-g5-singleton-source-coefficients.json
- research/benincasa/checkers/five_site_g5_singleton_kummer_quotients.py
- research/benincasa/results/five-site-g5-singleton-kummer-quotients.json
- allocator claim: seqclaim-ac00f271acc09f967faa4faa
