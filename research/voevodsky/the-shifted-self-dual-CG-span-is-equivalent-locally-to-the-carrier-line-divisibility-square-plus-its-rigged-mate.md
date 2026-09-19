# The shifted-self-dual CG span is locally the carrier-line divisibility square plus its rigged mate

Fresh inspection of the prior Koszul-to-Green frontier identifies the concrete
local form of the abstract middle-facet span.  Write

\[
K_\tau=[\mathcal L_\theta\xrightarrow{\tau}\mathcal O]
\]

and let

\[
C_{\rm FP}=[\mathcal D_{\rm Gr}\xrightarrow{C(s)}\mathcal Y_{\rm Gr}]
\]

be a candidate stratified Green Fredholm complex.  A chain map from `K_tau` to
`C_FP` consists precisely of two holomorphic maps

\[
i_s:\mathcal L_{\theta,s}\to\mathcal D_{{\rm Gr},s},
\qquad
w_s:\mathcal O_s\to\mathcal Y_{{\rm Gr},s}
\]

satisfying the divisibility square

\[
C(s)i_s=w_s\tau_s.
\]

Thus the abstract `CG` correspondence does not first require an arbitrary
higher categorical object: its first executable chart is this square.  At an
Xi zero `s_0`, it gives

\[
C(s_0)i_{s_0}=0.
\]

If `i_(s_0)` remains injective, the carrier line produces a nonzero Green
kernel state without division by Xi.

The shifted reciprocal self-duality

\[
M_{CG}\simeq\mathbb D(M_{CG})[1]
\]

adds the opposite-oriented mate square.  In rigged notation it requires the
transpose incidence and lower equation to be compatible with the same map,
not fitted independently.  On divisor states this contains the shellwise
condition

\[
B_\Sigma^\dagger u_{s_0}=0,
\]

or, before a Hilbert Riesz identification, the corresponding
`B_Sigma^times` equation.  Hence the apparent two-sided missing facet reduces
to one source incidence `i` together with proof that its canonical rigged mate
satisfies the reflected square.

Acyclicity of the mapping cone remains stronger than the divisibility square.
It additionally requires holomorphic complement splitting and local
module-length preservation.  The construction ladder is therefore:

1. construct `i` independently and prove `C i=w tau`;
2. prove injectivity of `i` through the divisor;
3. verify the rigged mate/lower shell equations;
4. construct a bounded holomorphic contraction of the comparison cone.

The repository currently has `K_tau`, the local Green/Weyl charts, and the
formal target equation, but no independent `i`.  This is now the earliest
nonredundant constructor for the restarted 25-turn cycle.
