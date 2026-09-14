# PF5 Failure — Verification Scripts  (v3, fully rigorous)

Code for: **"De Bruijn–Newman Kernel: Certified Failure at Order Five"**

## Requirements
```
pip install mpmath
```

---

## Rigor levels

| Script | Rigor | What it certifies |
|--------|-------|-------------------|
| `verify_pf5.py` | ✅ **Full iv certificate** | Table 4 + all 9 Table 5 entries |
| `rigorous_analysis.py` | ✅ **Full iv certificate** | C₅(u₀) < 0 on {0.001,...,0.031} |
| `critical_analysis.py` | ✅ **iv bracket certificate** | u₀* sign-change bracket (bisection) |
| `gaussian_threshold.py` | 🔷 Exploratory (mpf) | Table 6 values |

---

## Certification rules (applied in all ✅ scripts)

1. **Zero `float()`** in the certification chain — all comparisons via `iv.mpf`.
2. **Outward rounding** automatic throughout `mpmath.iv` context.
3. **Truncation margin** added as `iv._mpi('-1e-72', '1e-72')` (not Python `float`).
4. **Termination** via `t.a > iv.mpf('200')` (iv comparison, not float).
5. **Sign test**: `d.b < iv.mpf('0')` or `d.a > iv.mpf('0')` — not `float(d) < 0`.
6. **No `mpmath.diff`** — derivatives via exact polynomial recurrence:
   `P₀(v)=1`, `P_{m+1}(v) = 4v·[P_m'(v) − Cₙ·P_m(v)]`.

---

## Scripts

### `verify_pf5.py`  (~30s)
```
python verify_pf5.py
```
Certifies det(M₅) < 0 for all 10 configurations via `iv.det` on `iv.matrix`.
Output example:
```
  5  [-1.847236073e-9, ...]  <0 ✓
All 9 certified (d.b < 0): YES ✓
```

### `rigorous_analysis.py`  (~15s)
```
python rigorous_analysis.py
```
Certifies C₅(u₀) < 0 for u₀ ∈ {0.001,...,0.031}.  
Output: `0.031  [-3.127e+16, -3.127e+16]  <0 ✓`

### `critical_analysis.py`  (~40s)
```
python critical_analysis.py
```
Part 1: C_r(0.01) sign scan r=2..7 (mpf, illustrative).  
Part 2: Certified iv bracket for u₀*:
```
  C_5(L) ∈ [...],  hi < 0  ✓
  C_5(U) ∈ [...],  lo > 0  ✓
  u0* ∈ (0.031139763..., 0.031139763...)
```

### `gaussian_threshold.py`  (~5 min)
```
python gaussian_threshold.py
```
Table 6: λ₅*(u₀, h) via mpf bisection (not certified enclosures).
