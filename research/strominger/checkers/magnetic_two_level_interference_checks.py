"""Separate residual carrier loss from full magnetic sheet interference."""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
gamma = -2 * zb / (1 + u)


def simplify(value):
    return sp.factor(sp.cancel(sp.together(value)))


def reflection(value):
    return value.xreplace({z: zb, zb: z})


def chain(grade, datum, barred=False):
    value = datum
    variable = zb if barred else z
    connection = reflection(gamma) if barred else gamma
    for weight in range(2, grade + 2):
        value = simplify(sp.diff(value, variable) - weight * connection * value)
    return value


def sheet_packet(grade, datum):
    unbarred = chain(grade, datum)
    barred = chain(grade, reflection(datum), barred=True)
    return simplify(sp.diff(unbarred, zb)), simplify(sp.diff(barred, z))


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


E1 = 1 - zb**-2
E2 = zb**-8 - 3 * z**-4 * zb**2 + 2 * z**-6
packets = {"E1": sheet_packet(2, E1), "E2": sheet_packet(2, E2)}

for name, (left, right) in packets.items():
    record(f"{name}.nonzero", f"{name} has two nonzero physical sheet outputs",
           left != 0 and right != 0, "A!=0 and B!=0")
    record(f"{name}.magnetic", f"{name} is magnetic-zero by equal-sheet coherence",
           simplify(left - right) == 0, "A-B=0")
    record(f"{name}.electric", f"{name} remains visible to the complementary sum readout",
           simplify(left + right) != 0 and simplify(left + right - 2 * left) == 0,
           "A+B=2A!=0")

E1_expected = 40 * (z + zb) / (1 + u)**3
record("E1.closed", "the first exceptional sheet has the closed formula",
       simplify(packets["E1"][0] - E1_expected) == 0, E1_expected)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_two_level_interference_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact full-fold mechanism distinction",
              "grade": 2, "classes": ["E1", "E2"]},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Residual observation-carrier loss explains why the source matrix acquires E1 and E2 circuits, but neither class loses its full physical sheet packet. Both have A=B nonzero, so M=A-B vanishes by lawful equal-sheet coherence while the complementary electric readout A+B=2A remains nonzero. Local birth mechanism and final readout mechanism are distinct levels.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_two_level_interference.json"),
          "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
