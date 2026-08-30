# WP969 — Preparation-context covariance transport gate

Owner: `marici.Figueiredo`.

## Question

Can a two-feature covariance certificate established at one preparation context
authorize the same instrument over a larger admitted context domain?

## Claim boundary

A preparation context is a label (c) in a declared non-temporal context space
(mathcal C). It has no physical-time interpretation without an independent
map to a physical-time object. For each context, let

[
K_N(c)=rac1{N^2}sum_{i,j=1}^N
operatorname{Cov}_c(phi(X_i),phi(X_j)),
qquad phi(X)=(X,X^2)^T.
]

A certificate at (c_0),

[
K_N(c_0)preceqrac{kappa_0}{N}I_2,
]

does not transport by coordinate compatibility alone. A sufficient transport
constructor consists of a source-derived context distance (d) and a
calibrated operator-norm modulus

[
|K_N(c)-K_N(c_0)|_{m op}leq L,d(c,c_0).
]

Then

[
K_N(c)preceq
left(rac{kappa_0}{N}+L,d(c,c_0)ight)I_2
=rac{kappa(c)}{N}I_2,
qquad
kappa(c)=kappa_0+NL,d(c,c_0).
]

Combined with WP968, this yields

[
Pr_c(|widehat p-p|_1geqeta)
leqrac{6kappa(c)}{Neta^2}.
]

This is a stability theorem for an already typed readout. It does not define a
selector, a rigidifier, a context metric, or a physical reset operation.

## Exact hostile transport

Use two slots and the uniform one-slot route law on
({-1,0,1}). Let (sin[0,1]) label the joint preparation

[
P_s=(1-s)P_{m product}+sP_{m shared},
]

where the product component draws both routes independently and the shared
component draws one uniform latent route and copies it into both slots. Every
(P_s) has exactly the same calibrated one-slot marginals.

The single-slot feature covariance is

[
G=operatorname{diag}(2/3,2/9).
]

The cross-slot covariance is (sG), hence

[
K_2(s)=rac{1+s}{2}G.
]

At the calibration context (s=0),

[
K_2(0)preceqrac{2/3}{2}I_2.
]

At (s=1), the same nominal certificate fails because the largest eigenvalue
is (2/3), twice its certified value (1/3). All one-slot calibration records
remain unchanged.

The exact transport modulus is

[
|K_2(s)-K_2(s_0)|_{m op}=rac{|s-s_0|}{3}.
]

Thus a source authorization over this family requires the context constructor,
the meaning and calibration of (s), and a supported bound on its admitted
distance from the calibration context. Merely reusing the nominal covariance
number is invalid.

## Domain, quotient, instrument, and falsifiers

- State domain: two-slot joint route preparations (P_s), or a declared
  extension equipped with a source-derived context metric.
- Faithful quotient coordinate: the two route moments and their exact
  three-weight inversion, conditional on the established `physical16` route
  typing.
- Probe family: the pair ((X,X^2)) at each labelled slot.
- Contextual partition: contexts are equivalent when they induce the same
  joint feature-mean law, not merely equal slot marginals.
- Operation class: neither selector nor rigidifier; conditional stability of a
  readout certificate.
- Instrument gate: a physical constructor for context preparation/reset plus a
  calibrated, domain-supported modulus for (K_N).
- Smallest exact falsifier: (P_0) and (P_1), which share every slot marginal
  but differ by a factor two in the largest feature-mean covariance.
- Additional falsifiers: no source-derived context metric; violation of the
  operator-norm modulus; or uncertainty that exhausts the transported margin.

## Disposition

WP968 cannot be extended from a calibration point to an admitted context domain
without a named stability arrow. The exact mixture family proves that fixed
marginals and a nominal covariance bound do not supply that arrow. If a
source-derived modulus is later provided, the certificate transports with the
explicit inflation (kappa(c)=kappa_0+NLd(c,c_0)).
