#!/usr/bin/env python3
import hashlib
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/winding-port-sizing.json"


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def main():
    root_orders = [2, 3]
    modulus = lcm(*root_orders)
    assert modulus == 6

    residues = []
    for n in range(6):
        residues.append({"mod_6": n, "square_monodromy": n % 2,
                         "cube_monodromy": n % 3})
    assert len({(x["square_monodromy"], x["cube_monodromy"])
                for x in residues}) == 6

    smaller_cyclic_ports = {}
    for m in range(1, 6):
        collision = None
        for a in range(0, 18):
            for b in range(a + 1, 18):
                if a % m == b % m and (a % 2 != b % 2 or a % 3 != b % 3):
                    collision = [a, b]
                    break
            if collision:
                break
        assert collision is not None
        smaller_cyclic_ports[str(m)] = collision

    log_hostiles = []
    for m in (2, 3, 6, 12):
        assert 0 % m == m % m
        assert (0 == 0) != (m == 0)
        log_hostiles.append({"modulus": m, "indistinguishable_windings": [0, m],
                             "logarithm_status": [True, False]})

    payload = {
        "schema": "marici.kitaev.winding_port_sizing.v1",
        "status": "pass",
        "authorized_root_orders": root_orders,
        "minimal_cyclic_port_modulus": modulus,
        "joint_residue_table": residues,
        "smaller_port_collisions": smaller_cyclic_ports,
        "finite_ports_fail_for_global_logarithm": log_hostiles,
        "square_root_only_port": "one parity bit",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
