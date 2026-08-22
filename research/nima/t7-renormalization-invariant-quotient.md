# Renormalization Reduces the Scheme-Independent T7 Frontier to Rank One

## Construction

Let

\[
R=T_7/(\operatorname{im}_{\log}+\operatorname{im}_{\rm Cut})
\]

be the previously derived rank-two residual space. It has one odd--odd line
\(R_{\rm odd}=\langle e_1\rangle\) and one supported residual line
\(R_{\rm supp}\), detected in the frozen frame by
\(e_2^\vee-e_4^\vee+180v_{\rm alg}^\vee\).

The leading physical UV counterterm maps to a nonzero mixed line in \(R\),
with a nonzero \(R_{\rm odd}\) component and generically a supported component
from the \(v_{\rm alg}\) tail. Consequently the renormalization-invariant
object is not \(R\), but

\[
R_{\rm phys}=R/\operatorname{im}(C_{\rm UV}\to R).
\]

Already the leading grade gives

\[
\dim R_{\rm phys}\le 2-1=1.
\]

## Consequence

\[
\boxed{
\text{a scheme-independent rank-two physical completion is impossible at
this level.}
}
\]

One mixed residual value may be fixed after choosing a renormalization
condition, but it is then renormalization data rather than a prediction of the
Carrier/support calculus. The only possible scheme-independent unresolved
direction is the quotient transverse to that mixed line. Lower UV grades may
remove it as well; they cannot restore a second intrinsic direction.

This changes the correct falsifier. We should no longer ask whether one bulk
period orbit detects both residual directions. We should:

1. derive the complete UV counterterm image in \(R\);
2. compute \(R_{\rm phys}=R/\operatorname{im}C_{\rm UV}\);
3. test whether the source-normalized supported Betti/Stokes map detects the
   surviving quotient.

The outcomes are now sharp:

\[
\begin{array}{c|c}
\dim R_{\rm phys}=1 &
\text{one genuine supported coefficient remains to be constructed}\\
\dim R_{\rm phys}=0 &
\text{the apparent two-line deficit was entirely renormalization structure}
\end{array}
\]

## Reproduction

```text
python research/nima/checkers/check_t7_renormalization_invariant_quotient.py
```
