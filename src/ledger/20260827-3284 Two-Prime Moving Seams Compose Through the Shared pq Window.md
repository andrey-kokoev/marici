# 3284 — Two-Prime Moving Seams Compose Through the Shared pq Window

For commuting prime shifts, the second seam must be evaluated in the already
shifted chart. Its interval runs from \(\log p\) to
\(\log p+\log q\), giving the exact concatenation

\[
B_{pq}=B_p+B_{q\mid p}=B_q+B_{p\mid q}.
\]

Consequently both prime-addition orders produce the same endpoint corner

\[
r_pr_q(F-B_{pq}).
\]

For the full depth-one valuation square, the Evans endpoint equals the bare
Euler product plus the three source-derived boundary windows, including the
mixed \(pq\) window. The same shared \(pq\) state therefore carries both the
endpoint-seam coherence and the previously derived det3 anomaly.

This identifies the first finite common-lift candidate: the four states
\(1,p,q,pq\) with their transported interval incidences. Its endpoint shadow
must give seam concatenation and its determinant shadow must give the det3
cocycle.

- Research packet: research/grothendieck/two-prime-moving-seams-compose-through-the-shared-pq-window.md
- Checker: research/grothendieck/checkers/check_two_prime_moving_seam_composition.py
- Sequence claim: seqclaim-90f1bc033c647942a827d016
- Graph event: 6962
