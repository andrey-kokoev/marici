# The Hardy support convention selects the upper resolvent boundary and fixes the Green jump sign

Use the self-adjoint history generator

\[
T=-i\partial_q
\]

and write its resolvent as `(T-z)^(-1)`.  The source-declared positive-support
Paley--Wiener branch is holomorphic for `Im z>0`; it is the causal branch.  The
lower branch is its adjoint/reflection, not an independently selectable state.

For the sandwiched spectral density `G(lambda)=beta(lambda)^*beta(lambda)`, the
standard distribution identity gives

\[
R_+(\lambda)
=B^\dagger(T-(\lambda+i0))^{-1}B
=\operatorname{PV}\int\frac{G(\xi)}{\xi-\lambda}\,d\xi
+i\pi G(\lambda),
\]

and

\[
R_-(\lambda)=R_+(\lambda)^*
=\operatorname{PV}\int\frac{G(\xi)}{\xi-\lambda}\,d\xi
-i\pi G(\lambda).
\]

Hence

\[
R_+(\lambda)-R_-(\lambda)=2\pi iG(\lambda),
\qquad
\operatorname{Im}R_+(\lambda)=\pi G(\lambda)\ge0.
\]

This sign is fixed by causal support and the convention `T=-i partial_q`.
Writing the skew generator `partial_q` instead moves the factor `i` into the
parameter and must not be interpreted as a second physical choice.

The strict diagonal Euler inverse preserves existence of both boundary values.
This closes the local Green-side selection and jump normalization. It does not
prove that reciprocal feedback glues their Fredholm determinant frames to the
completed Xi line; that is a global two-sided sewing statement.
