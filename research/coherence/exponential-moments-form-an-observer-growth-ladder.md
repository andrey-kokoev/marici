# Exponential moments form an observer-growth ladder

## Finite labelled packet

Let a finite flux or Green packet have coefficients \(u_i\) at distinct positive multiplicative positions

\[
y_1,\ldots,y_n.
\]

For an integer exponent \(\lambda\), define the observer

\[
q_\lambda(u)=\sum_{i=1}^n u_i y_i^\lambda.
\]

The original endpoint observers are

\[
q_{-1},q_{+1}.
\]

## Observer matrix

For exponents \(\lambda_1,\ldots,\lambda_m\), the observation matrix is

\[
V_{ri}=y_i^{\lambda_r}.
\]

Choosing distinct consecutive Laurent exponents gives a Vandermonde matrix up to invertible column rescaling. Therefore

\[
\operatorname{rank}V=\min(m,n).
\]

Each new exponent contributes exactly one independent observer until the finite packet is fully reconstructed.

## Endpoint-first schedule

A reversal-balanced observer ladder can begin with the physical endpoint pair and fill outward:

\[
-1,+1,0,+2,-2,+3,-3,\ldots
\]

Every prefix of this schedule is a consecutive Laurent interval after reordering. For ten contexts, the exact ranks are

```text
observers:            1  2  3  4  5  6  7  8  9 10
resolved rank:        1  2  3  4  5  6  7  8  9 10
unresolved dimension: 9  8  7  6  5  4  3  2  1  0
```

## Controlled forgetting

After \(m\) observers, the unresolved sector is

\[
\ker(q_{\lambda_1},\ldots,q_{\lambda_m})
\]

of dimension \(n-m\) for \(m<n\). This gives a graded replacement for the abrupt endpoint quotient:

```text
2 observers: endpoint shadow
3 observers: endpoint shadow plus total mass
4 observers: add second direct moment
...
n observers: complete labelled reconstruction
```

## Reversal

Reciprocal reversal \(y_i\mapsto y_i^{-1}\) sends

\[
q_\lambda\longleftrightarrow q_{-\lambda}.
\]

Thus observers should be added in \(\pm\lambda\) pairs when reversal closure is required. The exponent-zero observer is fixed by reversal.

## Stability caveat

Algebraic rank increases by one at every step, but generalized Vandermonde systems may be poorly conditioned. Stable observer selection should orthogonalize candidate moments against the Green Gram metric or optimize their smallest singular value. Exact rank alone does not choose the best schedule.

## Verification

```text
python research/coherence/check_exponential_observer_growth.py
```

The checker performs exact rational rank calculations for the ten-context endpoint-first ladder.

Artifacts:

- `check_exponential_observer_growth.py`
- `exponential-observer-growth.v1.json`
