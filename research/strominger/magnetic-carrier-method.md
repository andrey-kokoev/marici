# Testing rank defects by observation-carrier loss

The proposed method predicts exceptional circuits without computing
nullspaces:

1. choose the minimal boundary observation state;
2. factor every independent route carrying its transverse observation;
3. solve for simultaneous carrier loss;
4. only then compute the primitive circuit from surviving Plucker minors.

For `q=1`, the second observation has one carrier,

\[
(g-2)4^{\overline g},
\]

so the method predicts the unique defect `(g,q)=(2,1)`.

For odd low-grade components, `d=q-g>=3`, the two `R_2` carriers are

\[
L_{g,d}=-\left(2dg+2d-g^2-11g-4\right)
\frac{(d+g-3)!}{(d-2)!},
\]

\[
R_{g,d}=\frac{g(d-4)(d-3)(g-2)(g-1)(g+3)}{2}
\frac{(d+g-3)!}{d!}.
\]

In the admissible odd domain, `R=0` implies `g=2` or `d=3`.

- At `d=3`, the remaining polynomial is `-g^2-5g+2`, nonzero for `g>=2`.
- At `g=2`, the left route is `-6(d-1)(d-5)`, whose unique admissible zero
  is `d=5`.

Thus simultaneous carrier loss predicts exactly

\[
(g,d)=(2,5),
\qquad
(g,q)=(2,7).
\]

## Falsification result

The checker makes these predictions before rank computation, then compares
them with exact matrices.  Agreement is complete across:

- 435 odd local collision cores, `2<=g<=30`, odd `3<=d<=31`;
- 99 `q=1` blocks, `2<=g<=100`;
- 570 full initialization blocks, `2<=g<=20`, `1<=q<=30`.

The full blocks lose rank only at `(2,1)` and `(2,7)`, exactly as predicted.
No null vector is used by the predictor.

## Negative controls

The method must require loss of every independent carrier, not the vanishing
of one preferred coordinate.

At the even divisor `d=g+8`, the primary collision coordinate vanishes.  The
alternate row-`3` carrier is

\[
\tau_g=-\frac{8(2g+3)(g^2-g-26)(2g+1)!}
{3(g+5)(g+6)(g+7)(g-1)!}.
\]

The only potentially vanishing factor has discriminant `105`, so it has no
integral root.  Thus the carrier atlas remains jointly faithful and the
method correctly reports a chart boundary, not a kernel class.

At the seam `d=1`, overlapping labels change the presentation, but the
endpoint carrier determinant

\[
-\frac{g(g+3)(2g-1)g!(g+3)!}{3}
\]

is nonzero.  The method again predicts no information loss.

The method therefore survives its first independent test:

\[
\boxed{
\text{factor carrier routes}
\longrightarrow
\text{predict the rank discriminant}
\longrightarrow
\text{extract circuits only on that discriminant}.
}
\]

The augmented checker passes nine gates, including both negative controls.
Its present proven scope is the magnetic component atlas.  Applying it to a
different operator requires deriving that operator's observation state and
carrier routes from its own source law; the magnetic factorization must not be
assumed universal.
