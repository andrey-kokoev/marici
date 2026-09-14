# Translation-coherent oriented mesh factorization is exactly circle positivity

Suppose an oriented positive-cell carrier represents translated primitives by

\[
\Phi_a(\alpha)=s_a(\alpha)\sqrt{c_\alpha},
\qquad c_\alpha>0.
\]

Forward/reverse translation coherence requires

\[
s_{a+b}(\alpha)=s_a(\alpha)s_b(\alpha),
\qquad
s_{-a}(\alpha)=\overline{s_a(\alpha)}.
\]

Thus each cell phase is a unitary character. On an equally spaced circle packet,

\[
s_m(\alpha)=e^{im\theta_\alpha}.
\]

The kernel factorization becomes

\[
\boxed{
K((i-j)h)
=
\sum_\alpha c_\alpha e^{i(i-j)\theta_\alpha}.
}
\]

More generally, the sum is an integral against a positive circle measure.

This immediately gives

\[
\sum_{i,j}\overline{z_i}z_jK((i-j)h)
=
\sum_\alpha c_\alpha
\left|\sum_i z_i e^{ii\theta_\alpha}\right|^2
\geq0.
\]

Conversely, Herglotz positivity of the circle moments supplies exactly such a positive measure and phase-character realization.

Therefore

\[
\boxed{
\text{translation-coherent oriented positive mesh carrier}
\iff
\text{positive circle pushforward}.
}
\]

## Interpretation

Orientation successfully explains how negative cross-pairings coexist with positive diagonal energy. Translation and reversal force the phases into the correct character form.

But the remaining requirement

\[
c_\alpha\geq0
\]

is precisely the original circle-positivity gate. The oriented mesh does not independently prove it; it is the Fourier feature realization that exists once positivity holds.

For the RH programme, a noncircular construction must derive the positive weights directly from the coupled endpoint--gamma--prime source. Recovering them by Herglotz, spectral decomposition, Cholesky, or assumed Gram positivity merely reconstructs the desired carrier after solving the gate.

## Verification

```text
python research/voevodsky/checkers/check_oriented_mesh_factorization_is_positive_Fourier_measure.py
```

Artifacts:

- `research/voevodsky/checkers/check_oriented_mesh_factorization_is_positive_Fourier_measure.py`
- `research/voevodsky/results/oriented_mesh_positive_Fourier_factorization.json`
