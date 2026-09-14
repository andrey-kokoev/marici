# Raw gamma subtraction cannot repair the paired resolvent conjecture

## Necessary parity

A regular paired self-adjoint resolvent has the form

\[
R_A(z)
=
\left\langle
\Omega,
\left((z-iA)^{-1}+(z+iA)^{-1}\right)
\Omega
\right\rangle.
\]

It is odd in \(z\), and therefore

\[
R_A(0)=0.
\]

The completed centered function \(\Xi\) is even, so its logarithmic derivative is likewise odd and vanishes at zero.

## Raw gamma subtraction

The gamma contribution to the logarithmic derivative at the center is

\[
G(0)
=
\frac12
\left(
\psi(1/4)-\log\pi
\right).
\]

Using

\[
\psi(1/4)
=
-\gamma-rac\pi2-3\log2,
\]

one obtains

\[
G(0)
\approx-2.68609.
\]

Consequently

\[
\frac{\Xi'(0)}{\Xi(0)}-G(0)
\approx2.68609,
\]

which does not vanish at the center and cannot equal a paired resolvent.

## Meaning

The raw gamma sector is not separately odd under centered functional-equation reversal. Oddness emerges only after endpoint, gamma, and prime contributions are combined. Removing gamma repairs the large-real-axis growth but destroys the parity required by the proposed self-adjoint resolvent.

Thus the first suggested repair is false in its naive sectorwise form.

## Surviving possibility

A viable subtraction would have to be an explicitly odd reference function that:

- carries the logarithmic asymptotic;
- preserves the center value zero;
- preserves functional-equation parity;
- retains all required pole cancellations;
- is itself source-derived before positivity.

No such reference has yet been constructed. Symmetrizing the gamma term introduces additional pole questions and cannot be accepted formally.

## Verification

```text
python research/voevodsky/checkers/check_gamma_subtracted_resolvent_parity_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_gamma_subtracted_resolvent_parity_no_go.py`
- `research/voevodsky/results/gamma_subtracted_resolvent_parity_no_go.json`
