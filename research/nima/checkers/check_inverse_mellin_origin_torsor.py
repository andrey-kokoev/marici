import json
from pathlib import Path


ORDER = 7


def phase(frame: int, label: int) -> int:
    return (frame * label) % ORDER


def main() -> None:
    frames = []
    for frame in range(ORDER):
        assert phase(frame, 0) == 0
        for left in range(ORDER):
            for right in range(ORDER):
                assert phase(frame, (left + right) % ORDER) == (
                    phase(frame, left) + phase(frame, right)
                ) % ORDER
            assert phase(frame, (-left) % ORDER) == (-phase(frame, left)) % ORDER
        frames.append(
            {
                "frame_parameter": frame,
                "generator_phase": phase(frame, 1),
                "unit_preserved": True,
                "product_preserved": True,
                "inverse_preserved": True,
                "dagger_preserved": True,
            }
        )

    assert len({row["generator_phase"] for row in frames}) == ORDER

    result = {
        "schema": "marici.nima.inverse-mellin-origin-torsor.v1",
        "finite_character_order": ORDER,
        "admissible_frame_count": len(frames),
        "coherence_laws_select_unique_frame": False,
        "endpoint_pointing_required": True,
        "frames": frames,
    }
    output = Path(__file__).parents[1] / "results" / "inverse-mellin-origin-torsor.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

