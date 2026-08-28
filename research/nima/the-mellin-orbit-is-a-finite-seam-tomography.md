# The Mellin Orbit Is an Off-Diagonal Seam Tomography

## Question

The primitive density and the seam image have the same diagonal. A single
scalar seam energy therefore cannot distinguish them. The source already
supplies a nontrivial family of comparisons, however: Mellin phase transport.
The question is whether that family sees the missing off-diagonal carrier.

For a finite prime packet \(c=(c_p)\), define

\[
S_t(c)=\sum_p c_p p^{-1/2-it}
\]

and observe its boundary energy

\[
E_c(t)=|S_t(c)|^2.
\]

Expansion gives

\[
E_c(t)=\sum_{p,q}
\frac{\overline{c_p}c_q}{\sqrt{pq}}
e^{it(\log p-\log q)}.
\]

The constant Fourier coefficient is the diagonal prime-square current. Every
nonzero Fourier coefficient is a cross-prime seam comparison.

## Finite tomography theorem

For ordered pairs of distinct primes, the frequencies

\[
\log p-\log q=\log(p/q)
\]

are distinct. Indeed, equality of two such frequencies gives \(p/q=r/s\),
so \(ps=rq\). Unique factorization then forces \(p=r\) and \(q=s\).

Consequently the Mellin orbit \(t\mapsto E_c(t)\) recovers every
off-diagonal coefficient

\[
\frac{\overline{c_p}c_q}{\sqrt{pq}}
\]

of the rank-one seam carrier \(bb^*\), where \(b_p=c_p/\sqrt p\). This is
exactly the cross-label information destroyed by diagonal observation.

The zero frequency needs separate typing. It contains only

\[
\sum_p |c_p|^2/p,
\]

not the individually labelled diagonal entries. Therefore the Mellin orbit
alone does not recover the full carrier. A packet supported at one prime has
constant energy, and the same constant can be produced at another prime by
rescaling its coefficient. This is the minimum hostile witness.

Full finite carrier tomography is obtained only from the jointly typed pair:
the labelled primitive diagonal and the Mellin orbit of seam energy. The first
port supplies each diagonal entry; the nonzero Mellin frequencies supply every
ordered off-diagonal entry. Neither port substitutes for the other.

The result is source-compatible: no auxiliary phase probe is invented. The
transport \(c_p\mapsto p^{-it}c_p\) is the Mellin character already present in
the Tate parameter.

## Typed factorization

The correct route is:

```text
labelled prime amplitudes
  -> Mellin phase transport
  -> global seam synthesis
  -> quadratic observation
  -> Fourier coefficient extraction
  -> cross-prime carrier entries
```

Quadratic observation at only \(t=0\) is not faithful. Quadratic observation
over the full Mellin orbit is faithful on the off-diagonal part. Together with
the labelled primitive diagonal it is faithful on every finite seam carrier.

This does not yet prove a completion theorem. In an infinite packet, Fourier
coefficient extraction requires a declared distribution or almost-periodic
topology, and accumulation or loss at infinity remains possible. The present
result fixes the finite comparison functor that any completion must extend.

## Minimum falsifiers

Three failures close a proposed implementation:

1. If it returns only the zero-frequency coefficient, it has collapsed back
   to the diagonal prime-square current.
2. If two distinct ordered prime pairs are assigned the same nonzero
   frequency, its label transport violates unique factorization.
3. If it claims to recover labelled diagonal entries from the Mellin orbit
   alone, two rescaled single-prime packets falsify it.

For the packet \(\{2,3,5\}\), all six ordered off-diagonal ratios are distinct.
The checker verifies their reconstruction and the sparse-support diagonal
falsifier.

## Frontier

The remaining question is no longer whether the source contains a comparison
capable of seeing seam coherence. It does, finitely, but only as one member of
a two-port observation system. The exact frontier is whether the labelled
diagonal and Mellin off-diagonal tomography extend jointly and faithfully
through the source-selected arithmetic completion, including the primitive
boundary current and the completion-at-infinity channel.
