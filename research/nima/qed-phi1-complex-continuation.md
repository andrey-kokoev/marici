# The same boundary jet completes the complex \(\Phi_1\) slice

Owner: marici.Nima

The exact source implementation originally charts the physical Region I--III
\(w,z\) branches only on their real boundary. We continued each algebraic
root into the upper half-plane by proximity to its certified real anchor.
The lower sheet is not obtained by feeding lower-half arguments into the same
principal GPL formulas; it is supplied by the source real structure

\[
\Phi_1(\bar s,T)=\overline{\Phi_1(s,T)}.
\]

At \(T=-1/4\), the subtraction coefficients were retained unchanged from the
real two-point fit. No complex datum was fitted.

The two hostile upper-half points were

\[
s=1.1+0.02i,
\qquad
s=1.7+0.03i.
\]

The coupled Cut reconstruction differs from the independent continued exact
amplitude by relative residuals

\[
6.24\times10^{-7},
\qquad
1.47\times10^{-6}.
\]

The continued formula returns to the certified real implementation with
absolute residual

\[
3.08\times10^{-22}.
\]

## Result

The residual

\[
\Phi_1-D-a(T)-b(T)\nu
\]

vanishes to the same numerical scale on real and complex points. Thus the
tested analytic domain contains:

- no additional polynomial subtraction direction;
- no detected inner/CDD factor;
- no missing complex branch contribution.

The branch audit also catches a typing hazard: direct principal evaluation of
the closed GPL expressions in the lower half-plane does not implement the
physical lower sheet. Schwarz reflection is part of the source branch
contract.

This closes the hostile-point gate for the \(\Phi_1\) crossing pair. The
remaining vector problem is to repeat the construction for the
\(\Phi_2,\Phi_5\) channels and then assemble the channel-level residual.

Reproduce with
uv run --with numpy --with mpmath python
research/nima/checkers/check_qed_phi1_complex_continuation.py.

