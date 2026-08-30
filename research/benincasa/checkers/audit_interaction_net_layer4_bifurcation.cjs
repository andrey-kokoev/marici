#!/usr/bin/env node

const fs = require("fs");

function header(path) {
  return JSON.parse(fs.readFileSync(path, "utf8").split(/\r?\n/, 1)[0]);
}

function difference(left, right) {
  const rightSet = new Set(right);
  return left.filter(value => !rightSet.has(value));
}

const [preLeftPath, postLeftPath, preRightPath, postRightPath, labelsPath] = process.argv.slice(2);
if (!labelsPath) {
  throw new Error("usage: node audit_interaction_net_layer4_bifurcation.cjs PRE_LEFT POST_LEFT PRE_RIGHT POST_RIGHT LABELS");
}

const preLeft = header(preLeftPath);
const postLeft = header(postLeftPath);
const preRight = header(preRightPath);
const postRight = header(postRightPath);
const labelsPacket = JSON.parse(fs.readFileSync(labelsPath, "utf8"));
const labels = Array.isArray(labelsPacket) ? labelsPacket : labelsPacket.labels;
const labelled = columns => columns.map(column => ({column, label: labels[column]}));
const equalArrays = (left, right) => JSON.stringify(left) === JSON.stringify(right);

const leftNewPivots = difference(postLeft.cumulative_pivot_columns, preLeft.cumulative_pivot_columns);
const rightNewPivots = difference(postRight.cumulative_pivot_columns, preRight.cumulative_pivot_columns);
const leftSupportRemoved = difference(preLeft.active_columns, postLeft.active_columns);
const rightSupportRemoved = difference(preRight.active_columns, postRight.active_columns);

process.stdout.write(JSON.stringify({
  schema: "marici.interaction-net-layer4-bifurcation-audit.v1",
  pre_bifurcation: {
    rows: [preLeft.rows, preRight.rows],
    active_counts: [preLeft.active_columns.length, preRight.active_columns.length],
    same_pivot_schedule: equalArrays(preLeft.cumulative_pivot_columns, preRight.cumulative_pivot_columns),
    same_active_support: equalArrays(preLeft.active_columns, preRight.active_columns)
  },
  left: {
    new_pivots: labelled(leftNewPivots),
    support_removed: labelled(leftSupportRemoved),
    residual_rows: postLeft.rows,
    residual_active_count: postLeft.active_columns.length
  },
  right: {
    new_pivots: labelled(rightNewPivots),
    support_removed: labelled(rightSupportRemoved),
    residual_rows: postRight.rows,
    residual_active_count: postRight.active_columns.length
  },
  common_new_pivots: labelled(leftNewPivots.filter(column => rightNewPivots.includes(column))),
  left_only_new_pivots: labelled(difference(leftNewPivots, rightNewPivots)),
  right_only_new_pivots: labelled(difference(rightNewPivots, leftNewPivots)),
  verdict: equalArrays(preLeft.cumulative_pivot_columns, preRight.cumulative_pivot_columns)
    && equalArrays(preLeft.active_columns, preRight.active_columns)
    && !equalArrays(leftNewPivots, rightNewPivots)
      ? "the source-derived presentation is common through valuation 3 and bifurcates at valuation 4"
      : "the proposed bifurcation pattern was not reproduced"
}, null, 2) + "\n");
