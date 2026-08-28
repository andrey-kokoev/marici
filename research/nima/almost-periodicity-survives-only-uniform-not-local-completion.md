# Almost periodicity survives only uniform, not local, completion

Author: `marici.Nima`

## Topology gate

Grothendieck's regularized resolution signal separates the two divisor types:
the atomic seam contribution is Bohr almost periodic, while the diffuse
off-seam contribution lies in \(C_0(\mathbb R)\). Since their intersection is
zero, RH becomes pure almost periodicity of the full signal.

Finite Euler-character cutoffs are trigonometric sums and therefore almost
periodic. The unresolved issue is whether their completion topology preserves
that class.

## Exact hostile sequence

For positive integers \(n\), define

\[
 f_n(t)=\left(\cos\frac{t}{\sqrt n}\right)^{2n}.
\]

Each \(f_n\) is a finite trigonometric polynomial. It is periodic, hence Bohr
almost periodic, and satisfies \(0\le f_n\le1\).

For every fixed \(t\), the logarithmic expansion of cosine gives

\[
 2n\log\left(\cos\frac{t}{\sqrt n}\right)
 \longrightarrow -t^2.
\]

Therefore

\[
 f_n(t)\longrightarrow e^{-t^2}.
\]

The convergence holds with every fixed derivative on every compact interval.
Thus pointwise convergence, local uniform convergence, local Sobolev
convergence, and every fixed-window finite observer all accept the sequence.

The limit is a nonzero member of \(C_0(\mathbb R)\), so it is not Bohr almost
periodic.

## Failure of global uniform convergence

Set

\[
 t_n=2\pi\sqrt n.
\]

Then

\[
 f_n(t_n)=1,
 \qquad
 e^{-t_n^2}=e^{-4\pi^2n}.
\]

Hence

\[
 \|f_n-e^{-t^2}\|_\infty
 \ge 1-e^{-4\pi^2n}
 \longrightarrow1.
\]

The sequence cannot converge in the global sup norm. This is exactly the
topology that would preserve Bohr almost periodicity.

## Consequence for the theta programme

It is insufficient to prove that every finite regularized Euler cutoff is
almost periodic and that the cutoffs converge:

- pointwise;
- on every compact seam interval;
- in local \(L^2\) or Sobolev norms;
- against every fixed finite observer;
- in a topology that forgets translating recurrence peaks.

Any of these completions may create a nonzero diffuse \(C_0\) component.

The source theorem must provide a cutoff-independent global recurrence bound,
equivalently uniform convergence in the seam variable or another topology
known to embed continuously into the Bohr sup-norm completion.

## Relation to earlier completion obstructions

The peaks at \(t_n\) escape every fixed observation window. This is the same
completion-at-infinity mechanism previously seen as:

- a seam partner escaping to infinite norm;
- adjacent arithmetic labels collapsing in a continuous Gram topology;
- cutoffwise observability losing its smallest singular value;
- finite coherence surviving while uniform strictification fails.

The almost-periodic formulation packages these as loss of global recurrence
under completion.

## Finite falsifier

For any proposed completion-stable AP theorem, evaluate its claimed uniform
tail control at \(t_n=2\pi\sqrt n\). A bound tending to zero is impossible for
this hostile sequence. If the proposed topology still declares convergence,
it is too weak to exclude diffuse divisor charge.

## Verdict

Almost periodicity is the first genuinely source-facing orientation candidate
to survive the rank-one completion-law audit, but only with a global uniform
completion theorem. Finite AP grammar plus local convergence carries no RH
force. The next exact theta calculation is the sup-norm tail of the fully
coupled, regularized Euler-to-seam resolution signal.

