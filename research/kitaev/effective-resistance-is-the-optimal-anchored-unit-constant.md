# Effective Resistance Is the Optimal Anchored Unit Constant

Let \(G=(V,E,c)\) be a finite source-authorized weighted graph with positive
conductances \(c_e\), vacuum anchor \(a\), and scalar normalization values
\(u:V\to\mathbb C\) satisfying \(u(a)=1\). Define the Dirichlet energy

\[
\mathcal E_G(u)=\sum_{\{x,y\}\in E}c_{xy}|u(x)-u(y)|^2.
\]

For every vertex \(v\) in the anchored component,

\[
|u(v)-1|^2
\le
R_{\mathrm{eff}}(a,v)\,\mathcal E_G(u).
\]

Effective resistance is the optimal constant:

\[
R_{\mathrm{eff}}(a,v)
=
\sup_{u\not\equiv\mathrm{const}}
\frac{|u(v)-u(a)|^2}{\mathcal E_G(u)}.
\]

Therefore, with

\[
R_* = \max_{v\in V}R_{\mathrm{eff}}(a,v),
\]

the strict energy threshold

\[
R_*\mathcal E_G(u)<1
\]

implies \(\|u-1\|_\infty<1\), hence a uniform inverse, canonical logarithm,
zero winding on the graph cycles, and all finite root frames.

## Seam augmentation

On the chain \(0-1-2\) with unit conductances and anchor \(0\),

\[
R_{\mathrm{eff}}(0,2)=2.
\]

Adding the authorized seam edge \(0-2\) places resistance one in parallel
with resistance two, giving

\[
R_{\mathrm{eff}}^{\mathrm{seam}}(0,2)=\frac23.
\]

This is the exact geometric benefit of the seam: it lowers the optimal
energy-to-pointwise constant. Rayleigh monotonicity guarantees that adding
authorized positive-conductance edges cannot increase effective resistance.

If a component is disconnected from the anchor, its effective resistance is
infinite and no anchored unit theorem is available there. This recovers the
path-coverage hostile without choosing arbitrary paths.

## Sharp fixture

For \(u=(1,3/4,1/2)\) on the chain,

\[
\mathcal E_{mathrm{chain}}(u)=1/8,
\qquad
R_{\mathrm{eff}}(0,2)\mathcal E(u)=1/4
=|u(2)-1|^2.
\]

After adding the seam, the same voltage has energy \(3/8\) and resistance
\(2/3\), again giving equality. It is the harmonic voltage for the prescribed
boundary values in both networks.

## Shared Carrier geometry versus coefficient lens

Shared Carrier geometry supplies:

- vertices, authorized edges, incidence, conductances, anchor components;
- graph Laplacian, effective resistance, and Rayleigh monotonicity;
- the optimal anchored Poincare constant.

The coefficient lens supplies:

- the scalar or Hilbert-valued norm in the edge energy;
- the interpretation of \(u\) as a normalization, amplitude, or operator
  coefficient;
- the quantum meaning of sheet/root frames and physical observability.

No quantum postulate is needed for the resistance inequality itself. Conversely,
Carrier geometry alone does not authorize which Clark, seam, or current rows
belong to the theta/Tate energy.

## Theta/Tate consequence

The bulk-to-path gate can be replaced by a finite graph compiler if the
doubled tail, seam, endpoints, and currents define an authorized weighted
incidence graph. Grothendieck then needs:

1. the exact source graph and conductances;
2. a uniform bound on its anchored resistance radius \(R_{*,X}\);
3. a uniform Green/Clark energy bound with
   \(R_{*,X}\mathcal E_X<1\).

This turns seam necessity into an exact resistance comparison rather than an
informal connectivity claim.

## Falsifiers

- A disconnected component is assigned finite resistance.
- An unauthorized seam edge is added to improve the bound.
- Conductances are tuned after inspecting the desired state.
- Graph energy is identified with the Green form without a source-derived
  equality.
- Finite resistance radii are bounded cutoffwise but diverge in completion.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to replace arbitrary path length by the optimal Carrier-
geometric constant and type the seam contribution.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Effective resistance is the exact compiler, seam augmentation is
Rayleigh monotonicity, and shared geometry is cleanly separated from the
quantum/source coefficient lens.
