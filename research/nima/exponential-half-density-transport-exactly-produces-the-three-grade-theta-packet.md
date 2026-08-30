# Exponential half-density transport exactly produces the three-grade theta packet

## Half-density transport

Let \(f\) be a function on the positive spatial ray. For each theta label \(n\ge1\), define
\[
(\mathcal M_n f)(u)
=
\sqrt n\,e^{u/2}f(ne^u).
\]

With \(x=ne^u\),
\[
du=\frac{dx}{x},
\qquad
n e^u=x.
\]
Therefore
\[
\|\mathcal M_n f\|_{L^2(du)}^2
=
\int_{\mathbb R}n e^u|f(ne^u)|^2\,du
=
\int_0^\infty |f(x)|^2\,dx.
\]

Thus \(\mathcal M_n\) is an isometry from the positive-ray \(L^2(dx)\) space into the label-\(n\) logarithmic-scale fiber. The factor \(\sqrt n\,e^{u/2}\) is fixed by half-density transport, not by arithmetic fitting.

## Gaussian label

Take
\[
f_0(x)=e^{-\pi x^2}.
\]
Then
\[
(\mathcal M_n f_0)(u)
=
\sqrt n\,e^{u/2}
e^{-\pi n^2e^{2u}}.
\]

Up to the separate label normalization \(\sqrt n\), this is exactly the uncompleted theta label.

The transport changes the argument before scalar evaluation:
\[
x
\longmapsto
ne^u.
\]
This is precisely the nonlinear operation capable of escaping the Gaussian-in-\(\log p\) no-go.

## Intertwining of generators

Let
\[
A_x=x\partial_x.
\]
A direct differentiation gives
\[
\partial_u\mathcal M_n
=
\mathcal M_n\left(A_x+\frac12\right).
\]

Consequently,
\[
\left(\partial_u^2-\frac14\right)\mathcal M_n
=
\mathcal M_n\left(A_x^2+A_x\right).
\]

So the theta completion differential is the transported positive-ray operator
\[
A_x(A_x+1).
\]

## Exact three-grade completion

For the Gaussian \(f_0(x)=e^{-\pi x^2}\), set
\[
X=\pi x^2.
\]
Then
\[
A_xf_0=-2Xf_0,
\]
and
\[
A_x^2f_0=(4X^2-4X)f_0.
\]
Hence
\[
(A_x^2+A_x)f_0
=
(4X^2-6X)e^{-X}.
\]

Transporting back gives
\[
\left(\partial_u^2-\frac14\right)
\left(e^{u/2}e^{-\pi n^2e^{2u}}\right)
=
e^{u/2}
\left(4X_n(u)^2-6X_n(u)\right)e^{-X_n(u)},
\]
where
\[
X_n(u)=\pi n^2e^{2u}.
\]

This is exactly the completed theta label formula. The three grades \(1,X,X^2\) arise from the transported second-order dilation operator.

## Consequence for constructor order

The required operator-valued bridge is no longer hypothetical:
\[
\text{positive-ray Gaussian}
\xrightarrow{\mathcal M_n}
\text{log-scale theta label}
\xrightarrow{\partial_u^2-1/4}
\text{three-grade completed label}.
\]

It must be applied before scalar Stokes contraction. Event 10378's order-of-operations obstruction is therefore met at the single-label analytic level.

## Remaining mismatch with the window path

The comoving windows use translated Gaussian fronts
\[
e^{-\pi(q\pm t)^2}.
\]
The transport above acts on positive-ray dilation,
\[
x\mapsto ne^u,
\]
not on the translated \(q\)-front automatically.

The next comparison must decompose each translated front into positive and negative ray carriers, apply the appropriate labelled half-density transports, and prove that the oriented interval history is preserved. One cannot simply substitute \(q\pm t=ne^u\) independently, because that would destroy the common cell geometry.

## Uniformity

Each single-label transport is isometric. Any completion instability must therefore enter through:

- summing over \(n\);
- the three-grade differential graph norm;
- the comparison from translated two-front windows to ray carriers;
- arithmetic prime sampling after theta synthesis.

No superexponential scalar calibration is needed at the label transport itself.

## Frontier

The earliest missing arrow has contracted to:
\[
\text{translated two-front window history}
\longrightarrow
\bigoplus_{n\ge1}
\text{positive/negative ray half-density fibers}.
\]

After that arrow, theta completion is an exact transported dilation polynomial rather than a guessed normalization.
