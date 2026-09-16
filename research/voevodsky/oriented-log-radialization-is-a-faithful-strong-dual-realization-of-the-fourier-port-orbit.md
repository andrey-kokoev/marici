# Oriented log-radialization is a faithful strong-dual realization of the Fourier-port orbit

## Question

Does retaining the two radial orientations merely avoid the visible collapse, or does it give an injective analytic realization of the complete generic Fourier orbit?

## Claim boundary

It gives an injective topological realization on distributional test/dual rungs away from the zero atom. Fourier transport conjugates to an exact order-four operator on the oriented radial image. This does not identify that transported operator with an independently declared external G4 sewing map.

## Oriented logarithmic chart

The map

$$
\rho:\mathbb R^\times
\longrightarrow
\{+,-\}\times\mathbb R,
\qquad
\rho(x)=(\operatorname{sgn}x,\log|x|)
$$

is a diffeomorphism, with inverse

$$
\rho^{-1}(+,u)=e^u,
\qquad
\rho^{-1}(-,u)=-e^u.
$$

Therefore pushforward by \(\rho\) is a topological isomorphism between the corresponding compactly supported test spaces, and its transpose is an injective topological map on distribution spaces. Half-density normalization changes only the nonzero smooth Jacobian weight and does not affect injectivity.

The zero atom is not in \(\mathbb R^\times\) and must be retained as its separate endpoint port.

## Faithfulness on the rational-coset orbit

For generic \(a=r/q\), the four distributions

$$
P_a,
\quad C_{-r},
\quad P_{1-a},
\quad C_r
$$

remain distinct after oriented log-radial pushforward because that pushforward is injective. Their Mellin transforms are respectively encoded by the ordered Hurwitz pair and the two ordered periodic-Dirichlet pairs.

Thus no odd Fourier character is lost. The kernel found for absolute radialization arises exactly from applying the subsequent channel-sum map

$$
(f_+,f_-)\longmapsto f_++f_-.
$$

It is not a kernel of oriented radialization.

## Transported Fourier action

On the oriented radial image define

$$
W_{\rm or}
=
\rho_*\mathcal F\rho_*^{-1}.
$$

Then

$$
W_{\rm or}^4
=
\rho_*\mathcal F^4\rho_*^{-1}
=I,
$$

and

$$
W_{\rm or}^2
=
\rho_*\mathcal R\rho_*^{-1},
$$

which is the oriented radial channel swap. On Mellin sections, the equation \(W_{\rm or}\rho_*P_a=\rho_*C_{-r}\) is the completed Hurwitz/periodic-zeta functional equation.

## Pairing preservation

Because the realization is a test-space isomorphism with transpose dual action, it preserves the canonical distribution/test pairing:

$$
\langle\rho_*T,\varphi\rangle
=
\langle T,\rho^*\varphi\rangle.
$$

This is the correct rigged analogue of unitarity for the unsmoothed comb orbit. No Hilbert norm of the delta-comb seed is invoked.

## External comparison boundary

The operator \(W_{\rm or}\) is source-derived by conjugating additive Fourier transport. To identify it with the separately proposed metaplectic radial lift or an external G4 operator, one must compare their action on one cyclic support seed and the endpoint orientation. Matching order and spectrum alone remains insufficient.

## Disposition

The generic four Fourier ports now have a faithful analytic realization on the oriented log-radial strong-dual carrier, with exact order-four transport and preserved rigged pairing. The remaining G4 gate is equality of this explicit transported action with the externally declared sewing action.