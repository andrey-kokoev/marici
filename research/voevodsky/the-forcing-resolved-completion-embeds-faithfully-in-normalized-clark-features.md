# The forcing-resolved completion embeds faithfully in normalized Clark features

## Result

The actual normalized Clark feature map is injective on the whole weighted forcing Hilbert space H_beta, not just compact shell combinations. Its finite projective tensor powers map injectively into the Hilbert tensor feature carrier. Retaining degree and typed record labels therefore gives faithful realization of the corresponding summable forcing-resolved normal-form records.

This closes noncollapse for the richer domain used to prove separate bulk/forcing convergence. It supplies no bounded inverse; the one-letter map is in fact Hilbert--Schmidt.

Inputs:
- `clark-source-interface-domain-and-positivity-audit.md`
- `bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`
- `holomorphic-feature-closure-retains-completed-cross-spectral-packets.md`
- `endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`

## 1. Normalization preserves a separating cosine trace

In canonical raw port order the fixed normalized sewing matrix is

    A_Cl = (1/2) [[1,1,-1,1], [1,1,1,-1]].

The sum of its rows is (1,1,0,0). Thus vanishing of both normalized amplitudes implies

    h_(+,0)(f;z)+h_(-,0)(f;z)=0.

For f in H_beta, the raw traces are holomorphic on the connected strip |Im z|<beta. This follows from exponential weighted integrability, with polynomial factors controlled on every smaller strip. The fixed spectral disk lies inside that strip.

If the function-valued feature Lhat(f) vanishes in its Hilbert norm, its amplitudes vanish almost everywhere on the disk, hence everywhere there by holomorphicity. The displayed trace sum then vanishes on the entire strip by analytic continuation.

Define the even extension F(t)=f(|t|) on the real line. It is in L1, and its Fourier transform is exactly h_(+,0)+h_(-,0) on the real axis. Fourier uniqueness gives F=0 and therefore f=0. Compact support and entire continuation are unnecessary; the strip and exponential weight suffice.

This uses the normalized two-sheet map itself, not an inverse of the rank-two raw four-port coefficient.

## 2. Projective tensor completion does not create a kernel

Let H=H_beta, E be the normalized feature Hilbert carrier, and L:H->E the bounded injective map just proved. Its adjoint L^* has dense range because the orthogonal complement of its range is ker L.

For finite d consider

    L_d: H tensor_projective ... tensor_projective H
         -> E tensor_Hilbert ... tensor_Hilbert E.

This is bounded with norm at most ||L||^d. Suppose L_d(u)=0. Pairing against every elementary target tensor shows that u evaluates to zero on all products of vectors from range(L^*). Density and continuity imply the same for every product of Hilbert vectors in H.

To conclude u=0 in the PROJECTIVE completion, choose finite-rank orthogonal projections P_n converging strongly to identity on H. The operators P_n^(tensor d) are contractions for the projective norm and converge strongly there: prove it first on elementary finite sums and then use their density. Each P_n^(tensor d)u is finite dimensional, and all its product-coordinate evaluations vanish. It is therefore zero. Taking the projective-norm limit proves u=0.

This final approximation step is essential. One cannot assert injectivity of completed tensor products merely from injectivity on algebraic tensors for arbitrary Banach spaces.

## 3. Records, labels, and normal forms

A forcing-resolved normal-form record retains its typed seam edges, coefficient-buffer endpoints, retained degrees, and ordered feature slots. On a fixed shape the forcing tensor maps by the injection above. Vacua and actual edge sectors retain their distinct labels.

In a weighted l1 sum over these shapes and degrees, coordinate projections are continuous. A zero feature record therefore has zero forcing tensor in every shape. The summed map is injective wherever the source degree weight controls ||L||^d; equivalently choose the forcing radius at least ||L|| times the desired feature radius. The all-radius scale intersections accommodate every such fixed finite scale loss.

This is a statement about NORMAL-FORM records, not about an unbalanced presentation before its genuine balancing kernel is removed. For the arithmetic associated layers, the earlier endpointwise source-quotient argument and finite balanced injections still identify that kernel. No new quotient is inferred from a vanishing self-pairing.

Signature-transformed observer channels remain labelled operations on the existing envelope. The argument does not declare an arbitrary pair of forcing copies mapping by L(f)+J L(g) to be a new injective primal source. Such a sum would require its own kernel analysis.

## 4. Why inverse stability is still unavailable

After identifying H_beta with unweighted L2 via f(x)=exp(-beta x)u(x)/(1+x), a raw feature port has integral kernel

    K_(sigma,j)(z,t;x)
       = [x^j/(1+x)] exp(-beta x) exp(sigma i z x) exp(i z t).

With a=beta-Y and Im z>=eta, its squared modulus is bounded by exp(-2a x)exp(-2eta t). Summing four ports and integrating over x,t,z gives

    ||L_raw||_HS^2 <= mu(Omega)/(a eta),
    ||Lhat||_HS <= ||A_Cl|| sqrt(mu(Omega)/(a eta)).

Hence Lhat is compact. Since H_beta is infinite dimensional and Lhat is injective, it cannot be bounded below or have closed infinite-dimensional image. This is consistent with, and independent of, the forgotten-suffix closed-range obstruction for the path-weighted receiver.

The stronger source topology therefore remains substantive. Separate current continuity in that topology cannot be promoted to continuity in the feature-image norm by invoking injectivity.

## 5. Combined conclusion

On the specified forcing-resolved summable domain, the separately labelled bulk, forcing, and vacuum-incidence currents converge, and the underlying normal-form feature realization is faithful. Relative sewing and pentagon identities survive with every spectral pair retained on compact spectral interiors.

This provides convergence AND noncollapse for that declared domain. It does not prove positivity, a stable inverse, arbitrary inverse-limit completeness, or an independent identification of the bulk/forcing split with arithmetic gamma/prime channels.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_forcing_resolved_feature_noncollapse.py`

Exact tests check the normalized row sum, distinguish the singular raw coefficient from J, and exercise tensor separation without a lower bound. The infinite-dimensional argument is the strip-Fourier/dense-adjoint/finite-projection proof above, not a finite spectral-rank calculation.
