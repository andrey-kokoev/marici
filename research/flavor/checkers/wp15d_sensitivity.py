#!/usr/bin/env python3
"""WP15d -- App-II.a / Fig-S2 sensitivity reproduction.

For the Fig.-2 texture (class 4 of the phi=pi/2 fixed-phase classes), switch
on each of the nine vanishing entries one at a time at its hierarchical size
    Y_ij ~ sqrt(y_i * y_j)        (= sqrt(m_i m_j)/v, paper Eq. S37 context)
and compute the numerical derivative of alpha (Eq. S37), in degrees, for
purely real and purely imaginary perturbations, retaining the smaller of the
two signs in each case.

Paper expectation (App. II.a): Y^u_13, Y^d_13, Y^d_32 must be suppressed by
1-2 orders of magnitude vs. their natural values independently of phase;
Y^d_11 (real) and Y^u_21 (imaginary) become dangerous only at projected
LHCb precision.

Candidate Fig.-2 members (constraints: loop = {u12,d12,u22,d22} 4-cycle,
u21 = 0, d11 = d13 = d32 = 0, R_alpha ~ D12/U12 = d12 u22 / (d22 u12)):
    (275, 314)  orbit 17   Yd = {d12,d21,d22,d23,d33}
    (275, 370)  orbit 15   Yd = {d12,d22,d23,d31,d33}
    (275, 346)  orbit 15   Yd = {d12,d21,d22,d31,d33}  (control: no d23 ->
                           Vcb ~ 0 at LO, expected unviable)
Fits pin phi = pi/2 (App. II.a procedure) with 9 free magnitudes.
"""

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wp7_ensemble", HERE / "wp7_ensemble.py")
wp7 = importlib.util.module_from_spec(spec)
sys.modules["wp7_ensemble"] = wp7
spec.loader.exec_module(wp7)

PHI_FIXED = math.pi / 2.0
CANDIDATES = [(275, 314), (275, 370), (275, 346)]
N_STARTS = 48
SEED = 20260822


def fit_pinned(mask_u, mask_d, phase_sector, phase_slot, phi=PHI_FIXED, n_starts=N_STARTS, seed=SEED):
    """Fit the 9 magnitudes with phi pinned at PHI_FIXED.

    Mirrors wp7.fit_member's two-stage bounded strategy (mass-only
    pre-fit, then full 17-observable trf) with phi removed from the
    variable set."""
    us, ds = wp7.mask_slots(mask_u), wp7.mask_slots(mask_d)
    nat = np.array([wp7.natural_value("u", s) for s in us]
                   + [wp7.natural_value("d", s) for s in ds])
    log_nat = np.log(nat)
    lb = log_nat - 6.0 * math.log(10.0)
    ub = log_nat + 3.0 * math.log(10.0)
    rng = np.random.default_rng(seed)

    def resid(logm):
        theta = np.concatenate([logm, [phi]])
        Yu, Yd = wp7.build_texture(mask_u, mask_d, phase_sector, phase_slot, theta)
        with np.errstate(all="ignore"):
            obs = wp7.observables17(Yu, Yd)
        obs = np.where(np.isfinite(obs), obs, 1.0e6)
        return (obs - wp7.CENTRAL) / wp7.SIGMA

    best = None
    for _ in range(n_starts):
        t0 = np.clip(np.array(wp7.start_point(us, ds, rng), dtype=float), lb, ub)
        try:
            s1 = least_squares(lambda t: resid(t)[:6], t0, bounds=(lb, ub),
                               max_nfev=8000)
            if 2.0 * s1.cost > 25.0:
                continue
            s2 = least_squares(resid, s1.x, bounds=(lb, ub), method="trf",
                               xtol=1e-12, ftol=1e-12, gtol=1e-12,
                               max_nfev=50000)
        except Exception:
            continue
        chi2 = float(2.0 * s2.cost)
        if best is None or chi2 < best["chi2"]:
            best = {"chi2": chi2, "log_mags": [float(v) for v in s2.x]}
    return best


def alpha_deg(Yu, Yd):
    return float(wp7.observables17(Yu, Yd)[12])


