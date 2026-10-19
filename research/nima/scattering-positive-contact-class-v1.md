# Positive scalar-port contact class against the retained source

## Scope

Keep the actual finite core K, metric M and two normalized rim port columns W/sqrt(3), and the equal known channel threshold. The reciprocal real scalar-port contact block is

    C = [[a I, -g W^dagger], [-g W, b WW^dagger]],
    a,b >= 0, g real, a b >= g^2, beta > 0.

Here W denotes **normalized** ports in formulas; the checker uses the raw bright ports with metric Gram and an explicit division by 3. On the two-dimensional port image, completing the square proves positivity for b>0. If b=0, positivity forces g=0; zero a also forces g=0. The orthogonal core directions carry no contact penalty. This classification is for the declared scalar identity contact, not all matrix-valued reciprocal boundaries, unequal thresholds, or a native operation principle.

## Elimination and real poles

Away from bare/dressed resolvent poles, put r_s(E) for the exact bare parity response in the preceding source audit. Eliminating the core yields

    v_s(E) = a + g^2 r_s(E)/(1-b r_s(E)).

For the actual metric core D_b=K+b WW^dagger, the rank-two resolvent identity gives R_b=R_0(I-b R_0)^-1. The direct term a does not disappear. The checker recomputes D_b resolvents at two rational b values from actual five-state matrices and compares exact parity functions; it does not infer the identity from a toy core. At E=5391/3292 the two bare parity responses coincide, and choosing b=2442123/5418632 produces an exact double dressed eigenvalue there; the port Krylov rank remains five. A coincident pole does not remove the required memory states. A contact pole has a perfectly reflecting parity limit if the other variables stay regular; elimination exactly at a pole is not a valid evaluation of a matrix inverse.

For a,b,g positive, rho=g^2/(ab) belongs to (0,1]. Then v_s=a[1-b(1-rho)r_s]/(1-b r_s). rho=1 is rank-one completion; rho<1 is a strictly positive two-by-two contact block. The balanced rule a=b=g is only a special representative of rho=1, not forced by positivity. With g=0, v_s=a is constant and b and the bare source are invisible to continuum scattering; if a=g=0 it is free transmission. These decoupled sectors must not be inverted using divisions by g or a.

## Coordinate quotient and observables

Under the transported lead-coordinate dilation psi_new(x)=s^-1/2 psi_old(x/s), holding native K, W and energy labels fixed,

    a -> s a,  g -> sqrt(s) g,  b -> b,  beta -> s^2 beta.

The contact form and kinetic integral transform together. The impedance z=2 sqrt(beta(E-theta)) scales by s, so on-shell t_s=iz/(iz-v_s) and its channel fluxes are unchanged when the coordinate reader is transported. An independently fixed position reader is NOT quotiented. Signed g is invisible in the continuum S when the core has no incoming prepared excitation; a core-port phase change can reverse its sign. This is not a claim about core-local probes.

For coupled g!=0, the dimensionless response y_s=v_s/sqrt(beta) has three invariants

    A=a/sqrt(beta), C=g^2/sqrt(beta), b,
    y_s=A+C r_s/(1-b r_s), rho=C/(A b).

Each invariant is fixed by the dilation. Conversely equal A,C,b for two positive coupled representatives imply a common positive dilation; modulo sign of g, they lie in one coordinate orbit. Taking s=b/a gives a=b and |g|=b sqrt(rho); only rho=1 admits a balanced a=b=|g| representative. The principal (a,b,g,beta)=(2,2,2,1) and (8,2,4,16) are gauge-related, whereas (2,2,1,1) has rho=1/4 and is not. The actual source responses and exact E=4 fluxes distinguish the latter, without physical data. At E=4, balanced total transmission is approximately 0.3112449312 and cross-rim flux 3.5695223e-5; strict-positive total transmission is approximately 0.6260811423 and cross-rim flux 9.0283985e-6. The exact rational numbers are in the receipt.

For an **ideal exact energy function** and known threshold, r_s(E)=1/E+mu1/E^2+O(E^-3) with the source's common even/odd moment mu1=1193/1646. Then

    A=lim y_s, C=lim E(y_s-A),
    b=lim E^2(y_s-A-C/E)/C - mu1.

This is a formal broadband function identity and only applies for C>0, not an available finite-energy observation procedure. Exact phase and the fixed threshold are needed to reconstruct y; intensity-only data can retain phase aliases. Scattering cannot distinguish b when g=0. At finite energies, rational interpolation and alias analysis remain to be done.

## Boundary and verification

Checker: `research/nima/checkers/check_scattering_positive_contact_class.py`. Receipt: `research/nima/results/scattering-positive-contact-class-v1.json`. Work net: `research/nima/contracts/scattering-core-bridge-work-net.v6.json`.

No selection of a native contact extension, physical species, measured noise model, or root proof is inferred. The next executable scoped task is the finite-energy contact-class inverse. Exact source rational identities, positivity and gauge tests are code-controlled; the classification/completeness and ideal-function implications are written arguments, not a kernel proof. No stationary field solver or acquisition is run.
