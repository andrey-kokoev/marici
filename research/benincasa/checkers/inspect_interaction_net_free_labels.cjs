#!/usr/bin/env node
"use strict";

const fs = require("fs");

if (process.argv.length < 4) {
  throw new Error("usage: node inspect_interaction_net_free_labels.cjs LABELS INDEX...");
}
const packet = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const rows = process.argv.slice(3).map(text => {
  const index = Number(text);
  if (!Number.isInteger(index) || index < 0 || index >= packet.labels.length) {
    throw new Error("invalid label index " + text);
  }
  const label = packet.labels[index];
  return {
    index,
    k_pole: label[0],
    q_levels: label.slice(1, 6),
    monomial: label[6]
  };
});
process.stdout.write(JSON.stringify({
  schema: "marici.interaction-net-free-label-inspection.v1",
  source: process.argv[2],
  label_count: packet.labels.length,
  rows
}, null, 2) + "\n");
