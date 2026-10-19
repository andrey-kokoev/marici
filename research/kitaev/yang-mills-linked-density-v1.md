# Iteration 6 — linked second-order density on arbitrary cubic boxes

## Question and disposition

Does iteration 5's connected pair correction extend to a volume-local coefficient formula, or does its apparent locality disappear as the number of plaquettes grows?

**Constructed:** the order-two normalized log ground-density coefficient on every finite open cubic box. Edge-disjoint pair terms cancel exactly, including pairs sharing a vertex. The surviving terms have bounded support and bounded incidence. This gives explicit volume-independent conditional oscillation and influence bounds for the degree-two log-density surrogate.

**Not constructed:** a uniform bound on the actual analytic remainder, an interacting-source tensorization inequality, or a uniform mass gap. `faithful-excitation-detection` remains open. This turn makes the missing remainder estimate precise rather than silently promoting a Taylor polynomial into the source measure.

[Contract](contracts/yang-mills-linked-density.v1.json). The Hamiltonian, physical quotient and actual vacuum are unchanged. Small r=lambda/kappa here is the source's electric-dominant regime, not an asserted weak-coupling continuum trajectory.

## All-box linked coefficient theorem

Use the open spatial boxes of iteration 3. Let P be the plaquette count, p the fundamental trace on a plaquette, S=sum_p p and L=H0/kappa. Subtract the scalar rP from H/kappa. As before, the perturbation is -rS/2. Distinct plaquette characters are Haar orthogonal and each has norm one. The intermediate-normalized ground vector therefore obeys

\[
a=S/6,\qquad Lb=(S^2-P)/12,
\quad E_0/\kappa=rP-r^2P/12+O_L(r^3).
\]

A subscript L on the remainder allows dependence on box size; it must not be dropped.

For a self pair p squared=1+C_p, the nonconstant character has electric energy 8. Its contribution to b is C_p/96. For distinct plaquettes with no shared link, their edge-variable supports are disjoint, so the link Laplacian product rule has no cross derivatives. Their product is an eigenfunction of L with energy 6. Its b contribution is pq/36.

For a link-sharing pair, cyclically choose basepoints and reverse one loop if necessary so both loops use the common link in the same direction. SU(2) fundamental traces are unchanged by reversal. The recoupling proof from iteration 2 applies verbatim: F=pq=F0+F1 with energies9/2 and13/2. Its b contribution is F0/27+F1/39.

Now normalize rho=Omega squared/<Omega squared> and take the logarithm. Since <a squared>=P/36, the coefficient is 2b-a squared-P/36. Every edge-disjoint pair pq/36 in b is canceled by a squared. Consequently

\[
\log\rho=\frac r3\sum_p p+r^2
\left[-\frac P{18}-\frac1{144}\sum_p C_p
+\sum_{p\sim q}J_{pq}\right]+R_L(r),
\]

\[
J_{pq}=F_0/54-F_1/234,
\qquad R_L(r)=O_L(r^3).
\]

The sum runs over unordered pairs sharing a link, not merely a vertex. Two different elementary squares in an open cubic graph share at most one link. This is an all-size coefficient identity from the actual operator, not a conjectured cluster truncation. Finite-box analyticity and smooth pointwise coefficients use the same imported spectral perturbation/elliptic results as iteration 5.

## Exact support norm, not a volume norm

Write the two common-basepoint loop holonomies as unit quaternions x=(x0,x_vec), y=(y0,y_vec). Then F0=x0 y0+x_vec dot y_vec and F1=3x0 y0-x_vec dot y_vec, giving

\[
J_{pq}=(2x_0y_0+8x_{vec}\cdot y_{vec})/351.
\]

Its supremum absolute value is exactly 8/351 by the operator norm of diag(2,8,8,8)/351, attained by equal imaginary units. It is supported on the seven links in the pair. No sum over all P plaquettes is needed to bound one anchored link's contribution.

In a three-dimensional open cubic graph:

