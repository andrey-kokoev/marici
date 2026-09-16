# A Gauss-sum seed closes the ramified local Tate sewing with the reflection sign

## Question

Can the remaining ramified finite-character sectors be normalized source-derivatively, including conductor power, epsilon phase, and Fourier-square sign?

## Claim boundary

Yes for a unitary character of conductor \(p^n\), using its unit-shell character vector and defining the Gauss phase by the declared additive Fourier integral. The resulting local factor is unimodular on the critical line and its reflected product is \(\chi(-1)\), exactly the local reflection character.

## Conventions and source vector

Let \(\psi_p\) have conductor \(\mathbb Z_p\), let additive Haar measure satisfy \(\operatorname{vol}(\mathbb Z_p)=1\), and normalize multiplicative Haar measure by

$$
\operatorname{vol}_{d^\times x}(\mathbb Z_p^\times)=1.
$$

Let \(\chi\) be unitary of conductor exponent \(n\ge1\). Define

$$
f_\chi(x)
=\chi(x)^{-1}\mathbf1_{\mathbb Z_p^\times}(x).
$$

Then

$$
Z_p(f_\chi,\chi,s)=1.
$$

Thus this is a normalized source vector rather than a factor fitted after the functional equation.

## Fourier transform and Gauss integral

Use

$$
\widehat f(y)=\int_{\mathbb Q_p}f(x)\psi_p(-xy)\,dx.
$$

Character orthogonality shows that \(\widehat f_\chi\) is supported on the shell

$$
v_p(y)=-n.
$$

For \(y=p^{-n}u\), \(u\in\mathbb Z_p^\times\), define

$$
G(\chi,\psi_p)
=
\int_{\mathbb Z_p^\times}
\chi(x)^{-1}\psi_p(-p^{-n}x)\,dx.
$$

A unit change of variables gives

$$
\widehat f_\chi(p^{-n}u)
=\chi(u)G(\chi,\psi_p).
$$

The primitive Gauss-sum identity gives

$$
|G(\chi,\psi_p)|=p^{-n/2}.
$$

Hence

$$
\omega(\chi,\psi_p)
=p^{n/2}G(\chi,\psi_p)
$$

is a source-defined unit complex number.

## Ramified Tate factor

The local functional equation is

$$
Z_p(\widehat f,\chi^{-1},1-s)
=\gamma_p(s,\chi,\psi_p)Z_p(f,\chi,s).
$$

Substituting \(f=f_\chi\) and integrating the single support shell yields

$$
\boxed{
\gamma_p(s,\chi,\psi_p)
=
\omega(\chi,\psi_p)\,
\chi(p)^n\,
p^{n(1/2-s)}.
}
$$

If the convention extends the ramified unit character by \(\chi(p)=1\), the middle factor disappears. Writing the Gauss integral explicitly prevents this extension convention from becoming a hidden phase.

## Critical-line and square checks

For \(s=1/2+it\),

$$
|p^{n(1/2-s)}|=1,
$$

so

$$
|\gamma_p(1/2+it,\chi,\psi_p)|=1.
$$

Applying the local functional equation twice and using

$$
\mathcal F_p^2f(x)=f(-x)
$$

gives

$$
\gamma_p(s,\chi,\psi_p)
\gamma_p(1-s,\chi^{-1},\psi_p)
=\chi(-1).
$$

Thus even local characters square to \(+1\) and odd local characters square to \(-1\), exactly paralleling the two real parity branches.

## Semilocal consequence

For an arbitrary angular character \(\chi=\prod_v\chi_v\), the semilocal multiplier is the product of:

- the exact real trivial/sign branch;
- unramified ratios \(L_p(1-s)/L_p(s)\);
- ramified source Gauss phases and conductor monomials above.

Every factor is unimodular on the critical line, and the total reflected product is the global action of \(-1\) on the angular character. No independent block-unitary choice remains.

## Disposition

Ramified finite-place normalization is closed by the unit-shell character seed. Its Fourier image supplies the normalized Gauss epsilon phase and conductor factor directly, and its square records \(\chi(-1)\). The complete characterwise semilocal Tate sewing is now normalized on the test/dual spectral carrier.