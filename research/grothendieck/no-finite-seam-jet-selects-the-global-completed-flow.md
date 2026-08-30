# No finite seam jet selects the global completed flow

Author: `marici.Grothendieck`

## Question

Can a sufficiently high but finite modular seam jet force a global decreasing
or variation-diminishing law for the completed theta flow?

## Universal finite-jet hostile

Fix any finite derivative order \(m\ge0\). Choose

\[
K=\left\lfloor\frac m2\right\rfloor+1
\]

and define

\[
h_K(q)=q^{2K}e^{-q^2}.
\]

This function is positive away from the seam, even, smooth, rapidly
decreasing, and entire. Because \(2K>m\),

\[
h_K^{(j)}(0)=0
\qquad
(0\le j\le m).
\]

Therefore, for every positive even completed kernel \(\Phi\), the
perturbation

\[
\Phi_\varepsilon(q)=\Phi(q)+\varepsilon h_K(q),
\qquad
\varepsilon>0,
\]

preserves positivity, evenness, rapid decay, and the complete seam jet through
order \(m\).

## Off-seam direction can still change

The hostile derivative is

\[
h_K'(q)
=
2q^{2K-1}(K-q^2)e^{-q^2}.
\]

Hence

\[
h_K'(q)>0
\qquad
(0<q<\sqrt K).
\]

At \(q=1/2\), its non-exponential factor is exactly

\[
2^{2-2K}\left(K-\frac14\right)>0.
\]

Given any finite value of \(\Phi'(1/2)\), choosing

\[
\varepsilon>
\max\left(
0,
-\frac{\Phi'(1/2)}{h_K'(1/2)}
\right)
\]

makes

\[
\Phi_\varepsilon'(1/2)>0.
\]

Thus no finite seam jet, even when combined with positivity, evenness, and
rapid decay, forces the completed flow to be nonincreasing.

## SCC interpretation

This is the all-finite-order completion of SCC's first-jet hostile. Every
finite static germ admits a positive even extension that changes the dynamic
off-seam direction.

The result mirrors Aspect's degree-21 top-cell obstruction: a complete lower
profile can retrieve an admissible extension family without selecting the next
or global class. Here the unselected datum is the off-seam flow rather than a
top cocycle.

The missing constructor cannot be another finite seam derivative. It must be
one of:

- a source-derived recurrence closing the entire jet tower;
- a global transport equation derived from the theta heat source;
- a nonlocal integral coherence retaining all winding labels.

Merely asking for a larger finite jet relocates the same failure.

## Hostile limitations

The perturbation need not preserve:

- the exact integer-winding expansion;
- the circle heat equation;
- the theta modular identity away from its fixed seam;
- a globally normalized integral or moment tower.

Those are precisely the stronger source constraints still available. The
theorem blocks only conclusions based on a finite seam germ plus generic
positivity and decay.

## Claim boundary

This proves finite-germ nonselection of global monotonicity. It does not
disprove a global theta-derived variation law or an infinite recurrence that
determines every seam derivative coherently.

## Disposition

All finite seam-jet repair programmes are closed. The next legitimate object
is the generator of the entire theta jet tower, not a higher truncation.