def s37_table(mask_u, mask_d, phase_sector, phase_slot, log_mags, phi=PHI_FIXED, eps=1e-6):
    """Eq. S37 derivative of alpha (degrees) for each vanishing entry."""
    theta = np.concatenate([log_mags, [phi]])
    Yu0, Yd0 = wp7.build_texture(mask_u, mask_d, phase_sector, phase_slot, theta)
    a0 = alpha_deg(Yu0, Yd0)
    rows = []
    for sector in ("u", "d"):
        mask = mask_u if sector == "u" else mask_d
        for slot in wp7.SLOTS:
            k = wp7.SLOTS.index(slot)
            if mask >> k & 1:
                continue
            h = wp7.natural_value(sector, slot)
            rec = {"sector": sector, "slot": list(slot), "hierarchical_size": h}
            for kind, unit in (("imag", 1j), ("real", 1.0)):
                vals = []
                for sign in (+1.0, -1.0):
                    d = eps * h * unit * sign
                    Yu, Yd = Yu0.copy(), Yd0.copy()
                    if sector == "u":
                        Yu[slot] += d
                    else:
                        Yd[slot] += d
                    vals.append((alpha_deg(Yu, Yd) - a0) / eps)
                rec[kind] = min(vals, key=abs)  # smaller of the two signs
            rows.append(rec)
    return a0, rows


def main():
    out = {"phi_fixed_abs": PHI_FIXED, "candidates": []}
    for mask_u, mask_d in CANDIDATES:
        pe = wp7.paper_phase_edge(mask_u, mask_d)
        phase_sector, phase_slot = pe[0], tuple(pe[1])
        # The paper identifies +-phi; the viable basin picks a sign through
        # the phase-placement convention, so try both.
        trials = [(phi, fit_pinned(mask_u, mask_d, phase_sector, phase_slot, phi=phi))
                  for phi in (PHI_FIXED, -PHI_FIXED)]
        trials = [(p, b) for p, b in trials if b is not None]
        phi, best = min(trials, key=lambda t: t[1]["chi2"]) if trials else (PHI_FIXED, None)
        entry = {"member": [mask_u, mask_d], "phase_edge": pe, "phi": phi}
        if best is None:
            entry["status"] = "no_fit_converged"
            out["candidates"].append(entry)
            print(f"member ({mask_u},{mask_d}): no converged fit")
            continue
        entry["chi2"] = best["chi2"]
        entry["viable"] = bool(best["chi2"] <= wp7.CHI2_3SIGMA_7DOF)
        entry["log_mags"] = best["log_mags"]
        print(f"member ({mask_u},{mask_d}): chi2 = {best['chi2']:.4f} "
              f"({'viable' if entry['viable'] else 'NOT viable'})")
        if not entry["viable"]:
            entry["status"] = "not_viable"
            out["candidates"].append(entry)
            continue
        a0, rows = s37_table(mask_u, mask_d, phase_sector, phase_slot, best["log_mags"], phi=phi)
        entry["status"] = "ok"
        entry["alpha_base_deg"] = a0
        entry["s37"] = rows
        out["candidates"].append(entry)
        # LO Yukawa-triangle check: |R_alpha| vs |D12/U12|
        theta = np.concatenate([best["log_mags"], [phi]])
        Yu, Yd = wp7.build_texture(mask_u, mask_d, phase_sector, phase_slot, theta)
        R = None
        su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
        sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
        V = Uu.conj().T @ Ud
        R = -(V[2, 0] * V[2, 2].conj()) / (V[0, 0] * V[0, 2].conj())
        mon = (Yd[0, 1] / Yd[1, 1]) / (Yu[0, 1] / Yu[1, 1])
        entry["R_alpha"] = {"abs": abs(R), "arg_deg": math.degrees(math.atan2(R.imag, R.real))}
        entry["D12_over_U12"] = {"abs": abs(mon), "arg_deg": math.degrees(math.atan2(mon.imag, mon.real))}
        print(f"  alpha0 = {a0:.3f} deg; |R_a| = {abs(R):.4f}, arg = {entry['R_alpha']['arg_deg']:.2f}; "
              f"|D12/U12| = {abs(mon):.4f}, arg = {entry['D12_over_U12']['arg_deg']:.2f}")
        for r in rows:
            name = f"Y^{r['sector']}_{r['slot'][0]+1}{r['slot'][1]+1}"
            print(f"  {name:8s} h={r['hierarchical_size']:.2e}  imag {r['imag']:+9.2f} deg   real {r['real']:+9.2f} deg")
    dest = HERE.parent / "results" / "wp15d_sensitivity.json"
    dest.write_text(json.dumps(out, indent=1))
    print("->", dest)


if __name__ == "__main__":
    main()
