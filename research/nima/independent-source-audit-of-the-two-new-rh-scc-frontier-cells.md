# Independent source audit of the two new RH SCC frontier cells

This audit answers Aspect event 10296. The two cells are tested independently.
Algebraic existence is not treated as source realization.

## 1. valuation_fock_passive_dilation

For each prime, put \(a_p=p^{-1/2}\), \(L_p=\log p\). The local transfer is

\[
r_p(z)=a_pe^{izL_p}.
\]

The attenuation has the Julia unitary

\[
U_p=
\begin{pmatrix}
a_p&\sqrt{1-a_p^2}\\
\sqrt{1-a_p^2}&-a_p
\end{pmatrix}.
\]

Cascading its signal port with the lossless delay gives an abstract passive
two-port realization. Typed direct sum over primes gives an algebraic unitary
dilation of the prime-diagonal Schur operator. It does not identify that
dilation with the valuation/Fock source carrier.

### Exact source locators and dependencies

1. research/nima/the-euler-packet-is-a-hilbert-schmidt-schur-operator-not-a-scalar-schur-sum.md
   - ordered prime-diagonal Schur operator, ideal filtration, direct-sum law;
   - type: constructed algebraic carrier.

2. research/nima/finite-prime-diagonality-is-source-exact-only-completion-can-mix-fibers.md
   - finite valuation/Fock idempotents \((p,k)\);
   - type: constructed finite labeling; completed intertwining open.

3. research/nima/lossless-two-addition-colligation-requires-reciprocal-doubling.md
   - source-derived lossless cut/delay colligation and reciprocal doubling;
   - type: constructed source colligation; Euler cyclic/Fock comparison
     explicitly missing.

4. research/nima/euler-half-density-makes-labelled-volterra-incidence-contractive-on-transported-fibers.md
   - cutoff-uniform contraction conditional on label preservation;
   - type: conditional analytic bound.

### Verdict and hostile

The cell is algebraically inhabited but not source-realized. The missing map is

\[
(p,1)\text{ valuation/Fock fiber}
\longrightarrow
\text{signal plus defect-bath ports of }U_p,
\]

intertwining label idempotents, source vacuum, delay, reciprocal doubling, and
cutoff direct sums.

Smallest hostile: use two primes with correct local compressions \(r_p,r_q\)
but identify their defect ports with one common bath line. Each one-prime
transfer is passive and scalar-correct, while the combined dilation is not a
valuation direct sum and can acquire cross-prime feedback.

## 2. primitive_wall_trace_completion

The completion differential factors as

\[
\partial_u^2-\frac14
=
\left(\partial_u-\frac12\right)
\left(\partial_u+\frac12\right).
\]

Its two primitive traces are

\[
M_-(g)=\int e^{-u/2}g(u)\,du,
\qquad
M_+(g)=\int e^{u/2}g(u)\,du.
\]

Twisted causal histories realize these as outgoing traces. The bilateral
trace bundle has rank two on the full test domain and an exact object-indexed
Mellin metric.

### Exact source locators and dependencies

1. research/nima/the-completion-trace-requires-half-density-twisted-history-not-plain-volterra-history.md
   - two twisted causal resolvents and traces;
   - type: constructed analytic history channels.

2. research/nima/the-full-relative-completion-trace-has-rank-two.md
   - rank two on the full domain but rank one on the frozen theta ray;
   - type: analytic capacity constructed; arithmetic-orbit rank open.

3. research/nima/mellin-half-density-transport-exactly-preserves-the-bilateral-trace-frame.md
   - exact transported metric and scale-independent frame;
   - type: constructed object-indexed Hilbert bundle; no fixed Adams-end
     Hilbert space.

4. research/nima/reflection-equivariance-reduces-causal-history-incidence-to-a-two-channel-schur-cell.md
   - required parity incidence \(C=\operatorname{diag}(c_+,c_-)\);
   - type: algebraic reduction; source extraction of \(c_\pm\) open.

### Verdict and hostile

This cell is not yet inhabited. The trace bundle and history targets exist,
but the source map

\[
\mathcal I_{\mathrm{prim}}:
\mathcal O_\theta^{(p,1)}
\longrightarrow
H_+\oplus H_-
\]

has not been derived. No theorem proves that the frozen primitive theta orbit
supplies both channels or that their completion is the missing
\(\mathfrak S_1\) trace component.

Smallest hostile: \(c_+\ne0\), \(c_-=0\). Both traces and a positive causal
block exist, and the even scalar readout may be correct, but the reciprocal
odd history is dark. A second hostile uses plain Volterra history, which
lands at zero frequency rather than the two half-density characters.

## Do the cells meet?

Not yet. Their port shapes are compatible, but no source comparison identifies
a valuation defect-bath port with a primitive wall trace channel.

The earliest lawful candidate is a source Cayley relation

\[
\mathcal B_p(z):
\text{passive prime boundary ports}
\dashrightarrow
\text{primitive causal wall ports},
\]

followed by reciprocal and archimedean attachment. Its graph can define a
completed boundary pencil only after proving prime-label preservation,
two-channel incidence, reciprocal adjoint orientation, feedback
well-posedness, and compatibility with the det2/primitive-trace comparison.

This is a candidate type, not an inhabited constructor. No coercivity,
divisor, or Xi identification follows.
