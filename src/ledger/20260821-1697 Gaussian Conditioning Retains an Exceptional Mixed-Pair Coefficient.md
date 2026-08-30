# 1697 — Gaussian Conditioning Retains an Exceptional Mixed-Pair Coefficient

## Comparison

Entry 1696 shows that direct evaluation of the correlated cubic Cut pair is
polynomial across singular covariance.  Compare it with conditioning on a
Gaussian block whose variance degenerates.

## Generic conditional formula

For centered jointly Gaussian variables `X,Y,R`, let

\[
b=\operatorname{Var}(R),
\qquad
c_X=\operatorname{Cov}(X,R),
\qquad
c_Y=\operatorname{Cov}(Y,R).
\]

For `b>0`,

\[
\mathbb E[XY\mid R=r]
=A_{XY}
+\frac{c_Xc_Y}{b}
\left(\frac{r^2}{b}-1\right).
\]

The normalized exceptional coordinates are

\[
s=\frac r{\sqrt b},
\qquad
\xi=\frac{c_Xc_Y}{b}.
\]

Hence the strict transform is

\[
\boxed{
\mathbb E[XY\mid s]=A_{XY}+\xi(s^2-1).
}
\]

## Forget-support comparison

Gaussian averaging in `s` gives

\[
\mathbb E_s[s^2-1]=0,
\]

so the unconditional observable is again `A_XY`.  Nevertheless the
conditional exceptional fiber retains the coefficient `xi` pointwise.

## Narrow result

\[
\boxed{
\text{conditioning and singular specialization retain the Rees coefficient }\xi=c_Xc_Y/b\text{ that direct pair evaluation forgets.}
}
\]

This is a support-sensitive coefficient class, not a new carrier divisor.  It
uses the same rank-one Gaussian Rees geometry already forced in Entry 1670.
The apparent discrepancy disappears only after integrating over the
conditional fiber, so ordinary forget-support comparison is too coarse.

## Durable artifacts

- `research/benincasa/checkers/conditioned_pair_rees.rs`
- `research/benincasa/results/conditioned-pair-rees.json`
- `research/benincasa/conditioned-pair-rees.md`

## Next falsifier

Insert the actual cubic Cut coefficient `c_ij=-2tw_iw_j` and assemble all
conditioned labelled pairs.  Test whether their exceptional `xi_ij` packet is
exactly the symmetric-square Rees grade of the covariance normal bundle or
requires an additional coefficient extension at pair intersections.
