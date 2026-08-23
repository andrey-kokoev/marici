# Endpoint--remainder decomposition of the completed Loewner form

## Completed source split

Write

\[
c=\frac14,
\qquad
\zeta=w-c,
\qquad
C(w)=c+U(w),
\]

where

\[
\boxed{U(w)=\zeta T(w)}
\]

and \(T\) is the entire transform of the positive superexponential theta
remainder. The constant \(c\) is the exactly renormalized null-mode
contribution.

The angular-current function is

\[
H(w)=\frac{\zeta U'(w)}{c+U(w)}.
\]

## Denominator-free current decomposition

For \(w\) in the upper half-plane, the clockwise energy current is

\[
P(w)=2\Im\!\left(\zeta C'(w)\overline{C(w)}\right).
\]

Since \(C'=U'\),

\[
\boxed{
P=P_{\mathrm{end},\theta}+P_{\theta,\theta},
}
\]

with

\[
\boxed{
P_{\mathrm{end},\theta}
=2c\,\Im\!\left(\zeta U'(w)\right),
}
\]

and

\[
\boxed{
P_{\theta,\theta}
=2\Im\!\left(\zeta U'(w)\overline{U(w)}\right).
}

In terms of \(T\), the theta--theta term simplifies because
\(\Im(\zeta T\overline{\zeta T})=0\):

\[
\boxed{
P_{\theta,\theta}
=2|\zeta|^2\Im\!\left(\zeta T'(w)\overline{T(w)}\right).
}
\]

Thus completion contributes a linear endpoint--theta interference term, while
the nontrivial source contributes its own quadratic angular current.

## Loewner-kernel decomposition

The denominator-free real kernel likewise splits exactly:

\[
\boxed{
L_C(x,y)=L_{\mathrm{end},\theta}(x,y)
+L_{\theta,\theta}(x,y),
}

where

\[
L_{\mathrm{end},\theta}(x,y)
=c\,
\frac{\zeta_xU'(x)-\zeta_yU'(y)}{x-y},
\]

and

\[
L_{\theta,\theta}(x,y)
=
\frac{
\zeta_xU'(x)U(y)-\zeta_yU'(y)U(x)
}{x-y}.
\]

Neither term is asserted positive separately. Their sum is the faithful
completed object.

## Threshold behavior

At \(w=c\), \(U(c)=0\) and \(U'(c)=T(c)>0\). Hence the theta--theta current is
quadratic in \(\zeta\), while the endpoint--theta term supplies the leading
linear response. This yields

\[
H'(c)=\frac{U'(c)}c=4T(c)>0.
\]

So the renormalized endpoint constant is not inert: it seeds the correct
orientation of the current at the spectral edge. The quadratic theta current
becomes relevant only away from the center.

## Coupled positivity theorem

For any finite real tuple \(x_1,\ldots,x_n\), let \(E\) and \(R\) be the
matrices of \(L_{\mathrm{end},\theta}\) and
\(L_{\theta,\theta}\). If

\[
E\succ0
\]

and

\[
\left\|E^{-1/2}RE^{-1/2}\right\|<1,
\]

then

\[
\boxed{E+R\succ0.}
\]

The proof is the elementary quadratic-form bound. Its value here is to state
the exact source quantities for an endpoint-dominance mechanism.

This is conditional. In particular, the endpoint matrix \(E\) need not be
positive for generic positive transforms \(T\).

## Meaning

The polynomial completion is reinterpreted as a coupled source channel. It
does not merely remove poles: after renormalization it leaves a constant whose
interference with the theta remainder determines the initial positive current.

The global theorem may therefore have the form

\[
\text{endpoint--theta anchor}
+\text{theta--theta interaction}
>0,
\]

rather than positivity of either sector. This mirrors the earlier thimble
lesson: individual components can be negative while the source-canonical
coupled object is positive.

## Falsifiers and next test

The endpoint-dominance explanation is falsified by:

1. a finite tuple where \(E\) has a negative direction too large to be repaired
   canonically;
2. a generalized relative eigenvalue of \((R,E)\) reaching \(-1\); or
3. a direction in \(\ker E\) on which \(R<0\).

The next hostile numerical test should evaluate the two matrices separately
on the same tuples used for the full Pick scan. It must report generalized
relative eigenvalues, not merely compare entrywise absolute values.

## Hostile verdict: separate positivity fails at rank two

Direct completed-theta quadrature at 4,000 and 8,000 Simpson steps gives the
same verdict on a grid with real parts
\(-30,-3,-0.3,0.3,3,30\) and heights \(0.1,1\):

1. every sampled one-point endpoint and theta diagonal is positive;
2. the endpoint block has a stable negative two-point determinant
   \(-1.50290255869739\times10^{-7}\) at
   \((-30+0.1i),(-3+0.1i))\);
3. the theta--theta block has a stable negative two-point determinant
   \(-4.67211404765064\times10^{-9}\) at
   \((-30+0.1i),(30+0.1i))\); and
4. the completed sum has no resolved negative determinant through order three
   on all 298 sampled tuples.

The two resolutions agree on the displayed negative component determinants
to roughly \(10^{-22}\).

Therefore the endpoint channel is not a positive anchor matrix and the
conditional dominance theorem above is not the global theta mechanism. The
endpoint term seeds the correct local threshold orientation, but away from
the center both source channels are individually indefinite. Positivity, if
global, belongs irreducibly to their completed sum.

Because the prerequisite \(E\succ0\) already fails, generalized
endpoint-relative eigenvalues are not a valid global diagnostic and were not
used to repair the mechanism.

This is the same structural lesson found for thimbles, now one level deeper:

\[
\boxed{
\text{positive diagonals of both source channels}
\not\Rightarrow
\text{positive coupled kernels},
}
\]

while two indefinite presentation blocks may assemble into a positive
faithful object.

Returning to that faithful object immediately yields an exact theorem: the
full positive completed source proves diagonal Loewner positivity for every
real \(x>1/4\) by an expectation--variance identity. See
`theta-full-source-outer-diagonal-loewner-theorem.md`.

Artifacts:

- checkers/theta_endpoint_remainder_pick_split.py
- results/theta-endpoint-remainder-pick-split.json
