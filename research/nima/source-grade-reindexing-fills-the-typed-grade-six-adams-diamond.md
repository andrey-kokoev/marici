# Source grade reindexing fills the typed grade-six Adams diamond

## Missing type map

The grade-six audit left the type-fibre maps

\[
A_{r;p,k}:E_{p,k}\to E_{p,rk}
\]

undefined.  The retained labelled source supplies them canonically: Adams
multiplication reindexes the prime-power grade.

For every integer \(r\ge1\), define

\[
S_re_{p,k}=e_{p,rk}.
\]

This is not an identity between primitive, square, and connected operator
classes.  It is a typed map from one labelled source summand to another.

## Completed continuity

On the projective exponential Köthe source,

\[
q_\delta(c)=\sum_{p,k}|c_{p,k}|e^{\delta k\log p},
\]

one has

\[
q_\delta(S_rc)=q_{r\delta}(c).
\]

Because every positive exponential rung belongs to the projective topology,
\(S_r\) is continuous.  Finite packets are dense and grade/prime cutoffs
converge in every rung, so this definition extends uniquely to the completion.

Its range is the coordinate subspace supported on grades divisible by \(r\),
which is closed because all coordinate projections are continuous.

## Exact Adams composition

Grade reindexing satisfies

\[
S_sS_r=S_{sr},
\qquad
S_1=I.
\]

Thus associativity and the unit law hold strictly on the source, before any
analytic realization or scalar output.

For the grade-six diamond,

\[
S_3S_2e_{p,1}=e_{p,6}=S_2S_3e_{p,1}.
\]

More generally,

\[
S_3S_2=S_2S_3=S_6.
\]

This supplies the previously missing typed filler.

## Compatibility with Euler half-density weights

The source incidence weight is

\[
w_{p,k}=\frac1k p^{-k/2}.
\]

Its Adams ratio is

\[
\rho_r(p,k)
=\frac{w_{p,rk}}{w_{p,k}}
=\frac1r p^{-(r-1)k/2}.
\]

Let \(U_{r;p,k}\) be the already source-derived transport of the cut/history
atom from displacement \(k\log p\) to \(rk\log p\).  For the labelled analytic
incidence \(\mathcal I\),

\[
\mathcal I S_re_{p,k}
=w_{p,rk}u_{p,rk},
\]

while

\[
\rho_r(p,k)U_{r;p,k}\mathcal Ie_{p,k}
=\rho_r(p,k)w_{p,k}u_{p,rk}
=w_{p,rk}u_{p,rk}.
\]

Hence the finite naturality square commutes exactly:

\[
\mathcal I S_r
=M_{\rho_r}U_r\mathcal I.
\]

The identity extends to the projective completion by continuity.

## Coherence of the analytic side

The transport cocycle gives

\[
U_{s;p,rk}U_{r;p,k}=U_{sr;p,k},
\]

and the coefficient ratios satisfy

\[
\rho_s(p,rk)\rho_r(p,k)=\rho_{sr}(p,k).
\]

Therefore

\[
M_{\rho_s}U_sM_{\rho_r}U_r
=M_{\rho_{sr}}U_{sr}.
\]

For \(r=2,s=3\), both paths through grades \(1\to2\to6\) and
\(1\to3\to6\) equal the direct grade-six realization.  The equality holds in
the source, coefficient, transported history, and cut-atom factors.

## Operator-ideal typing

The map crosses the filtration

\[
\text{primitive}\longrightarrow\text{square}
\longrightarrow\text{connected}
\]

without identifying these classes.  The ideal classifications belong to the
weighted analytic realizations:

- grade one is continuous on the projective rigging and not Hilbert--Schmidt;
- grade two is Hilbert--Schmidt;
- grades at least three are nuclear.

The reindexing map is defined on the common labelled source before those
realizations.  This is why it may connect distinct classes without declaring
them equal.

## Reciprocal and cutoff compatibility

Reflection acts inside each transported reciprocal pair and does not alter
\((p,k)\).  Therefore

\[
S_r\mathcal R=\mathcal RS_r.
\]

Prime cutoffs commute exactly with \(S_r\).  Grade cutoffs satisfy the typed
relation

\[
P_{\le K}S_r=S_rP_{\le\lfloor K/r\rfloor},
\]

which is the correct naturality law for grade multiplication.

## Disposition

The previously missing type-fibre Adams map is the canonical source grade
reindexing \(S_r\).  It is continuous on the completed Köthe source, intertwines
the weighted analytic incidence, preserves reciprocal and prime typing, and
satisfies strict composition.

Consequently the grade-six typed diamond now has the filler

\[
S_3S_2=S_2S_3=S_6.
\]

This closes the first explicit higher-composition hostile for G2.  It does not
by itself prove every endpoint, archimedean, dagger, and Green-polarization
coherence required by the full constructor system, and it does not establish
G3, G4, or RH.
