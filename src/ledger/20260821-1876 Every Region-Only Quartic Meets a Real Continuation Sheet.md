# 1876 — Every Region-Only Quartic Meets a Real Continuation Sheet

## Question

Entry 1875 certifies four saturated region-only quartics. Before constructing
local period monodromy, test whether any factor is confined to complex
kinematics.

## Exact root isolation

Symbolica's rational root-isolation algorithm gives:

\[
\begin{array}{c|c|c}
\text{quartic} & \text{positive real roots} & \text{nonreal roots}\\
\hline
D_1&2&2\\
D_2&2&2\\
D_3&4&0\\
D_4&4&0
\end{array}
\]

All roots are simple and no quartic has a negative real root. Hence every
region-only divisor contains at least two points with

\[
z=t^2>0.
\]

The exact isolating intervals are retained in the result packet.

## Interpretation and scope

No factor can be rejected as a purely complex Landau component. Each admits
real values

\[
t=\pm\sqrt z.
\]

For the source wall solutions used here, positive loop-energy coordinates are
obtained on the negative-(t) continuation sheet. This is not the literal
all-positive Bunch--Davies chamber, and root reality does not prove that the
physical relative cycle has nonzero intersection with the vanishing cycle.

Thus the next test remains a Betti/period pairing test, now at an exact real
algebraic degeneration rather than an arbitrary complex root.

## Next falsifier

Choose one isolated positive root of (D_3), where all four roots are real.
Construct the local vanishing cycle and transport the source continuation
cycle from the negative-(t) sheet. Compute their intersection number with
the source orientation and deck character retained.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_region_real_roots.rs`
- `research/benincasa/results/five-site-cyclic-triple-region-real-roots.json`
- allocator claim: `seqclaim-6ecddb366384217335e9caab`
- epistemic event: `ev-000000002233-c93ece31-d57b-40e6-8c2c-8fe0c3106fd2`
