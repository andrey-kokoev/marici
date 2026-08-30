# 1510 — Exact de Sitter NPH Transport Produces an Infinite Derivative Tail

## Status

Exact free-field calculation closing the finite-order part of Entry 1508's falsifier.

## Frozen conventions

On de Sitter space let

\[
x=-k\eta_0=\frac{k}{a_0H}>0.
\]

Use the Bunch–Davies basis from Danielsson,

\[
u_k(\eta)
=
\frac{e^{-ik\eta}}{\sqrt{2k}}
\left(1-\frac{i}{k\eta}\right).
\]

At the common slice,

\[
u_k(t_0)
=
\frac{e^{ix}}{\sqrt{2k}}
\left(1+\frac{i}{x}\right).
\]

The boundary normal derivative convention of Greene et al. is

\[
\partial_n
=
H\frac{\partial}{\partial\ln a}
=
-H\eta\partial_\eta
=
-Hx\partial_x.
\]

For a Bogoliubov coefficient \(b\), the exact transported kernel is

\[
\kappa_b
=
-
\frac{\partial_nu_k+b\,\partial_nu_k^*}
{u_k+b\,u_k^*}.
\]

## Exact kernel

Define

\[
z=b\,e^{-2ix}.
\]

Direct differentiation gives

\[
\boxed{
\frac{\kappa_b}{H}
=
x\,
\frac{
\left(i-x^{-1}-ix^{-2}\right)
+
z\left(-i-x^{-1}+ix^{-2}\right)
}{
\left(1+ix^{-1}\right)
+
z\left(1-ix^{-1}\right)
}.
}
\]

The Bunch–Davies kernel is the \(z=0\) specialization. For every nonzero NPH excitation \(b\), the correction

\[
\delta\kappa_b=\kappa_b-\kappa_{\rm BD}
\]

is a nonconstant rational function of

\[
e^{-2ix}
=
\exp\!\left(-\frac{2ik}{a_0H}\right).
\]

## Finite-order obstruction

A finite local quadratic boundary action contributes a finite polynomial in spatial derivatives, hence—after Fourier transform—a finite polynomial in \(k^2/a_0^2\), with background-dependent coefficients.

No such polynomial can equal the displayed nonconstant Möbius function of \(e^{-2ik/(a_0H)}\) on an open momentum interval. Therefore

\[
\boxed{
b\neq0
\quad\Longrightarrow\quad
\kappa_b
\text{ has no exact finite local derivative-EFT representation.}
}
\]

Equivalently, transporting a nontrivial NPH state to one common slice generates an infinite derivative tail.

This conclusion already holds in exact de Sitter space, where \(b_{\rm NPH}\) can be independent of \(k\). Slow-roll dependence of \(H(k)\) adds further non-polynomial structure but is not needed for the obstruction.

## Pole typing

The denominator

\[
\left(1+ix^{-1}\right)
+
b e^{-2ix}\left(1-ix^{-1}\right)
\]

may vanish at isolated complex momenta. These are poles of the scalar boundary-kernel chart obtained by dividing by the field value \(u_k+b u_k^*\). They are not automatically new carrier support or singularities of the underlying two-dimensional solution line.

Thus:

\[
\text{kernel-chart pole}
\not\Rightarrow
\text{new physical divisor}.
\]

The invariant object is the projective solution line, or equivalently the undivided boundary relation

\[
\bigl(\partial_n+\kappa_b\bigr)v_k=0.
\]

## Consequence

The smallest common coefficient envelope is not the finite local boundary-operator algebra. It must retain either:

- the full Bogoliubov/projective solution line; or
- a completed pseudodifferential/infinite-jet boundary kernel.

Local BEFT is a finite-jet subobject. NPH is regular in the projective solution-line presentation but generally infinite-jet on a fixed spacetime boundary.

## Remaining falsifier

Determine whether the infinite derivative expansion is a controlled completion:

1. compute its Taylor/asymptotic coefficients in \(p_0/M\);
2. determine radius and domain of convergence;
3. identify whether kernel-chart poles obstruct the completed operator or disappear under projective gluing;
4. test compatibility with interacting boundary renormalization.

The finite-order closure question is settled negatively; all-order analytic or resurgent closure remains open.

## Provenance

- U. H. Danielsson, *A note on inflation and transplanckian physics*, arXiv:hep-th/0203198, Eq. (20).
- B. Greene, K. Schalm, J. P. van der Schaar, and G. Shiu, *Extracting New Physics from the CMB*, arXiv:astro-ph/0503458, Eqs. (1), (7)–(8).
- Ledger sequence claim: seqclaim-8471aa2b8bf1f7fc28e198fe.
- Epistemic graph event: ev-000000001639-46185905-8b1f-454d-99da-f96839e7da62.
