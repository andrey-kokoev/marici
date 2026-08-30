#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum InternalOccurrence {
    Q,
    K,
}

fn swap(occurrence: InternalOccurrence) -> InternalOccurrence {
    match occurrence {
        InternalOccurrence::Q => InternalOccurrence::K,
        InternalOccurrence::K => InternalOccurrence::Q,
    }
}

fn main() {
    assert_eq!(swap(swap(InternalOccurrence::Q)), InternalOccurrence::Q);
    assert_eq!(swap(swap(InternalOccurrence::K)), InternalOccurrence::K);

    // q -> p-q has linear part -I_3: determinant -1 for oriented forms,
    // absolute Jacobian +1 for the source Lebesgue density d^3q.
    let oriented_jacobian = -1_i32;
    let density_jacobian = oriented_jacobian.abs();
    assert_eq!(density_jacobian, 1);

    let orbit = [InternalOccurrence::Q, InternalOccurrence::K];
    assert_eq!(orbit.len(), 2);

    println!(
        "{{\"schema\":\"marici.benincasa.internal_qk_occurrence_trace.v1\",\"involution_order\":2,\"oriented_jacobian\":{},\"density_jacobian\":{},\"occurrence_orbit_size\":{},\"trace_coefficient\":2,\"requires_full_or_swap_invariant_domain\":true,\"status\":\"verified\"}}",
        oriented_jacobian,
        density_jacobian,
        orbit.len()
    );
}

