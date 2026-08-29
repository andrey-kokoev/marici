# Local window histories are bounded, but primitive global Hilbert summation diverges

## Local history operator

Fix \(p\), put \(L=\log p\), and work first on the analytic scale Hilbert space

\[
H_q=L^2(\mathbb R,dq).
\]

Let \(W_t\) act by multiplication:

\[
(W_t\psi)(q)
=
\bigl(H(q+t)-H(q-t)\bigr)\psi(q).
\]

Because \(0\le H\le1\),

\[
\|W_t\|_{H_q\to H_q}\le1.
\]

Also,

\[
\partial_tW_t(q)
=
-e^{-\pi(q+t)^2}
-e^{-\pi(q-t)^2},
\]

so

\[
\|\partial_tW_t\|_{H_q\to H_q}\le2.
\]

Therefore the history map

\[
\mathcal H_p\psi:t\mapsto W_t\psi
\]

is bounded from \(H_q\) into \(H^1([L,2L];H_q)\), with the explicit estimate

\[
\|\mathcal H_p\psi\|_{H^1_tH_q}^2
\le
5L\|\psi\|_{H_q}^2.
\]

It is consequently closed on \(H_q\), and hence closable on every dense source core continuously embedded in \(H_q\).

## Local endpoint traces

The endpoint traces are direct multiplication operators:

\[
\operatorname{Tr}_L\mathcal H_p\psi=W_L\psi,
\qquad
\operatorname{Tr}_{2L}\mathcal H_p\psi=W_{2L}\psi.
\]

Thus

\[
\|\operatorname{Tr}_L\mathcal H_p\psi\|
\le\|\psi\|,
\qquad
\|\operatorname{Tr}_{2L}\mathcal H_p\psi\|
\le\|\psi\|.
\]

These local trace bounds are independent of \(p\). They are stronger than invoking the generic interval trace theorem, whose constants can obscure the varying interval length.

The Banach-valued fundamental theorem gives

\[
\operatorname{Tr}_{2L}\mathcal H_p
-
\operatorname{Tr}_L\mathcal H_p
=
\int_L^{2L}\partial_tW_t\,dt
\]

in the strong operator sense on \(H_q\).

Therefore the local analytic-window history and its endpoint identity are already rigorous in the ordinary \(L^2\) carrier.

## The first quantitative obstruction

The history graph norm grows with the interval length:

\[
\|\mathcal H_p\|
\le
\sqrt{5\log p}.
\]

This does not obstruct one-prime closability. It does obstruct a naive primewise Hilbert direct sum after arithmetic weighting.

For the primitive endpoint weight \(p^{-1/2}\), the squared history bound contributes

\[
\frac{\log p}{p}.
\]

The prime sum diverges:

\[
\sum_p\frac{\log p}{p}=\infty.
\]

For the square endpoint weight \(\frac12p^{-1}\), the squared contribution is bounded by

\[
\frac{\log p}{4p^2},
\]

and

\[
\sum_p\frac{\log p}{p^2}<\infty.
\]

Hence:

- square histories fit an ordinary Hilbert direct sum;
- primitive histories do not.

This exactly reproduces the distinct completion grades from the history norm itself.

## No common global Hilbert history

The local theorem does not globalize into one unweighted Hilbert direct sum carrying both endpoints. Any construction claiming cutoff-uniform Hilbert control must explain the divergence

\[
\sum_{p\le X}\frac{\log p}{p}.
\]

The correct global object must retain the primitive history as a distributional or Laplace-rigged section over prime scale, while the square history may occupy a Hilbert grade.

Thus the operator-valued trace theorem is inherently anisotropic in two directions:

- Sobolev regularity along the finite scale path \(t\);
- arithmetic summability across prime labels.

## Typed history rigging

A plausible source topology is a test–Hilbert–dual tower over the prime-scale base:

\[
\mathcal E_{\mathrm{hist}}
\subset
\mathcal H_{\mathrm{hist}}
\subset
\mathcal E_{\mathrm{hist}}'.
\]

The primitive weighted history acts in the dual grade, tested against prime-scale sections with sufficient exponential/Laplace decay. The square weighted history lies in the Hilbert or tempered grade.

The endpoint traces must therefore be typed separately:

\[
\operatorname{Tr}_L:
\mathcal E_{\mathrm{hist}}'
\to
E_P',
\]

and

\[
\operatorname{Tr}_{2L}:
\mathcal H_{\mathrm{hist}}
\to
E_Q.
\]

A common tempered codomain silently weakens the primitive topology and is not authorized.

## Green identity still missing

The bounded local history proves the operator-valued fundamental theorem for multiplication windows. It does not yet produce the mixed arithmetic Green form.

The missing step is a relative pairing between:

- the primitive distributional history;
- the square Hilbert history;
- the first-order scale derivative;
- the wall endpoint fields.

That pairing must extend the local strong identity and remain meaningful after prime aggregation.

## Hostile classification

### Pointwise identity without global graph

Every prime has a valid local \(H^1\) history, but the primitive direct-sum graph norm diverges like

\[
\sum_{p\le X}\frac{\log p}{p}.
\]

Finite endpoint differences exist while no global Hilbert history does.

### Topology weakening

Both endpoints are embedded into a common tempered space. Local traces become continuous, but the primitive exponential/Laplace boundary grade has been discarded.

### Cancellation normalization

A cutoff-dependent factor is moved from the primitive endpoint into the path norm to force Hilbert summability. The scalar product remains bounded while source incidence normalization changes.

## Exact next theorem

The local analytic portion is closed:

\[
\mathcal H_p:
L^2_q
\to
H^1([L,2L];L^2_q)
\]

is bounded, has uniform endpoint contractions, and satisfies strong Stokes.

The remaining theorem is global and rigged:

> construct a prime-scale test–Hilbert–dual history object on which the primitive and square weighted endpoint traces retain their distinct source topologies and the summed relative Green/Stokes form is closable.

This is sharper than a generic trace theorem: the local trace is benign, while arithmetic aggregation is the exact obstruction.