- a link belongs to at most four elementary plaquettes;
- a plaquette has at most twelve other plaquettes sharing one of its four links;
- at most48 unordered adjacent-pair supports can contain a fixed link, by counting a containing plaquette and its neighbors (an upper bound allowing double counts);
- a pair support contains seven links.

These facts remain true at spatial boundaries, where the incidence decreases.

## Uniform conditional oscillation of the degree-two surrogate

Let T2 denote the displayed degree-two polynomial in r, including or excluding its irrelevant global constant. Vary one link while fixing all other links. Each incident fundamental trace has oscillation at most4. Each C_p=p squared-1 has oscillation4. Each J has oscillation at most16/351. Hence

\[
\operatorname{osc}_e T_2
\le\frac{16}3|r|+
\left(\frac19+48\frac{16}{351}\right)r^2
=\frac{16}3|r|+\frac{269}{117}r^2.
\]

This is genuinely independent of volume, but applies to T2, not automatically to log rho. A volume-local bound on osc_e R_L is the missing bridge for the actual conditional density. A total-volume O(P r cubed) estimate would not by itself supply it.

## A checked conditional influence bound for the surrogate

Define the artificial probability measure with normalized density exp(T2) relative to product Haar. It is a diagnostic approximation, not a replacement source. Let c_ej be the supremum total-variation change of its conditional link-e distribution when only link j in the conditioning changes.

For two one-link log weights whose difference has oscillation delta, their normalized laws have total variation at most tanh(delta/4)<=delta/4. An interaction Phi with supremum norm at most a contributes at most4a to that mixed oscillation, hence at most a to c_ej. Constants in an interaction can first be centered without changing the measure.

The first-order plaquette interaction has norm at most2|r|/3. Each incident plaquette involves three other links. The self-character term can be centered to norm r squared/72. An adjacent-pair term has norm8r squared/351 and at most six other links. Thus

\[
\sum_{j\ne e}c_{ej}
\le4\cdot3\cdot\frac{2|r|}3
+4\cdot3\frac{r^2}{72}
+48\cdot6\frac{8r^2}{351}
=8|r|+\frac{175}{26}r^2.
\]

At |r|=1/16 this upper bound is3503/6656<1. At1/8 this sufficient bound already exceeds1; this says nothing about the true maximal contraction regime. These estimates are for the continuous SU(2)-link surrogate itself, not inferred from a finite spin sample.

No approximate-tensorization constant A is asserted from that row bound alone. Any functional-inequality theorem used later must match the chosen state space, conditioning norm and density assumptions, with explicit constants. Moreover the actual source requires a mixed-oscillation row estimate on R_L. A small single-link remainder oscillation alone does not establish a summable influence row over arbitrarily many conditioned links.

## Exact checks and strongest remaining falsifier

The checker constructs open boxes, their ordered square boundaries and link-sharing graph at L=2,3,4. It checks incidence counts, seven-link pair supports, the exact linked coefficient algebra, the rational constants and the norm-attaining quaternion pair. A direct link-Casimir test on two disjoint square loops independently verifies the energy6 product and the canceled logarithmic coefficient; no general operator theorem is inferred from those fixtures.

A separate exact finite-law control checks the log-oscillation-to-total-variation inequality on rational positive weights. It is a control for the general likelihood argument, not an actual SU(2) density computation. The all-box coefficient proof and likelihood comparison are written analytic arguments.

The strongest residual remains R_L: fixed-volume O_L(r cubed) permits constants that grow without bound with L, even though every coefficient tested so far is local. Such a remainder could defeat both the conditional oscillation and influence estimates. Finite-order cancellation does not exclude this rival.

**Next executable operation:** construct or falsify a volume-local bound on the connected remainder/influence using the actual source eigen-equation. If that cannot be supplied, retain the open faithful-detection gate and move to another ready research branch rather than claiming a uniform gap from the surrogate.

Reproduce: `python research/kitaev/checkers/check_yang_mills_linked_density.py`.
Receipt: `research/kitaev/results/yang-mills-linked-density-v1.json`.

No uniform source tensorization, volume-uniform physical detection, continuum theory or atomic claim is made.
