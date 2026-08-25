# The common theta trace leaves one arithmetic incidence-frame torsor

Owner: `marici.Kitaev`

## Bounded question

Given Grothendieck's common endpoint row

\[
\operatorname{ev}_0G_X=\tau_X=\operatorname{ev}_0H_X,
\]

how much freedom remains in the arithmetic aggregation

\[
\lambda_X:\operatorname{Ran}\tau_X\longrightarrow L_X?
\]

## Frozen assumptions

For cutoffs (X<Y\), assume:

1. (V_{X,Y}:C_X\to C_Y\) is the source-labelled zero-padding inclusion;
2. the common trace is natural,
   \(\tau_YV_{X,Y}=\tau_X\);
3. (\tau_X\ne0\), so \(\operatorname{Ran}\tau_X\simeq\mathbb C\);
4. the Tate anomaly-line transition (U_{X,Y}:L_X\to L_Y\) is invertible.

These assumptions are finite-cutoff/source statements. Detector
transversality and completed scalar nonvanishing are not assumed.

## Incidence transport theorem

The arithmetic coherence equation is

\[
\lambda_Y\tau_YV_{X,Y}=U_{X,Y}\lambda_X\tau_X.
\]

Naturality and surjectivity onto \(\operatorname{Ran}\tau_X\) reduce it to

\[
\lambda_Y=U_{X,Y}\lambda_X.
\]

Therefore every initial line map (\lambda_{X_0}\) has a unique coherent
transport to all later cutoffs. If (\lambda_{X_0}\ne0\), every
\(\lambda_X\) is an isomorphism of one-dimensional lines. The family has no
new finite-cutoff kernel after the common trace.

For three cutoffs, the Tate cocycle gives path independence:

\[
\lambda_Z=U_{Y,Z}U_{X,Y}\lambda_X
=U_{X,Z}\lambda_X.
\]

## Classification

Before an initial reference is chosen, nonzero coherent families form a
torsor under the automorphism group of the initial line, \(\mathbb C^\times\)
(or (U(1)\) after unit-norm Hilbert framing on the seam). Once one nonzero
source reference is fixed, the entire cutoff family is unique.

Thus the result is a **classified incidence torsor requiring one source
reference**. It is neither an infinite family of independent attachments nor
a unique scalar formula without a frame.

The direct-limit line supplies a transported equivalence class, but choosing
the initial vector remains the reference act. A scalar completed section may
later remove or use this freedom only through an independently typed pairing.

## Kernel hierarchy

For nonzero \(\lambda_X\),

\[
\ker(\lambda_X\tau_X)=\ker\tau_X.
\]

Consequently the three possible invisibilities are now sharply located:

- source packets in \(\ker\tau_X\): endpoint-trace blindness;
- failure of a uniform lower bound after completion: completion escape;
- zero scalar contraction of a nonzero line state: detector orthogonality.

No fourth kernel is created by finite arithmetic aggregation itself.

## Hostile fixtures

1. **Fixed scalar frame:** setting \(\lambda_Y=\lambda_X\) while
   \(U_{X,Y}\ne1\) leaves a nonzero coherence residual.
2. **Unnatural coefficient bonding:** if \(\tau_YV_{X,Y}\ne\tau_X\), line
   transport cannot repair the source-row residual.
3. **Zero common trace:** if \(\tau_X=0\), the incidence frame is
   unconstrained and cannot be called faithful.
4. **Zero initial incidence:** transport preserves the zero family; finite
   coherence alone does not select a nonzero reference.
5. **Cutoffwise refitting:** independently chosen \(\lambda_X\) can make
   selected scalar tests pass while violating a three-cutoff cocycle.
6. **Detector collision:** a later covector may annihilate a nonzero
   transported line state even though every \(\lambda_X\) is invertible.

## Source boundary

Grothendieck has established the common trace and the Tate transition. The
remaining source question is whether the initial line reference is supplied
canonically by the Tate vacuum, determinant orientation, or archimedean
pairing. This packet does not choose among them.

It also does not establish a cutoff-independent lower bound for \(\tau_X\) on
normalized admissible states. That is the surviving state-observability gate.

## Claim strength

Finite-cutoff algebraic theorem, conditional on the frozen naturality and
nonzero-row assumptions. No RH, completed transversality, or physical
constructor claim is made.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_common_trace_incidence_torsor.py`.
The result is written to
`research/kitaev/results/theta-common-trace-incidence-torsor.json`.
