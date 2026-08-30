# 3612 — The Continuous Autocorrelation Half-Form Preserves Strict Radial Faithfulness after Completion

For a real completed source with integrable autocorrelation `C`, define

\[
A(z)=\frac{C(0)}2+int_0^\infty C(d)e^{zd}\,dd.
\]

In the left half-plane, `A` is bounded analytic and its boundary real part is
`|X(it)|^2/2`. The Poisson formula therefore gives strict positive real part
throughout the open half-plane.

At a zero of the bilateral transform,

\[
X(z)X(-z)=A(z)+A(-z)=0,
\]

so the oriented current `J=A(z)-A(-z)` equals `2A(z)` on the left and
`-2A(-z)` on the right. Its normal component has strict sign off the seam.

Thus radial faithfulness survives infinite-source completion pointwise; it
does not require a uniform finite-truncation lower bound. The sole remaining
RH-bearing gate is a source-derived polarization identity forcing zero normal
current at every completed theta zero-state.

Checker result: `24/24 contract and exact-regression gates passed`.

Artifact:
`research/grothendieck/the-continuous-autocorrelation-half-form-preserves-strict-radial-faithfulness-after-completion.md`.

