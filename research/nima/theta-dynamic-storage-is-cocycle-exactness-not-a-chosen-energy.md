# Dynamic storage is cocycle exactness, not a chosen energy

## Status

Research packet. This reframes the dynamic Green-current identity as a
cohomological extension problem and derives a storage-independent finite
falsifier. It does not prove that the theta/Tate cocycle is exact.

## Transport coefficient system

Let each authorized interval arrow (a\to b) carry a state transport

\[
S_{ab}:V_a\longrightarrow V_b.
\]

Hermitian forms are transported contravariantly by

\[
\rho_{ab}(X)=S_{ab}^{*}XS_{ab}.
\]

The relationship Gramian and typed boundary supply obey the same affine
composition law:

\[
W_{ac}=W_{ab}+\rho_{ab}(W_{bc}),
\qquad
B_{ac}=B_{ab}+\rho_{ab}(B_{bc}).
\]

Their difference

\[
C_{ab}=W_{ab}-B_{ab}
\]

is therefore a one-cocycle:

\[
C_{ac}=C_{ab}+\rho_{ab}(C_{bc}).
\]

## Storage is a primitive of the cocycle

The dynamic residual equation

\[
W_{ab}+S_{ab}^{*}P_bS_{ab}-P_a-B_{ab}=0
\]

is equivalent to

\[
C_{ab}=P_a-\rho_{ab}(P_b).
\]

Thus the RH-bearing source question is not whether one can choose an appealing
positive storage form. It is whether the source-derived cocycle (C=W-B) is
an exact coboundary in the transported Hermitian-form coefficient system.

This identifies the precise meeting point of control theory and categorical
coherence:

- control theory supplies storage, supply, and observability Gramians;
- category theory supplies arrows, pullback transport, cocycles, and
  obstruction classes;
- the theta/Tate source must decide whether the resulting class vanishes.

## Storage gauge

Storage representatives are not automatically unique. If endpoint forms are
changed by (K_a), then preserving the same residual requires

\[
P_a\mapsto P_a+K_a,
\qquad
B_{ab}\mapsto
B_{ab}+\rho_{ab}(K_b)-K_a.
\]

Consequently, no positivity conclusion may depend on an arbitrary storage
representative. It must either be invariant under this gauge or come with a
source-derived normalization that fixes it.

## Closed-loop obstruction

Consider a composable closed path ℓ based at (a). Its accumulated cocycle
is (C_\ell), and exactness requires

\[
C_\ell=P_a-S_\ell^{*}P_aS_\ell.
\]

When source coherence gives (S_\ell=I), exactness forces

\[
C_\ell=0.
\]

Therefore a closed authorized transport loop with identity endpoint transport
but nonzero accumulated (W-B) is a storage-independent finite falsifier. No
choice of (P) can repair it.

This is stronger than checking one residual after fitting endpoint storage:
the loop cancels the storage gauge before evaluation.

For a nonidentity loop, the obstruction is the class of (C_\ell) modulo the
image of

\[
P\longmapsto P-S_\ell^{*}PS_\ell.
\]

A witness in the cokernel of this map again disproves exact storage.

## Smallest theta test

The first source-specific audit should use the smallest doubled Clark–Green
segment and its reciprocal return:

1. construct the forward and reciprocal transports without scalar
   projection;
2. concatenate them into the source-authorized return loop;
3. verify whether the total state transport is identity;
4. accumulate the Gramian and every typed boundary incidence along both legs;
5. compute (C_\ell=W_\ell-B_\ell);
6. reject exact storage immediately if (C_\ell\ne0).

Only if the loop obstruction vanishes should one solve for endpoint storage
forms and ask whether a positive representative survives completion.

## Conclusion

The control-theoretic oddball has exposed a categorical invariant. The missing
Green-current law is the assertion that a source-derived relationship-energy
cocycle is exact. Closed-loop cocycle charge is its finite, gauge-independent
falsifier.
