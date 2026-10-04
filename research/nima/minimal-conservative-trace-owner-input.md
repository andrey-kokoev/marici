# Minimal conservative trace owner input

The cyclic trace side is fixed. For each prime shell `p`, the source generator is

$$
P_p\otimes\beta_g,
\qquad
\beta_g=(\rho_g(0),E_g,W_g,R_g),
$$

and Adams-two evaluation is

$$
\Lambda_{\rm cyc,s}(P_p\otimes\beta_g)
=p^{-2s}\beta_g.
$$

To decide conservative/cyclic naturality, the conservative owner need expose only:

1. a continuous functional
   $$
   \Lambda_{\rm cons,s}:\mathcal I_1(E)\widehat\otimes B_{\rm border}\to B_{\rm border};
   $$
2. its values on the independently normalized even and odd shell generators
   $$
   P_p\otimes w_\theta,
   \qquad
   P_p\otimes j_\theta;
   $$
3. confirmation that it respects the Stokes relation and analytic-transpose jets;
4. cutoff and reciprocal naturality.

The acceptance equations are

$$
\Lambda_{\rm cons,s}(P_p\otimes w_\theta)
=p^{-2s}w_\theta,
$$

$$
\Lambda_{\rm cons,s}(P_p\otimes j_\theta)
=p^{-2s}j_\theta,
$$

with the odd equation interpreted in the oriented Wronskian metric carrying `K_link=-J_link/2`.

The ordinary coordinate is already source-explicit, and the Stokes relation determines `R`. Thus these two equations are sufficient and minimal. Defining `Lambda_cons` by these equations is forbidden; it must come from the independent conservative Green constructor.

## Frozen local acceptance contract

The independently normalized columns are

$$
w_\theta=\binom{1/2}{1/2},
\qquad j_\theta=\binom{1/4}{-1/4}.
$$

For each declared shell and parameter domain, retain the full vector residuals

$$
\varepsilon_p^+(s)
=\Lambda_{\rm cons,s}(P_p\otimes w_\theta)-p^{-2s}w_\theta,
$$

$$
\varepsilon_p^-(s)
=\Lambda_{\rm cons,s}(P_p\otimes j_\theta)-p^{-2s}j_\theta,
\qquad
\mathcal E_p(s)=[\varepsilon_p^+(s)\mid\varepsilon_p^-(s)].
$$

Local acceptance is exactly `E_p(s)=0` as a two-column vector equality. Matching determinants, the scalar combination `R+2E`, norms, or only the two diagonal pairings is insufficient. For example, errors `epsilon_plus=j_theta` and `epsilon_minus=w_theta` have zero Euclidean diagonal pairings while both vector errors are nonzero. The odd column must retain the source-fixed oriented linking convention `K_link=-J_link/2`.

The constructor must supply its independent Green-system definition, the boundary readout, parameter domain, normalization, and variance conventions. The block operator `C(s)` without that readout is not a definition of `Lambda_cons`. A full classification of conservative functionals is unnecessary: the first test needs only this independently derived restriction to the one-shell even/odd plane.

## Dependency of the reciprocal row

Assume the independently constructed functional preserves

$$
zR-\rho(0)=E-\frac12W.
$$

Then the two vector equalities, together with the already identified ordinary coordinate, imply

$$
z(R_{\rm cons}-R_{\rm cyc})
=(\rho_{\rm cons}(0)-\rho_{\rm cyc}(0))
+(E_{\rm cons}-E_{\rm cyc})
-\frac12(W_{\rm cons}-W_{\rm cyc})=0.
$$

Thus `R_cons=R_cyc` for `z!=0`, and at zero by the declared analytic removable extension. The Stokes equation at zero alone does not determine `R`. No third independent reciprocal-row comparison is required once these hypotheses hold.

## Successor and completion layer

After local equality is established, prove that the **same** independently defined functional respects prime/shell cutoffs, reciprocal transport, parameter jets, and the stated completion topology. Selecting new readouts at successive cutoffs does not establish naturality of the original constructor. Local equality alone supplies neither continuity bounds nor passage to the completion.

For fixed endpoint columns, the cyclic jet targets are explicit:

$$
\partial_s^k(p^{-2s}w_\theta)
=(-2\log p)^k p^{-2s}w_\theta,
\qquad
\partial_s^k(p^{-2s}j_\theta)
=(-2\log p)^k p^{-2s}j_\theta.
$$

These are comparison targets, not definitions of conservative jets.

## Status and next deliverable

- **Missing constructor:** independent `Lambda_cons,s` from the conservative Green system.
- **First falsifier:** one nonzero full vector residual on an admissible shell and parameter.
- **First theorem:** both residual columns vanish on the declared local domain.
- **Next theorem:** the same equality is compatible with successors, jets, reciprocal transport, and completion.

Current status: **constructor missing; comparison untested**. The cited repository search does not expose that independent readout. This is not a computed failure and not a passing equality theorem. No new analytic verification is claimed by this contract update. Further manipulation of the cyclic side alone cannot determine the absent conservative values.
