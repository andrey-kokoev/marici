# 1404 — The Asymmetric Five-Site Kummer Profile Does Not Admit the Source Cycle

## Status

Exact characteristic-zero obstruction for the declared asymmetric specialization.

## Source symmetry versus specialized coordinates

The five-cycle OFPT packet is cyclic at the labelled incidence level.

The cubic IBP pilot then specializes the five Kummer radicands to

\[
\begin{aligned}
f_1={}&2u_1^2+2u_2^2+u_3^2-2u_1u_2-2u_2u_3,\\
f_2={}&f_1-2u_1+1,\\
f_3={}&f_1-2u_2+2,\\
f_4={}&f_1-2u_3+3,\\
f_5={}&f_1+2u_1+2u_2-8u_3+29.
\end{aligned}
\]

This profile was introduced as an asymmetric finite specialization. It does not inherit cyclic covariance automatically.

## Unique possible affine lift

Seek an affine transformation \(u\mapsto u'\) satisfying

\[
f_i(u')=f_{i+1}(u),
\qquad i\pmod 5.
\]

The four affine differences \(f_i-f_1\) determine the candidate uniquely:

\[
\boxed{
u_1'=u_2-u_1,
\qquad
u_2'=u_3-u_1,
\qquad
u_3'=4u_3-2u_1-u_2-\frac{25}{2}.
}
\]

There is no remaining freedom to repair the common quadratic part.

## Exact obstruction

Substitution into the first four cyclic equations yields the common residual

\[
\boxed{
R=
\frac{621}{4}
+25u_2+2u_1u_2-6u_2u_3
+27u_1-6u_1u_3-75u_3
+u_2^2+9u_3^2.
}
\]

This polynomial is nonzero.

The fifth closure equation has residual

\[
R+
130+10u_1+10u_2-30u_3,
\]

which is also nonzero.

Therefore

\[
\boxed{
\text{no affine transformation of }(u_1,u_2,u_3)
\text{ realizes the source }C_5\text{ permutation on this profile.}
}
\]

The Symbolica checker verifies the result over characteristic zero.

## Consequence for Entry 1393

The rank-two affine mismatch plane was constructed after imposing this asymmetric specialization.

Hence it cannot be promoted to a cyclic coefficient object from data internal to this profile.

Its replicated rank remains a valid chart-level modular phenomenon, but cyclic descent is unavailable because the specialization itself breaks the source action.

## Architectural interpretation

This is not a failure of the source occurrence carrier.

It is a failure of symmetry descent through a non-equivariant coefficient specialization:

\[
\text{cyclic source carrier}
\longrightarrow
\text{asymmetric Kummer profile}
\]

does not commute with the \(C_5\) action.

The correct future route is to construct the torsor mismatch before asymmetric specialization, on a cyclicly labelled generic Kummer base, and only afterward specialize equivariantly where possible.

No post hoc coordinate transformation may be fitted to rescue the present plane.

## Artifact

- `research/benincasa/results/five-site-asymmetric-cyclic-specialization.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_cyclic_specialization.rs`

Allocator claim: `seqclaim-344d8bdd8f958e11f5ea2e4e`.
