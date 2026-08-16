use std::collections::{HashSet, VecDeque};
use std::process::ExitCode;

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
enum Object {
    AbsoluteH2,
    MarkedH2,
    WallH1Twist,
    AbsoluteH3,
}

fn reachable(start: Object, target: Object, arrows: &[(Object, Object)]) -> bool {
    let mut seen = HashSet::from([start]);
    let mut queue = VecDeque::from([start]);
    while let Some(node) = queue.pop_front() {
        if node == target {
            return true;
        }
        for &(source, destination) in arrows {
            if source == node && seen.insert(destination) {
                queue.push_back(destination);
            }
        }
    }
    false
}

fn main() -> ExitCode {
    // Frozen localization sequence for a divisor complement U = S \ W:
    // H^2(S) -> H^2(U) -> H^1(W)(-1) -> H^3(S).
    let frozen_arrows = [
        (Object::AbsoluteH2, Object::MarkedH2),
        (Object::MarkedH2, Object::WallH1Twist),
        (Object::WallH1Twist, Object::AbsoluteH3),
    ];

    assert!(reachable(
        Object::AbsoluteH2,
        Object::WallH1Twist,
        &frozen_arrows
    ));
    assert!(reachable(
        Object::WallH1Twist,
        Object::AbsoluteH3,
        &frozen_arrows
    ));
    assert!(!reachable(
        Object::WallH1Twist,
        Object::AbsoluteH2,
        &frozen_arrows
    ));

    println!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.wall-to-absolute-type-gate.v1\",\n",
            "  \"absolute_nine_master_degree\": 2,\n",
            "  \"wall_residue_degree\": 1,\n",
            "  \"wall_tate_twist\": -1,\n",
            "  \"localization_arrows\": [\"H2(S)->H2(U)\", \"H2(U)->H1(W)(-1)\", \"H1(W)(-1)->H3(S)\"],\n",
            "  \"canonical_wall_to_absolute_H2_arrow\": false,\n",
            "  \"parent_master_ancestry\": \"e6\",\n",
            "  \"ancestry_is_absolute_coordinate\": false,\n",
            "  \"required_extra_datum\": \"splitting or physical relative-realization map\",\n",
            "  \"new_carrier_incidence\": false\n",
            "}}"
        )
    );

    ExitCode::SUCCESS
}
