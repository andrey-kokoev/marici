# The prime state is Hilbertian but the Euler observer is necessarily singular

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator distinguished loss of meaning in a projection from loss of the
underlying Carrier.  The Schatten corridor makes this literal.  This packet
identifies the exact failed projection: the all-prime scalar observer is not
a bounded functional on the Hilbert space in which the prime state remains
well-defined.

## 1. The state survives in the open chamber

Let

\[
\mathcal H_p=\ell^2(\{\text{primes}\}),
\qquad
v_s=(p^{-s})_p.
\]

Then

\[
\|v_s\|^2=\sum_p p^{-2\operatorname{Re}s}<\infty
\]

exactly for

\[
\operatorname{Re}s>\frac12.
\]

Thus `v_s` is an honest vector throughout the distinguished right chamber.

## 2. The scalar observer is the all-ones covector

In the Euler region,

\[
\mathcal P_1(s)=\sum_p p^{-s}
\]

is formally the pairing

\[
\langle\mathbf1,v_s\rangle,
\qquad
\mathbf1=(1,1,\ldots).
\]

But

\[
\mathbf1\notin\mathcal H_p.
\]

For `Re(s)>1` the pairing exists because `v_s` happens to lie in `ell^1`.
When `Re(s)<=1`, that exceptional absolute convergence is lost even though
`v_s` remains in `ell^2` down to the critical seam.

Hence the anomaly corridor has the exact semantic typing

\[
\boxed{
\text{the state remains a valid Hilbert vector, while its scalar observer
has ceased to be continuous.}
}
\]

## 3. Bounded-observer no-go theorem

Suppose a bounded functional `Lambda` on `H_p` reproduced the primitive-prime
trace on the Euler domain:

\[
\Lambda(v_s)=\sum_p p^{-s}
\qquad(\operatorname{Re}s>1).
\]

By the Riesz theorem there would be `b=(b_p)_p in H_p` with

\[
\Lambda(v_s)=\sum_p\overline{b_p}\,p^{-s}.
\]

Uniqueness of absolutely convergent Dirichlet series on an open half-plane
then forces

\[
\overline{b_p}=1
\qquad\text{for every prime }p.
\]

This contradicts `b in ell^2`.  Therefore

\[
\boxed{
\text{no bounded observer on the prime Hilbert space can extend the Euler
linear trace.}
}
\]

This is an exact no-go, independent of RH.

## 4. Fock-space form

For `v in H_p`, the exponential vector in symmetric Fock space is

\[
\operatorname{Exp}(v)
=\bigoplus_{n\ge0}\frac{v^{\otimes n}}{\sqrt{n!}},
\]

with

\[
\langle\operatorname{Exp}(u),\operatorname{Exp}(v)\rangle
=e^{\langle u,v\rangle}.
\]

The chamber prime state therefore has a perfectly valid nonzero coherent
lift `Exp(v_s)`.  The Euler exponential would be

\[
e^{\sum_p p^{-s}}
=\langle\operatorname{Exp}(\mathbf1),
\operatorname{Exp}(v_s)\rangle,
\]

but `Exp(1)` does not exist in the same Fock representation because the
all-ones vector is not square-integrable.

So the exponentiated trace anomaly is an overlap with a distributional
boundary state, not an overlap of two ordinary coherent vectors.

## 5. What completion must do

The completed factor

\[
\mathcal T(s)
=\frac{2\pi^{s/2}\xi(s)}{s\Gamma(s/2)}
\det{}_2(I-P_s)
\]

continues

\[
(s-1)e^{\langle\mathbf1,v_s\rangle}.
\]

The factor `s-1` cancels the analytic singularity at the Euler boundary, but
it does not turn the all-ones covector into an element of `H_p`.  Completion
must instead construct a *relative observer* coupling:

\[
\text{singular prime covector}
+\text{endpoint continuum}
+\text{gamma/theta seam}.
\]

Only the combined functional may be meaningful.  None of its three pieces
is separately an authorized bounded readout in the anomaly corridor.

## 6. Why an honest coherent completion would prove too much

If the completed observer were independently realized as an ordinary
coherent vector `b_s in H_p` and

\[
\mathcal T(s)
=\langle\operatorname{Exp}(b_s),\operatorname{Exp}(v_s)\rangle,
\]

then `T(s)` would be an exponential and could never vanish.  This would prove
the right-chamber zero-free theorem.

But selecting `b_s` from `log T` is circular, and the bounded-observer no-go
shows that no fixed Hilbert vector can agree with the Euler trace.  A valid
construction must derive a relative or rigged-Fock boundary state from the
completed source and prove its overlap formula before using nonvanishing.

## 7. Meaning and integrality

The full integer-labelled prime state does not lose integrality at
`Re(s)=1`.  What fails there is the unlabelled scalar summation map.  The
quadratic labelled Carrier survives until `Re(s)=1/2`.

Thus the operator's proposed order is exact:

\[
\boxed{
\begin{array}{c}
\text{integer-labelled Hilbert state exists;}\\
\text{the all-label scalar projection becomes unbounded;}\\
\text{completion supplies a relative observation;}\\
\text{the quadratic Carrier itself ends at the fixed seam.}
\end{array}
}
\]

A zero is a failure of the completed relative observation, not a failure of
the underlying prime state.

## 8. Revised theorem target

Construct a source-derived rigged-Fock triple

\[
\mathcal E\subset\mathcal H_p\subset\mathcal E'
\]

together with a completed distributional observer

\[
\Omega_{\rm comp}(s)\in\mathcal E'
\]

whose pairing with `Exp(v_s)` is `T(s)` and whose modular sewing makes that
pairing a nonzero exponential or another manifestly nonvanishing relative
determinant.

The sharp falsifier is an uncancelled dependence on the prime cutoff or a
boundary state defined using `xi` itself rather than endpoint, gamma, and
theta source data.

## 9. Scope

The Hilbert-state domain, bounded-observer no-go, and coherent-vector formulas
are exact.  The completed rigged-Fock observer is conjectural.  Constructing
it with a manifestly nonzero overlap would prove the missing chamber theorem;
it has not been done, and RH is not proved.
