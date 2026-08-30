# Target domination is weaker than full-state observability

## Bounded question

When an observation interface loses a state direction at completion, can a
specific theorem-relevant output still be computed stably without reconstructing
the full state?

## Frozen observation and target

Let \(X,Y,Z\) be finite-dimensional Hilbert spaces. Let

\[
H:X\longrightarrow Y
\]

be the observed context or feature map, and let

\[
R:X\longrightarrow Z
\]

be the theorem-relevant target map.

The question is not whether \(H\) reconstructs every \(x\in X\). It is whether
there is a decoder

\[
D:Y\longrightarrow Z
\]

such that

\[
R=DH.
\]

## Algebraic factorization theorem

Such a linear decoder exists exactly when

\[
\ker H\subseteq\ker R.
\]

Necessity is immediate: if \(Hx=0\), then \(Rx=DHx=0\).

For sufficiency, define \(D\) on the range of \(H\) by

\[
D(Hx)=Rx.
\]

The kernel inclusion makes this definition independent of the chosen preimage.
In finite dimension, extend \(D\) to all of \(Y\).

Thus a target can descend through a nonfaithful observation quotient even when
the full state cannot.

## Quantitative domination theorem

A decoder with

\[
\|D\|\leq C
\]

exists exactly when

\[
\|Rx\|\leq C\|Hx\|
\]

for every \(x\in X\). Equivalently,

\[
R^*R\leq C^2H^*H.
\]

The sharp constant is

\[
C_*
=
\sup_{Hx\neq0}
\frac{\|Rx\|}{\|Hx\|}.
\]

It is also the norm of the minimal decoder on the range of \(H\).

The kernel condition gives algebraic descent. Domination prices stable descent.

## Uniform completion theorem

For a cutoff family \((H_N,R_N)\), target computation is completion-stable when
one constant \(C\) satisfies

\[
R_N^*R_N\leq C^2H_N^*H_N
\]

for every cutoff.

Cutoffwise factorization with constants \(C_N\) proves only finite descent. If

\[
C_N\longrightarrow\infty,
\]

the target becomes infinitely sensitive even though every finite decoder
exists.

## Smallest target-sensitive witness

Take

\[
H_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix}.
\]

First choose

\[
R_0=
\begin{pmatrix}
1&0
\end{pmatrix}.
\]

Then

\[
R_0=D_0H_N
\]

with

\[
D_0=
\begin{pmatrix}
1&0
\end{pmatrix}
\]

and \(\|D_0\|=1\) for every \(N\). The first coordinate remains uniformly
computable although the full observation gap collapses.

Now choose

\[
R_1=
\begin{pmatrix}
0&1
\end{pmatrix}.
\]

Every finite cutoff admits

\[
D_{1,N}=
\begin{pmatrix}
0&N
\end{pmatrix},
\]

but

\[
\|D_{1,N}\|=N.
\]

The second coordinate is algebraically available at every finite stage and
unstable at completion.

The same observation interface therefore supports one stable theorem and fails
another.

## The theorem-relevant quotient

For a target family \(\mathcal R=\{R_j\}\), define target equivalence by

\[
x\sim_{\mathcal R}x'
\]

when

\[
R_jx=R_jx'
\]

for every \(j\).

The observation need only separate this quotient. Algebraically, the condition
is

\[
\ker H
\subseteq
\bigcap_j\ker R_j.
\]

Quantitatively, the aggregate target Gramian

\[
Q_{\mathcal R}
=
\sum_jR_j^*R_j
\]

must satisfy

\[
Q_{\mathcal R}\leq C^2H^*H.
\]

This is the exact target-relative replacement for full-state observability.

## Full observability as the maximal target

Set \(R=I_X\). Then target domination becomes

\[
I_X\leq C^2H^*H,
\]

which is precisely a lower singular bound for full-state reconstruction.

Thus full observability is the special case where every state coordinate is
declared theorem-relevant. It may be unnecessarily strong when the programme
needs only a quotient, current, control action, or scalar decision.

Weakening to a target is legitimate only when the target family is frozen
before the collapsing mode is discovered. Discarding a direction after it
causes failure is an outcome-fitted quotient.

## Minimal feature augmentation

Return to the hostile \(H_N\). Add one source-authorized seam row

\[
J=
\begin{pmatrix}
0&1
\end{pmatrix}.
\]

The augmented observation map is

\[
\widetilde H_Nx=(H_Nx,Jx).
\]

Its Gramian is

\[
\widetilde H_N^*\widetilde H_N
=
\begin{pmatrix}
1&0\\
0&1+N^{-2}
\end{pmatrix}.
\]

The lower bound is now at least one. One independent row observing the escaping
direction repairs full observability.

The algebra can identify the required row direction. Source theory must still
derive the actual seam constructor and its normalization.

## Regularization is a declared quotient

Truncated singular-value inversion discards directions below a threshold. It
can stabilize reconstruction of targets that ignore those directions.

