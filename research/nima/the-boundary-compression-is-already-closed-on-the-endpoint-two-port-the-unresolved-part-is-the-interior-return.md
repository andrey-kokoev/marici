# The boundary compression is already closed on the endpoint two-port; the unresolved part is the interior return

## Question

Are both boundary-compression maps still absent?

## Claim boundary

No. Fresh comparison with the retained endpoint packets shows that the observer
and endpoint-state parts are already constructed.

At every local place, the canonical observer packet is

\[
E_{\partial,p}^*=\operatorname{span}\{\epsilon_p,\mu_p\},
\qquad
\epsilon_p(f)=f(0),\quad \mu_p(f)=\int f,
\]

and local Fourier exchanges its coordinates:

\[
(\epsilon_p,\mu_p)\mathcal F_p=(\mu_p,\epsilon_p).
\]

The unramified vector has observer value `(1,1)`, so the exchange globalizes on
the restricted-product cylinder without creating infinitely many excited
places.

After the source-fixed endpoint metric is supplied, the weighted Hadamard map
identifies the wall and jump characters with the normalized Wronskian columns.
It is an isometry in the transported metrics and extends primewise with
cutoff-independent inverse. In particular, the reciprocal-odd chain

\[
\text{endpoint jump}
\longrightarrow
\text{Wronskian odd column}
\longrightarrow
\text{ordered tail history}
\]

is already closed, including its fixed Schur half-amplitude.

## Correct residual

The notation `(U_partial,V_partial*)` in the preceding packet merged two
different obligations:

1. endpoint observer/state transport, which is constructed;
2. incidence and observation of the interior additive Tate resolvent, which is
   not constructed on all nonspherical modes.

The missing object is therefore the interior return comparison

\[
V_{\rm int}^*(I-S_{{\rm Tate},p}(s))^{-1}U_{\rm int}
\longrightarrow G_{4,p}^{\rm retained}(s),
\]

subject to agreement with the already fixed endpoint restriction. Its
construction must determine whether translated and character-twisted shell
modes are annihilated, routed into a retained port, or contribute a controlled
Schur residual.

## Finite falsifier

At conductor `p^N`, decompose the additive Tate carrier into the endpoint-visible
subspace and its nonspherical complement. Compare the compressed return on two
states with the same endpoint pair `(epsilon_p,mu_p)` but distinct character
phase. If their retained returns differ while the proposed compression depends
only on endpoint data, the compression is not well defined. If they agree, the
calculation must exhibit the annihilating or decoupling identity rather than
infer it from equal endpoint coordinates.

## Disposition

The endpoint route/coherencer cell is closed. The next executable question is
observability of the finite-conductor nonspherical complement under the
interior Green return. Global completion and the final Xi readout remain
downstream.