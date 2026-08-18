---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Proper Top Connection Is Exactly the Triple-Residue Kummer Line

## Geometric prediction

Entry 568 identified the proper (111) class with the transverse triple
intersection

\[
q_{\mathfrak g_1}=q_{\mathfrak g_2}=q_{\mathcal G_{12}}=0.
\]

At its point (P), the Cayley--Menger polynomial restricts to

\[
K(P)=
\left[E(-x+y+z)(x-y+z)\right]^2.
\]

Write

\[
F=E\ell_-\ell_+,
\qquad
\ell_-=-x+y+z,
\qquad
\ell_+=x-y+z.
\]

In the connection convention of the literal twisted-de-Rham checker, the
triple-residue coefficient therefore predicts

\[
\boxed{\nabla_{\mathrm{top}}=d+2\gamma\,d\log F.}
\]

## Exact comparison

At \(\gamma=5\) over \(\mathbf F_{32003}\), the predicted directional
scalars are

\[
A_x=2\gamma\left(\frac1E-\frac1{\ell_-}+\frac1{\ell_+}\right),
\qquad
A_y=2\gamma\left(\frac1E+\frac1{\ell_-}-\frac1{\ell_+}\right).
\]

They agree exactly with the independently reduced proper-quotient connection
at all five available fibers:

- the two generic points of Entries 584--586;
- the three generic \(\mathcal Q=0\) points of Entry 587.

Thus all ten finite-field directional comparisons pass.

## Consequence

The diagonal transport of the proper physical line is now completely
explained by frozen source geometry:

\[
\boxed{
L_{\mathrm{top}}
=
\text{the rank-one Tate/Kummer triple-residue coefficient line}.
}
\]

This explains simultaneously why the line remains regular at generic
\(\mathcal Q=0\) and why \(\tfrac12d\log\mathcal Q\) failed in Entry 584.
No additional divisor is needed.

It also prevents a mistyped next step.  The proper top line cannot simply be
identified with the older rank-two elliptic infinity-Gysin quotient: their
ranks and coefficient types differ.  Any comparison with the elliptic block
must instead be a supported extension, boundary map, or filtration map
involving the rank-twenty boundary—not an isomorphism of the proper line.

The next admissible calculation is therefore to decompose the
connection-stable boundary (B_{20}) by its three codimension-one face images
and their intersections, then test which graded face object admits the
source-derived infinity-Gysin projection.

## Evidence

- `research/benincasa/proper_top_triple_residue_connection.py`;
- `research/benincasa/proper_top_triple_residue_connection.json`;
- `research/benincasa/elliptic-top-support-geometry.json`;
- Entries 568 and 584--587.

## Outcome contract

~~~json
{
  "claim": "The diagonal connection of the literal proper-top line requires the source quartic or an unidentified elliptic coefficient.",
  "status": "falsified",
  "field_prime": 32003,
  "gamma": 5,
  "fibers_tested": 5,
  "directional_comparisons": 10,
  "mismatches": 0,
  "connection": "d+2*gamma*dlog(E*(-x+y+z)*(x-y+z))",
  "coefficient_type": "rank-one Tate/Kummer triple-residue line",
  "next_experiment": "Decompose the stable rank-twenty boundary by face images and intersections, then type the infinity-Gysin projection on its associated graded."
}
~~~
