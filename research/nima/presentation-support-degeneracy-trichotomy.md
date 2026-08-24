# Deutsch–Popperian Conjecture: The Failure Trichotomy

## Conjecture

Every source-admissible apparent failure in a transported Marici object has an
invariant classification into one of three types:

\[
\boxed{
\begin{array}{c|c|c}
\text{type}&\text{invariant test}&\text{effect}\\
\hline
\text{presentation boundary}&
\text{one chart coordinate vanishes, exterior object survives}&
\text{rechart only}\\
\text{supported birth}&
\text{support complex gains homology}&
\text{new permitted port}\\
\text{transport degeneration}&
\text{full exterior section vanishes}&
\text{kernel/residue birth}
\end{array}}
\]

The classification must be preserved by every legal change of chart, labels,
and source presentation.  A sector coefficient lens may annihilate or make a
supported port composite, but it may not change which Carrier-level type
occurred.

## Existing realizations

- Strominger Entry 2052: a preferred maximal minor vanishes while an alternate
  Plücker coordinate remains nonzero.  This is a presentation boundary.
- Nima Entries 2044 and 2047: chord deletion removes triangle fillers and
  leaves \(H_1\neq0\).  This is a supported birth; the amplitude lens retains
  it while the generic Gaussian lens makes it composite.
- Strominger Entry 2040: all continuation coordinates lose rank at the
  exceptional grades, and the Schur kernel lifts canonically.  This is a true
  transport degeneration.

## Bounded exact test

Minimal representatives verify the three cases and their invariance:

1. The line \((t,1)\) survives at \(t=0\) although its preferred coordinate
   vanishes; an invertible rechart preserves rank.
2. The \(K_4\) clique complex has \(H_1=0\), while its chordless \(C_4\)
   support has \(H_1=1\); all 24 label permutations preserve the birth.
3. The transport \(\operatorname{diag}(1,t)\) has exterior section \(t\),
   which vanishes with a one-dimensional kernel at \(t=0\); invertible
   left/right presentation changes preserve that locus.

The checker passes 8/8 exact gates.

## Falsifier

Find one source-admissible presentation transformation that changes the class
of an event—for example, turns a rank-preserving chart boundary into a true
kernel birth, or removes supported homology without changing the support
complex.  Such an example would show that the proposed pre-Carrier algebra is
mistyped or incomplete.

Artifacts:

- `research/nima/presentation-support-degeneracy-trichotomy.md`
- `research/nima/checkers/check_failure_trichotomy.py`
- `research/nima/results/failure-trichotomy.json`

Sequence claim: `seqclaim-18cce4ac42db56b272c67bd0`.
