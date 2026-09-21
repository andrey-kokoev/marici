# Window moment defects obstruct the even-port arithmetic attachment comparison

## Result

The fixed even-sheet map preserves actual window additivity and the algebraic relation construction. But the prepared full-theta arithmetic form identity does NOT extend to every event window of a genuine diamond. It therefore cannot, by slotwise tensoring alone, give the label-preserving paired two-seam attachment comparison.

The obstruction is explicit: the source moment port of a window need not equal the arithmetic operator applied to its even port. Two successive positive event windows already force a mismatch in at least one of their labelled diagonal observations. These sectors occur in an actual four-event two-seam relation product.

This does not refute the one-slot theorem for prepared full-theta packets, or algebraic balancing of the even-port map. It rules out promotion of that theorem to the full labelled window pairing without additional source data.

## 1. The two source ports and the arithmetic graph condition

Use the normalizations in

`../voevodsky/a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`.

For an actual forcing f put

`X_f(z)=integral cos(zx) f(x) dx`,

`M_f(z)=i X_f'(z)`.

The normalized Clark amplitudes are E_f=X_f+M_f and E_star,f=X_f-M_f. The fixed sum and difference of sheets therefore give the two half-line states

`U_f(z)=sqrt(2) X_f(z) exp(i z u)`,

`W_f(z)=sqrt(2) M_f(z) exp(i z u)`.

The original unweighted half-line pairing gives the exact identity

`K_Clark(f,g;w,z)=<U_f(w),W_g(z)>_0+<W_f(w),U_g(z)>_0`.

This is the prescribed two-sheet signed pairing expressed in its fixed even/moment coordinates. No arithmetic operator or fitted form is needed for it.

Write s_z=1/2-i z and L(s)=xi'(s)/xi(s) on the Euler chart. The independently constructed operator satisfies

`L_ar U_f(z)=sqrt(2) L(s_z) X_f(z) exp(i z u)`

for every forcing amplitude, since its exponential state is an eigenvector. The special prepared theta identity is the additional graph condition

`W_Phi(z)=L_ar U_Phi(z)`.

It is this condition, not linearity of the even projection, that identifies the two forms on the prepared theta family.

## 2. Exact defect for arbitrary windows

Define the source-computable residual

`R_f(z)=M_f(z)-L(s_z) X_f(z)`.

With d(w,z)=-i(z-conjugate(w)), direct expansion gives

`K_Clark(f,g;w,z)-q_ar(U_f(w),U_g(z))
 = 2 [conjugate(X_f(w)) R_g(z)
      +conjugate(R_f(w)) X_g(z)] / d(w,z)`.

Equivalently it is the two cross-pairings of U with W-L_ar U. The denominator stays attached to the given spectral pair and is the UNWEIGHTED half-line denominator.

The residual is a diagnostic, not a newly fitted correction channel or an identification with the prime or gamma term. Both M_f and L_ar were already prescribed independently. The identity records exactly which source moment information the even-port arithmetic substitution discards.

On compact Euler spectral interiors, all these maps are continuous on the forcing domain: the even port lies in the declared D_gamma graph domain, the moment trace has the established forcing bound, and L_ar:D_gamma->H_gamma is bounded. The defect is therefore a genuine continuous form difference, not an undefined endpoint operation.

## 3. Two actual event windows cannot both obey the graph condition

Take z=i y in the admitted spectral interior, with y>1/2; for the fixed disk one may use its imaginary center. Let f be a nonzero positive window forcing on [a,b] subset [log(2),infinity). The theta atoms are positive on this half-line, so every nonempty event window has this property.

Then

`X_f(i y)=integral cosh(yx) f(x) dx >0`,

`M_f(i y)=integral x sinh(yx) f(x) dx`.

Their ratio is the positive weighted mean

`mu_f(y)=M_f(i y)/X_f(i y)
 = weighted_mean_f [x tanh(yx)]`.

The function h_y(x)=x tanh(yx) is strictly increasing for x>0, since

`h_y'(x)=tanh(yx)+yx sech(yx)^2 >0`.

Now take the actual two-event route with arithmetic vertices 2Q,4Q,12Q. Its consecutive windows are

