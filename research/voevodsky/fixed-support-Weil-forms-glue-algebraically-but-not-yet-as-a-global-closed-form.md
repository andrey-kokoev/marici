# Fixed-support Weil forms glue algebraically but not yet as a global closed form

## Local theorem

For each finite support radius \(L\), let \(\mathcal H_{\log,L}\) be the zero-extended logarithmic Fourier graph domain supported in \([-L,L]\).

On this domain the completed form has three controlled pieces:

- endpoint functionals are bounded because support is fixed;
- the gamma multiplier is controlled by the logarithmic Fourier norm;
- only prime translations with \(\log n\leq2L\) contribute.

The prime sum is therefore finite. The completed form is continuous, hence closed as a bounded form relative to the declared graph norm, on every fixed window.

## Compatibility

If \(L<L'\), extend a function by zero from the smaller window to the larger one. For a translation distance greater than \(2L\), the function and its translate have disjoint support. Hence every newly admitted prime term vanishes on the old vector.

Therefore the local forms agree under zero extension. They define a well-defined form on the algebraic union

\[
\mathcal D_c=
\bigcup_{L>0}\mathcal H_{\log,L}.
\]

This supplies an exact compact-support source domain rather than merely unrelated finite cutoffs.

## Global obstruction

The elementary prime bound on the radius-\(L\) window contains

\[
C_L=
\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}.
\]

These constants grow with \(L\). Thus local boundedness does not provide a uniform global form bound, a common lower bound, or closability in a single Hilbert completion.

This is the same distinction as local triviality versus global transport in the geometric model: compatible local data exist, but a global completion requires control of the transition to arbitrarily large windows.

## Disposition

The common-domain gate is now partially inhabited:

- fixed-window closed forms: constructed;
- compatibility under zero extension: proved;
- algebraic compact-support inductive-limit form: constructed;
- one global closable semibounded Hilbert form: still open.

The next analytic gate is not another finite-window calculation. It is a source-derived global estimate that controls the joint gamma-prime form uniformly in the expanding-support topology, allowing cancellation before separate absolute-value bounds are taken.

## Verification

```text
python research/voevodsky/checkers/check_local_weil_window_compatibility.py
```

The checker verifies 510 exact zero-extension cases. It also records the increasing prime coefficient majorants for five support radii.

Artifacts:

- `research/voevodsky/checkers/check_local_weil_window_compatibility.py`
- `research/voevodsky/results/local_weil_window_compatibility.json`
