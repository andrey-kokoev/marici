# Von Mangoldt support forbids coprime tensor interchange term by term

The arithmetic part of the centered Weil distribution has translation
coefficients supported at prime powers:

```
w(n)=Lambda(n)/sqrt(n).                               (1)
```

For distinct primes `p!=q`,

```
w(p)>0,       w(q)>0,       w(pq)=0.                 (2)
```

Thus the direct arithmetic edge at displacement `log(pq)` vanishes, whereas
the product of the `log p` and `log q` edge weights is nonzero:

```
w(p)w(q)=(log p)(log q)/sqrt(pq)>0.                  (3)
```

Consequently the arithmetic Weil block cannot satisfy the exact tensor law
`r_pq=r_p r_q` or the coprime Mackey interchange required by the product
kernel. Euler multiplicativity concerns the product of local factors; after
taking the logarithmic derivative, it becomes an additive prime-power
distribution and deliberately has no mixed-composite atoms.

## Completed-form consequence

The coprime tensor gluing theorem remains a valid sufficient positivity
theorem, but it is not realized termwise by the source arithmetic current.
Any completed rectangle identity would have to be produced by the global
gamma/endpoint cross form or by an auxiliary Schur completion. It cannot be
claimed from unique factorization or Euler multiplicativity alone.

This makes the mixed rectangle defect unavoidable rather than a small error.
For `0,log p,log q,log(pq)`, the direct edge and the two-step routes have
different support provenance. Their even/odd parity inequalities must be
tested on the completed Weil form; exact tensor factorization is generally
the wrong target.

## Revised role of Mackey structure

Mackey coherence may still organize the two-step route and provide a
contractive dilation of the missing direct edge. But the dilation must retain
the logarithmic-derivative support rule `Lambda(pq)=0`. A construction that
fills the direct arithmetic edge with `w(p)w(q)` changes the explicit formula
and is falsified before any positivity test.