`f_1=1_[log(2Q),log(4Q)] Phi`,

`f_2=1_[log(4Q),log(12Q)] Phi`.

Strict positivity on the interiors gives

`mu_(f_1)(y) < h_y(log(4Q)) < mu_(f_2)(y)`.

But the fixed arithmetic operator supplies the SAME scalar L(1/2+y) for both windows. They cannot both satisfy mu_f(y)=L(1/2+y).

Since L is real there, their diagonal defects are

`Delta_f(i y,i y)=2 X_f(i y)^2 [mu_f(y)-L(1/2+y)]/y`.

In particular

`Delta_(f_2)/X_(f_2)^2 - Delta_(f_1)/X_(f_1)^2
 =2[mu_(f_2)-mu_(f_1)]/y >0`.

At least one actual window has a nonzero defect. This proof does not need a numerical value or sign for L, and does not use a sampled Clark matrix. A nonzero diagonal defect also persists on a sufficiently small compact spectral neighborhood by continuity.

## 4. The relation still descends algebraically

Complete the diamond with the other route 2Q,6Q,12Q. Splitting its forcing interval into the three consecutive chambers gives the four edge forcings

`a`, `b+c`, `a+b`, `c`.

Thus the singly retained relation records

`a+(b+c)-(a+b)-c=0`.

The even map, the moment map and the residual are all linear in forcing. They preserve this identity. The forgotten relation is preserved as well. Ordered tensor substitution consequently preserves the terminal zero records, the derivative product rule and the genuine balancing relations on finite presentations. On the admitted forcing-resolved domains the compact-interior bounds provide the corresponding fixed-slot continuity.

So the failure is NOT a new algebraic kernel or loss of interval additivity. Additive cancellation of residuals in a terminal relation does not imply preservation of its labelled sesquilinear seam observations.

## 5. Locate the failure in an actual two-seam product

Let a_rel be the singly retained relation on this first diamond. In D(a_rel), projection onto either retained seam edge along the route 2Q->4Q->12Q, with the two buffers vacuum, gives that edge's actual feature with coefficient +1.

Append a forgotten diamond relation c_rel on two fresh events. At four events,

`D2(a_rel c_rel)=D(a_rel) tensor_balanced D(c_rel)`.

Choose a forgotten edge sector of the second derivative cycle with coefficient +1. Projection onto this edge together with either selected first-diamond retained edge gives a genuine balanced two-seam sector with one retained feature and all other letters/buffers vacuum. Its Green observation is precisely the corresponding first-window form times the unit vacuum factor.

Applying the proposed arithmetic even-port substitution slotwise would replace that form by q_ar(U_f,U_f), retaining the same edge labels and vacuum factor. Section 3 proves that at least one of these two actual sectors changes. The product has eight nonzero source coefficients and I^3=0 in its four-event corner, so this is not a product class erased by an extra quotient.

The conclusion is channelwise failure of the proposed label-preserving ambient paired comparison. It is not an uncomputed assertion about the unprojected total self-pairing of the entire relation vector: other sectors have their own contributions. Ambient typed-channel observations are part of the declared receiver comparison and cannot be discarded to hide this defect.

## 6. Consequence for the lane

The arithmetic operator realizes the full-theta one-slot form on its specified prepared family. The seam construction requires actual window forcings and their ordered moment data. The former result cannot simply be tensorized into the latter paired attachment.

Any stronger comparison must address the residual W_f-L_ar U_f, or restrict its claim to a source family where that residual is controlled in a way sufficient for the desired pairing. No new arithmetic interpretation of this residual, no positivity claim, and no equivalence with the independent semilocal operator is supplied here.

The existing source relation tower, observer module, and separate bulk/forcing currents are unchanged.

## Verification

`uv run --with sympy python research/nima/checkers/check_window_arithmetic_attachment_defect.py`

Artifact: `results/window-arithmetic-attachment-defect.json`.

Passed the exact two-port expansion and residual identity, imaginary-axis diagonal formula, the monotonicity derivative identity, diamond additivity, and the selected sectors of an actual balanced four-event product cycle. The strict inequality for the actual theta windows follows from positivity and ordered supports, not numerical quadrature.
