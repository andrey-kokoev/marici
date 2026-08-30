# 1877 — The Galois Sheet Removes Two Real Triple-Wall Branches

## Refinement of Entry 1876

Entry 1876 isolates the real roots of the four rational field norms. A real
root of a norm may belong to either embedding

\[
\sqrt5\mapsto+\sqrt5
\qquad\text{or}\qquad
\sqrt5\mapsto-\sqrt5.
\]

The source routing geometry uses the first embedding. The real-sheet test
must therefore retain this Galois label.

## Exact interval audit

The checker refines every rational root interval below width (10^{-9}) and
uses the certified enclosure

\[
\frac{2236067977}{10^9}
<\sqrt5<
\frac{2236067978}{10^9}.
\]

Corner evaluation of the quadratic-field discriminant identifies its Galois
branch. On the (+sqrt5) branch, the same rational interval calculation
certifies the signs of the repeated critical squares.

## Result

For the first two quartics,

\[
D_1,qquad D_2,
\]

both real norm roots belong exclusively to the conjugate
(-\sqrt5) branch. Their source (+sqrt5) discriminants have no real root.

For each of

\[
D_3,qquad D_4,
\]

exactly two positive real roots belong to the source branch. At all four
source-branch roots,

\[
x>0,
\qquad
v>0,
\]

so both unsolved squared loop energies are positive. Taking (t<0) also
makes every wall-fixed loop energy positive.

Therefore

\[
\boxed{
\text{two region-only divisors meet the real positive-loop continuation,}
\quad
\text{two require complex continuation.}
}
\]

## Scope

This corrects the physical interpretation of Entry 1876, not its exact norm
root census. It still does not prove that the Bunch--Davies relative cycle
pairs nontrivially with either real vanishing cycle.

The next physical test should use (D_3) or (D_4), not (D_1) or (D_2),
because the former admit exact real source-branch critical points with all
loop-energy squares positive.

## Next falsifier

At the first (+sqrt5) root of (D_3), derive the local Morse normal form
of the reduced two-equation system and its vanishing-sphere orientation.
Compare it with the continued source contour on the (t<0) sheet.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_real_roots.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-real-roots.json`
- allocator claim: `seqclaim-f753d1f9f2c44865d9fa4828`
- epistemic event: `ev-000000002234-a1e0fae1-2205-459a-b868-65d93b342b69`
