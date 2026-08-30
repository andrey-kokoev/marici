# The relative Haar domain has a Dirichlet-or-anomaly dichotomy

## Status

Exact local boundary theorem, with its direct theta interpretation corrected
by `theta-relative-haar-coordinate-audit-identifies-the-constant-channel-defect.md`.
The endpoint and finite-part statements remain valid. However, the tail
condition at \(q=0\) maps to the sewing point \(x=1\), not the singular endpoint
\(x=0\). It therefore does not by itself solve the relative-Haar domain gate.

## Relative energy near the endpoint

The relative Haar form is

\[
\mathcal E(f)
=
\int_0^\infty|f(x)|^2\frac{dx}{x}.
\]

Suppose \(f\in H^1(0,1)\). If \(f(0)=0\), then

\[
|f(x)|^2
\le
x\int_0^x|f'(t)|^2\,dt.
\]

Consequently,

\[
\int_0^1|f(x)|^2\frac{dx}{x}
\le
\int_0^1(1-t)|f'(t)|^2\,dt
\le
\|f'\|_{L^2(0,1)}^2.
\]

Thus a regular state with zero endpoint trace lies in the relative form
domain near \(x=0\).

Conversely, if \(f\) is continuous and \(f(0)=a\ne0\), then

\[
\int_0^1|f(x)|^2\frac{dx}{x}=\infty.
\]

For regular states, endpoint trace zero is therefore the exact local
admission condition.

## Direct zero-state route

The source-derived tail construction has the schematic implication

\[
\Xi(s)=0
\quad\Longrightarrow\quad
L(s)f_s=0,
\qquad
\tau_0f_s=0.
\]

If \(\tau_0f_s=f_s(0)\) in the additive Haar coordinate and \(f_s\) has the
required first-order regularity, then

\[
f_s\in\operatorname{Dom}\mathcal E.
\]

No finite-part renormalization is needed on zero-states. The relative Green
identity could then use the strictly positive form directly:

\[
2\operatorname{Re}(s-1/2)\mathcal E(f_s)
=
\mathcal B(f_s).
\]

If the completed boundary supply vanishes, every nonzero zero-state is forced
to the critical seam.

The decisive typing question is whether the endpoint condition in the
rank-two tail system is the same trace as the singular endpoint of the
relative Haar inclusion. Equality of scalar formulas is insufficient; the
coordinate and domain maps must coincide.

## Finite-part branch

For a continuous state with \(f(0)=a\), introduce the truncated form

\[
\mathcal E_\varepsilon(f)
=
\int_\varepsilon^\infty|f(x)|^2\frac{dx}{x}.
\]

When the limit exists, define its scalar finite part by

\[
\mathcal E_{\mathrm{fp}}(f)
=
\lim_{\varepsilon\downarrow0}
\left(
\mathcal E_\varepsilon(f)
-
|a|^2\log\frac1\varepsilon
\right).
\]

Let

\[
(U_a(p)f)(x)=p^{1/2}f(px).
\]

Its endpoint value is \(p^{1/2}a\). Direct substitution gives

\[
\mathcal E_{\mathrm{fp}}(U_a(p)f)
=
p\mathcal E_{\mathrm{fp}}(f)
-
p|a|^2\log p.
\]

The second term is an exact boundary scale anomaly.

## The anomaly cannot itself be a positive energy

Iteration gives

\[
\mathcal E_{\mathrm{fp}}(U_a(p^k)f)
=
p^k
\left(
\mathcal E_{\mathrm{fp}}(f)
-
k|a|^2\log p
\right).
\]

For \(a\ne0\), the right-hand side becomes negative for sufficiently large
\(k\). Hence no scalar finite-part form with this covariance can be positive
on a dilation-invariant domain containing a nonzero endpoint state.

This is a no-go theorem. Subtracting the logarithmic divergence produces the
correct primitive increment \(\log p\), but it cannot be the missing positive
orientation law.

## Required boundary reservoir

If nonzero endpoint states must be retained, the endpoint value has to remain
an independent typed state component. Write an augmented state as

\[
(f,a,r),
\]

where \(r\) is boundary storage rather than a fitted counterterm. Its transport
must supply the opposite anomaly:

\[
\Delta\mathcal E_{\mathrm{boundary}}
=
p|a|^2\log p.
\]

Only the sum of bulk relative energy and source-derived boundary storage can
remain positive and covariant. Endpoint, primitive, square, and archimedean
currents are candidates for this reservoir, but their incidence and sign must
be derived before scalar completion.

## Interpretation of the primitive current

The same logarithmic weight now has two compatible meanings:

\[
\log p
=
\frac{d}{dk}\log p^k
\]

for relative metric transport, and it is the scale anomaly generated when a
nonzero endpoint trace is forced through the singular relative Haar form.

This does not yet identify the anomaly with the Euler primitive current. It
provides the exact coefficient and boundary type that such an identification
must match.

## Minimal falsifiers

The direct Dirichlet route fails if any of the following occurs:

1. the scalar zero imposes a different endpoint condition from \(f_s(0)=0\);
2. the zero-state lacks the regularity needed for relative-energy admission;
3. the state lies in the form domain but the relative Green residual is
   nonzero;
4. the completed boundary supply does not vanish.

The reservoir route fails if:

1. no independently typed boundary state carries the anomaly;
2. its transport increment has the wrong sign or coefficient;
3. the augmented form is not positive;
4. completion allows the boundary partner to escape.

## Verdict

The best route is now the direct one. A source zero already supplies an
endpoint condition; if that condition is exactly the Dirichlet trace of the
relative Haar operator, the singularity removes nonzero endpoint states while
admitting the zero-states needed for the RH argument. Renormalization is the
fallback, and scalar finite-part renormalization is proven insufficient.
