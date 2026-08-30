# Typed UV-to-physical16 contract (WP117)

## Pipeline

\[
(\mathcal U,\mu_{\rm UV})/G_{\rm UV}
\xrightarrow{\;V\;}
\operatorname{Vac}(\Phi)/G_{\rm UV}
\xrightarrow{\;Y\;}
[(Y_u,Y_d)]_{\rm WB}
\xrightarrow{\;c_{16}\;}
X_{16}
\xrightarrow{\;\pi_{10}\;}
X_{10}.
\]

`V` is vacuum selection derived from the UV action, `Y` is the covariant
vacuum-to-Yukawa/matching map, `c16` is the faithful quotient coordinate, and
`pi10` is the nonfaithful measured projection. A physical ensemble is

\[
 \nu_{16}=(c_{16}\circ Y\circ V)_*\mu_{\rm UV}.
\]

It exists only after all arrows and `mu_UV` are source-defined. The output
classification is unique for one fixed normalized source state; finitely or
continuously ambiguous when the source itself supplies such a mixture; and
undefined when the action, coefficient law, or normalization is absent.

## Current classification

The present source class supplies no independently derived coefficient measure
or normalized UV state. Consequently `nu16` is **undefined without additional
source data**. The minimal missing datum is one jointly authorized package:

1. a concrete UV action and coefficient domain;
2. an independently normalized positive measure/state on its quotient;
3. a covariant vacuum/matching map to Yukawa orbits.

Naming a potential after locating a fitted point does not supply this package.

## RG and downstream contract

For frozen `(Lambda_UV, Lambda_IR, scheme, matching)`, RG acts by pushforward
`nu_IR=(R_IR<-UV)_* nu16`. An invertible RG flow transports a partition and
does not select it. Scheme comparison must commute on the quotient or carry an
explicit matching uncertainty.

Phenomenology is evaluated only after `nu16` and RG data are immutable. The
existing canonicalization, thermal branch record, detector inverse,
repeatability, and route-weight pipeline is a conditional readout. Its
reliability remains bounded by

\[
\epsilon_{\rm route}\le
(\epsilon_s+\epsilon_d)/\gamma+\epsilon_c+\epsilon_r,
\]

for positive declared margin `gamma`. None of these downstream arrows gains
selector authority.
