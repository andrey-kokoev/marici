# Exact portal setting compiler

Work package: WP580  
Owner: marici.Figueiredo

## Purpose

WP579 requires finite portal settings with a controlled nonlinear remainder.
On the nonzero-mixing domain, the invariant map is explicitly invertible, so
orthogonal invariant perturbations can be compiled exactly rather than
approximated by the local Jacobian.

Let

\[
F(z,\lambda_s)
=
\left(z,{\lambda_s z^2\over\lambda_H}\right)
=(r,q),
\qquad
z>0,\quad\lambda_s>0,\quad\lambda_H>0.
\]

## Exact finite settings

At a base point \((z,\lambda_s)\), a finite pure-\(r\) step of size \(h\) is

\[
S_r(h)
=
\left(z+h,\lambda_s{z^2\over(z+h)^2}\right),
\qquad z+h>0.
\]

It obeys exactly

\[
F(S_r(h))-F(z,\lambda_s)=(h,0).
\]

A finite pure-\(q\) step is

\[
S_q(h)
=
\left(z,\lambda_s+{\lambda_H h\over z^2}\right),
\]

and obeys

\[
F(S_q(h))-F(z,\lambda_s)=(0,h).
\]

It remains in the declared quartic-stable domain only if

\[
\lambda_s+{\lambda_Hh\over z^2}>0.
\]

The two-setting invariant design is therefore \(X=hI\), with
\(\sigma_{\min}(X)=|h|\). Dividing calibrated responses by the declared step
size gives the unit orthogonal design without a portal-coordinate truncation
error.

For symmetric pure-\(r\) settings, both \(z-h\) and \(z+h\) must remain
positive, so \(0<h<z\). Additional stability or phenomenology restrictions on
\(\lambda_s\) must be intersected with this exact domain before execution.

## Linearized-setting hostile

The first-order pullback from WP579 would approximate the pure-\(r\) setting
as

\[
\widetilde S_r(h)
=
\left(z+h,\lambda_s-{2\lambda_s h\over z}\right).
\]

Its invariant \(q\) contamination is exactly

\[
q(\widetilde S_r(h))-q(z,\lambda_s)
=
-{\lambda_s\over\lambda_H}
\left(3h^2+{2h^3\over z}\right).
\]

Thus a Jacobian-orthogonal setting is not finitely orthogonal. At the rational
hostile \(z=\lambda_s=\lambda_H=1\), \(h=1/2\), the exact compiler uses
\((z',\lambda_s')=(3/2,4/9)\) and preserves \(q=1\). The linearized setting
uses \((3/2,0)\) and changes \(q\) by \(-1\).

## Authority and classification

WP580 is a source-coordinate setting compiler on an admitted invariant portal
family. It removes finite-step geometric bias from a prospective calibration,
but it does not supply detector transport, publication binding, or a source
selector. Parameter preparation in a generator remains a research operation
until joined to an admitted physical experiment.

The compiler descends under the full weak-basis groupoid because both its
input and target coordinates are invariant. It introduces no reference port.
Its smallest falsifiers are \(z=0\), where the inverse is undefined,
\(\lambda_s\le0\), where the declared isolated quartic ray is not stable, and any
finite setting that leaves the declared stable or phenomenological source
domain.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp580_exact_portal_setting_compiler.py

The generated result is
research/flavor/results/wp580_exact_portal_setting_compiler.json.
