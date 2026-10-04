# Fixed-forcing placement and diagonal Haar transport are different squares

## Question

Does the existing separation-density/relative-Haar realization identify the history-translation route with the prime modular route, while preserving the realized state and its energy?

This audit responds to the operator's request to execute that comparison. The SCC obligation is route/coherencer compatibility, not construction of another carrier. The input contracts are the fixed-forcing joint graph, the one-leg relative-Haar tensor colligation, and the correction distinguishing energy equality from vector equality.

## Claim boundary

State placement already exists as a retained joint graph. Its fixed-forcing covariance is under a one-leg action. The relative-Haar modular operation acts on both pair slots. These actions are not the same; they become naturally comparable only when the forcing base is transported too.

On an exact real Haar core at p=2 and the critical seam, the two candidate outputs have equal positive energies 1/16 but squared difference 1/72. Thus this example rejects identification of the two transport maps, not their seam energy equality. It does not test or disprove RH.

A further exact identity explains why running the construction in reverse cannot force confinement: the forward and inverse positive energy multipliers cancel at every spectral real part. One-step energy conservation is strictly stronger than positive, invertible round-trip transport.

## What was already constructed

The fixed-forcing realization is

\[
F_\Phi(u)=(C_\Phi u,\Phi\otimes u),\qquad
(C_\Phi u)(t)=\int\Phi(q)u(q+t)\,dq.
\]

Conjugate slots are retained according to the mixed-Haar source type; the explicit test below uses a real core, so it does not replace the separate holomorphic/contragredient conventions.

When the declared correlation is bounded, the tensor coordinate gives

\[
\|F_\Phi(u)\|\ge\|\Phi\|\,\|u\|.
\]

It therefore has closed image on the Hilbert history carrier and admits source recovery by contraction of the tensor's first leg against Phi, divided by its squared norm. Closedness follows from this lower bound and completeness, not merely continuity of the two coordinate maps. No inverse to the correlation multiplier is required.

For S_a u(q)=u(q+a), the existing covariance is

\[
F_\Phi(S_au)
=(S_a^{\rm sep}\oplus(I\otimes S_a))F_\Phi(u).
\]

This is a valid fixed-base, one-leg square.

## The different relative-Haar operation

On the two independently normalized Haar spaces, write

\[
(U_a(p)f)(x)=\sqrt p\,f(px),\qquad
(U_m(p)g)(x)=g(px).
\]

They are unitary for dx and dx/x, respectively. The diagonal pair operation is

\[
D_p=U_a(p)\otimes\overline{U_m(p)}.
\]

Its action on a pointed tensor is

\[
D_p(\Phi\otimes\overline u)
=U_a(p)\Phi\otimes\overline{U_m(p)u}.
\]

Thus the natural map is between the fibers based at Phi and U_a(p)Phi. It is not an endomorphism of a fixed-Phi fiber. On logarithmic relative-Haar coordinates, simultaneous translation of both legs leaves their separation coordinate unchanged; translating only the history leg shifts that coordinate.

For the real correlation convention above,

\[
C_{S_a\Phi}(S_au)=C_\Phi u,
\qquad
C_\Phi(S_au)=S_a^{\rm sep}C_\Phi u.
\]

The additive half-density contributes the additional sqrt(p) amplitude to the first identity for the unweighted D_p. These formulas explicitly locate the missing forcing-base transport in an attempted fixed-base identification.

For any nonzero admitted forcing with a square-integrable logarithmic relative-Haar profile, it cannot be fixed by a nonzero log-prime translation: its squared modulus would be periodic and have infinite integral unless zero. Allowing a proportionality constant does not help, because translation unitarity forces that constant to have modulus one. Thus fixed-forcing vector closure under diagonal prime transport is not a valid requirement even on the seam.

## Exact core falsifier

Use

\[
f_a(x)=ax e^{-ax},\qquad a>0.
\]

These functions belong to both Haar spaces. Their exact inner products are

