import json
import subprocess
from pathlib import Path

exe = Path("research/benincasa/marici-gm/target/release/five_site_disjoint_mixed_pair_landau.exe")
run = subprocess.run(
    [str(exe)], check=True, capture_output=True, text=True,
    encoding="utf-8", errors="ignore",
)
start = run.stdout.index('{"label"')
payload = '{"schema":"marici.five_site_disjoint_mixed_pair_landau.v1","cases":[' + run.stdout[start:]
packet = json.loads(payload)

assert len(packet["cases"]) == 6
assert {c["label"] for c in packet["cases"]} == {
    "G_minus_e12|g_3", "G_minus_e12|g_4", "G_minus_e12|g_5",
    "G_minus_e12|g_34", "G_minus_e12|g_45", "G_minus_e12|g_345",
}
assert all(c["removed_universal_factor"] == "x" for c in packet["cases"])
assert all("x^6" in c["saturated_resultant"] for c in packet["cases"])
assert all("x*(-" not in c["saturated_resultant"] for c in packet["cases"])

out = Path("research/benincasa/results/five-site-disjoint-mixed-pair-landau.json")
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "schema": packet["schema"],
    "case_count": len(packet["cases"]),
    "degrees_after_total_energy_saturation": [6] * 6,
    "output": str(out),
}, sort_keys=True))
