# The half-density-twisted four-front window incidence is explicit

## Boundary packet

Let

\[
f_0(q)=e^{-\pi q^2},
\qquad
(U_af)(q)=f(q+a),
\]

and, for \(L=\log p\), let the differentiated adjacent-window packet be

\[
b_p
=U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

This is exactly

\[
b_p=D(W_{2L}-W_L).
\]

The completion-matched trace ports are

\[
M_z(g)=\int_{\mathbb R}e^{zq}g(q)\,dq,
\qquad z=\pm\frac12.
\]

## Gaussian half-density moment

Completing the square gives

\[
M_z(f_0)
=\int_{\mathbb R}e^{zq-\pi q^2}\,dq
=e^{z^2/(4\pi)}.
\]

Translation obeys

\[
M_z(U_af_0)
=e^{-za}M_z(f_0).
\]

Therefore

\[
\begin{aligned}
M_z(b_p)
&=e^{z^2/(4\pi)}
\left(e^{2zL}-e^{-2zL}-e^{zL}+e^{-zL}\right)\\
&=2e^{z^2/(4\pi)}
\left(\sinh(2zL)-\sinh(zL)\right).
\end{aligned}
\]

At the two completion characters,

\[
M_+(b_p)
=2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0,
\]

\[
M_-(b_p)
=-2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)<0.
\]

## Pure reciprocal-odd output

The half-density even and odd ports are

\[
w_{1/2}=\frac{M_-+M_+}{\sqrt2},
\qquad
j_{1/2}=\frac{M_+-M_-}{\sqrt2}.
\]

For the four-front packet,

\[
\boxed{w_{1/2}(b_p)=0,}
\]

and

\[
\boxed{
s_p^{(1/2)}
:=j_{1/2}(b_p)
=2\sqrt2\,e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0.
}
\]

Thus the differentiated adjacent window lands exactly in the reciprocal-odd
half-density trace line; no even completion wall contaminates it.

In prime variables,

\[
\boxed{
s_p^{(1/2)}
=\sqrt2\,e^{1/(16\pi)}
\left(p-p^{-1}-p^{1/2}+p^{-1/2}\right).
}
\]

## Comparison with the plain Stokes value

The plain distributional Stokes readout is

\[
s_p=4(H(L)-H(2L)).
\]

It is positive but decays on the logarithmic-Gaussian scale.  By contrast,

\[
s_p^{(1/2)}\sim\sqrt2\,e^{1/(16\pi)}p.
\]

Hence

\[
s_p^{(1/2)}\ne s_p.
\]

This explicitly confirms the spectral-location warning: the plain Stokes port
cannot be substituted for the completion Wronskian trace.

## Candidate completed normalization

If the twisted-history mate square identifies \(b_p\) with the retained
boundary generator and propagates it to the completed-theta Wronskian line,
then the only possible scalar is

\[
\boxed{
\lambda_p^{(1/2)}
=\frac{-\kappa_p}{2s_p^{(1/2)}}>0.
}
\]

This ratio is now built from matching half-density ports.  Its denominator is
explicit and nonzero.  However, the scalar formula still does not prove the
mate square, domain continuity, or source authorization of the comparison.

Because \(s_p^{(1/2)}\) grows linearly while \(\kappa_p\) decays
superexponentially, \(\lambda_p^{(1/2)}\) is even more smoothing than the
previous plain-port candidate.  It cannot be a boundedly invertible unweighted
all-prime comparison.

## Revised gate

The missing local calculation is no longer the twisted trace value.  It is the
operator theorem that the exponentially conjugated histories \(H_-\) and
\(H_+\):

1. are closed on the declared relative graph domains;
2. carry the differentiated window packet to the traces computed above;
3. commute with reciprocal reflection and prime cutoffs;
4. form the source mate square with Euler-to-theta incidence and the frozen
   Wronskian readout.

Only then may \(\lambda_p^{(1/2)}\) be inserted into the first-Adams linking
block.  No RH conclusion is authorized.
