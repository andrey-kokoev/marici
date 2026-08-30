# The comoving window kernel is the source-derived arithmetic endpoint comparison

## Result

The missing arithmetic endpoint comparison is already contained in the comoving source kernel.

Define the kernel transform

\[
(\mathcal K\mu)(q)
=
\int W_t(q)\,d\mu(t),
\qquad
W_t(q)=H(q+t)-H(q-t).
\]

Then

\[
\mathcal K\delta_{\log p}=W_{\log p},
\qquad
\mathcal K\delta_{2\log p}=W_{2\log p}.
\]

Thus the primitive and square arithmetic delta incidences map to the exact analytic endpoint windows, with no fitted embedding.

The map is contractive from finite total-variation measures to the multiplier algebra, preserves prime labels, and has the correct reciprocal odd character.

## Source scale measures

Let \(\mathcal M_{\mathrm{fin}}(\mathbb R)\) be the finite signed or complex measures on the scale coordinate \(t\), with total-variation norm.

The local primitive and square incidences are

\[
\mu_{P,p}
=
p^{-1/2-\sigma-it}\delta_{\log p},
\]

\[
\mu_{Q,p}
=
\frac12p^{-1-2it}\delta_{2\log p}.
\]

Their endpoint locations and coefficients remain separately typed.

## Kernel transform

Define

\[
\mathcal K:
\mathcal M_{\mathrm{fin}}(\mathbb R)
\longrightarrow
L^\infty(\mathbb R_q)
\]

by

\[
\mathcal K\mu
=
\int W_t\,d\mu(t).
\]

Since

\[
|W_t(q)|\le1,
\]

we have

\[
\|\mathcal K\mu\|_\infty
\le
\|\mu\|_{\mathrm{TV}}.
\]

Therefore multiplication gives a bounded comparison into the analytic operator carrier:

\[
J(\mu)
=
M_{\mathcal K\mu}
\in
\mathcal B(L^2(\mathbb R_q)),
\]

with

\[
\|J(\mu)\|
\le
\|\mu\|_{\mathrm{TV}}.
\]

This realizes the arithmetic distribution as an analytic endpoint multiplier, not as an \(L^2(q)\) vector.

That distinction resolves the earlier delta-versus-Hilbert mismatch.

## Exact endpoint images

For a point mass,

\[
\mathcal K\delta_t=W_t.
\]

Hence the unweighted endpoint comparison maps are

\[
J_{P,p}(1)
=
M_{W_{\log p}},
\]

\[
J_{Q,p}(1)
=
M_{W_{2\log p}}.
\]

With source coefficients retained,

\[
J(\mu_{P,p})
=
p^{-1/2-\sigma-it}M_{W_{\log p}},
\]

\[
J(\mu_{Q,p})
=
\frac12p^{-1-2it}M_{W_{2\log p}}.
\]

The coefficients are not absorbed into the window kernel or Green metric.

## Reciprocal covariance

The window kernel is odd in the scale parameter:

\[
W_{-t}(q)
=
-H(q-t)+H(q+t)
=
-W_t(q).
\]

Let reciprocal reflection on measures be

\[
(\mathcal R\mu)(E)=\mu(-E).
\]

Then

\[
\mathcal K(\mathcal R\mu)
=
-\mathcal K\mu
\]

for the sheet-oriented source convention.

Thus the comparison intertwines reciprocal scale reversal with the odd analytic window character.

If the analytic reciprocal operation also reflects \(q\), its additional action must be composed explicitly; the scale-odd law above is already exact.

## Prime labels

Let the global source be the algebraic direct sum

\[
\bigoplus_p
\mathcal M_p.
\]

Define

\[
\mathcal K_{\mathrm{glob}}
=
\bigoplus_p\mathcal K_p.
\]

Then for prime idempotents \(P_p\),

\[
P_p\mathcal K_{\mathrm{glob}}
=
\mathcal K_{\mathrm{glob}}P_p.
\]

Therefore

\[
P_q\mathcal K_{\mathrm{glob}}P_p=0
\qquad
(p\ne q).
\]

Prime diagonality is constructor-level, not inferred from scalar orthogonality.

Finite cutoff restriction commutes exactly with \(\mathcal K_{\mathrm{glob}}\).

## Source topology

On each local measure fiber, the comparison is total-variation contractive.

For the global projective exponential source packet, apply \(\mathcal K\) coefficientwise. Because its local norm is at most one, every weighted \(\ell^1\) seminorm is nonincreasing:

\[
q_\delta(\mathcal K\mu)
\le
q_\delta(\mu).
\]

Thus finite-prime truncations remain equicontinuous and converge in the same test topology.

On fixed finite-order dual rungs, the transpose comparison is likewise continuous because no prime-order growth is introduced.

## Endpoint scales

The strict-front theorem gives

\[
m_W
\le
\|M_{W_{\log p}}\|,
\|M_{W_{2\log p}}\|
\le
1.
\]

Hence the unweighted endpoint basis has a uniform nonzero image in the multiplier norm.

Combined with the Pauli-twirl identity, this gives a uniform arithmetic endpoint frame in the multiplier target.

Transporting that frame into a Green endpoint energy still requires a norm-comparison theorem.

## Composition with the history right inverse

The endpoint pair

\[
\left(
M_{W_{\log p}},
M_{W_{2\log p}}
\right)
\]

can be lifted by the explicit affine right inverse \(R_{\log p}\), with graph norm \(O(\sqrt{\log p})\).

Alternatively, the actual source history

\[
t\longmapsto M_{W_t}
\]

provides the preferred path because its derivative produces the Green/Stokes boundary.

Thus the full analytic realization factors as

\[
\text{arithmetic scale measures}
\xrightarrow{\mathcal K}
\text{endpoint multipliers}
\xrightarrow{\text{source history}}
\text{history graph}.
\]

The first formerly missing arrow is now explicit.

## Remaining Green theorem

The kernel transform does not by itself prove that the relative Green form equals the desired mixed Adams form.

The next identity must be established on a common core:

\[
b_p(x,y)
=
\left\langle
J_{Q,p}y,\,
M_{W_{2L}-W_L}J_{P,p}x
\right\rangle_{\mathrm{rel}},
\qquad
L=\log p,
\]

with the adjoint order corrected to the frozen Green convention.

The remaining gates are:

- definition of the relative pairing on multiplier-valued endpoint images;
- radical annihilation;
- closability;
- preservation under graph closure;
- reciprocal adjoint orientation;
- compatibility with the typed Pauli outputs.

## Consequence

The earliest missing constructor has advanced by one arrow:

\[
\text{arithmetic endpoint incidence}
\xrightarrow{\text{solved }\mathcal K}
\text{analytic endpoint multipliers}
\xrightarrow{\text{missing relative Green pairing}}
\text{mixed Adams form}.
\]

The arithmetic endpoint lifts are no longer arbitrary rigged embeddings. They are evaluations of the source comoving window kernel.
