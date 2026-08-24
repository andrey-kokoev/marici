"""Symbolic grade classification of the two magnetic exception templates."""
import json
import os

import sympy as sp

g = sp.symbols("g", integer=True, positive=True)
rf4 = sp.rf(4, g)

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# q=1, a=0 reflected pair on semantic rows 1,2.
q1_block = sp.Matrix([[-g * rf4, -2 * rf4],
                      [0, (g - 2) * rf4]])
q1_minor = sp.factor(q1_block.det())
q1_expected = -g * (g - 2) * rf4 ** 2
record("Q1.block", "the general q=1 exceptional template has the displayed 2x2 block",
       sp.simplify(q1_minor - q1_expected) == 0, str(q1_block))
record("Q1.factor", "its determinant vanishes among g>=2 exactly at g=2",
       sp.factor(q1_minor / q1_expected) == 1 and
       all((q1_expected.subs(g, gv) == 0) == (gv == 2)
           for gv in range(2, 101)), str(q1_expected))

q1_at_two = q1_block.subs(g, 2)
q1_kernel = q1_at_two.nullspace()[0]
q1_primitive = sp.Matrix([1, -1])
record("Q1.circuit", "at grade two the primitive q=1 circuit is (1,-1)",
       q1_at_two * q1_primitive == sp.zeros(2, 1) and
       q1_kernel[0] / q1_kernel[1] == -1, list(q1_primitive))


def source_coefficient(depth, index):
    return (sp.binomial(g, index) * (-1) ** (g - index) *
            sp.rf(depth, g - index) * sp.rf(4 - depth, index))


def path_coefficient(depth, m_value, index):
    if index == 0:
        return sp.factor(m_value * source_coefficient(depth, 0))
    return sp.factor((m_value + index) * source_coefficient(depth, index) +
                     (m_value + index - 1 - g) *
                     source_coefficient(depth, index - 1))


# General continuation of the q=7 geometry: q=g+5 and the three columns
# (a,s)=(0,-q),(4,+q),(6,+q), restricted to rows 0,1,2.
col_zero_minus = sp.Matrix([[-(g + 4) * rf4],
                            [-2 * (g + 2) * rf4],
                            [0]])
c0_at_four = (-1) ** g * rf4
col_four_plus = sp.Matrix([[0], [-2 * c0_at_four],
                           [(g - 2) * c0_at_four]])
col_six_plus = sp.Matrix([-path_coefficient(6, 0, index)
                          for index in (1, 2, 3)])
qg5_block = sp.Matrix.hstack(col_zero_minus, col_four_plus, col_six_plus)
qg5_minor = sp.factor(qg5_block.det())
qg5_expected = (-4 * g * (g - 2) * (g + 5) *
                 sp.rf(6, g - 1) * rf4 ** 2)

# SymPy needs the elementary rising-factorial step to expose the compact form.
qg5_reduced = sp.factor(qg5_minor.xreplace({sp.rf(6, g):
                                            (g + 5) * sp.rf(6, g - 1)}))
record("QG5.block", "the q=g+5 collision template has a fixed 3x3 minor",
       sp.simplify(qg5_reduced - qg5_expected) == 0,
       "columns a=0-,4+,6+; rows 0,1,2")
record("QG5.factor", "the 3x3 minor vanishes among g>=2 exactly at g=2",
       all((qg5_expected.subs(g, gv) == 0) == (gv == 2)
           for gv in range(2, 101)), str(qg5_expected))

qg5_at_two = qg5_block.subs(g, 2)
primitive = sp.Matrix([1, -3, 2])
record("QG5.circuit", "at grade two the primitive collision vector is (1,-3,2)",
       qg5_at_two * primitive == sp.zeros(3, 1) and
       qg5_at_two.rank() == 2, list(primitive))
record("QG5.identify", "the grade-two alignment is precisely q=7",
       (g + 5).subs(g, 2) == 7, "q=g+5")

# Removing the extra row at grades above two would hide the restoring pivot.
record("FALSIFIER.row", "the restoring third row is proportional to g-2",
       sp.factor(col_four_plus[2] / c0_at_four) == g - 2,
       "a=4 plus endpoint")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_exception_minor_symbolic_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic all-grade theorem for both known exception templates",
              "domain": "integer g>=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Both known magnetic exception geometries are grade-two-only boundary shortenings. The q=1 reflected a=0 pair has minor -g(g-2)rf(4,g)^2. The q=g+5 block on a=0-,4+,6+ has minor -4g(g-2)(g+5)rf(6,g-1)rf(4,g)^2. Both are nonzero for every g>=3 and degenerate at g=2 to the primitive circuits (1,-1) and (1,-3,2), with q=g+5=7 in the latter case.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_exception_minor_symbolic.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
