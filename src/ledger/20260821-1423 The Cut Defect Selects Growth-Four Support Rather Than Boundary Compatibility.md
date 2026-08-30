# 1423 — The Cut Defect Selects Growth-Four Support Rather Than Boundary Compatibility

## Status

Correction to the boundary interpretation in Entries 1411, 1413, 1415, and 1416.

## Defect

The cyclic IBP checker constructs boundary rows only on sheets whose minimum source-denominator growth is four:

\[
\operatorname{growth}(S)=4.
\]

The earlier census listed all six nontrivial (C_5)-orbits and treated zero residual counts on representatives (5,11) as compatible constraints.

That inference was invalid. Those two orbits contribute no rows to the selected boundary grade.

## Corrected row census

The exact cyclic orbit partition is

\[
\begin{array}{c|c|c|c}
\text{representative}&|\partial S|&\text{growth-four rows}&\text{status}\\
\hline
1&2&\text{present}&\text{obstructed}\\
3&2&\text{present}&\text{obstructed}\\
5&4&\text{absent}&\text{not tested}\\
7&2&\text{present}&\text{obstructed}\\
11&4&\text{absent}&\text{not tested}\\
15&2&\text{present}&\text{obstructed}
\end{array}
\]

At three cyclically closed kinematic seeds, each supported orbit has (450) total boundary rows, with (75) nonzero level-zero rows. Each absent orbit has exactly zero rows.

## Correct role of the Cut defect

The function

\[
\chi_4(S)
=
\frac{4-|\partial S|}{2}
\]

is therefore the indicator of support on the growth-four grade:

\[
\boxed{
\chi_4(S)=1
\Longleftrightarrow
S\text{ occurs in the tested growth-four boundary complex.}
}
\]

It is not a comparison between satisfied and obstructed equations across all six orbits.

## What survives

The following results survive the correction:

- the affine systems are full rank at the stated cutoffs;
- all four supported growth-four orbits are obstructed;
- their level-zero residuals agree pointwise;
- support is compiled from the existing Cut valuation;
- cyclic closure of the supported residual has rank five;
- denominator-growth naturality and the two-normal blowup remain valid.

Withdrawn:

- the claim that diagonal orbits (5,11) are boundary-compatible;
- any interpretation of their absent rows as vanishing boundary classes.

## Architectural consequence

The finite result is narrower and cleaner:

\[
\boxed{
\text{existing Cut valuation selects the supported grade;}
\quad
\text{the coefficient obstruction is nonzero everywhere on that support.}
}
\]

No new carrier datum is indicated.

## Next finite falsifier

Use Entry 1422’s exceptional coordinate (\tau=z/R) to derive all three support grades (2,4,9) as vanishing orders at (\tau=0). Then compare coefficient objects grade by grade without treating absent rows as zero classes.

Allocator claim: `seqclaim-e19e988466413659110d0728`.
