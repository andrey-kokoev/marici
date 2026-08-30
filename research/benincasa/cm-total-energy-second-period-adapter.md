# Cayley–Menger labelled-normal second-period adapter

## Correction to the bounded question

The path

\[
P_3\mapsto P_3+\tau
\]

is a labelled transverse-normal path. It is not a source-derived lift of the
scalar total-energy conormal. The calculation below therefore tests a
conditional \(P_3\)-normal coefficient adapter. It does not close Entry 2558's
missing reverse-map problem.

## Bounded calculation

Let

\[
L_3=\frac{\partial K}{\partial(P_3^2)}.
\]

Since

\[
K(\tau)=K+2P_3L_3\tau+L_3\tau^2,
\]

the algebraic \(K^{-5}\) audit twist has second coefficient

\[
[\tau^2]K(\tau)^{-5}
=K^{-5}
\left(
-5\frac{L_3}{K}
+60P_3^2\frac{L_3^2}{K^2}
\right).
\]

The physical residue system instead carries \(K^{-1/2}\), whose adapter is

\[
\mathsf A_{E,\mathrm{phys}}^{(2)}
=-\frac12\frac{L_3}{K}
+\frac32P_3^2\frac{L_3^2}{K^2}.
\]

Both normalizations are frozen and reduced independently.

## Acceptance contract

- retain both \(K^{-5}\) and physical \(K^{-1/2}\) normalizations;
- derive both \(K^{-1}\) and \(K^{-2}\) terms before reduction;
- use Entry 2554's Gröbner basis and labelled column conventions;
- keep A, B, HOMA, and SOFT1 separate;
- test two primes;
- do not infer a total-energy reverse map, marked-wall class, or physical
  activation.

## Result

The exact finite-field reductions pass at A, B, HOMA, and SOFT1, with A
replicated at a second prime. In every run,

\[
\dim H_{\rm CM}=7,
\qquad
\operatorname{rank}
\left\langle N_{\leq3},
\mathsf A_{P_3,K^{-5}}^{(2)},
\mathsf A_{P_3,K^{-1/2}}^{(2)}
\right\rangle
=4.
\]

Both adapter relations have support only in

\[
\left\langle
\nu_1,\nu_2,\nu_3,\nu_1^2,
\mathsf A_{P_3}^{(2)}
\right\rangle,
\]

and both have a nonzero coefficient in the unique quadratic quotient. Thus
the algebraic and physical twists select the same quadratic quotient line
projectively along the chosen \(P_3\)-normal. Neither creates a fifth
direction.

The affine coordinate varies with kinematics. No affine generator,
total-energy lift, marked-wall class, or physical pairing has been derived.

## Branch disposition

- nonzero projective \(P_3\)-normal component: survives;
- cancellation into the first-normal span: falsified;
- new fifth direction: falsified;
- source-derived total-energy adapter: remains untyped.

## Optionality snapshots

Before the calculation:

- four live reduction outcomes;
- one chosen labelled normal;
- no source-derived scalar-to-labelled conormal map.

After the calculation:

- one projective conditional line survives;
- the total-energy reverse-map problem remains open;
- the marked subconnection test is gated on that missing map.

## Activation observations

Pre:

- excitement: 9/10;
- confidence in a nonzero conditional component: 6/10;
- expected information gain: 9/10.

Post:

- excitement: 8/10;
- confidence in the conditional projective statement: 9/10;
- confidence that it solves the total-energy problem: 0/10;
- realized information gain: 10/10, because the typing failure was exposed.

These activation observations are process metadata, not theorem evidence.
