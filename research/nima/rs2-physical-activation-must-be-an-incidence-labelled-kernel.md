# RS-2: physical activation must be an incidence-labelled kernel

## Tensor obstruction

Let \(A_{\rm occ}\) be the six-dimensional occurrence module and \(V\) the
rank-four cosmological coefficient fiber. Modulo three, the two-orbit norm
homology has dimension two, so the coefficient-valued syndrome has dimension

\[
\dim\bigl(H(N_{\rm occ})\otimes V\bigr)=2\cdot4=8.
\]

The declared scalar source readout factors as

\[
R_{\rm occ}\otimes\ell
\]

for a coefficient covector \(\ell\). But

\[
H(N_{\rm occ})\subseteq\ker R_{\rm occ}.
\]

Therefore, for every \(\ell\),

\[
\boxed{
(R_{\rm occ}\otimes\ell)
\big|_{H(N_{\rm occ})\otimes V}=0.
}
\]

Changing the global coefficient projection cannot repair this. The
annihilation occurs in the occurrence-label factor before the coefficient
fiber is read.

## Consequence

Any nonzero physical activation of the syndrome must be nonfactorizable:

\[
\boxed{
\text{occurrence-labelled coefficient kernel}
\neq
\text{global occurrence sum}\otimes\text{coefficient covector}.
}
\]

The required map must distinguish at least some lower-denominator
occurrences while coupling that distinction to residue or coefficient data.
This points toward an iterated residue, incidence Gysin map, or relative-chain
kernel. It rules out searching for another universal row of the rank-four
connection.

Occurrence forgetting is the first example of the required label sensitivity:
it is nonzero on norm homology because it retains the marked Cut. It is not
yet a scalar physical period.

## Architectural meaning

The hidden order-three record is not stored in the coefficient lens alone and
not in the final readout alone. It lives in their correlation. A readout that
forgets labels before pairing necessarily destroys it.

## Durable evidence

- Entries 356, 764, 1552, and 1553;
- research/nima/checkers/check_rs2_factorized_readout_no_go.py;
- research/nima/results/rs2-factorized-readout-no-go.json.
