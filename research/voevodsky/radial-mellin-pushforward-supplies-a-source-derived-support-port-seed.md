# Radial Mellin pushforward supplies a source-derived support-port seed

## Question

Is there a canonical source map sending the shifted-support Fourier port to a radial analytic object, rather than choosing a metaplectic seed by its desired Gram matrix?

## Claim boundary

Yes on the Mellin distribution rung. Radial pushforward of the shifted Dirac comb is the symmetric Hurwitz-zeta section, while radial pushforward of the character comb is a periodic Dirichlet section. Poisson summation gives their Fourier functional-equation relation. This constructs a source-derived seed, but not yet a Hilbert-unitary map into the retained G4 radial graph.

## Shifted support seed

Let

$$
a=\frac rq\in(0,1),
\qquad
P_a=\sum_{n\in\mathbb Z}\delta_{n+a}.
$$

On \(\operatorname{Re}s>1\), define radial Mellin pushforward by pairing the nonzero support with \(|x|^{-s}\). Then

$$
\mathcal M_{\rm rad}(P_a)(s)
=
\sum_{n\in\mathbb Z}|n+a|^{-s}
=
\zeta(s,a)+\zeta(s,1-a).
$$

Thus the canonical radial seed is

$$
v_a(s)=\zeta(s,a)+\zeta(s,1-a).
$$

It is derived directly from the support port and has its standard meromorphic continuation.

## Character-port image

For

$$
C_r=\sum_{n\in\mathbb Z}e^{2\pi irn/q}\delta_n,
$$

remove or separately retain the zero endpoint atom. The nonzero radial Mellin pushforward is

$$
\mathcal M_{\rm rad}^{\times}(C_r)(s)
=
2\sum_{n\ge1}
\cos\left(\frac{2\pi rn}{q}\right)n^{-s}.
$$

This is the even periodic Dirichlet section attached to the additive character. Hence support displacement and amplitude character remain distinct after radialization: they become a Hurwitz pair and a periodic Dirichlet series.

## Fourier compatibility

The distributional identity

$$
\mathcal FP_a=C_{-r}
$$

becomes, after Mellin completion, the classical Hurwitz/periodic-zeta functional equation. Applying Fourier twice sends \(a\mapsto1-a\), matching reflection of the symmetric Hurwitz pair. Therefore the four additive ports have canonical radial Mellin shadows without identifying the port index with a semilocal presentation index.

## Relation to the seed classifier

For the finite orbit intertwiner, the previously missing seed can now be taken distributionally as

$$
C(P_a)=v_a.
$$

The rest of the orbit is forced by Fourier transport and the functional equation. This is not fitted from target phases or zeros.

## Remaining analytic gate

The retained G4 radial carrier uses weighted history/Green graph norms, whereas \(v_a\) is presently a meromorphic Mellin distribution. To promote this seed to the finite unitary interface one must:

1. specify the completion and endpoint subtraction at \(s=1\);
2. show the completed Hurwitz and periodic sections belong to the declared rigged radial target;
3. compare their four-character Gram matrix with the Fourier-orbit boundary Gramian.

No Hilbert norm equality is inferred from the functional equation alone.

## Correction: absolute radialization is not faithful

A subsequent orbit test shows that the symmetric seed identifies \(P_a\) with \(P_{1-a}\), and its cosine character image identifies \(C_r\) with \(C_{-r}\). It therefore realizes only the half-turn quotient and kills the odd Fourier character sectors. The faithful replacement is the oriented radial double with seed \((\zeta(s,a),\zeta(s,1-a))\).

## Disposition

A source-derived support-port-to-radial seed is constructed on the Mellin distribution rung, but the symmetric Hurwitz seed is only the half-turn shadow. Full order-four typing requires the separately retained positive and negative radial channels.