It does not recover the original full state. It replaces the target by its
projection onto a well-observed quotient. The threshold, norm, and induced bias
must therefore appear in the claim boundary.

Regularization is principled when the discarded modes are already equivalent
under all declared future constructors. It is a change of problem when they
alter a theorem-relevant output.

## Control-theory translation

A plant need not be fully observable to support one control objective. A target
functional, regulated output, or safety predicate may factor through the
available sensor map even when hidden state remains.

The stable question is whether the target lies in the bounded observation
closure. A controller that estimates an unobservable state coordinate is
unjustified; a controller using only an observable quotient can be valid.

This is functional observability rather than complete state observability.

## Diagnostic-code translation

A diagnostic signature need not identify every microscopic mechanism. It must
identify every equivalence class requiring a different authorized action.

The discrete kernel condition says that candidates colliding under observation
must also collide under the action target. Robust distance is then required only
between action-inequivalent classes.

This prevents overdiagnosis while preserving control faithfulness.

## Toric-code instance

Syndrome does not reconstruct the encoded quantum state. It can nevertheless
determine a local repair class when every error with the same syndrome is
equivalent under the declared correction objective.

Logical loop information becomes necessary when the target includes logical
sector identification or operations whose outcome differs across homology
classes. The target family decides whether syndrome-only observation is
sufficient.

No classical target quotient authorizes reconstruction of conjugate logical
amplitudes.

## Software instance

A health monitor need not reconstruct all service internals. It may stably
compute a safety action if all hidden states with the same telemetry require the
same action.

If two telemetry-equivalent states require different recovery, the monitor is
not control-faithful. Adding internal detail that never changes an authorized
action increases observability without increasing operational value.

## Theta/Tate hostile instance

Full source-state reconstruction may be stronger than the RH-bearing target.
The correct audit freezes the primitive current, square current, seam term,
archimedean term, and mixed Green form as target maps and tests their uniform
domination by one authorized constructor-generated observation family.

A collapsing mode is harmless only if every required current vanishes on it at
the controlled rate. If one target remains finite while its observed feature
tends to zero, the domination constant diverges and the completed identity is
not continuous through that quotient.

The seam row is justified when it observes precisely such an escaping target
direction and is independently source-derived.

## DPC: observe what the explanation uses

The conjecture is:

> A programme need not reconstruct the entire hidden state. It must prove that
> every conclusion and executable continuation it claims factors continuously
> through the observed carrier with one source-normalized bound. Hidden
> directions may be quotiented only when all declared targets annihilate them.

This replaces maximal observability with target-complete explanation.

## Critics

### Choosing the target invites cherry-picking

Correct unless the target is frozen before the audit and includes every future
constructor used by the conclusion. Context closure prevents omitting an
inconvenient continuation.

### A bounded decoder may be nonphysical

Correct. Factorization proves mathematical computability from the observation.
A physical implementation still needs an executable, causal, and costed
constructor.

### The kernel condition should be enough

Only for finite exact algebra. Completion and noise require uniform domination.
A sequence of finite decoders with diverging norm is not stable descent.

### Regularization solves ill-conditioning

It solves a modified approximation problem. Its bias is harmless only when the
discarded modes are irrelevant to the frozen target.

### Full observability is safer

It is stronger, but may be impossible or unnecessarily expensive. The exact
safety condition is faithful observation of every action-relevant quotient.

## Exact falsifiers

- A target nonzero on \(\ker H\) claimed computable from \(H\).
- Finite decoder existence used without a uniform norm bound.
- Full-state observability demanded although only a smaller frozen quotient is
  used.
- A collapsing direction discarded after discovering that it falsifies the
  target.
- Regularized reconstruction called exact recovery of the original state.
- An algebraically bounded decoder presented as a physical controller without
  implementation authority.
- A target family omitting a future constructor used later in the conclusion.

## Machine-readable target packet

```json
{
  "code": "target_relative_observability",
  "observation": "H_N",
  "target": "R_N",
  "kernel_inclusion": true,
  "sharp_decoder_bound": "C_N",
  "uniform_domination": false,
  "full_state_reconstruction_required": false,
  "target_family_frozen": true,
  "physical_decoder_authorized": false
}
```

## Deutschian explanation

An observation is sufficient for a conclusion when every hidden distinction it
erases is also irrelevant to that conclusion. The decoder then acts on the
observed quotient rather than reconstructing an invented full state.

Stability asks more: the conclusion must not amplify an increasingly invisible
feature without bound. The target domination inequality states exactly how much
of the hidden state the explanation genuinely needs.

## Claim boundary

This packet proves finite target factorization and its quantitative domination
criterion, with a uniform cutoff formulation. It does not derive the target
family, source norms, or a physical decoder for any sector.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 10/10, and expected
information gain 10/10. The target was the weakest sufficient replacement for
full-state observability.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Stable explanation is target-relative domination:
observe every distinction used by the conclusion, not every hidden coordinate.
