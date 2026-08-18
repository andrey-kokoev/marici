# Entry 469 — The Even Resonance Is the Koszul Relation Cell

Entry 468 supplied the missing coherence for the odd resonant block: after
normalization its differential and complementary homotopy are

\[
d_-=-6z,\qquad h_-=-\frac z6,
\qquad d_-h_-=h_-d_-=z^2.
\]

The even block should not admit another factorization of this kind.  It is
the relation cell itself.

## Restoring the universal factor

The frozen even generator is \([a^4]\).  It arose only after the universal
factor \(a^4\) had been divided out of the exact differential.  On the
weighted blowup, after translating the strict transform as in Entry 461,
that restored factor is the carrier equation

\[
K/u^2=z^2.
\]

Consequently the correct doubled-carrier coefficient complex is the Koszul
resolution

\[
\mathcal K_{z^2}=\bigl[\mathcal O\,\epsilon
  \xrightarrow{\ d\epsilon=z^2\ }\mathcal O\bigr].
\]

The even resonance is its tautological degree-minus-one relation cell
\(\epsilon\), not an additional ordinary element of \(\mathcal O/(z^2)\).
This immediately explains the asymmetry seen in Entry 464:

\[
\sigma_z(d\epsilon)=0,
\qquad
\sigma_{z^2}(d\epsilon)=1.
\]

Thus the first Cartier boundary cannot shorten the even block.  Its two
ordinary Cartier layers, represented by \(1,z\) in \(\mathcal O/(z^2)\),
remain intact.

## Blockwise derived assembly

The local resonant associated model therefore separates canonically into

\[
\boxed{
  \text{even Koszul relation block }\mathcal K_{z^2}
  \quad\oplus\quad
  \text{odd matrix-factorization block }(-6z,-z/6).
}
\]

The two blocks encode different roles of the same equation.  The even block
remembers the derived relation defining the doubled carrier.  The odd block
records a coherent square root of that relation in the singularity
category.  Their ordinary Cartier lengths are respectively two and one,
recovering the length-three result of Entry 464, while reduction has one
generator from each parity and hence rank two.

The symbolic checker verifies the vanishing first and unit second Cartier
symbols of \(z^2\), the two composites in the odd matrix factorization, and
the resulting layer count.

## Scope of the result

This closes the local **associated, blockwise** doubled-carrier model.  It
does not yet prove that this direct sum is induced by the complete exact
complex: the quartic tail and the carrier-reduction morphism have not been
transported through the same chain-level splitting.  The next gate is
therefore precise: construct that full morphism and test whether its
homotopy fiber is quasi-isomorphic to the Koszul-plus-factorization model
above.  Failure would be a genuine extension between the parity blocks,
not missing carrier geometry.

## Reproducibility

Run:

```text
python research/voevodsky/check_soft_axis_even_koszul_cell.py
```
