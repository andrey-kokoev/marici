# The Euler odd port cannot be restricted to the completed-theta odd line before source incidence

## Correction

The Wronskian and seam-normal observers both act on the analytic completed-theta odd line

\[
\mathcal O_\Phi=\mathbb C\Phi'.
\]

The reciprocal Euler odd current does not. It lives in the prime-power coefficient dual.

Therefore the proposed next operation,

\[
J_{\mathrm{Euler}}|_{\mathcal O_\Phi},
\]

is undefined until a source incidence map is supplied.

The three-port calibration is a mate-square theorem between towers, not equality of three functionals on one pre-existing vector space.

## The three objects

Keep the following spaces distinct:

1. \(\mathcal E_\theta\): the theta source test space;
2. \(\mathcal E_\theta'\): the Euler current space;
3. \(\mathcal H_{\mathrm{tail}}\): the analytic Green/tail graph space.

The completed theta odd forcing belongs to

\[
\Phi'\in\mathcal E_\theta.
\]

For each prime \(p\), the reciprocal Euler odd current is a functional

\[
\nu_p^{\mathrm{Euler}}\in\mathcal E_\theta'
\]

after the source sampling theorem. Its intrinsic coefficient is

\[
h_p^{\mathrm{Euler}}
=
\frac{(\log p)p^{-1/2}}{1-p^{-1/2}}.
\]

The analytic Wronskian and seam-normal ports act only after the theta forcing has propagated into the analytic tail/Jacobi realization.

## Authorized scalar incidence

The only canonical arithmetic-to-theta contraction is evaluation:

\[
B_{\Phi'}^\times:
\mathcal E_\theta'
\longrightarrow
\mathbb C,
\qquad
B_{\Phi'}^\times(\nu)=\nu(\Phi').
\]

The forward source incidence is

\[
B_{\Phi'}:
\mathbb C
\longrightarrow
\mathcal E_\theta,
\qquad
B_{\Phi'}(c)=c\Phi'.
\]

Thus an Euler current can influence the analytic odd line only through

\[
\nu_p^{\mathrm{Euler}}
\longmapsto
\nu_p^{\mathrm{Euler}}(\Phi')
\longmapsto
\nu_p^{\mathrm{Euler}}(\Phi')\Phi'
\longmapsto
\text{analytic propagation}.
\]

There is no authorized direct equation between \(h_p^{\mathrm{Euler}}\) and \(\Phi''(0)\).

## The calibrated analytic leg

On \(\mathcal O_\Phi\), the two analytic observers satisfy

\[
J_{\mathrm N}
=
c_{\mathrm{N/Wr}}J_{\mathrm{Wr}},
\qquad
c_{\mathrm{N/Wr}}=-2\Phi''(0)>0.
\]

For a scalar incidence value

\[
c_p=B_{\Phi'}^\times(\nu_p^{\mathrm{Euler}}),
\]

the propagated source vector is \(c_p\Phi'\), and hence

\[
J_{\mathrm{Wr}}(c_p\Phi')
=
-\frac12c_p,
\]

\[
J_{\mathrm N}(c_p\Phi')
=
c_p\Phi''(0).
\]

This is the exact analytic output once the arithmetic incidence scalar \(c_p\) is known.

## What must be compared

The arithmetic Euler coordinate \(h_p^{\mathrm{Euler}}\) and the incidence scalar \(c_p\) are different typed quantities. A source theorem may relate them,

\[
c_p=\eta_p h_p^{\mathrm{Euler}},
\]

but the coefficient \(\eta_p\) must be derived from the theta sampling packet. It cannot be set to one by identifying the two towers.

If such a theorem holds, then

\[
J_{\mathrm{Wr}}(c_p\Phi')
=
-\frac{\eta_p}{2}h_p^{\mathrm{Euler}},
\]

and

\[
J_{\mathrm N}(c_p\Phi')
=
\eta_p\Phi''(0)h_p^{\mathrm{Euler}}.
\]

These are the correctly typed three-port calibration formulas.

## Reciprocal mate square

Let \(\mathcal R_E\) be reciprocal transport on Euler currents, \(\mathcal R_\theta\) reciprocal transport on theta forcing, and \(\mathcal R_A\) the analytic reciprocal sewing.

The required constructor theorem is commutativity, up to the declared comparison cell, of

\[
\begin{array}{ccc}
\mathcal E_\theta' & \xrightarrow{B_{\Phi'}^\times} & \mathbb C\\
\downarrow\mathcal R_E && \downarrow\chi_{\mathrm{odd}}\\
\mathcal E_\theta' & \xrightarrow{B_{\mathcal R_\theta\Phi'}^\times} & \mathbb C,
\end{array}
\]

followed by the analytic propagation square into the Wronskian/seam-normal line.

Scalar equality after erasing the two intermediate towers is insufficient. The mate square must preserve:

- prime and grade labels;
- reciprocal orientation;
- cutoff restriction;
- wall versus positive-label splitting;
- the source half-density metric;
- the chosen normal and Wronskian sign frames.

## Granularity

The full local Euler coefficient contains every grade:

\[
h_p^{(\infty)}
=
\frac{(\log p)p^{-1/2}}{1-p^{-1/2}}.
\]

A strict primitive-square cell contains only

\[
h_p^{(1,2)}
=
(\log p)(p^{-1/2}+p^{-1}).
\]

Therefore the incidence scalar must be computed at the same granularity as the target analytic packet. If the completed all-grade current is used, the connected tail must propagate through its own source channel before compression. Directly attaching \(h_p^{(\infty)}\) to a two-endpoint analytic line repeats the earlier granularity defect.

## Exact next calculation

The next source theorem is not “evaluate the Euler port on \(\mathcal O_\Phi\).” It is:

> Compute \(B_{\Phi'}^\times(\nu_p^{\mathrm{Euler}})\) from the source sampling formula, separately for the strict grades \(1,2\) and the connected tail, and prove the reciprocal mate square before analytic scalarization.

Only then can the Euler, Wronskian, and seam-normal outputs be compared by source-derived nonzero coefficients.
