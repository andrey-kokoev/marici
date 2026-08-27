# F-Theory Vertical-Flux Mirror and Moduli No-Go

## Question

Does global \(G_4\)-flux quantization provide the missing single source
principle by forcing odd index three together with its orientation, magnitude,
stable basin, thresholds, and physical readout?

## Claim boundary

The admitted domain is the finite collection of globally resolved elliptic
Calabi--Yau fourfolds over \(\mathbb P^3\) studied in
arXiv:1503.02068, restricted to vertical \(G_4\)-flux. Fluxes must satisfy
shifted quantization,

\[
G_4+\frac{c_2(X)}2\in H^4(X,\mathbb Z),
\]

the homogeneous M/F-theory matching and transversality constraints, D-term
primitivity, and the D3 tadpole relation

\[
\frac{\chi(X)}{24}
=n_{\mathrm{D3}}+\frac12\int_XG_4\wedge G_4.
\]

Within the concrete finite model list, these gates make three the minimum
permitted family number. This is stronger than choosing a charge-three field
after the fact: geometry, quantization, and tadpole capacity jointly exclude
smaller chiral multiplicities in the admitted scan.

It is not a singleton theorem. A lower bound does not select a unique flux
class, and the paper explicitly restricts the result to vertical flux in a
discrete collection of fourfolds. Horizontal flux is expected to enlarge the
allowed set. Vector-like matter required for some Higgs transitions is also
assumed rather than controlled.

## Exact mirror theorem

Let \(G_4\) be any admitted flux and define its mirror by
\(G_4^\vee=-G_4\). Shifted quantization is preserved: if

\[
k=G_4+\frac{c_2(X)}2
\]

is integral, then

\[
G_4^\vee+\frac{c_2(X)}2=-k+c_2(X)
\]

is integral. All transversality and primitivity equations are homogeneous, so
their zero loci are preserved. The flux contribution to the tadpole is
quadratic:

\[
\int_XG_4^\vee\wedge G_4^\vee
=\int_XG_4\wedge G_4.
\]

For every matter surface \(\mathcal C_{\mathbf R}\), however, chirality is
linear:

\[
\chi_{\mathbf R}(G_4^\vee)
=\int_{\mathcal C_{\mathbf R}}G_4^\vee
=-\chi_{\mathbf R}(G_4).
\]

Thus the admitted source gates pair every three-family flux with an
anti-three-family flux of identical tadpole cost. The construction selects a
minimum absolute multiplicity in its scan, not an orientation.

## Remaining fibers

The admitted scan does not compute a complete moduli-stabilization Hessian.
Vertical flux can constrain complex structure through its Hodge-type condition,
so no zero-potential claim is made here. D-term primitivity constrains Kähler
moduli but is not a proof that all volume and normalization directions are
fixed. Consequently the packet does not determine a portal magnitude or a
universal threshold clock.

The chiral index and three-dimensional Chern--Simons coefficients are exact
topological readouts, but they are not detector instruments. No calibrated
map from the compactification's source perturbations to the faithful
physical16 flavor coordinate is present, and neither finite widths nor
threshold-sensitive observables are derived.

## Classification

- Global geometry, quantization, and tadpole cancellation jointly rigidify a
  lower bound of three in the admitted finite vertical-flux scan.
- The construction does not select the sign because \(G_4\) and \(-G_4\) are
  source-equivalent under every admitted gate except the chiral readout.
- It does not select a unique flux, portal magnitude, stabilized RG basin, or
  threshold response.
- It has a formal topological readout but no calibrated physical instrument.

This is a partial Deutschian explanation of a minimum magnitude. It is not a
Deutschian explanation of the asymmetric flavor portal.

## Smallest exact falsifier

The pair \(G_4,-G_4\) is the smallest falsifier. It has equal quantization
status, equal tadpole charge, and the same homogeneous consistency conditions,
but opposite chiral indices. No fitted scalar or low-energy convention can
remove this source-level doublet.

## Disposition

Retain globally quantized flux as evidence that topology can derive odd family
magnitude without inserting charge three by hand. Reject the vertical-flux
packet as the complete portal selector. A positive successor must derive an
orientation-odd source operation from the same global compactification, show
that it removes the mirror without an external reference choice, and stabilize
the normalization and moduli before any RG, threshold, or physical16 claim.

Verification:

- checker:
  research/flavor/checkers/wp793_f_theory_vertical_flux_mirror_moduli_no_go.py
- generated result:
  research/flavor/results/wp793_f_theory_vertical_flux_mirror_moduli_no_go.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp793_f_theory_vertical_flux_mirror_moduli_no_go.py
- global three-family source:
  [Cvetič et al.](https://arxiv.org/abs/1503.02068)
- flux and global-consistency source:
  [Krause, Mayrhofer, and Weigand](https://arxiv.org/abs/1109.3454)
