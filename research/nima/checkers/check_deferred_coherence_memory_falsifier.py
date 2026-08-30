import json
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "strominger" / "results" / "leading_triangle_exact_checks.json"
OUT = ROOT / "nima" / "results" / "deferred_coherence_memory_falsifier.json"


packet = json.loads(SOURCE.read_text(encoding="utf-8"))
source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
checks = {item["id"]: item for item in packet["checks"]}

# For a scalar spherical harmonic of degree l, the common charge operator is
# O = (1/4) D^2(D^2+2), with eigenvalue (l-1)l(l+1)(l+2)/4.
l = 2
charge_eigenvalue = (l - 1) * l * (l + 1) * (l + 2) // 4

required = ["G3.4", "G3.5", "G4.2.l2", "G4.4", "G4.5", "G5.1", "G5.2"]
source_checks_pass = all(checks[k]["status"] == "pass" for k in required)
memory_nonzero = charge_eigenvalue != 0 and checks["G4.4"]["status"] == "pass"
coherent_triangle = source_checks_pass

result = {
    "checker": "deferred_coherence_memory_falsifier",
    "source_packet": str(SOURCE.relative_to(ROOT.parent.parent)).replace("\\", "/"),
    "source_sha256": source_sha256,
    "harmonic_degree": l,
    "charge_operator_eigenvalue": charge_eigenvalue,
    "required_source_checks": required,
    "source_checks_pass": source_checks_pass,
    "memory_nonzero": memory_nonzero,
    "coherent_triangle": coherent_triangle,
    "broad_identification_falsified": bool(memory_nonzero and coherent_triangle),
    "surviving_distinction": {
        "value_boundary_channel": "nonzero memory may be transported by commuting maps",
        "coherence_defect_channel": "measures failure of a declared comparison or composition law",
        "record_channel": "requires source, admitted effect, positive pairing, and record map",
    },
}

assert result["broad_identification_falsified"]
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
