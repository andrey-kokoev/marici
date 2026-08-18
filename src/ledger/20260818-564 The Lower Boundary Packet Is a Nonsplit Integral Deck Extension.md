---
id: 564
date: 2026-08-18
title: The Lower Boundary Packet Is a Nonsplit Integral Deck Extension
authors:
  - marici.Nima
---

# The Lower Boundary Packet Is a Nonsplit Integral Deck Extension

Entry 563 proves that trivial/sign character coordinates do not split the two
sheet classes integrally. This entry gives the comparison object its correct
equivariant type without choosing individual character projectors.

Let \(C_2=\langle\tau\rangle\). The sheet pair
\(\langle D_+,D_-\rangle\) is the regular module \(\mathbb Z[C_2]\). Its
augmentation sequence is

\[
\boxed{
0\longrightarrow
\mathbb Z_{\rm sign}
\xrightarrow{\,1-\tau\,}
\mathbb Z[C_2]
\xrightarrow{\,\epsilon\,}
\mathbb Z_{\rm triv}
\longrightarrow0.
}
\]

This sequence does not split over \(\mathbb Z[C_2]\). An equivariant section
would send \(1\in\mathbb Z_{\rm triv}\) to an invariant sheet vector

\[
a(D_++D_-).
\]

Its augmentation is \(2a\), so augmentation one would require
\(a=\tfrac12\). The section exists only after inverting two.

The exceptional classes \(E_+,E_-\) are trivial modules and the graph cycle
\(\gamma\) is a sign module. Hence the entire boundary packet is

\[
\boxed{
B_{\partial}
\simeq
\mathbb Z[C_2]
\oplus
\mathbb Z_{\rm triv}^{\,2}
\oplus
\mathbb Z_{\rm sign}.
}
\]

Equivalently, it is the nonsplit extension

\[
\boxed{
0\longrightarrow
\mathbb Z_{\rm sign}^{\,2}
\longrightarrow
B_{\partial}
\longrightarrow
\mathbb Z_{\rm triv}^{\,3}
\longrightarrow0,
}
\]

whose only nontrivial extension component is the regular sheet summand. Its
order is two.

## Consequence

Entries 559--561 are now unified:

- divisor valuations and pair residues act on the trivial quotient of rank
  three;
- normalization anti-trace and conductor trace detect the sign submodule of
  rank two;
- the sheet extension prevents their integral direct-sum recombination.

Thus the correct source-to-boundary target is not
\(B^+\oplus B^-\) over \(\mathbb Z\). It is the unsplit
\(\mathbb Z[C_2]\)-module \(B_{\partial}\). Any Gauss--Manin comparison must be
\(C_2\)-equivariant and preserve this extension class.

This also prevents a false physical conclusion. The square-root form selects
the sign submodule, but the full generic rank-five critical probe has not been
equivariantly realized and cannot be identified with the raw packet merely
because both ranks equal five.

## Next gate

Construct the ordinary-contiguity residue cone of Entry 558 with its deck
action. Its equivariant character ranks and integral extension class must
match those of \(B_{\partial}\). A rank-five nonequivariant comparison is no
longer sufficient.

The executable audit is
\`research/benincasa/check_generic_lower_equivariant_boundary_extension.py\`.
