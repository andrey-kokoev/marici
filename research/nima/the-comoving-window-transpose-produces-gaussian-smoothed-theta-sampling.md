# The comoving-window transpose produces Gaussian-smoothed theta sampling

## Exact transpose calculation

The differentiated comoving kernel sends a scale atom to the reciprocal
Gaussian front

\[
D\mathcal K\delta_t=q_t,
\qquad
q_t(q)=f_0(q-t)-f_0(q+t),
\qquad
f_0(q)=e^{-\pi q^2}.
\]

Let \(\psi\) be a real odd test function.  Then

\[
\begin{aligned}
\langle q_t,\psi\rangle
&=\int f_0(q-t)\psi(q)\,dq
 -\int f_0(q+t)\psi(q)\,dq\\
&=(f_0*\psi)(t)-(f_0*\psi)(-t)\\
&=2(f_0*\psi)(t).
\end{aligned}
\]

Therefore the ordinary transpose of the differentiated comoving kernel is

\[
\boxed{
(D\mathcal K)^\times\psi(t)=2(f_0*\psi)(t)
}
\]

on the reciprocal-odd test sector.

For the completed-theta forcing \(\psi=\Phi'\),

\[
\boxed{
(D\mathcal K)^\times\Phi'(t)
=2(f_0*\Phi')(t),
}
\]

not \(2\Phi'(t)\).

## Euler sampling comparison

At grade \(k\), the logarithmic Euler coefficient contributes

\[
kL\,a_{p,k}=Lp^{-k/2},
\qquad
a_{p,k}=\frac1k p^{-k/2}.
\]

Pairing the differentiated window image with \(\Phi'\) therefore gives

\[
2Lp^{-k/2}(f_0*\Phi')(kL).
\]

The frozen Euler-to-theta incidence is instead

\[
\kappa_p^{(k)}
=2Lp^{-k/2}\Phi'(kL).
\]

The exact defect is

\[
\boxed{
\delta_{p,k}^{\mathrm{heat}}
=2Lp^{-k/2}
\left[(f_0*\Phi')(kL)-\Phi'(kL)\right].
}
\]

Thus the shared translation coefficients and labels do not make the lower
mate square commute under the ordinary Hilbert/distribution pairing.  The
comoving kernel inserts one unit Gaussian heat smoothing.

## Fourier hostile

With the repository Fourier normalization,

\[
\widehat f_0(\xi)=e^{-\pi\xi^2}.
\]

If

\[
f_0*\Phi'=\Phi',
\]

then

\[
(e^{-\pi\xi^2}-1)\widehat{\Phi'}(\xi)=0.
\]

The multiplier vanishes only at \(\xi=0\).  Hence \(\widehat{\Phi'}\) would
have to be supported at zero.  A rapidly decreasing nonzero odd function
cannot have that Fourier support.  Therefore

\[
\boxed{f_0*\Phi'\ne\Phi'.}
\]

So the defect is structural, not a missing scalar normalization.

## Required repair

A commuting Green adjunction must explicitly compensate for the Gaussian
smoothing.  The possible typed mechanisms are:

1. a source-authorized inverse heat operator \(e^{-\Delta/(4\pi)}\) on the
   admitted theta-forcing range;
2. replacement of the test vector \(\Phi'\) by a declared preimage
   \(\Psi'\) satisfying \(f_0*\Psi'=\Phi'\);
3. a relative Green pairing whose metric operator contributes the inverse
   Gaussian multiplier;
4. a different boundary kernel whose differentiated transpose is literal
   point evaluation.

None is automatic.  Inverse heat multiplication grows like
\(e^{\pi\xi^2}\), so its domain and continuity are substantive and may fail on
the declared completion.

## Revised earliest gate

The middle map \(D\mathcal K\) exists, but its ordinary transpose is the wrong
sampling functional.  The earliest local theorem is now:

> Construct a source-authorized relative Green metric that removes exactly
> the Gaussian heat factor on the completed-theta odd forcing, and prove that
> the resulting inverse-heat operation is defined and continuous on the common
> source core.

Until then, the labelwise arithmetic mate square does not commute.  The
conditional determinant margin remains valid after any successful repair, but
it cannot supply the missing inverse-heat adjunction.  Radical descent and
global closed range remain open.  No RH conclusion is authorized.
