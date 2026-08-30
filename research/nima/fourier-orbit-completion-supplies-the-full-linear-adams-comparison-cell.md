# Fourier orbit completion supplies the full linear Adams comparison cell

## Multiplication is not Fourier-stable by itself

The base analytic presentation of the coefficient window is

\[
\pi_0([W_t])=M_{W_t}.
\]

Conjugating by Fourier does not generally produce another multiplication operator. It produces convolution:

\[
\pi_1([W_t])
=
\mathcal F M_{W_t}\mathcal F^{-1}
=
C_{\widehat W_t}.
\]

Thus literal commutation of the Adams window history with Fourier is the wrong naturality law.

## Four presentations

The source Fourier orbit supplies the complete comparison packet:

\[
\pi_j([W_t])
=
\mathcal F^j M_{W_t}\mathcal F^{-j},
\qquad
j=0,1,2,3.
\]

These presentations are:

1. multiplication by \(W_t\);
2. convolution by \(\widehat W_t\);
3. multiplication by the reflected window;
4. convolution by the reflected Fourier window.

Fourier acts by cyclic permutation:

\[
\mathcal F\pi_j(u)\mathcal F^{-1}
=
\pi_{j+1}(u),
\]

with indices modulo four. Hence the orbit-completed representation is strictly Fourier-natural.

## Adams boundary

For \(L=\log p\), the coefficient Adams boundary is

\[
d_p=[W_{2L}-W_L].
\]

Each orbit presentation preserves the oriented difference:

\[
\pi_j(d_p)
=
\pi_j([W_{2L}])-\pi_j([W_L]).
\]

Because Fourier conjugation is linear and independent of \(L\), it also commutes with the history derivative on the common transformed core:

\[
\mathcal F^j
\partial_tM_{W_t}
\mathcal F^{-j}
=
\partial_t\pi_j([W_t]).
\]

Thus the four Green/Stokes identities are transported copies of the base identity, not four new analytic constructions.

## Labels and coefficients

The prime and grade labels remain external to the analytic presentation. Fourier acts on the feature carrier, not on the arithmetic coefficient

\[
p^{-1/2-\sigma-it}
\quad\text{or}\quad
\frac12p^{-1-2it}.
\]

Therefore orbit completion preserves:

- prime label;
- grade \(1\to2\);
- endpoint orientation;
- cutoff restriction;
- Euler half-density normalization.

## Green control

The saturated Gram is exactly the sum of the four transported base Grams. Once the base history is bounded and closable, every orbit presentation has the same bound by unitary conjugation.

Hence the full linear Fourier comparison cell for the Adams edge is already generated canonically by orbit completion.

## Remaining qualification

This does not prove that the arithmetic Adams type-fiber map itself is complete under arbitrary constructor words. It proves only that its analytic window-history representation has the required finite Fourier comparison cell.

The remaining word problem concerns:

- iteration along grades;
- Euler-weighted norm growth;
- compatibility with seam and endpoint attachment;
- the source associators joining these constructors.

## Hostiles

Demanding that multiplication commute with Fourier rejects the valid source construction because multiplication and convolution are different presentations.

Keeping only the multiplication presentation produces a bounded local Adams edge that is not closed under sewing.

Absorbing arithmetic coefficients into the four analytic presentations can create presentation-dependent Euler weights and destroy cyclic naturality.

## Frontier

The Adams edge now has a complete linear Fourier orbit packet. The next unresolved quantitative gate is:

> Bound the Euler-weighted Adams type-fiber semigroup on the saturated completed source domain, including its seam and endpoint comparison cells.

This is the constructor-word problem identified earlier, no longer a missing Fourier cell.
