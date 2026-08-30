# Local dilation transports the odd character frame while preserving its Weyl phase

## Additive dilation

For \(a\in\mathbb Q_p^\times\), use the unitary additive dilation

\[
(\mathcal D_a f)(x)
=
|a|_p^{1/2}f(ax)
\]

on \(L^2(\mathbb Q_p)\).

With

\[
(T_hf)(x)=f(x+h),
\qquad
(M_\eta f)(x)=\psi_p(\eta x)f(x),
\]

direct conjugation gives

\[
\mathcal D_aT_h\mathcal D_a^{-1}
=
T_{h/a}
\]

and

\[
\mathcal D_aM_\eta\mathcal D_a^{-1}
=
M_{a\eta}.
\]

Therefore the Weyl pairing is invariant:

\[
(a\eta)\left(\frac h a\right)=\eta h.
\]

## Comoving compact-open support

Let \(B\subset\mathbb Q_p\) be a compact-open additive lattice and define

\[
f_{\eta,B}(x)
=
\psi_p(\eta x)\mathbf 1_B(x).
\]

Then

\[
\mathcal D_af_{\eta,B}
=
|a|_p^{1/2}
f_{a\eta,a^{-1}B}.
\]

The character conductor and support lattice move contragrediently.

For the antisymmetric pair,

\[
f_{\eta,B}^{\mathrm{odd}}
=
\frac{
f_{\eta,B}-f_{-\eta,B}
}{2i},
\]

we obtain

\[
\mathcal D_a f_{\eta,B}^{\mathrm{odd}}
=
|a|_p^{1/2}
f_{a\eta,a^{-1}B}^{\mathrm{odd}}.
\]

Thus local dilation preserves odd parity while transporting the phase frame.

## Parity-changing finite difference

Define

\[
P_{\eta,h}
=
T_h-T_{-h}.
\]

Conjugation gives

\[
\mathcal D_aP_{\eta,h}\mathcal D_a^{-1}
=
P_{a\eta,h/a},
\]

where the first label records the comoving character frame.

If

\[
P_{\eta,h}f_{\eta,B}^{\mathrm{odd}}
=
2\sin(\theta)
f_{\eta,B}^{\mathrm{even}}
\]

with

\[
\psi_p(\eta h)=e^{i\theta},
\]

then the transported relation has the same coefficient because \(\eta h\) is invariant.

Hence Adams-scale dilation does not intrinsically worsen the local odd margin. The \(p^{-1}\) phase coefficient comes from the canonical residue choice, not from repeated grade transport.

## A second Adams type functor

There are now two lawful odd type constructions.

### Fixed observer frame

Keep \((\eta,B)\) fixed and let Adams act only on the external grade label. This gives the strict tensor-product subfunctor constructed previously.

### Comoving additive frame

Let the Adams scale arrow carry a local dilation \(a_{r,k}\) and transport

\[
(\eta,B,h)
\longmapsto
(a_{r,k}\eta,a_{r,k}^{-1}B,h/a_{r,k}).
\]

If the scale factors compose,

\[
a_{s,rk}a_{r,k}=a_{sr,k},
\]

then the dilation maps form an exact type functor:

\[
\mathcal D_{a_{s,rk}}
\mathcal D_{a_{r,k}}
=
\mathcal D_{a_{sr,k}}.
\]

The Weyl phase is unchanged along every path.

## Grade-six coherence

For the diamond \(1\to2\to6\) and \(1\to3\to6\), the two comoving phase frames agree exactly when

\[
a_{3,2}a_{2,1}
=
a_{2,3}a_{3,1}
=
a_{6,1}.
\]

Then both paths transport:

\[
\eta\mapsto a_{6,1}\eta,
\qquad
B\mapsto a_{6,1}^{-1}B,
\qquad
h\mapsto h/a_{6,1}.
\]

Thus the additive conductor supplies no additional associator defect beyond the multiplicative scale cocycle.

## Fourier covariance

Under the self-dual Fourier convention, dilation satisfies the contragredient law

\[
\mathcal F_p\mathcal D_a
=
\mathcal D_{a^{-1}}\mathcal F_p
\]

up to the frozen convention for unitary normalization.

Therefore the comoving type functor has an explicit Fourier naturality target. The reciprocal chart must use inverse scale transport.

This is stronger than the fixed observer frame, where Fourier–dilation comparison remains external.

## Source decision still required

The two functors are not the same presentation:

- fixed frame treats the odd port as a stationary observer attached to changing multiplicative grades;
- comoving frame treats it as part of the locally dilated state.

A source theorem must decide which role the odd port plays in the complete boundary system.

They may be related by a natural transformation, but that comparison must carry the changing support lattice and conductor.

## Completion implications

Each \(\mathcal D_a\) is unitary on the local additive Hilbert space. Therefore the comoving type transport adds no local condition-number growth.

The only all-prime softness remains the initial phase coefficient

\[
2\sin\left(\frac{2\pi}{p}\right).
\]

Repeated Adams composition does not multiply that coefficient when the phase port is transported as one comoving frame.

## Hostiles

1. Transport \(\eta\) without transporting \(h\) contragrediently.
2. keep the support lattice fixed while calling the action local dilation.
3. multiply the sine loss at every Adams stage.
4. identify fixed and comoving phase frames without a natural transformation.
5. use the Fourier covariance law without reciprocal inverse dilation.

## Verdict

Local additive dilation gives a canonical comoving Adams transport for the odd character fiber:

\[
(\eta,B,h)
\mapsto
(a\eta,a^{-1}B,h/a).
\]

It preserves the Weyl phase exactly and passes the grade-six coherence gate whenever the scale cocycle composes. The remaining choice is whether the RH odd port is a fixed observer or a comoving state.
