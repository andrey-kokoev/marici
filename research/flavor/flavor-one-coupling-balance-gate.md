# One-coupling balance gate

## Question

WP982 asks when a one-coupling source completion can remove the dimensionless
coefficient fiber isolated in WP981.

Let one positive source coupling \(g\) generate the normalized mediator
parameters monomially:

\[
\gamma=\Gamma g^s,qquad
a=A g^p,qquad
b=B g^q,qquad
c=C g^r,
\]

where \(\Gamma,A,B,C>0\) are source constants. Then

\[
\widehat\rho
=\frac{\gamma^2a^4}{bc^5}
=\frac{\Gamma^2A^4}{BC^5}g^E,
\qquad
E=2s+4p-q-5r.
\]

## Two exact gates

The continuous \(g\)-fiber disappears only if

\[
E=0.
\]

This balance is necessary but not sufficient for numerical selection. When it
holds, the surviving value is

\[
\widehat\rho=\frac{\Gamma^2A^4}{BC^5},
\]

so the source must also fix this dimensionless prefactor independently.

## Hostile completion

The natural same-coupling mass pattern

\[
(s,p,q,r)=(0,1,2,2)
\]

has \(E=-8\), not zero. With \((\Gamma,A,B,C)=(8,5,1,1)\), changing only
the admitted positive coupling from \(g=1\) to \(g=2\) sends

\[
\widehat\rho:40000\longmapsto\frac{625}{4}.
\]

The pair crosses the WP978 boundary \(24696\). A shared origin for all masses
and vertices therefore does not by itself select the full-rank side.

The balanced example \((s,p,q,r)=(0,1,4,0)\) removes the \(g\)-dependence
but leaves the prefactor arbitrary. It is a ray rigidifier until
\(\Gamma,A,B,C\) are source-fixed.

## Consequence

A viable one-coupling selector requires both:

1. exponent balance \(2s+4p-q-5r=0\);
2. independent source determination of \(\Gamma^2A^4/(BC^5)\) in the
   required range.

Neither condition is supplied by the current WP977 grammar. The smallest
falsifier is an admitted completion deriving both gates before flavor fitting,
followed by the complete coupled-vacuum and instrument tests.

## Reproduction

Run:

    python research/flavor/checkers/wp982_one_coupling_balance_gate.py

The generated result is
research/flavor/results/wp982_one_coupling_balance_gate.json.
