# RH valuation-boundary construction splits finite incidence from rigged extension

## Question

Does the live theta source still lack valuation/Fock-to-boundary incidence, or
is the missing constructor specifically its extension through completion?

## Existing finite constructor

For a prime-Fock label ((p,k)), the finite atomic incidence is already fixed:

\[
I_k(p,k)=\frac1k p^{-k/2}\delta_{k\log p}.
\]

The primitive and square ports are (P=I_1) and (Q=I_2). At every finite
prime cutoff they are source-derived, natural under cutoff inclusion, occupy
different Fock grades, and reproduce the corresponding Tate countercurrents.

Therefore the live obstruction must not be described as absence of finite
incidence.

## Forced completion split

The two images have inequivalent growth.

- The primitive current has cumulative scale comparable to
  (e^{q/2}/q). It acts on exponentially decaying Laplace tests with decay
  strictly greater than one half, but not at the critical half-order boundary.
- The square current has logarithmic cumulative growth and defines a tempered
  positive measure. Its undamped sine readout still does not converge
  absolutely.

Thus no single ordinary Hilbert or Schwartz boundary grade carries both ports
with their required readouts. The completion object must retain at least the
typed pair

\[
\mathcal B_{\mathrm{exp}}
\oplus
\mathcal B_{\mathrm{temp}},
\]

before relative archimedean sewing and scalar compression.

## Exact surrogate

A dyadic discrete model isolates the same threshold without prime asymptotics.
Let the primitive weights be (2^n/n). Against critical tests (2^{-n}), the
terms are (1/n) and diverge. Against stronger tests (2^{-2n}), the terms
are (2^{-n}/n) and converge.

Let the square weights be (1/n). They act on rapidly decaying tests such as
(1/n^2), while the constant readout again produces the harmonic series.

The checker records exact finite partial sums and the strict separation of the
four cases. The convergence and divergence conclusions use the standard
geometric and harmonic series theorems.

## Refined missing constructor

The remaining valuation-boundary constructor is a morphism of rigged systems,
not a new finite row. It must provide:

1. the exponential primitive boundary grade;
2. the tempered square boundary grade;
3. cutoff-natural embeddings of every finite atomic current;
4. a properly supported comoving correspondence in relative coordinate
   (u=q-\log p), preventing traveling-support loss;
5. continuous archimedean and reciprocal sewing on the typed sum;
6. preservation of primitive, square, seam, endpoint, and archimedean
   distinctions;
7. agreement with every finite Euler cutoff after sewing;
8. prohibition of separate undamped scalarization before the relative
   completion exists.

## Deutschean prediction

If the split is explanatory, any attempted single-grade completion must fail
in one of two preregistered ways:

- it excludes the primitive current by imposing only tempered growth;
- or it admits the primitive current by weakening topology so far that the
  square/readout and Clark continuity gates lose control.

A successful completion must transport the two grades jointly without merging
them. That is the risky source theorem.

## Relation to the compiler ablation

Strominger's two-constructor fixture remains correct, but the first constructor
should be read as:

```text
existing finite atomic incidence
+
missing typed rigged completion extension
```

The other conjunct is the fixed finite family uniformly dominating Clark
current matrices on the common completed module. Neither can be inferred from
the other.

## Claim boundary

This packet does not construct the archimedean sewing morphism or prove its
continuity. It refines the missing-constructor statement and verifies the
forced two-grade topology in an exact surrogate. It does not prove RH.

## Disposition

Finite valuation-boundary incidence is closed. The open constructor is the
joint, distinction-preserving extension through exponential and tempered
boundary grades into the relative completed carrier.

