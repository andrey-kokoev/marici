---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Clean Top Line Has Matching Energy-Boundary Characters

## Input

Entry 573 identifies the connection induced on the clean proper top-support
line as

\[
\nabla_\Sigma
=d+2\gamma\bigl(d\log E+d\log\ell_-+d\log\ell_+\bigr),
\]

where

\[
\ell_-=X_2+X_3-X_1,
\qquad
\ell_+=X_1+X_3-X_2.
\]

It also proves that both first residues and their common second residue are
horizontal maps of rank-one local systems.

## Boundary characters

The logarithmic residue of the induced connection is the same at all three
energy boundaries:

\[
\boxed{
\operatorname{Res}_{E=0}\nabla_\Sigma
=\operatorname{Res}_{\ell_-=0}\nabla_\Sigma
=\operatorname{Res}_{\ell_+=0}\nabla_\Sigma
=2\gamma.
}
\]

Consequently the local monodromy character of the clean line at each
boundary is

\[
\chi_\Sigma=\exp(-4\pi i\gamma)
\]

for the convention \(\nabla=d+A\), with horizontal equation
\(ds=-As\).  Reversing that convention inverts all three characters but
does not affect their equality.

Because the residue arrows of Entry 573 are horizontal and nonzero between
rank-one lines, they intertwine these characters.  Thus the character on
the top line agrees with the character on each mixed-face image and on the
common \(q_{\mathcal G_{12}}\)-closed image.  No additional character twist
is available at semisimplified rank one.

## What this does not prove

This comparison concerns only the canonical clean support subquotient.  It
does not imply that this line is a direct summand of the rank-21 top module,
nor that nearby cycles commute with a chosen splitting.  The first remaining
obstruction is an extension class of the form

\[
\boxed{
0\longrightarrow \mathcal R_{20}
\longrightarrow \mathcal M_{21}
\longrightarrow \mathcal L_\Sigma
\longrightarrow0,
}
\]

or the oppositely oriented filtration sequence, depending on the admitted
support convention.  Rank-one characters alone cannot detect whether this
extension splits, and equality of semisimplified monodromy must not be
promoted to equality of nearby-cycle objects.

## Consequence for the shared architecture

The top-sector test now separates cleanly:

\[
\boxed{
\text{Cartier/Cousin maps and their Kummer characters are shared}
\quad+\quad
\text{extension data remain sector-specific}.
}
\]

There is no evidence here for a new carrier divisor.  The next admissible
calculation is the off-diagonal logarithmic residue from the complementary
rank-20 filtration piece into or out of \(\mathcal L_\Sigma\) at one of
\(E,\ell_-,\ell_+\).  That requires the filtered connection, not merely the
restricted rank-one connection.

## Outcome contract

~~~json
{
  "claim": "The clean top residue line acquires a mismatched monodromy character on an energy boundary.",
  "status": "falsified_on_the_semisimplified_rank_one_subquotient",
  "logarithmic_residues": {
    "E": "2 gamma",
    "X2+X3-X1": "2 gamma",
    "X1+X3-X2": "2 gamma"
  },
  "character": "exp(-4 pi i gamma), up to the global connection-sign convention",
  "new_carrier_datum": false,
  "remaining_problem": "Compute the off-diagonal boundary residue of the filtered rank-21 connection and classify the resulting extension class."
}
~~~
