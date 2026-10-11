# Unit-norm phase: Taylor-series proof

Let `c_n` and `s_n` be the rational cosine and sine coefficients, including zeros at the opposite parity. They satisfy

`(n+1)c_(n+1)=-s_n`, `(n+1)s_(n+1)=c_n`, `c_0=1`, `s_0=0`.

## All-degree identity

In the formal power-series ring over the rationals, write `C=sum c_n X^n`, `S=sum s_n X^n`. The recurrences give `C'=-S`, `S'=C`. Consequently

`(C²+S²)' = -2CS+2SC = 0`.

Characteristic zero forces every positive-degree coefficient to vanish; the constant coefficient is one. Thus `C²+S²=1` as formal series. This is an all-degree argument, not an inference from finite samples.

## Explicit finite-sum error

Truncate both series at total degree `N`, obtaining `C_N,S_N`. The coefficients of `C_N²+S_N²-1` vanish through degree `N`. For higher degree `k`, the absolute coefficient is bounded by

`sum_(j=0)^k 1/(j!(k-j)!) = 2^k/k!`.

For `|x|<=B`, therefore,

`|C_N(x)²+S_N(x)²-1| <= sum_(k=N+1)^(2N) (2B)^k/k!`.

If `N+2>=4B`, successive majorant terms have ratio at most `1/2`, yielding

`|C_N(x)²+S_N(x)²-1| <= 2(2B)^(N+1)/(N+1)!`.

This bound tends to zero and gives a precision-search algorithm using only rational arithmetic. Absolute convergence of the sine/cosine series and continuity of multiplication then give the analytic Pythagorean identity. The phase components proved in `TickCompletionPhase.agda` reduce unit norm to precisely this identity.

## Executed checks

`checkers/check_phase_pythagorean_series.py`: 305 exact checks. These cover recurrence instances, coefficients through degree 128, and uniform error certificates on radii 1, 2, 4, 8 at 8, 16, 32 bits. On radius 4, total degree 37 suffices for 32-bit norm-defect control.

## Agda transfer implemented; scheduled bound still required

`agda/TickPhaseNormTransfer.agda` defines the actual norm representative using canonical sine/cosine representatives, canonical products, and Cauchy addition. It proves that this representative descends to the operational trigonometric norm, then proves `ScheduledNormBound → phase-unit-norm` by quotient elimination.

`ScheduledNormBound` is the exact remaining hypothesis: for every input representative, the scheduled norm representative is metric-equivalent to constant one. It has not been instantiated.

Validation: cached-dependency Agda check passed; fresh closure timed out at 900 seconds. Receipts: `results/agda-TickPhaseNormTransfer-cached.json` and `results/agda-TickPhaseNormTransfer.json`.

## Schedule perturbation estimate proved in Agda

`agda/TickPhaseNormError.agda` proves the rational estimate

`|a²+b²-1| <= 4 M epsilon + delta`

from `|a|,|b|,|c|,|d| <= M`, `|a-c|,|b-d| <= epsilon`, and `|c²+d²-1| <= delta`. Here `a,b` are independently scheduled operational samples, and `c,d` are common-input Taylor controls. The proof uses the exact difference-of-squares decomposition and ordered rational magnitude bounds. Fresh dependency closure passed; receipt: `results/agda-TickPhaseNormError.json`.

For precision `2^-k`, it suffices to obtain `delta <= 2^-(k+1)` and `epsilon <= 2^-(k+3)/M` with `M>0`. This specifies the budget the schedule synchronization must meet.

## Remaining estimate

The operational sine and cosine use their own scheduled partial sums and input approximations. Transfer requires synchronizing those schedules with the common total-degree truncation above, transporting the error bound through completion multiplication, and applying metric separation. The formal-series argument and exact controls do not yet supply that Agda theorem.
