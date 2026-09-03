# Endpoint-corrected remainder form is nonclosable in the order topology

## Correction

The previous version reversed the nonclosability disposition. Decomposing one form into two nonclosable pieces does not show the sum is nonclosable; their singular residuals may cancel. Using the sourced decay \(H(t)\to0\) determines the correct direction.

## Question

Which algebraic source form fails closability in the order topology: the decaying completed-heat difference or the endpoint-corrected remainder localizer?

## Claim boundary

The endpoint-corrected remainder form is nonclosable, with an explicit null sequence. The raw completed-heat difference tends to zero on that sequence, so this argument does not decide its closability. Therefore the source-positive order completion cannot be the common form domain for the remainder-localizer cone.

## Kernels

Let

\[
K_H(a,b)
=
H(a+b)-H(a+b+h)
\]

and

\[
H_R(t)=H(t)-e^{t/4}.
\]

The remainder-localizer kernel is

\[
\begin{aligned}
K_R(a,b)
&=H_R(a+b)-H_R(a+b+h)\\
&=K_H(a,b)
+(e^{h/4}-1)e^{(a+b)/4}.
\end{aligned}
\]

Thus the remainder form adds a positive endpoint rank-one term to the decaying completed-heat form.

## Null sequence

Let \(g_a\) be the Gaussian Riesz vector and set

\[
f_a=e^{-a/4}g_a.
\]

The order estimate gives

\[
\lVert f_a\rVert_{\rm ord}
\longrightarrow0.
\]

The endpoint evaluation satisfies

\[
L_E(f_a)=1,
\qquad
L_E(f_a-f_b)=0.
\]

For the raw completed-heat part,

\[
q_H(f_a)
=
e^{-a/2}
\bigl[H(2a)-H(2a+h)\bigr]
\longrightarrow0
\]

because \(H(t)\to0\). The mixed values in \(q_H(f_a-f_b)\) also tend to zero as both parameters tend onward.

For the remainder form,

\[
q_R(f_a)
=
q_H(f_a)+(e^{h/4}-1)
\longrightarrow
e^{h/4}-1.
\]

Meanwhile,

\[
q_R(f_a-f_b)
=
q_H(f_a-f_b)
\longrightarrow0
\]

because the endpoint functional cancels on differences.

Hence \((f_a)\) is base-null and form-Cauchy for \(q_R\), but its form value tends to a nonzero constant. The remainder form is not closable.

## Consequence

The exact endpoint correction is forced if one wants the remainder-localizer moments, but that same correction creates a singular feature line relative to the order topology. Therefore the order completion cannot carry the remainder-localizer form as a closable extension.

This rules out

`H_ord as common_closed_form_domain for K_R`.

It does not rule out a stronger source-derived topology in which endpoint evaluation is continuous, nor does it prove closability of \(K_H\).

## Revised coherencer interpretation

The endpoint line is not a removable defect when the target is the remainder-localizer cone; it is part of that target. Removing it returns to the raw completed-heat form and changes the positivity problem. The required higher coherencer must therefore strengthen the domain rather than subtract the endpoint again.

## Disposition

`endpoint_corrected_remainder_form_closability_on_H_ord` fails. The first missing object returns to a stronger common closed-form domain that continuously controls both the order norm and endpoint evaluation. RH is not implied.

## Verification

- `research/voevodsky/checkers/check_endpoint_form_nonclosability.py`
- `research/voevodsky/results/endpoint_form_nonclosability.json`
