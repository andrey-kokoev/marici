//! Executable type gate for the unconstructed global normalization-Cech source.

use std::marker::PhantomData;

struct OccurrenceRees;
struct TorCech;
struct SheetPair;
struct RingedTarget;
struct SpanProjections;
struct RingedSpan;
struct PcExtraordinaryCostalk;
struct EndpointPlus;
struct EndpointMinus;
struct ExpandedCarrier;
struct CentralTwo;
struct CentralOne;

struct MissingBlock<From, To> {
    id: &'static str,
    marker: PhantomData<(From, To)>,
}

impl<From, To> MissingBlock<From, To> {
    const fn new(id: &'static str) -> Self {
        Self {
            id,
            marker: PhantomData,
        }
    }
}

struct MissingSourceBlocks {
    occurrence_rees: MissingBlock<OccurrenceRees, OccurrenceRees>,
    tor_cech: MissingBlock<TorCech, TorCech>,
    central_flip_target_ringed_enhancement: MissingBlock<PcExtraordinaryCostalk, RingedTarget>,
    central_flip_projections: MissingBlock<(SheetPair, RingedTarget), SpanProjections>,
    central_flip_dualizing_trace: MissingBlock<SpanProjections, RingedSpan>,
    central_flip_pc_purity: MissingBlock<RingedSpan, PcExtraordinaryCostalk>,
    endpoint_plus: MissingBlock<SheetPair, EndpointPlus>,
    endpoint_minus: MissingBlock<SheetPair, EndpointMinus>,
    full_log: MissingBlock<SheetPair, ExpandedCarrier>,
    central_21: MissingBlock<CentralTwo, CentralOne>,
}

impl MissingSourceBlocks {
    const fn new() -> Self {
        Self {
            occurrence_rees: MissingBlock::new("d_occurrence_rees"),
            tor_cech: MissingBlock::new("d_tor_cech"),
            central_flip_target_ringed_enhancement: MissingBlock::new(
                "d_central_flip_target_ringed_enhancement",
            ),
            central_flip_projections: MissingBlock::new("d_central_flip_projections"),
            central_flip_dualizing_trace: MissingBlock::new("d_central_flip_dualizing_trace"),
            central_flip_pc_purity: MissingBlock::new("d_central_flip_pc_purity"),
            endpoint_plus: MissingBlock::new("d_endpoint_plus"),
            endpoint_minus: MissingBlock::new("d_endpoint_minus"),
            full_log: MissingBlock::new("d_full_log"),
            central_21: MissingBlock::new("central_21_row"),
        }
    }

    fn ids(&self) -> [&'static str; 10] {
        [
            self.occurrence_rees.id,
            self.tor_cech.id,
            self.central_flip_target_ringed_enhancement.id,
            self.central_flip_projections.id,
            self.central_flip_dualizing_trace.id,
            self.central_flip_pc_purity.id,
            self.endpoint_plus.id,
            self.endpoint_minus.id,
            self.full_log.id,
            self.central_21.id,
        ]
    }
}

struct KnownPacket {
    id: &'static str,
    ranks: &'static [usize],
}

const KNOWN_PACKETS: [KnownPacket; 9] = [
    KnownPacket {
        id: "koszul_sheet_plus",
        ranks: &[1, 3, 3, 1],
    },
    KnownPacket {
        id: "koszul_sheet_minus",
        ranks: &[1, 3, 3, 1],
    },
    KnownPacket {
        id: "scalar_conductor",
        ranks: &[1, 2, 1],
    },
    KnownPacket {
        id: "repeated_normal_tor",
        ranks: &[1, 2, 1],
    },
    KnownPacket {
        id: "endpoint_cech",
        ranks: &[1, 4, 6, 4, 1],
    },
    KnownPacket {
        id: "road_skeleton",
        ranks: &[1, 4, 5, 1],
    },
    KnownPacket {
        id: "expanded_source_carrier",
        ranks: &[8, 24, 18],
    },
    KnownPacket {
        id: "expanded_target_carrier",
        ranks: &[9, 21, 14],
    },
    KnownPacket {
        id: "central_flip_finite_profile",
        ranks: &[1, 2, 1],
    },
];

fn main() {
    let missing = MissingSourceBlocks::new();
    let packets = KNOWN_PACKETS
        .iter()
        .map(|packet| {
            let ranks = packet
                .ranks
                .iter()
                .map(usize::to_string)
                .collect::<Vec<_>>()
                .join(",");
            format!("{{\"id\":\"{}\",\"ranks\":[{}]}}", packet.id, ranks)
        })
        .collect::<Vec<_>>()
        .join(",");
    let obligations = missing
        .ids()
        .iter()
        .map(|id| format!("\"{id}\""))
        .collect::<Vec<_>>()
        .join(",");

    println!(
        "{{\"status\":\"derived_partial\",\"known_packets\":[{packets}],\"global_source_dimensions\":\"unknown\",\"central_flip_finite_normal_form\":\"PROVED\",\"central_flip_rees_geometry\":\"PROVED_NOT_A_SPAN\",\"target_cellular_cosheaf\":\"PROVED\",\"first_geometric_obligation\":\"d_central_flip_target_ringed_enhancement\",\"missing_blocks\":[{obligations}],\"global_totalization\":\"NOT_INSTANTIATED\",\"global_d_squared\":\"NOT_RUN\",\"smith_form\":\"PROHIBITED_UNTIL_ALL_BLOCKS_ARE_FILLED\",\"six_functor_kernel\":\"NOT_CONSTRUCTED\"}}"
    );
}
