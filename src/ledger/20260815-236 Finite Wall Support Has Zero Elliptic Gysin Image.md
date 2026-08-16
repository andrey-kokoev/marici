---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Finite Wall Support Has Zero Elliptic Gysin Image

## Record

Status: the first complete weight-\(-1\) wall class of entry 235 has zero
image under the infinity-Gysin map for support reasons. Any pushforward of
that class into the nine-master \(q_{\mathcal G_{12}}\)-sector lies in the
rank-seven algebraic/Tate kernel of entry 150.

This conclusion uses no fitted master projector and adds no carrier cell,
support summand, denominator, or normalization.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the finite weight }-1\text{ exceptional-wall class may have a
nonzero infinity-Gysin image in the Legendre block.}
}
\]

The finite falsifier was the frozen incidence of the two supports in the
source compactification.

## Frozen supports

Let \(\overline S_E\) be the compactified residue surface used in entry
150, with anticanonical elliptic boundary

\[
D_\infty=\{s=0\}.
\]

The lower-divisor collision of entries 225--235 is a finite marked point in
the affine chart \(s=1\). Let

\[
\beta:\widetilde S_E\longrightarrow\overline S_E
\]

be its blow-up and let \(W_{\rm exc}\) denote the supported wall on the
exceptional divisor. The blow-up center is disjoint from \(D_\infty\), so
the strict transform \(\widetilde D_\infty\) is unchanged near infinity.

Scheme-theoretically the two support ideals contain

\[
s,
\qquad
s-1,
\]

and therefore contain the unit

\[
\boxed{s-(s-1)=1.}
\]

Consequently

\[
\boxed{
W_{\rm exc}\cap\widetilde D_\infty=\varnothing.
}
\]

The same certificate applies to all three cyclic finite collision centers.

## Support base change

Write

\[
i_W:W_{\rm exc}\hookrightarrow\widetilde S_E,
\qquad
j_\infty:\widetilde D_\infty\hookrightarrow\widetilde S_E.
\]

The Cartesian pullback of \(i_W\) along \(j_\infty\) has empty source.
Proper/support base change therefore gives

\[
\boxed{
j_\infty^*i_{W!}=0.
}
\]

The infinity-Gysin projection factors through this boundary restriction.
Hence for the complete wall coefficient class \([F_{-1}]\),

\[
\boxed{
R_\infty\bigl(i_{W!}[F_{-1}]\bigr)=0.
}
\]

This is a support-level statement. It does not require coordinates in the
nine-master basis.

## Placement in the nine-master extension

Entry 150 established the generic de Rham exact sequence

\[
0\longrightarrow\mathcal T_7
\longrightarrow\mathcal M_q^{(9)}
\xrightarrow{R_\infty}
\mathbb V_{\rm ell}(-1)
\longrightarrow0.
\]

Therefore, whenever the finite supported class is pushed into
\(\mathcal M_q^{(9)}\), exactness forces

\[
\boxed{
\operatorname{push}[F_{-1}]\in
\ker R_\infty=\mathcal T_7.
}
\]

The result excludes a Legendre/Gauss--Manin quotient component. It does not
identify the coordinates of the class inside \(\mathcal T_7\), prove that
it spans the unpublished \(L_1\) line, or assign it to the
\(\langle e_6,v_{\rm alg}\rangle\) plane.

## Verdict

The conjectured nonzero elliptic image is falsified:

\[
\boxed{
\text{finite exceptional support}
\xrightarrow{\ R_\infty\ }
0.
}
\]

The nonzero coefficient found in entry 235 is genuine, but its new
complexity remains in the algebraic/relative coefficient sector over an
existing carrier wall. Its literal symmetric source-wall period remains
zero independently by oddness in \(n\).

## Classification

- existing carrier: unchanged finite collision wall and exceptional divisor;
- coefficient support: finite exceptional wall;
- algebraic/Tate placement: rank-seven kernel \(\mathcal T_7\), after
  pushforward to the nine-master sector;
- Legendre/Gauss--Manin image: zero by disjoint support;
- physical relative-chain pairing: zero at this grade by entry 235;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_finite_wall_infinity_gysin.rs`;
- `research/benincasa/finite-wall-infinity-gysin.json`;
- the unit-ideal certificate \(s-(s-1)=1\);
- the rank identity \(7+2=9\) from the explicit sequence of entry 150;
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Construct the source-defined pushforward of \([F_{-1}]\) in the
nine-master basis and compute its Gauss--Manin transport inside
\(\mathcal T_7\).

Test, without choosing a projector after seeing the answer, whether its
flat saturation:

1. lies in the final-block algebraic plane
   \(\langle e_6,v_{\rm alg}\rangle\);
2. selects the rank-one algebraic factor \(L_1\);
3. has nonintegral singular support on \(\mathcal Q=0\);
4. or occupies one of the other \((1,2,2)\) algebraic character blocks.

Failure to enter \(\langle e_6,v_{\rm alg}\rangle\) would separate this
finite wall correction from the current \(L_1/\mathcal Q\) candidate, but
would not create a new carrier incidence.

## Outcome contract

~~~json
{
  "claim": "The finite weight -1 exceptional-wall class may have a nonzero infinity-Gysin image.",
  "status": "falsified",
  "support_certificate": "s-(s-1)=1",
  "elliptic_gysin_image": 0,
  "nine_master_placement": "rank-seven algebraic/Tate kernel, conditional on source-defined pushforward",
  "kernel_coordinates": "uncomputed",
  "new_carrier_incidence": false,
  "next_experiment": "Compute the source-defined nine-master pushforward and its flat saturation inside T7."
}
~~~
