# Translation and reversal cannot reduce composite ancestry

Let a finite composite Gaussian primitive be

\[
p=\sum_{a\in S}c_a u_a,
\qquad c_a\neq0.
\]

Its ancestry size is the support cardinality

\[
|S|.
\]

Translation acts by

\[
U_t p=\sum_{a\in S}c_a u_{a+t},
\]

and reversal acts by

\[
Jp=\sum_{a\in S}\overline{c_a}u_{-a}.
\]

Both maps are bijections on channel labels. Therefore

\[
|\operatorname{supp}(U_tp)|
=|\operatorname{supp}(Jp)|
=|S|.
\]

No combination of forward translation and reverse-plane reflection can turn a genuine multichannel composite into a single-translate primitive.

Consequently, a negative rung-four Schwarz square propagates throughout its bidirectional time orbit but never reaches the independently positive one-channel base class. The proposed ancestry-reduction boundary theorem is false for the available transport operations.

Any support-reducing operation must instead be a quotient, fold, projection, or coarse-graining. Such maps are not automatically conservative: their kernels can contain the negative witness. A valid replacement requires

\[
Q(p)<0
\Longrightarrow
Q(Cp)<0
\]

for at least one declared reduction branch \(C\), together with termination at a genuinely source-positive base class.

The previous parity folding supplies the first implication into one branch, but its terminal leaves remain composite observations rather than known positive primitives. Thus the obstruction is now structural:

> invertible forward/reverse transport preserves ancestry, while noninvertible ancestry reduction can erase negativity.

A successful proof must construct a branching reduction family that is jointly conservative for negative squares and whose leaves have independent source positivity.

## Verification

```text
python research/voevodsky/checkers/check_translation_reversal_ancestry_reduction_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_translation_reversal_ancestry_reduction_no_go.py`
- `research/voevodsky/results/translation_reversal_ancestry_reduction_no_go.json`
