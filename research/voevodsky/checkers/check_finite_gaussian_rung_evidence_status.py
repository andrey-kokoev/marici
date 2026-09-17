#!/usr/bin/env python3
"""Classify existing finite Clark/Gaussian evidence without promoting it to a global proof."""
import json,hashlib
from pathlib import Path
R=Path(__file__).parents[1]/"results"
cert=R/"suzuki-debranges-kernel-scout.json"
num=R/"physical-xi-packet-douglas-scout.json"
a=json.loads(cert.read_text(encoding="utf-8"));b=json.loads(num.read_text(encoding="utf-8"))
checks={
 "certified_listed_diagonals_positive":all(x["positive"] for x in a["points"]),
 "certified_listed_two_by_two_minors_positive":all(x["positive_definite"] for x in a["two_by_two_minors"]),
 "numerical_packets_have_no_reported_negative_eigenvalue":all(x["negative_eigenvalues_below_tolerance"]==0 for x in b["packets"]),
 "numerical_Douglas_outputs_constructed":all(x["douglas_status"]=="CONSTRUCTED" for x in b["packets"]),
 "finite_samples_do_not_cover_continuum":True,
 "spectral_split_Douglas_is_diagnostic_not_source_factorization":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.finite-gaussian-rung-evidence-status.v1",
 "checks":checks,"passed":True,
 "certified_scope":{"points":len(a["points"]),"two_by_two_minors":len(a["two_by_two_minors"]),"precision_bits":a["precision_bits"]},
 "numerical_scope":{"packets":len(b["packets"]),"packet_sizes":[len(x["points"]) for x in b["packets"]]},
 "positive_clue":"No hostile direction is seen in the listed certified 1x1/2x2 tests or three numerical four-point packets.",
 "critical_limitation":"The packet Douglas constructor obtains A_S and A_B by spectrally splitting the already assembled Gram matrix. It is not the required source-derived coherent Krein-Langer factorization and cannot establish positivity at later rungs.",
 "next_executable_target":"Build A_S,N and A_B,N directly from Gaussian translates and source prime/gamma/endpoint channels, then test kernel inclusion, kappa_N<=1, and restriction compatibility C_(N+1)|range(A_S,N)=C_N.",
 "rh_proved":False,
 "dependencies":{"certified":{"path":cert.name,"sha256":hashlib.sha256(cert.read_bytes()).hexdigest()},"numerical":{"path":num.name,"sha256":hashlib.sha256(num.read_bytes()).hexdigest()}}
}
p=R/"finite_gaussian_rung_evidence_status.json";p.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
