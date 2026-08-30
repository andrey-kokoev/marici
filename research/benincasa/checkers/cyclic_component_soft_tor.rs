// Character census for three labelled copies of the local (1,2,1) Tor packet.

fn main() {
    let local = [1_i32, 2, 1];
    let global = local.map(|rank| 3 * rank);
    assert_eq!(global, [3, 6, 3]);

    // Each grade is rank(local) copies of the regular C3 representation.
    let characters = local.map(|rank| [3 * rank, 0, 0]);
    assert_eq!(characters, [[3, 0, 0], [6, 0, 0], [3, 0, 0]]);

    println!(
        "{{\"status\":\"pass\",\"local\":[1,2,1],\"cyclic_global\":[3,6,3],\"characters\":[[3,0,0],[6,0,0],[3,0,0]],\"occurrences_collapsed\":false}}"
    );
}
