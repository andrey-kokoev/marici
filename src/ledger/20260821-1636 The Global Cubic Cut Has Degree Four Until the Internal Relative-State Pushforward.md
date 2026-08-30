# 1636 — The Global Cubic Cut Has Degree Four Until the Internal Relative-State Pushforward

## Hostile multi-mode test

Entry 1635 proves strict degree preservation for the reduced observed creation channel.  Test the actual occurrence-resolved cubic jump before tracing the internal modes.

## Global labelled jump

For one source channel,

\[
L_{p;qk}
=
C_{p;qk}
a_p^\dagger a_q^\dagger a_k^\dagger.
\]

On the three-mode number algebra, the trace-balanced adjoint generator is

\[
\mathcal L_{p;qk}^\dagger f
=
(N_p+1)(N_q+1)(N_k+1)
\left[
f(N_p+1,N_q+1,N_k+1)
-f(N_p,N_q,N_k)
\right].
\]

For a number polynomial of total degree \(D\), the finite difference has top degree \(D-1\), while the prefactor has degree three.  Thus

\[
\deg_N\mathcal L_{p;qk}^\dagger f
=D+2.
\]

Since each number variable has physical Weyl degree two,

\[
\boxed{
\text{global physical moment-degree shift}=+4.
}
\]

The full occurrence-resolved cubic channel is therefore not a same-level endomorphism of the global three-mode moment tower.

## Relative-state pushforward

Push the two internal modes to their vacuum relative state:

\[
(N_q+1)(N_k+1)\mapsto1.
\]

For an observed moment \(f(N_p)\),

\[
\mathcal L_{p}^\dagger f
=(N_p+1)[f(N_p+1)-f(N_p)],
\]

which preserves observed degree exactly.

Thus the strict tower of Entries 1634--1635 is obtained only after the physical internal-state pushforward.

## Occurrence covariance

Every formula is invariant under

\[
(q,k)\leftrightarrow(k,q).
\]

The checker verifies 55 global number monomials, 55 occurrence-exchange identities, and 32 pushed observed degrees.

## Narrow result

\[
\boxed{
\text{The degree-four global shift is removed by the typed internal relative-state pushforward, not by unlabelled occurrence forgetting.}
}
\]

This corrects any interpretation of Entry 1635 as a pre-pushforward global theorem.

## Architectural consequence

The coefficient architecture has two filtered levels:

\[
\text{global occurrence-resolved moment tower}
\xrightarrow[+4]{\mathcal L_{p;qk}}
\text{global tower},
\]

followed by

\[
\text{internal relative-state pushforward}
\longrightarrow
\text{strict observed moment tower}.
\]

The pushforward changes filtration behavior and is therefore substantive six-functor/coefficient calculus, not mere bookkeeping.

## Durable artifacts

- `research/benincasa/checkers/multimode_cubic_cut_filtration.rs`
- `research/benincasa/results/multimode-cubic-cut-filtration.json`
- `research/benincasa/multimode-cubic-cut-filtration.md`

## Next falsifier

Replace the internal vacuum pushforward by the source general Gaussian state with occupations \(n_q,n_k\) and anomalous pairings \(\beta_q,\beta_k\).  Compute the induced observed generator and its maximum degree shift.  Test whether the pushforward remains a finite-order filtered map or couples the observed tower to the full internal moment tower.
