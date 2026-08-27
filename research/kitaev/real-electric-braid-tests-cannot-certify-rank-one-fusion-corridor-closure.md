# Real electric braid tests cannot certify rank-one fusion-corridor closure

## Bounded question

Can the frozen electric braid operations and fusion-channel measurements
certify that a closed \(C,C,C\to C\) fusion corridor has rank-one environment
Gram matrix?

Not by themselves. The frozen qutrit braid matrices and fusion projectors are
real. Experiments built only from real preparations, real braid words, and real
fusion effects depend only on the real part of the corridor Gram matrix. Two
valid Gram matrices can have the same real part while one has rank one and the
other rank two.

## Real operational surface

Use the fusion basis

\[
|A_L\rangle,
\qquad
|B_L\rangle,
\qquad
|C_L\rangle.
\]

The elementary electric braid matrices \(B_{12}\) and \(B_{23}\) are real.
Every braid word is therefore a real orthogonal matrix. The fusion-channel
effects

\[
P_A,
\qquad
P_B,
\qquad
P_C
\]

are real diagonal projectors.

Starting from fusion basis states and applying only these operations produces
real density matrices. Conjugating fusion effects by braid words produces real
symmetric effects.

This is the frozen real tester surface.

## What a real tester sees

After removing known intended diagonal phases, a channel-preserving corridor
acts as

\[
\rho_{ef}\longmapsto G_{ef}\rho_{ef}.
\]

Let \(\rho\) be real and symmetric and let \(M\) be a real symmetric effect.
Then

\[
\operatorname{Tr}\bigl(M\mathcal C_G(\rho)\bigr)
\]

depends on each off-diagonal Gram entry only through

\[
\operatorname{Re}G_{ef}.
\]

The imaginary parts cancel between conjugate matrix entries. Real
preprocessing and postprocessing do not change this conclusion.

Therefore every experiment on the frozen real tester surface factors through

\[
G\longmapsto\operatorname{Re}G.
\]

## Exact hostile family

For \(0\le a\le1\), define

\[
G(a)=
\begin{pmatrix}
1&-ia&1\\
ia&1&ia\\
1&-ia&1
\end{pmatrix}.
\]

Each matrix is Hermitian with unit diagonal. The vector

\[
(1,0,-1)
\]

is in its kernel. On the orthogonal span of \((1,0,1)/\sqrt2\) and
\((0,1,0)\), the determinant is

\[
2(1-a^2).
\]

Hence \(G(a)\) is positive semidefinite for the stated interval.

At \(a=1\),

\[
G(1)=vv^\dagger,
\qquad
v=(1,i,1),
\]

so \(G(1)\) has rank one and describes exact coherent closure.

At \(a=0\),

\[
G(0)=
\begin{pmatrix}
1&0&1\\
0&1&0\\
1&0&1
\end{pmatrix},
\]

which has rank two. The \(A\) and \(C\) branches share one environment ray,
while the \(B\) branch is orthogonal and therefore dephases against them.

But for every \(a\),

\[
\operatorname{Re}G(a)
=
\begin{pmatrix}
1&0&1\\
0&1&0\\
1&0&1
\end{pmatrix}.
\]

In particular, \(G(1)\) and \(G(0)\) are operationally indistinguishable to
every real-only braid-and-fusion experiment despite having different closure
rank.

## Consequence for certification

The real electric tester cannot establish the rank-one environment condition.
It may certify selected real visibilities while remaining blind to whether
imaginary coherence completes those visibilities into a pure Gram matrix.

The obstruction is not lack of sample size. It is a kernel of the admitted
tester algebra. Repeating real experiments indefinitely cannot recover the
missing antisymmetric quadrature.

Complex conjugation is a simpler ambiguity, but it preserves rank. The hostile
family is stronger: it changes the rank while preserving every real statistic.

## Minimal missing quadrature

For each pair \(e,f\), define logical quadratures

\[
X_{ef}=|e_L\rangle\langle f_L|+|f_L\rangle\langle e_L|
\]

and

\[
Y_{ef}
=-i|e_L\rangle\langle f_L|
+i|f_L\rangle\langle e_L|.
\]

Real preparations and effects access the \(X\) quadrature. Certifying a general
complex Gram entry requires one trusted route to the \(Y\) quadrature.

Equivalent additions include:

