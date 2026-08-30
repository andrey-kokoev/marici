# Entry 1893 — A Generic Nonsoft Six-Site Critical Divisor Survives Chartwise Saturation

## Frozen calculation

Use Entry 1891's unspecialized wall equations

\[
F(x,v,w,z,k)=0,
\qquad
G(x,v,w,z,k)=0
\]

in one full-rank routing chart.  The critical ideal is

\[
(F,G,\wedge^2 d_{x,v,w}(F,G)).
\]

No symmetry condition among (x,v,w) is imposed.

## Exact elimination

Because (G) is linear in (x,v,w), choose any nonzero component of
(dG).  Then (G=0) and the two corresponding Jacobian minors form a
linear system for (x,v,w).  Cramer's rule gives the unique generic
critical point, and substitution into (F) eliminates the fiber variables.

The calculation was repeated independently on all three pivot charts

\[
\partial_xG\ne0,
\qquad
\partial_vG\ne0,
\qquad
\partial_wG\ne0.
\]

After removing the pivot, routing-Gram, and linear-system factors, every
chart leaves the same divisor

\[
\boxed{
D_6(k,z)=
-5586-5341k-98k^2-392k^3
+z(1026+69k-500k^2+196k^3).
}
\]

The common linear-system factor is

\[
A(k)=1026+69k-500k^2+196k^3.
\]

It is removed by localization at the unique-solution chart; it is not part
of (D_6).

## Generic nonsoftness

On (D_6=0),

\[
z=
\frac{5586+5341k+98k^2+392k^3}{A(k)},
\]

and the three free squared loop coordinates are

\[
\begin{aligned}
x&=\frac{2(4674+3161k-247k^2+658k^3)}{A(k)},\\
v&=-\frac{2(-2622-2981k+10k^2)}{A(k)},\\
w&=\frac{2(2622+209k-934k^2+616k^3)}{A(k)}.
\end{aligned}
\]

None vanishes identically.  At the exact witness (k=1/10),

\[
(z,x,v,w)
=
\left(
\frac{2989}{502},
\frac{38971}{4016},
\frac{45625}{8032},
\frac{41159}{8032}
\right),
\]

so all four squared coordinates are positive.

## Local type

Restrict the constant Hessian of (F) to (ker dG).  Its determinant is

\[
-\frac{k(6+7k)^2A(k)}{(k-3)^2}.
\]

It is generically nonzero.  Hence the critical fiber is an ordinary
quadratic node, not a higher corank degeneration.  For small positive (k)
the transverse determinant is negative, so the real node has two local
branches.

## Narrow conclusion

\[
\boxed{
\text{The nonsymmetric six-site incidence has a generic, chartwise,
nonsoft critical divisor.}
}
\]

This reverses the negative result of the stabilizer-fixed sector in Entry
1886 without contradicting it: (D_6) lives in the full three-coordinate
sector.

It is not yet a physical singularity.  Source wall-multiplier saturation,
residue cancellation across the nine source completions, and the
Bunch--Davies sheet pairing remain uncomputed.

## Next falsifier

Derive the source-ordered wall multipliers and signed-loop sheets on (D_6).
Reject the divisor if every real sheet has a zero multiplier, if the nine
source residues cancel, or if the Bunch--Davies prescription has zero
intersection with its vanishing cycle.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_generic_critical.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-generic-critical.json`
- allocator claim: `seqclaim-8cef0706c6e2f2149acc7f7b`
- epistemic event: `ev-000000002255-1637571f-84d4-42d2-9cf8-8be02d150adf`
