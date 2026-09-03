# Completion with a controlled asymptotic radical

## Question

Can mixed-bridge completion survive loss of uniform global coercivity when the collapsing sector is explicitly typed and quotient-compatible?

## Claim boundary

This packet constructs a synthetic completion theorem replacing global coercivity by uniform coercivity on a declared complement. It does not construct the missing arithmetic transition maps for Weil cutoffs.

## Filtered form model

Let a Hilbert space split as

\[
H=R\oplus P,
\]

where \(R\) is a fixed finite-dimensional nominated vanishing sector and \(P\) is its typed complement. For positive \(\varepsilon_N\to0\), define

\[
q_N(r,p)=\varepsilon_N\lVert r\rVert^2+q_P(p),
\]

where \(q_P\) is closed and satisfies \(q_P(p)\ge c\lVert p\rVert^2\) for fixed \(c>0\).

Every finite \(q_N\) may be positive definite while the limit

\[
q_\infty(r,p)=q_P(p)
\]

has radical exactly \(R\). The quotient forms on \(H/R\cong P\) are all exactly \(q_P\), hence closed, uniformly coercive, and strictly compatible with identity transition maps.

## Categorical certificate

A controlled-radical completion cell contains:

1. a source-derived nominated sector \(R_N\) at each cutoff;
2. transition maps carrying \(R_N\) into \(R_{N+1}\);
3. induced maps on quotients;
4. convergence of quotient forms;
5. uniform coercivity on quotient complements;
6. proof that no additional limiting radical appears.

Composition is defined only when nominated sectors and quotient maps agree at the pasted boundary. Associativity then follows from functoriality of quotient maps and ordinary closed-form composition on the uniformly coercive quotient system.

## Exact fixture

The checker uses \(R=\mathbb Q^2\), a three-dimensional physical complement, \(\varepsilon_N=1/N\), and quotient weights \((2,3,5)\). Finite determinants tend to zero, while every quotient Gram matrix remains \(\operatorname{diag}(2,3,5)\). A hostile transition mixing one radical basis vector into the physical complement fails to descend because equivalent representatives acquire different quotient images.

## Relation to the Weil rectangle response

Grothendieck's reported \(\theta\to1\) excludes the previous uniform-global-coercivity route but is compatible with this theorem if the rank-two asymptotic radical and its cutoff transition maps are source-derived. The reciprocal Mellin-Schwartz algebra supplies a candidate common algebraic core, not those transition maps or an intertwiner into the Green target.

## Disposition

Controlled-radical completion is analytically and categorically realizable. For the radial programme, the first missing typed object is now sharper: a source-side transition map between cutoff quotient spaces preserving the rank-two wedge/radical classes. Without it, the synthetic theorem cannot be applied.

## Verification

- `research/voevodsky/checkers/check_controlled_asymptotic_radical_completion.py`
- `research/voevodsky/results/controlled_asymptotic_radical_completion.json`
- `research/grothendieck/voevodsky-completion-audit-meets-weil-rectangle-gap-collapse.md`