- preparing \((|e_L\rangle+i|f_L\rangle)/\sqrt2\);
- measuring \(Y_{ef}\);
- applying one trusted relative quarter phase before a real measurement;
- or using a controlled multi-copy cyclic-shift tester with a phase-sensitive
  pointer.

At least one such complex reference is necessary. Which implementation is
source authorized remains open.

## Pairwise rank-one test

Because \(G\) is a normalized Gram matrix, rank one is equivalent to

\[
|G_{AB}|=|G_{AC}|=|G_{BC}|=1.
\]

Each equality says the corresponding environment vectors lie on one ray. If
all three hold, all branches share that ray.

Thus a practical complete test may estimate both quadratures of every pair and
verify unit visibility. The phases determine the implemented logical diagonal
unitary; the moduli decide coherent closure.

Testing only the determinant is weaker under noise and can conceal which pair
first lost coherence. The pairwise report gives the first failed branch cut.

## Circularity boundary

The desired pair-channel bridge itself supplies complex relative phases. Using
that unverified actuator as the sole complex reference to certify its own
corridor is circular.

A valid certification requires:

- an independently characterized complex tester;
- a source-derived complex phase whose error model is separate from the
  corridor;
- or a multi-copy permutation instrument whose phase-sensitive pointer is
  independently verified.

The tester may be more powerful than the protected data actuator, but its
authority and faults must be typed separately.

## Relation to the associator-loop tester

The existing four-copy cyclic-shift construction shows how ordered complex
overlaps can be converted into a pointer statistic on prepared copies. It is a
candidate tester-side mechanism for the missing quadrature.

However, its controlled cyclic shift and coherent copy preparation are
themselves apparatus assumptions. The abstract trace identity does not make the
tester executable. Nor does a destructive multi-copy test synthesize the
single-copy data-plane bridge.

The distinction is useful:

- corridor certification may use sacrificial prepared copies;
- logical actuation must preserve an unknown qutrit state;
- neither capability automatically supplies the other.

## Exact falsifiers

- Real braid words claimed to generate a complex qutrit phase reference.
- Fusion-channel probabilities claimed to determine imaginary Gram entries.
- \(G(1)\) and \(G(0)\) above claimed distinguishable by a real-only tester.
- Correct real visibilities promoted to a rank-one certificate.
- More repetitions offered as a repair for the tester kernel.
- A complex quadrature inferred from complex conjugate models without an
  oriented phase reference.
- The unverified bridge used to certify its own phase-sensitive closure.
- An abstract cyclic-shift trace identity called an executable tester without
  controlled-copy apparatus.

## Machine-readable tester obstruction

```json
{
  "code": "real_tester_cannot_certify_fusion_gram_rank",
  "logical_basis": ["A", "B", "C"],
  "braid_matrices_real": true,
  "fusion_projectors_real": true,
  "accessible_gram_projection": "real_part",
  "hostile_rank_one_parameter": 1,
  "hostile_rank_two_parameter": 0,
  "hostile_real_parts_equal": true,
  "real_only_rank_certificate": false,
  "missing_quadrature": "Y_ef",
  "independent_complex_reference_required": true,
  "pairwise_unit_visibility_sufficient": true,
  "bridge_self_certification_allowed": false
}
```

## Deutschian explanation

A real interferometer can see whether two amplitudes reinforce or cancel along
one axis. It cannot tell whether missing contrast was rotated into the
orthogonal complex quadrature or leaked into an environment.

The two hostile corridors exploit exactly that ambiguity. One is perfectly
coherent with an imaginary relative phase; the other has genuinely lost the
same branch coherence. Their real shadows coincide.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier statement is a tester-kernel theorem: certification fails
when the admitted experiment family factors through a quotient that identifies
successful and failed constructors.

The quantum coefficient lens supplies complex Gram phases, real and imaginary
fusion quadratures, and rank-one purity. A purely real lens cannot certify the
complex closure condition.

## Claim boundary

This packet proves the real-tester factorization and the explicit rank-one versus
rank-two hostile pair. It identifies the missing complex quadrature. It does
not compile a physical quarter-phase reference, cyclic-shift tester, or full
qutrit process tomography apparatus.

## Process calibration

Excitement is 10/10 and confidence in the finite obstruction is 10/10. The
fusion corridor now has both a success theorem and a smallest hostile tester
kernel. The next apparatus decision is where the independent complex phase
reference comes from.
