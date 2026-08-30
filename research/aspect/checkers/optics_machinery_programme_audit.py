"""Programme-wide coverage and result-pairing audit for Aspect optics."""

import json
from pathlib import Path


PACKETS = {
    "minimal-two-path-interferometer": ["source", "route", "order", "phase", "norm", "detector", "completion", "hostile"],
    "polarization-marker-quantum-eraser": ["source", "tensor", "condition", "phase", "environment", "detector", "completion", "hostile"],
    "reciprocal-lossy-cavity-plant": ["source", "port", "order", "phase", "loss", "detector", "completion", "hostile"],
    "free-propagation-green-transfer": ["source", "port", "order", "frame", "loss", "detector", "completion", "hostile"],
    "selected-channel-transmission-zero": ["source", "port", "delay", "phase", "unitary", "detector", "completion", "hostile"],
    "nonreciprocal-polarization-scattering": ["source", "port", "order", "basis", "loss", "analyzer", "completion", "hostile"],
    "calibrated-homodyne-heterodyne-detection": ["source", "mode", "calibr", "phase", "noise", "detector", "completion", "hostile"],
    "finite-bandwidth-continuum-completion": ["source", "space", "causal", "frequency", "energy", "detector", "completion", "hostile"],
    "cross-sector-optics-machinery-audit": ["source", "map", "order", "phase", "kernel", "readout", "completion", "prohibited"],
    "calibrated-photon-counting-intensity-statistics": ["source", "povm", "temporal", "phase", "loss", "detector", "completion", "hostile"],
    "causal-dispersive-magneto-optic-response": ["source", "port", "order", "frame", "dissip", "detector", "completion", "hostile"],
    "positive-real-impedance-versus-dark-reflection": ["source", "port", "order", "reference", "conserv", "detector", "completion", "hostile"],
    "reciprocal-denominator-sewing-network": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "directional-double-triangle-moving-fiber-interferometer": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "two-frontier-optical-instrument-build-audit": ["source", "instrument", "finite", "phase", "authority", "detector", "completion", "hostile"],
    "two-instrument-calibration-robustness": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "finite-lossy-photodetection-quantum-instrument": ["source", "port", "order", "phase", "conserv", "detector", "completion", "hostile"],
    "finite-dead-time-photodetection-memory-instrument": ["source", "port", "order", "phase", "conserv", "detector", "completion", "hostile"],
    "calibrated-six-port-scale-identification-instrument": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "quantum-bath-dilation-of-magneto-optic-loss": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "finite-multibin-quantum-bath-dilation": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "dyadic-passive-bath-refinement": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "markov-oscillator-loss-noise-identity": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "thermal-sideband-detailed-balance-instrument": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "multifrequency-kms-coherence-instrument": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "dual-clock-coprime-antialias-instrument": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "high-q-cavity-completion-escape": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "robust-dual-clock-jitter-observability": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "reciprocal-cross-sheet-phase-interferometer": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "closed-loop-boundary-schur-zero": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "boundary-mode-lift-determinant-control": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "minimal-optical-transfer-identifiability": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "live-calibration-epoch-interlock": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "cross-run-optical-witness-splicing": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "frame-transport-joint-witness-audit": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
    "marici-joint-witness-composition-coverage": ["source", "port", "order", "frame", "conserv", "detector", "completion", "hostile"],
}

INVENTORY_COVERAGE = {
    "coherent_and_single_photon_sources": ["minimal-two-path-interferometer", "polarization-marker-quantum-eraser", "calibrated-photon-counting-intensity-statistics"],
    "free_propagation_green_transfer": ["free-propagation-green-transfer"],
    "beam_splitters_ordered_paths": ["minimal-two-path-interferometer"],
    "phase_and_frame_calibration": ["minimal-two-path-interferometer", "calibrated-homodyne-heterodyne-detection"],
    "polarization": ["polarization-marker-quantum-eraser", "nonreciprocal-polarization-scattering"],
    "reciprocal_nonreciprocal": ["reciprocal-lossy-cavity-plant", "nonreciprocal-polarization-scattering", "causal-dispersive-magneto-optic-response"],
    "cavity_delay_feedback_memory": ["reciprocal-lossy-cavity-plant"],
    "loss_decoherence_environment": ["reciprocal-lossy-cavity-plant", "polarization-marker-quantum-eraser", "nonreciprocal-polarization-scattering", "causal-dispersive-magneto-optic-response", "quantum-bath-dilation-of-magneto-optic-loss"],
    "homodyne_heterodyne_counting_intensity": ["calibrated-homodyne-heterodyne-detection", "calibrated-photon-counting-intensity-statistics"],
    "bandwidth_continuum_infinite_time": ["finite-bandwidth-continuum-completion"],
}


def main():
    aspect = Path(__file__).parents[1]
    packet_findings = {}
    all_contracts = True
    all_pairs = True
    all_results_pass = True

    for stem, terms in PACKETS.items():
        packet = aspect / f"{stem}.md"
        checker = aspect / "checkers" / f"{stem.replace('-', '_')}.py"
        result = aspect / "results" / f"{stem.replace('-', '_')}.json"
        text = packet.read_text(encoding="utf-8").lower() if packet.exists() else ""
        missing_terms = [term for term in terms if term not in text]
        result_payload = json.loads(result.read_text(encoding="utf-8")) if result.exists() else {}
        paired = packet.exists() and checker.exists() and result.exists()
        passing = result_payload.get("status") == "pass"
        contract_ok = not missing_terms
        all_contracts &= contract_ok
        all_pairs &= paired
        all_results_pass &= passing
        packet_findings[stem] = {
            "paired": paired,
            "result_status": result_payload.get("status"),
            "contract_terms_present": contract_ok,
            "missing_contract_terms": missing_terms,
        }

    coverage = {
        requirement: all(name in PACKETS for name in names)
        for requirement, names in INVENTORY_COVERAGE.items()
    }
    checks = {
        "all_inventory_requirements_have_named_packets": all(coverage.values()),
        "every_packet_has_checker_and_result": all_pairs,
        "every_result_reports_pass": all_results_pass,
        "every_packet_exposes_required_contract_families": all_contracts,
        "laboratory_index_exists": (aspect / "optics-integrating-laboratory-index.md").exists(),
        "cross_sector_audit_exists": (aspect / "cross-sector-optics-machinery-audit.md").exists(),
    }
    result = {
        "schema": "marici.aspect.optics_machinery_programme_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "inventory_coverage": coverage,
        "packet_findings": packet_findings,
        "bounded_completion": "finite exact machinery named by the laboratory inventory",
        "retained_boundaries": [
            "continuum stochastic fields and microscopic detector instruments",
            "source-derived microscopic magneto-optic response and its quantum bath dilation",
            "sector-owned physical instantiation of crosswalk templates",
            "no RH or theta zero-exclusion authority",
        ],
    }
    out = aspect / "results" / "optics_machinery_programme_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
