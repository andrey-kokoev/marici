# Smooth hard flux constructs the low kernel, with parity-specific source channels

## 1. Electric displacement channel

The scalar displacement-memory constraint has the angular operator

\[
 \mathcal K=D^2(D^2+2),
\]

whose scalar-harmonic multiplier, up to sign conventions, is

\[
 \kappa_l=(l-1)l(l+1)(l+2).
\]

It vanishes only at `l=0,1` and is invertible for every `l>=2`. Therefore a
smooth hard energy-flux component in any `l=2,3,4` harmonic constructs the
corresponding electric shear low mode.

Positivity of energy flux does not forbid these components. For a real
normalized harmonic profile `Y` with bounded supremum, choose

\[
 T_{uu}(u,\Omega)=F(u)(\rho_0+\epsilon Y(\Omega)),
 \qquad \rho_0>|\epsilon|\|Y\|_\infty,
\]

with `F>=0` integrable. The isotropic term supplies positivity and changes
only the conserved/background channel; the `l>=2` component survives the
memory projection. Four-momentum conservation constrains `l=0,1`, not
`l=2,3,4`.

Thus all 21 real electric low modes are source-constructible within the smooth
positive-flux completion. Whether they are observables or large-supertranslation
vacuum data is a later quotient choice.

## 2. Magnetic angular-momentum channel

Decompose a smooth angular flux one-form by Hodge theory:

\[
 T_{uA}=D_A\alpha+\epsilon_A{}^BD_B\beta.
\]

Its curl reads only the coexact potential,

\[
 \epsilon^{AB}D_AT_{uB}=D^2\beta.
\]

Since the Laplacian multiplier `-l(l+1)` is nonzero for every `l>=1`, the
linear PSZ angular-momentum source map is onto every magnetic scalar harmonic
with zero mean. In particular it can construct all magnetic `l=2,3,4` source
profiles and hence all 21 magnetic shear kernel modes after the appropriate
Green/spin reconstruction.

This is source authority at the level of the declared smooth hard
angular-momentum flux. A stronger demand that every such one-form arise from a
specific nonlinear matter model with pointwise dominant-energy inequalities
would be an additional constructor problem and is not inferred here.

## 3. Finite particles versus functional completion

A finite atomic angular packet has point singular support and cannot equal a
nonzero finite smooth harmonic sum. This is why the earlier finite-puncture
kernel was zero on the magnetic sector.

Finite atomic measures are nevertheless weak-* dense in finite Radon
measures. Sequences of increasingly many hard directions can converge to the
smooth flux densities above. The low kernel is therefore born at the
functional closure, not at any finite labelled stage:

\[
 \mathcal A_{\rm fin}\cap\mathcal H_{2:4}=\{0\},
 \qquad
 \overline{\mathcal A_{\rm fin}}^{\,w^*}
 \cap\mathcal H_{2:4}=\mathcal H_{2:4}.
\]

Total-variation convergence requires approximating densities by genuinely
absolutely continuous or finely partitioned measures; bare empirical delta
measures generally converge weak-* but not in total variation to a smooth
density. The topology therefore records which closure was taken.

## 4. Conservation and antipodal matching

The low `l=2,3,4` channels are orthogonal to global translation charges.
Likewise the coexact magnetic modes with `l>=2` do not alter the global `l=1`
angular-momentum constraint. Conservation restriction does not remove them.

Antipodal matching multiplies each harmonic by its fixed parity sign and
transports the source history to the opposite null boundary. Because that map
is invertible, constructibility is preserved.

## 5. Constructor verdict

| low kernel sector | finite point packet | smooth hard-flux completion |
|---|---:|---:|
| electric `l=2,3,4` | no exact pure mode | yes, positive `T_uu` |
| magnetic `l=2,3,4` | no exact pure mode | yes, coexact `T_uA` at linear source level |
| characteristic high-frequency ridge | no | no global paired source state |

The finite-energy physical kernel is therefore nonempty in the smooth source
completion. What fails is not constructibility of the low modes, but the
grade-three readout's ability to observe them.

## Evidence

`checkers/hard_flux_low_kernel_constructibility_checks.py` verifies the
electric and magnetic source multipliers, positivity constructions through
`l=4`, conservation orthogonality, finite-atomic singular-support exclusion,
and weak-* recovery by exact quadrature moments.
