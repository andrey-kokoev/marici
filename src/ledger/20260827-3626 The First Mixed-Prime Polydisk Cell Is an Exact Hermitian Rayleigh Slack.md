# 3626 — The First Mixed-Prime Polydisk Cell Is an Exact Hermitian Rayleigh Slack

For the first multiaffine prime-labelled cell

\[
F(u,v)=a+bu+cv+duv,
\]

bidisk zero exclusion reduces exactly to a one-variable Hermitian slack. After
minimizing the phase of `u`, the slack is

\[
q(r)=a^2-c^2+(b^2-d^2)r^2-2|ab-cd|r,
\qquad 0\le r\le1.
\]

One must additionally exclude a common interior zero of `a+bu` and `c+du`.
The minimum of `q` is elementary and exact, so this is a finite symbolic gate,
not a numerical root census.

The mixed determinant `ad-bc` is the interaction curvature. Independent Fock
formation makes it zero and factors the cell into its two one-prime factors.
Completion-induced interaction deforms it, and the Hermitian slack decides
whether that deformation pushes a zero into the bidisk.

The hostile `1+4uv` has stable axis restrictions but slack `1-16r^2` and the
interior zero `u=v=i/2`. The common-factor hostile `(1+2u)(1+v)` has zero
slack yet an interior zero, demonstrating why the separate common-factor gate
is essential.

The exact checker passes 8/8 gates. The next source test is to extract each
finite two-prime theta/Tate coefficient cell before diagonal restriction and
evaluate its local walls, interaction curvature, radial minimum, and
common-factor locus.

Artifacts:

- `research/grothendieck/the-first-mixed-prime-polydisk-cell-is-an-exact-hermitian-rayleigh-slack.md`
- `research/grothendieck/checkers/check_biaffine_prime_polydisk_rayleigh_slack.py`
