# The Cut fixes the no-event probability but not its state update

Owner: `marici.Nima`

Status: this identifies what the inclusive Cut alone cannot determine.  The
missing one-loop elastic phase has now been reconstructed from the oriented
Cut and its source boundary jet; see `qed-elastic-pair-instrument.md`.

Let (E_{\rm cut}\) be the positive forward Breit--Wheeler helicity Gram
matrix.  After a dimensionless exposure (\tau), the event effect is

\[
E_{\rm event}=\tau E_{\rm cut}.
\]

A binary effect-valued measurement exists exactly while

\[
0\le\tau\le\tau_{\max},
\qquad
\tau_{\max}=\lambda_{\max}(E_{\rm cut})^{-1},
\]

because then

\[
E_\varnothing=I-\tau E_{\rm cut}\succeq0.
\]

This supplies exclusive event/no-event probabilities.  It still does not
select a quantum instrument.  If

\[
N=\sqrt{E_\varnothing},
\]

then for every unitary (U),

\[
N_U=UN
\]

has the same effect:

\[
N_U^\dagger N_U=E_\varnothing.
\]

But the conditional successor states

\[
N\rho N^\dagger
\quad\hbox{and}\quad
N_U\rho N_U^\dagger
\]

are generally different.  The Cut therefore fixes the inclusive loss
probability but not the coherent elastic evolution of the surviving photon
state.

The missing datum is the source-normalized elastic (S)-matrix channel,
including its dispersive phase.  This is the scattering counterpart of the
recurring Marici distinction:

\[
\text{effect/readout}
\neq
\text{state-transforming instrument}.
\]

The event branch is better determined: the Breit--Wheeler amplitude itself
supplies its Kraus density and outgoing pair state.  The ambiguity is
localized to completing the absorptive Cut into the full elastic-plus-pair
channel.

## Consequence

The correct next scattering theorem is not another positivity bound.  It is
a source-derived completion square

\[
\begin{array}{ccc}
H_{\gamma\gamma}&\xrightarrow{S_{\rm elastic}}&H_{\gamma\gamma}\\
\downarrow A&&\downarrow\\
H_{e^+e^-}&\longrightarrow&\text{inclusive channel}
\end{array}
\]

whose unitarity relation reproduces the Cut and whose phases descend through
the declared helicity/crossing conventions.

## Falsifiers

- (E_\varnothing) remains positive for (\tau>\tau_{\max}).
- The Cut alone distinguishes (N) from (UN).
- A no-event Lüders update is called source-derived without deriving the
  elastic amplitude.
- The completed channel fails to reproduce the established Cut effect.
