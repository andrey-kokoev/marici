# Primitive boundary flux needs a weighted scale-energy law

## The circular bound to reject

After subtracting the continuum mean, the primitive logarithmic connection has the Mellin form

\[
J(s)=s\int_1^\infty (\psi(x)-x)x^{-s-1}\,dx
\]

where initially justified and then continued. Directly requiring this integral to be controlled throughout \(\operatorname{Re}s>1/2\) is equivalent in strength to the desired prime-counting estimate. It renames the analytic problem.

The source-derived target must instead be an operator energy law whose boundary readout is \(\psi-x\).

## Scale coordinate

Set

\[
t=\log x,
\qquad
e(t)=e^{-t/2}\bigl(\psi(e^t)-e^t\bigr).
\]

Here \(t\) is logarithmic scale, not physical time. Then

\[
\frac{J(s)}{s}
=\int_0^\infty e(t)e^{-(s-1/2)t}\,dt.
\]

Thus the primitive completion problem is a Laplace transform of a centered, critically rescaled boundary flux.

## Sufficient energy estimate

Suppose a source-derived finite system produces fluxes \(e_X(t)\) and proves, for every \(\varepsilon>0\), a cutoff-independent estimate

\[
\int_0^\infty |e_X(t)|^2e^{-2\varepsilon t}\,dt
\le C_\varepsilon.
\]

For \(s=1/2+\delta+i\tau\), Cauchy–Schwarz gives

\[
\left|\int_0^\infty e_X(t)e^{-\delta t}e^{-i\tau t}\,dt\right|
\le
\left\|e_Xe^{-\delta t/2}\right\|_2
\left\|e^{-\delta t/2}\right\|_2.
\]

Hence

\[
\left|\frac{J_X(s)}{s}\right|
\le
\sqrt{\frac{C_{\delta/2}}{\delta}}.
\]

The same estimate on compact subsets, together with source convergence of the fluxes, yields a holomorphic completed primitive connection in the open right sector.

## What the conservation law must supply

The weighted estimate is useful only if it follows from a prior source system. A valid constructor must provide:

1. a labelled state and flux before scalar prime counting;
2. a local scale-divergence or Green identity;
3. a positive bulk energy and typed boundary terms;
4. the exact readout identifying the centered boundary flux with \(\psi-x\);
5. cutoff-independent weighted estimates;
6. convergence in a topology strong enough to pass the flux identity to completion;
7. reciprocal transport of the corresponding left-sector law.

Defining the state from \(\psi-x\), from \(\zeta'/\zeta\), or from zero locations fails source independence.

## Candidate doubled law

The existing doubled Clark–Green system is a plausible carrier because its finite bulk is already a positive Gram form and its unresolved content lies in typed boundary currents. The precise test is whether its primitive boundary component equals the centered flux and whether the positive bulk controls the weighted scale norm above.

This is not automatic. Feature-space positivity does not imply observability of the primitive boundary state, and finite positivity does not give a cutoff-independent estimate.

## Finite falsifier

At every cutoff and damping parameter, compile the quadratic estimate

\[
\|e_Xe^{-\varepsilon t}\|_2^2
\le C_\varepsilon\mathcal E_X
\]

from the source Gram energy \(\mathcal E_X\). Reject the law if:

- a nonzero primitive flux lies in the energy kernel;
- the sharp domination constant grows with the cutoff;
- the boundary readout differs from the exact primitive current;
- the endpoint or archimedean term is silently discarded;
- a hostile signed prime source satisfies the same estimate without the source grammar.

Passing this gate would provide an independent analytic mechanism. Failing it confirms that the proposed conservation law merely repackages the RH-equivalent primitive current.

