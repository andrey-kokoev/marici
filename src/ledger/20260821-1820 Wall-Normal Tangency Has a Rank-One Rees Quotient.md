# 1820 — Wall-Normal Tangency Has a Rank-One Rees Quotient

## Question

What happens to Entry 1811's quadratic quotient when the two wall normals
become dependent at a deeper Gram--wall locus?

## Rank-one normal form

Near a generic loss of wall-normal rank, choose local Morse coordinates so
that

\[
g_1=h_1+u,
\qquad
g_2=h_2+\alpha u+\varepsilon v.
\]

Here \(\varepsilon\) is \(\det L\) up to a unit. Define the compatibility
normal

\[
k=h_2-\alpha h_1.
\]

Solving both wall equations in the quadratic threshold germ gives

\[
\boxed{
\operatorname{Res}_{1,2}
\sim
\frac{\varepsilon}
{k^2+\varepsilon^2(\tau+h_1^2)}.
}
\]

## Rees specialization

The source-derived center is

\[
(\varepsilon,k),
\]

with equal Rees weights. On the chart

\[
k=\varepsilon\kappa,
\]

the pulled-back residue is

\[
\frac1{
\varepsilon(\kappa^2+\tau+h_1^2)
}.
\]

Removing the derived common exceptional pole gives the normalized grade

\[
\boxed{
\varepsilon\operatorname{Res}_{1,2}
=
\frac1{\kappa^2+\tau+h_1^2}.
}
\]

It is rank one, meromorphic, and has no nilpotent monodromy.

## Result

Tangency alone does not support the exceptional class. If
\(\varepsilon=0\) but \(k\neq0\), the original residue specializes to zero.
The exceptional object is supported only on

\[
\boxed{
\varepsilon=k=0.
}

This is the derived polar/compatibility locus of two already declared wall
sections. It is not a new primary carrier generator.

## Scope

The universal local Rees object is derived here. Which of the 22 physical
pair orbits meet this center, and whether the physical current activates its
exceptional line, remain uncomputed.

## Next falsifier

Pull the labelled five-site wall equations to a generic external-Gram
corank-one chart. For each active pair, solve

\[
\det L=0,
\qquad
h_2-\alpha h_1=0,
\]

and classify the resulting loci as existing soft support, existing marked
incidence, or genuinely new derived support. Then compute the physical
intersection with the exceptional line.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_tangency_rees.py
- research/benincasa/results/five-site-g5-transverse-pair-tangency-rees.json
- Entries 1811 and 1819
- allocator claim: seqclaim-dd5a3d04b3901dbc6d38f44c
