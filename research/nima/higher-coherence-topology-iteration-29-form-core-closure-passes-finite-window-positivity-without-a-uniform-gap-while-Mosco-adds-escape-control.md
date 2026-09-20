# Higher-coherence topology iteration 29: form-core closure passes finite-window positivity without a uniform gap, while Mosco adds escape control

## Candidate topology

Let

\[
\mathcal D_L=C_c^\infty([-L,L]),
\qquad
\mathcal D=\bigcup_L\mathcal D_L,
\]

and let `W_L` be the complete endpoint--gamma--prime form restricted to
`D_L`. Use the closed logarithmic form topology

\[
\|f\|_{W,graph}^2
=\|f\|_2^2+W_{arch}(f,f)
\]

with the signed arithmetic part defined exactly on the compact-support core.

## Exact stabilization

For `f,g in D_L`, translated overlap vanishes when `log n>2L`. Hence the finite
prime sum stabilizes exactly after the corresponding arithmetic cutoff. If
`L' >= L`, the complete global formula restricts consistently:

\[
W_{L'}(f,g)=W_L(f,g).
\]

There is no limiting rearrangement of the signed prime series on a fixed core
vector.

## Positivity passage

Assume every finite Schur certificate from iteration 28 is nonnegative, so

\[
W_L(f,f)\ge0
\qquad(f\in\mathcal D_L)
\]

for every `L`. Then every `f in D` lies in one finite window and satisfies

\[
W(f,f)\ge0.
\]

If `W` is closable in the declared logarithmic graph topology, its closure is
nonnegative. No cutoff-uniform coercivity constant is required merely to pass
positivity from the core to the closed form.

Thus completion itself is not an additional RH-strength obstacle once all
finite-window certificates and closability are proved.

## Mosco strengthening

Mosco convergence asks additionally:

1. a liminf inequality for every weakly convergent sequence with supports that
   may escape;
2. a recovery sequence for every vector in the limiting form domain.

Recovery is natural from the form core. The liminf condition controls moving
negative or near-null packets that no fixed window sees uniformly. It yields
strong resolvent convergence and stability of spectral projections.

Mosco convergence is therefore needed for operator-level spectral transport,
but not for the basic implication

\[
\text{all finite }W_L\ge0
\Longrightarrow
\overline W\ge0.
\]

## Higher-coherence interpretation

The strict support tower is a local-to-global totalization in which each vector
enters at a finite stage and its value then stabilizes. Higher cone fillers can
be checked window by window. There is no requirement that one filler have a
uniform norm over all windows unless a global bounded operator, rather than a
closed form, is claimed.

This avoids over-demanding a uniform positive angle while retaining every
signed arithmetic cancellation.

## Remaining gate

The substantive problem is now concentrated at finite support:

\[
S_L\ge0
\quad\text{for every }L,
\]

where `S_L` is the low-mode Schur complement. This family is equivalent in
strength to positivity of the complete Weil form on its standard core. The
topology makes the reduction rigorous but does not prove the certificates.

## Verdict for topology 29

Form-core closure is a positive result: finite-window positivity passes to the
completed closed form without a uniform spectral gap. Full Mosco convergence
adds control of escaping modes and strong-resolvent realization, but is not the
first positivity gate.

The next nonredundant topology to test is a scale of Sobolev/Gelfand triples or
interpolation spaces, asking whether the finite Schur blocks become uniformly
small relative to the archimedean operator on a better-balanced rung.