# Compact-tail no-gap theorem for completed comparison mates

## Question

Can a source-native tail that repairs every finite-cutoff comparison cell also repair loss of strict invertibility in the completed Green–Ward mate?

## Claim boundary

Let \(A:H\to K\) be the completed comparison operator on the source-authorized Hilbert or rigged-Hilbert state space. Let \(T:H\to K\) be the completed tail correction. Suppose there is an orthonormal, hence weakly null, sequence \(v_n\) with

\[
\|Av_n\|\longrightarrow0.
\]

This is an essential approximate kernel: invisibility escapes through infinitely many independent directions rather than through one finite-dimensional defect.

If \(T\) is compact, then \(Tv_n\to0\). Therefore

\[
\|(A+T)v_n\|\le \|Av_n\|+\|Tv_n\|\longrightarrow0.
\]

Hence \(A+T\) is not bounded below. A compact tail cannot open a uniform gap across an essential approximate kernel.

This is stronger than the finite relative-gain bound. It permits the tail to repair every finite-dimensional kernel encountered by a cutoff scheme. What it forbids is conversion of cutoffwise injectivity into completion-stable faithfulness when the lost information escapes through weakly null modes.

### Minimal hostile model

On \(\ell^2(\mathbb N)\), let

\[
Ae_n=\frac1n e_n.
\]

Every finite truncation is invertible, but its smallest gain is \(1/N\). The completed operator is injective yet not bounded below. Any finite-rank repair changes only finitely many diagonal entries and leaves the escaping basis sequence invisible. More generally, every compact repair still satisfies \((A+T)e_{n_j}\to0\) along a subsequence.

This distinguishes three notions that cutoff rank conflates:

- algebraic injectivity: no exact kernel;
- Fredholm or essential faithfulness: no infinite-dimensional escaping defect modulo compact errors;
- coercivity: a positive lower gain on the full authorized state space.

### Smallness is not the classifier

Let \(0<\varepsilon\ll1\). The operator \(\varepsilon I\) is norm-small but noncompact on an infinite-dimensional state space, and

\[
\|\varepsilon Iv\|=\varepsilon\|v\|.
\]

It opens a uniform gap \(\varepsilon\). Conversely, a finite-rank operator may have arbitrarily large norm and still be unable to see an orthogonal escaping sequence.

Therefore the completion-bearing distinction is not large tail versus tiny tail. It is:

\[
\text{coercively extensive support}
\quad\text{versus}\quad
\text{compact or smoothing support}.
\]

A source-native exponentially small coefficient can be completion-decisive if it multiplies an extensive identity-like or elliptic symbol. An analytically prominent correction can be completion-irrelevant if it occupies only finitely many label or character directions.

### Characterwise essential spectrum

For the Fourier boundary decomposition

\[
H=H_1\oplus H_{-1}\oplus H_i\oplus H_{-i},
\]

an equivariant mate splits as \(A=\bigoplus_\chi A_\chi\). Uniform conditioned coherence requires every reachable block to be bounded below. One block with an essential approximate kernel defeats the aggregate comparison, even if all scalar-visible blocks are coercive.

The modular tail must therefore be classified in each character sector by:

1. whether its restriction is compact, relatively compact, or coercive;
2. whether the uncorrected block has a finite kernel or an essential approximate kernel;
3. whether the tail changes only isolated singular values or shifts the bottom of the essential spectrum;
4. whether these properties are natural under cutoff refinement.

A scalar invariant section observes principally the trivial character. It cannot certify the essential gap of odd boundary characters.

### Relation to the four escape mechanisms

The compact-tail theorem refines the earlier list.

- Authorized localization removes the escaping sector from the task object.
- Relative renormalization changes which sequences are normalized and must be fixed before compactness is assessed.
- Independent observation must be noncompact or coercive on the escaping sector; a finite set of bounded rank-one rows cannot control an infinite orthonormal escape.
- Dynamical exposure can work when the observability Gramian accumulates order-one energy on every escaping mode, even though the instantaneous observation is compact. This requires a uniform dynamical estimate, not finite-time rank alone.

### Grothendieck-facing decision tree

The next source audit should determine the operator class of the completed modular residue before attempting another positivity argument.

First construct the tail as a map between the actual rigged source and boundary spaces. Then test:

- Does an authorized weakly null normalized sequence exist on which the uncorrected mate tends to zero?
- Is the tail compact or relatively compact on that topology?
- Does the tail's principal symbol act nontrivially on every such sequence?
- Does the corrected block possess a coercive estimate, or only injectivity?

If the first two answers are yes, the tail cannot be the missing completion constructor. It may still be the exact seam-sewing residue or may repair a finite-dimensional mate torsor, but another extensive constructor is necessary.

If the tail is noncompact because it acts diagonally with a uniformly nonzero principal symbol on the escaping labels, its exponentially small coefficient is not an obstruction: it can open a small but genuine gap.

### Categorical interpretation

Compact corrections are invisible in the Calkin quotient. The completed comparison has a stable mate only if its image in that quotient is left-invertible on the reachable object. Thus the completion-level Beck–Chevalley question factors into two layers:

1. essential coherence in the quotient by compact morphisms;
2. finite-defect repair inside the compact ideal.

The tiny modular tail can solve the second layer without solving the first. This is the infinite-dimensional analogue of a local syndrome repair that fixes finitely many representatives while leaving the global logical sector unresolved.

## Disposition

The highest-information next test is an essential-spectrum audit of the character-valued Green–Ward mate. Cutoffwise determinant and rank calculations are structurally incapable of deciding it.

The decisive falsifier is a weakly null normalized source sequence \(v_n\) for which both the uncorrected mate and the modular tail tend to zero. Such a witness proves that the tail, despite exact seam importance, cannot supply completion-stable coherence.

The decisive positive certificate is a source-derived coercive principal-symbol estimate on every reachable Fourier character block. This would show that the tail is not merely a compact repair but an extensive component of the completed coherencer.