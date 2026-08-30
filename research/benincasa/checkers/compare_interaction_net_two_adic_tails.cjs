#!/usr/bin/env node

const fs = require("fs");

function header(path) {
  const firstLine = fs.readFileSync(path, "utf8").split(/\r?\n/, 1)[0];
  return JSON.parse(firstLine);
}

function difference(left, right) {
  const rightSet = new Set(right);
  return left.filter(value => !rightSet.has(value));
}

const [leftPath, rightPath, labelsPath] = process.argv.slice(2);
if (!leftPath || !rightPath || !labelsPath) {
  throw new Error("usage: node compare_interaction_net_two_adic_tails.cjs LEFT RIGHT LABELS");
}

const left = header(leftPath);
const right = header(rightPath);
const labelsPacket = JSON.parse(fs.readFileSync(labelsPath, "utf8"));
const labels = Array.isArray(labelsPacket) ? labelsPacket : labelsPacket.labels;
if (!Array.isArray(labels) || labels.length !== left.original_columns) {
  throw new Error("label packet does not match the source-column count");
}

const activeLeftOnly = difference(left.active_columns, right.active_columns);
const activeRightOnly = difference(right.active_columns, left.active_columns);
const pivotLeftOnly = difference(left.cumulative_pivot_columns, right.cumulative_pivot_columns);
const pivotRightOnly = difference(right.cumulative_pivot_columns, left.cumulative_pivot_columns);
const labelled = columns => columns.map(column => ({column, label: labels[column]}));

process.stdout.write(JSON.stringify({
  schema: "marici.two-adic-tail-comparison.v1",
  left: {
    path: leftPath,
    rows: left.rows,
    active_count: left.active_columns.length,
    cumulative_pivot_sha256: left.cumulative_pivot_sha256
  },
  right: {
    path: rightPath,
    rows: right.rows,
    active_count: right.active_columns.length,
    cumulative_pivot_sha256: right.cumulative_pivot_sha256
  },
  same_source_column_count: left.original_columns === right.original_columns,
  same_export_grade: left.divided_by_power_of_two === right.divided_by_power_of_two,
  same_active_support: activeLeftOnly.length === 0 && activeRightOnly.length === 0,
  same_cumulative_pivot_schedule: pivotLeftOnly.length === 0 && pivotRightOnly.length === 0,
  active_left_only: labelled(activeLeftOnly),
  active_right_only: labelled(activeRightOnly),
  cumulative_pivot_left_only: labelled(pivotLeftOnly),
  cumulative_pivot_right_only: labelled(pivotRightOnly)
}, null, 2) + "\n");
