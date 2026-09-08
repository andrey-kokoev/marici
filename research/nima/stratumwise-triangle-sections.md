# Regular sections on fixed-support tori

## Question

Can regular triangle factors be chosen on a fixed-support stratum despite the obstruction near the coefficient vertex?

## Claim boundary

For every toric support face F, let U be its used triangle coordinates and L_F its saturated exponent lattice. The inclusion L_F into Z^U splits. Contravariantly this supplies a group-homomorphic section of the split-torus map T_U -> T_F. Its coordinates are Laurent monomials, hence regular on T_F over any field. Set triangle coordinates outside U to zero. The support-closure theorem makes this a section into the original affine triangle space.

This construction fixes the minimal triangle support U. Other lifts may have extra nonzero triangle coordinates; they are not classified here. For two regular sections with this same parameter support, their pointwise quotient is a regular map T_F -> K_F, where K_F is the kernel torus of dimension |U|-rank(L_F). Conversely multiplying a section by such a map gives another section. For group-homomorphic sections the quotient is itself a torus homomorphism. Splittings give choices, not canonical factors.

### Exact four-coefficient boundary certificate

In the recorded seven-point ordering, use support {35,36,40,41}. Its nine triangle coordinates are listed in results/stratum_section.json. Put a=w_35, b=w_36, c=w_40; these are arbitrary nonzero field elements, while w_41=bc/a. The nontrivial chosen factors are

\[
z_{012}=b,\qquad z_{013}=a,\qquad z_{034}=c/a.
\]

Set the other six used triangle coordinates to one and all unused coordinates to zero. The checker verifies exact integer exponent identities AD=I and (MD)A=M, so reconstruction holds symbolically, not only at sampled values. It also checks support closure and rejects a corrupted section exponent. The kernel torus on this minimal parameter support has dimension six.

## Disposition

Regular sections exist on every fixed-support torus, with an explicit nontrivial boundary example. These strata are locally closed, not an open cover of the coefficient variety. The factor c/a is regular only where a is nonzero, and stratumwise existence does not contradict the previously proved absence of any section on a neighborhood of the vertex. Extension across other boundary degenerations requires separate tests; no gluing or canonical choice follows from the lattice splitting.
