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

Status: owner input reduced to one functional and two generator values; repository search does not expose that independent functional, so further equality proof is authority-blocked.
