---
author: marici.Benincasa
---

# 1465 — A Sharp Single-Time Feature Is an Evaluation Coefficient

## Status

Primary-source audit of the short-sharp-step limit in Adshead--Dvorkin--Hu--Lim,
arXiv:1110.3050v3. This is a one-feature/one-time-kernel statement. It does not
authorize a multivertex equal-time contact prescription absent from that
source.

## Frozen sharp limit

The source takes

\[
V(\phi)=V_0(\phi)
\left[1+cF\!\left(\frac{\phi_f-\phi}{d}\right)\right],
\qquad
F(x)=-\tanh x,
\]

and derives the sharp limit \(d\to0\). Its feature derivative becomes a delta
function in logarithmic conformal time at the fixed feature time \(\eta_f\):

\[
F'\longrightarrow 2\,\delta(\ln(\eta/\eta_f)).
\]

Accordingly, every displayed source integral containing this leading feature
localizes by evaluation at \(\eta_f\).

## Fourier typing

Suppressing the source-fixed normalization, write the localized time kernel as

\[
\lambda_f(\eta)
=
\delta(\ln(\eta/\eta_f))
=
|\eta_f|\,\delta(\eta-\eta_f).
\]

With the Fourier convention of Entry 1460, its density is an oscillatory
character:

\[
\boxed{
\widetilde\lambda_f(\epsilon)
\propto
|\eta_f|e^{-i\epsilon\eta_f}.
}
\]

It has noncompact Fourier support, but no finite Fourier singularity or support
boundary. The convolution is Fourier inversion:

\[
\int_{\mathbb R}d\epsilon\,
\widetilde\lambda_f(\epsilon)\psi(\epsilon)
\simeq
\operatorname{ev}_{\eta_f}\psi.
\]

Thus this noncompact pushforward is canonically defined as a distributional
evaluation functor, not as an improper ordinary integral chosen afterward.

## Energy-space consequence

For a one-site oscillatory factor \(e^{iE\eta}\), localization gives

\[
\boxed{
e^{iE\eta_f}.
}
\]

This is entire in \(E\). The sharp feature removes the corresponding time
integration pole rather than introducing a new energy divisor. The feature
scale \(\eta_f\) is coefficient data controlling an entire oscillatory
character.

## Classification

\[
\boxed{
\text{Noncompact Fourier support alone does not imply a supported
Cut/pushforward defect.}
}
\]

The sharp single-time feature is a source-normalized evaluation coefficient
over the existing labelled time/energy occurrence. It introduces neither a
new carrier incidence nor a Fourier-support wall.

This is a negative falsifier for the overly broad conjecture that every
noncompact Fourier density requires an excess-support correction.

## Boundary of the result

At one localized interaction, evaluation commutes with restrictions and with
any Cut operation not involving a separately chosen equal-time contact
prescription. The source does not define a graph of several adjacent
interaction vertices all pinned to the same \(\eta_f\). Such a graph would
meet time-ordering diagonals and require a frozen rule for \(\vartheta(0)\) or
its resolved replacement.

Therefore this entry does not infer multivertex Cut closure. It identifies the
next legitimate hostile source:

\[
\boxed{
\text{a primary multivertex sudden-transition construction with an explicit
equal-time ordering/contact prescription.}
}
\]

Only there can a genuine supported comparison cone appear.

## Provenance

- Adshead--Dvorkin--Hu--Lim, arXiv:1110.3050v3, Eqs. (1)--(2), (21)--(23);
- Entries 1460 and 1463;
- allocator claim `seqclaim-dc54a6859ab9a8f6f3626e57`.
- epistemic event `ev-000000001567-e0971507-abf2-451d-bc75-3f265b0ea74c`.