\[
\langle f_a,f_b\rangle_m=\frac{ab}{(a+b)^2},\qquad
\langle f_a,f_b\rangle_a=\frac{2ab}{(a+b)^3}.
\]

Their logarithmic separation correlation is

\[
C_{a,b}(t)=\frac{ab e^t}{(a+be^t)^2}.
\]

Take Phi=u=f_1. At s=1/2, the Mellin-normalized diagonal operation cancels the sqrt(p) factor. The fixed-base and diagonal outputs are respectively

\[
\Psi_R=f_1\otimes f_p,\qquad
\Psi_D=f_p\otimes f_p.
\]

In the relative-Haar energy norm,

\[
\mathcal E(\Psi_R)=\mathcal E(\Psi_D)=\frac1{16},
\]

but

\[
\|\Psi_R-\Psi_D\|_{\mathcal E}^2
=\frac{(p-1)^2}{8(p+1)^2}>0.
\]

At p=2 this is 1/72. The two separation readouts at zero differ by

\[
C_{p,p}(0)-C_{1,p}(0)
=\frac{(p-1)^2}{4(p+1)^2},
\]

which is 1/36 at p=2. Both retained coordinates detect the distinction. Equal marginal energies do not identify the joint state or its transport.

Moving the forcing base to f_p repairs the normalized tensor square exactly. The general repair is the source-prescribed update Phi -> U_a(p)Phi, not a fitted mixing coefficient or deconvolution.

## Positive round trips do not imply one-step conservation

Let s=1/2+z and

\[
V_s(p)=p^{-s}D_p.
\]

The relative-Haar colligation gives

\[
\mathcal E(V_s(p)\Psi)=p^{-2\operatorname{Re}z}\mathcal E(\Psi).
\]

Both factors are positive for every z. Moreover,

\[
V_s(p^{-1})V_s(p)=I,
\qquad
p^{2\operatorname{Re}z}p^{-2\operatorname{Re}z}=1.
\]

Thus the source, its positivity and its original energy are recovered by the reciprocal round trip at every z. This proves neither that one step is isometric nor that Re(z)=0. For a nonzero state, the one-step energy condition is

\[
\mathcal E(\Psi)=\mathcal E(V_s(p)\Psi)
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

The missing Xi-specific implication remains that the two stable-history routes identified at an Xi zero close this particular one-step energy comparison. Neither state placement nor the reciprocal inverse law supplies it.

## Falsification and disposition

Rival claims were: (a) the fixed-forcing graph already intertwines the diagonal modular prime action without changing its base; (b) only a moving-base family does so; (c) a positive reciprocal round trip forces each leg to preserve energy. The exact Haar-core test rejects (a) and (c), while constructing (b). It does not replace the original energy-level closure condition with the stronger, impossible state-invariance condition.

Reproduce:

```text
python research/nima/checkers/check_fixed_forcing_vs_diagonal_haar_transport.py
```

The dependency-free rational checker verifies the two Haar Gram laws, positive Gram pivots on four independent profiles, 256 correlation covariance checks, four primes, composition, recovery, and positive inverse multiplier cancellation at five centered real parts. It deliberately retains the p=2 unequal-state/equal-energy hostile. Result: `research/nima/results/fixed-forcing-vs-diagonal-haar-transport.json`.

Surviving conclusion: the source realization and reverse recovery exist, and diagonal prime covariance is a moving-base construction. The relative-Haar energy-cycle law on every Xi state remains open. No independent spectral-to-label realization is still being requested by this audit.

## Source references

- `research/nima/fixed-forcing-correlation-graph-is-the-density-to-haar-comparison.md`
- `research/nima/evans-to-joint-response-source-map-and-fixed-marginal-hostile.md`
- `research/voevodsky/one_leg_relative_haar_tensor_constructs_the_pair_modular_colligation_20260908.md`
- `research/nima/correction-haar-cycle-closure-is-energy-equality-not-state-equality.md`
- `research/nima/xi-torsion-lift-iteration-20-final-disposition-the-two-strict-range-theorems-do-not-form-the-claimed-Xi-torsion-equivalence.md`
