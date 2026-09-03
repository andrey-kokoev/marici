# RH and the remainder-cone equivalence skeleton

## Question

What exact theorem should be completed before another source-factor mechanism is proposed?

## Claim boundary

This packet states the equivalence between RH and the all-rank remainder Hankel cone. Its abstract moment and pole steps, source normalization, paired infinite expansion, convergence bounds, common initial domain, and classical Hadamard input are established in companion packets. The source owner independently confirmed the endpoint--gamma--prime comparison and inspected Titchmarsh's Hadamard source equations. The only substantive unproved statement is now the all-rank cone inequality itself.

## Cone statement

For positive \(t,h\), let

\[
a_n(t,h)
=
H_R(t+nh)-H_R(t+(n+1)h)
\]

with \(H_R\) fixed by one completed explicit-formula normalization. Define

\[
A_N(t,h)
=
(a_{i+j}(t,h))_{0\leq i,j<N}.
\]

The cone assertion is

\[
A_N(t,h)\geq0
\]

for every finite \(N\) and positive rational \(t,h\).

## Forward direction

Assume RH. Then

\[
\lambda_\rho
=-\left(\rho-\frac12\right)^2
=
\gamma_\rho^2>0.
\]

Since \(H_R=H-e^{t/4}\), the completed identity expresses the remainder moments as one endpoint atom

\[
Y=e^{h/4}>1,
\qquad
c_E=e^{t/4}(e^{h/4}-1)>0,
\]

plus zero-side localizer moments with bases

\[
y_\rho=e^{-h\gamma_\rho^2}\in(0,1).
\]

Consequently, for every coefficient vector \(c\),

\[
c^*A_N(t,h)c
=
c_E\left|\sum_{j=0}^{N-1}c_jY^j\right|^2
+
\sum_{[\rho]}
w_\rho(t,h)
\left|\sum_{j=0}^{N-1}c_jy_\rho^j\right|^2
\geq0.
\]

Convergence and multiplicity normalization for this Gram representation are established in the paired-Hadamard and endpoint--gamma--prime audit packets.

## Reverse direction

Assume the cone.

### Rational to real meshes

Every finite matrix depends continuously on \(h\). Density of positive rationals and closure of the PSD cone extend positivity to every positive real mesh.

### Moment representation and endpoint extraction

Hamburger representation gives a positive measure for \((a_n)\). The source-derived asymptotic

\[
\frac{a_n}{Y^n}\to c,
\qquad
Y=e^{h/4},
\]

forces support in \([-Y,Y]\), mass \(c\) at \(+Y\), and no mass at \(-Y\). Subtracting the endpoint atom leaves a compact positive full-localizer measure.

### Pole comparison

The moment generating germ is the compact-measure transform

\[
\int\frac{d\mu_h(y)}{1-yz}.
\]

The exact general-zero expansion gives a second expression with grouped poles at

\[
z=e^{h\lambda_\rho}.
\]

On a common continuation domain and at a generic mesh, distinct nonzero grouped residues expose distinct poles. A compact real measure has only real singular support, so

\[
e^{-h\lambda_\rho}\in\mathbb R.
\]

Arbitrarily small generic meshes eliminate phase aliases and force

\[
\operatorname{Im}\lambda_\rho=0.
\]

Finally,

\[
\operatorname{Im}\lambda_\rho
=-2\left(\beta-\frac12\right)\gamma.
\]

Since nontrivial zeros have \(\gamma\neq0\),

\[
\beta=\frac12.
\]

Thus the cone implies RH once the analytic pole comparison is source-complete.

## Source-obligation status

The nine source obligations now have the following dispositions:

1. the definitions of \(H\), \(H_R\), and the endpoint coefficient are fixed;
2. all endpoint--gamma--prime signs and normalizations passed an independent audit and source-owner confirmation;
3. the general-complex-zero expansion uses one \(a\sim-a\) orbit with the original multiplicity;
4. local uniform convergence follows from the dyadic \(O(k/2^k)\) majorant;
5. unconditional decay \(H(t)\to0\) follows from the Gaussian majorant and dominated convergence;
6. the endpoint moment asymptotic is established in the endpoint-extraction packet;
7. both transforms agree initially on \(\operatorname{Re}x>1/4\), which fixes meromorphic continuation;
8. generic small meshes give nonzero grouped residues;
9. equality with the single completed Xi logarithmic derivative excludes additional completed-term pole cancellation.

The source owner inspected Titchmarsh, *The Theory of the Riemann Zeta-function*, introduction equations (10)--(11), for the Hadamard input. The source bridge is closed. This supplies no proof of the all-rank cone inequality.

## What remains after completion

If these obligations are discharged, the theorem becomes

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
A_N(t,h)\geq0
\text{ for all }N,t,h.
\]

At that point only the cone remains unproved. Constructing its positive source factor would prove RH; finding a certified negative minor would disprove RH.

## Disposition

Freeze further unnamed-factor conjectures. The next valid increment is source completion of this equivalence or a genuinely new explicit endpoint--gamma--prime identity. The current abstract equivalence skeleton is not yet a theorem about zeta because its source obligations remain open.

## Verification

- `research/voevodsky/rh-remainder-cone-equivalence-skeleton-v1.json`
- `research/voevodsky/checkers/check_rh_remainder_cone_equivalence_skeleton.py`
- `research/voevodsky/results/rh_remainder_cone_equivalence_skeleton.json`
