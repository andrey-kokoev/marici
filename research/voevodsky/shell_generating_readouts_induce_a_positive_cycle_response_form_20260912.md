# Shell-generating readouts induce a positive cycle response form

## Question

Once the countable shell-generating probes are jointly faithful, what positive form do their responses induce on route residue?

## Claim boundary

The damped direct-sum readout canonically induces a positive definite response form after the probe parameters and channel weights are fixed. It satisfies reciprocity and presentation independence. It becomes a physical covariance or Fisher metric only if those probes and their noise normalization are physically implemented.

## Countable response form

Use

\[
t_n=\frac12+\frac1{n+3},
\qquad
\alpha_n=2^{-n-1},
\qquad
A_n=BD_{t_n},
\]

where \(D_t(e)=t^{j(e)}\). Define on the completed cycle space

\[
Q_{\rm resp}(z,w)
=
\sum_{n\geq0}\alpha_n^2
\langle A_nz,A_nw\rangle_{\mathcal H}.
\]

The uniform history bound for \(|t_n^{j(e)}|\leq1\), together with

\[
\sum_{n\geq0}\alpha_n^2=\frac13,
\]

makes this series absolutely bounded by one projective source seminorm in each argument.

## Positivity

For every \(z\),

\[
Q_{\rm resp}(z,z)
=
\sum_n\alpha_n^2\|A_nz\|^2
\geq0.
\]

If it vanishes, each \(A_nz=0\). Joint faithfulness of the generating family then gives \(z=0\). Thus \(Q_{\rm resp}\) is positive definite on route residue.

This is stronger than assigning arbitrary diagonal edge weights: the form is the pullback of declared differential history readouts.

## Coherence

The definition is made on the invariant cycle subspace, not in one forest coordinate system. Under a forest change \(z=F_Tu=F_Uv\), both coordinate Gram matrices represent the same form and obey congruence. Reciprocal exchange preserves shell index and acts isometrically on every history target, hence preserves \(Q_{\rm resp}\).

Cutoff restrictions are compatible because every finite form is obtained by restricting the same completed probe family.

## Noise-weighted form

If measured channel noise is a positive operator \(N\) on the readout direct sum, the Fisher form is

\[
Q_N(z,w)
=
\langle\mathcal Az,N^{-1}\mathcal Aw\rangle.
\]

It is positive definite when \(N^{-1}\) is positive and nonsingular on the response range. Correlated noise is allowed; diagonal independent noise is not assumed.

## Remaining authority boundary

The mathematical response form is now complete. Its physical interpretation requires three measured arrows:

1. the actual intervention implements \(t^j\) on shell-labelled source channels;
2. the recorded output is the declared differential common-history readout;
3. the operator \(N\) is the measured joint noise covariance for those channels.

Changing \((t_n,\alpha_n)\) changes \(Q_{\rm resp}\). Joint faithfulness alone does not select these values. A uniform integral over \(t\), a geometric sequence, and another accumulating sequence generally yield inequivalent forms.

## Disposition

A positive, reciprocal, presentation-independent cycle response form has been constructed from a specified measurement design. This closes the mathematical covariance construction conditionally on that design. Physical covariance remains exactly the calibration and authority question above.
