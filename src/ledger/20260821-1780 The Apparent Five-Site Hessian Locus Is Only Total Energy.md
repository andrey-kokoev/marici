# 1780 — The Apparent Five-Site Hessian Locus Is Only Total Energy

## Question

Entry 1779 left a uniform degree-two factor after separately eliminating the
two Landau equations against the first transverse-Hessian degeneracy. Does
that factor describe a common higher-degenerate critical point, or can the two
resultants use different roots of the auxiliary variable (p=y_i y_j)?

## Frozen compatibility test

Keep the two saturated Landau cubics

\[
f(p,x)=0,\qquad g(p,x)=0,
\]

and the quadratic Hessian equation

\[
h_z(p,x)=0,
\qquad x=t^2.
\]

Reduce both cubics in the same quotient

\[
\mathbb Q(\sqrt5)[x,p]/(h_z).
\]

Their remainders are linear in the same (p):

\[
r_f=a_f(x)p+b_f(x),
\qquad
r_g=a_g(x)p+b_g(x).
\]

A shared critical point therefore requires the compatibility determinant

\[
\boxed{
a_f b_g-a_g b_f=0.
}
\]

No root matching or numerical fitting is used.

## Exact result

For all six source-labelled disjoint-cut orbit representatives,

\[
\gcd\!\left(
\gcd(\operatorname{Res}_p(f,h_z),\operatorname{Res}_p(g,h_z)),
a_f b_g-a_g b_f
\right)
=x^2=t^4.
\]

Thus the degree-two factor retained by Entry 1779 is supported only at

\[
t=0,
\]

the already existing total-energy locus of the cyclic slice. Away from total
energy, every one of the six anomalous-threshold divisors is
Hessian-nondegenerate at every compatible point detected by this audit.

## Narrow conclusion

\[
\boxed{
\text{The six new degree-six divisors have no additional nonzero
transverse-Hessian degeneration locus.}
}
\]

The apparent secondary factor was not a new coefficient divisor or carrier
stratum. It was the existing total-energy support, exposed only after enforcing
same-critical-point compatibility.

This strengthens the five-site evidence for H2:

\[
\text{existing marked/routing carrier}
+
\text{new integrated coefficient support}.
\]

No physical-sheet claim is made.

## Durable evidence

- `research/benincasa/checkers/five_site_disjoint_mixed_pair_hessian.py`
- `research/benincasa/results/five-site-disjoint-mixed-pair-hessian.json`
- `research/benincasa/five-site-disjoint-mixed-pair-hessian.md`
- allocator claim: `seqclaim-e36b8b111371a4f8a6268ed4`
