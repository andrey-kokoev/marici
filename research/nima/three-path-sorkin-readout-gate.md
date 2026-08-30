# Three-path Sorkin readout gate

## Question

Does the nontrivial rank-three exterior/Bargmann port from Entry 2039 produce
an independent third-order interference term?

## Common-measure theorem

For alternatives indexed by a subset \(S\), let the unnormalized screen
record be

\[
p(S)=\left|\sum_{i\in S}\psi_i\right|^2.
\]

This set function contains only singleton populations and pairwise cross
terms.  Its Boolean-lattice Möbius coefficient therefore vanishes above order
two.  In particular,

\[
\boxed{
I_3
=p(123)-p(12)-p(13)-p(23)+p(1)+p(2)+p(3)-p(\varnothing)
=0.
}
\]

The exact checker verifies symbolic vanishing through order seven.

The result remains true when each path is correlated with a record vector:
replace \(\psi_i\) by \(\psi_i\otimes e_i\).  The readout remains quadratic,
and record overlaps only modify the pairwise coefficients.

## Role of the rank-three port

The Bargmann/exterior grade does not appear as a cubic screen contribution.
It constrains whether the complete set of oriented pairwise coherences can be
realized by one positive record Gram.  Hence

\[
\boxed{
\wedge^3\text{ is a coherence-consistency port, not third-order Born
interference.}
}

This separates higher relational structure from higher-order terminal
readout.

## Normalization trap

The Möbius comparison must use one common unnormalized measure.  If each slit
subset is separately postselected and normalized by its own accepted rate,
the resulting projective/nonlinear set function can have nonzero \(I_3\).

For three unit amplitudes, the checker applies the hostile normalization

\[
\bar p(S)=\frac{p(S)}{2+p(S)}
\]

and obtains a nonzero third-order statistic even though the underlying
quadratic \(p\) has \(I_3=0\).  Such a value diagnoses mismatched support or
normalization unless the conditioning itself is the declared physical object;
it is not automatically evidence for fundamental third-order interference.

## Marici consequence

The terminal readout order and the internal coherence grade are different
types:

\[
\text{internal exterior hierarchy}
\not\equiv
\text{Möbius order of the physical record}.
\]

Marici must preserve both.  Collapsing them would either erase legitimate
higher coherence or falsely promote a consistency relation into a new
observable interaction.

## Verification

```text
uv run --with sympy python research/nima/checkers/check_born_mobius_interference_order.py
```

