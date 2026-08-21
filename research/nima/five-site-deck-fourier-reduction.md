# The Deck-Saturated Five-Site Complex Splits into 32 Typed Character Blocks

Let \(p:\widetilde U\to U\) be the five-radical Kummer cover with deck group

\[
G=C_2^5.
\]

Once the marked divisor is replaced by its 91-section deck saturation, the
logarithmic de Rham complex is genuinely \(G\)-equivariant. In characteristic
zero the group algebra is semisimple, so the exact Fourier idempotents

\[
e_\chi=\frac1{32}\sum_{g\in G}\chi(g)g
\]

give a canonical chain-level decomposition

\[
Rp_*\Omega^\bullet_{\widetilde U,\log D}
\simeq
\bigoplus_{\chi\in\widehat G}
e_\chi Rp_*\Omega^\bullet_{\widetilde U,\log D}.
\]

Thus the next finite computation is not one undifferentiated 32-sheet
reduction. It is 32 independent rank-one Kummer-local-system reductions on
the base. This is a computational decomposition, not a projection: Entry
1253 shows that the physical integrand has nonzero components in all 32
characters, so no block may be discarded before the physical pairing.

## Exact divisor inventory by character weight

The generic 91-dimensional divisor permutation module is

\[
26\,\mathbf1
+9\sum_i\chi_i
+2\sum_{i<j}\chi_i\chi_j.
\]

At \(E_T=0\), the 45-dimensional marked module is

\[
15\,\mathbf1
+4\sum_i\chi_i
+\sum_{i<j}\chi_i\chi_j.
\]

The specialization kernel therefore has rank 46 and character packet

\[
11\,\mathbf1
+5\sum_i\chi_i
+\sum_{i<j}\chi_i\chi_j.
\]

After removing the total-energy carrier line, the first-Rees attachment is

\[
10\,\mathbf1
+5\sum_i\chi_i
+\sum_{i<j}\chi_i\chi_j,
\]

of rank 45. This agrees with the supported principal-parts cone: the Rees
correction introduces no weight-three-or-higher divisor generator.

## Sharp next test

For every character \(\chi\), construct the twisted base differential

\[
\nabla_\chi=d+\frac12\sum_{i:\chi_i\mid\chi}d\log R_i
\]

together with the saturated marked logarithmic poles, and compute its finite
cohomology. Then compare the generic 91-section complex with the
45-section-plus-Rees totalization character by character. A mismatch is the
first place where higher intersection coherence, rather than divisor support,
is required.

The distinction is essential:

- divisor generators occur only in character weights \(0,1,2\);
- cohomology in weights \(3,4,5\) is still possible through the Kummer
  connection and intersections;
- the physical numerator has support in every character.

Artifacts:

- `research/nima/check_five_site_deck_fourier_reduction.py`
- `research/nima/results/five-site-deck-fourier-reduction.json`
