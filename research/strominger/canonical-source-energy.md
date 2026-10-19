# Located and replayed: canonical source energy calculation

## Authoritative prior calculation

The existing source-bound calculation is in

- `research/nima/relative-anchor-canonical-chart.md`;
- `research/nima/checkers/check_relative_anchor_canonical_chart.py`, especially the all-port derivation starting at line 123.

It derives each addressed Hamiltonian from the existing source exchange projector and inherited metric, rather than proposing a new energy from the carrier dimension or transfer count. The underlying pulse adapter is `research/nima/checkers/check_seed_port_exchange_binding.py`.

## Formula and its inputs

The live registry contains AB, BC, CA, BA, AD, DB. Put

    G=10I+ones,
    H=G tensor G,
    f_ab=e_(a,b)/11,
    F=[f_AB,...,f_DB],
    K=I+F^T H F.

All diagonal entries of K are 2. Off-diagonal feature overlaps are 1/11 when one endpoint coordinate agrees and 1/121 when both differ.

For nonzero retained anchor c, center the six record coordinates using

    s=F^T H f_AB, b=K^-1 s,
    u=conj(c/|c|)(r-bc),
    q=Re u, p=2K Im u.

The energy generating port i is exactly

    h_i(q,p)=(Kq)_i²/2+p_i²/8.

Writing x=(q,p) and h_i=x^T H_i x,

    H_i=diag(K e_i e_i^T K/2, e_i e_i^T/8),
    xdot=A_i x, A_i=2J H_i.

The inherited complex projector is D_i=e_i e_i^T K/2. The comparison C=I+iK^-1/2 satisfies C A_i=-i D_i C. Thus the Hamiltonian follows the actual continuous source pulse, not just its final reflection.

Each A_i³=-A_i, giving

    U_i(theta)=I+sin(theta)A_i+(1-cos(theta))A_i².

At theta=pi this is the exact original exchange's cotangent lift. Port generators do not commute; this is an ordered pulse process, not the autonomous flow of sum h_i.

## Actual source preparation and energy values

Use the prior supplied preparation: only the AB record has amplitude one, carrier y=0, anchor c=1. Then

    q=K^-1 e_AB, p=0,
    h_AB=1/2,
    h_BC=h_CA=h_BA=h_AD=h_DB=0.

For the valid chronological history AB, BA, AB, BA, the active pulse energies at their successive starts are:

| Pulse | Energy |
|---|---:|
| AB | 1/2 |
| BA | 1/29282 |
| AB | 107164800/214358881 |
| BA | 857376961/6276856753442 |

Each addressed h_i remains constant during its own pulse. Switching to a different addressed Hamiltonian is not a statement that every h_j is conserved.

## Do not confuse energy with the conserved quadratic budget

Every pulse preserves

    Q=mu |c|² + q^T K q + p^T K^-1 p/4,
    mu=1-s^T K^-1 s.

For this preparation:

    mu=1707483601/3429275607,
    active budget=1721792006/3429275607,
    Q=1.

The sum of addressed energies changes under an AB pulse even though Q stays one. Therefore Q, h_i and sum h_i are different observables. The action primitive retains its endpoint term:

    p dq-Q dphi-d(q^T p)/2.

Our independent replay checks the fixed-reference primitive; the original prior checker supplies the full reference-pair derivation.

## Fresh verification

```sh
python research/strominger/checkers/check_canonical_source_energy.py
```

Twelve exact checks passed, including:

- source metric and centered projector reconstruction;
- all six Hamiltonian/intertwiner identities;
- symplecticity, pulse energy and budget conservation;
- exact midpoint and endpoint states for the four occurrences;
- complete reverse recovery;
- the retained action endpoint term;
- refusal to identify summed pulse energy with the conserved budget.

The replay uses the live registry and verifies the preceding source-operation receipt's bound file hashes. It does not run the original large SymPy/NumPy dependency chain or replace its shared stores.

Matrices, canonical generators, states and provenance are in `research/strominger/results/canonical-source-energy.json`.

This locates and independently calculates the canonical source pulse energy. Its parameter is the existing pulse angle. Physical time/action normalization and an operation-preserving particle adapter are separate from this completed retrieval and replay.
