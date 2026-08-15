const INLINE_MATH = /\\\(([\s\S]*?)\\\)/g
const FLOW_MATH = /^\s*\\\[([\s\S]*?)\\\]\s*$/

function sourceSlice(node, file) {
  const position = node?.position
  const start = position?.start?.offset
  const end = position?.end?.offset
  if (typeof start !== 'number' || typeof end !== 'number') return null
  return String(file.value).slice(start, end)
}

function unescapeMarkdownPunctuation(value) {
  return value.replace(/\\([!"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~])/g, '$1')
}

function mathData(display, value) {
  return {
    hName: display ? 'div' : 'span',
    hProperties: { className: [display ? 'math-display' : 'math-inline'] },
    hChildren: [{ type: 'text', value }],
  }
}

function ensureMathNode(node) {
  if (node.type !== 'math' && node.type !== 'inlineMath') return
  node.data = { ...(node.data ?? {}), ...mathData(node.type === 'math', node.value) }
}

function inlineReplacement(node, raw) {
  INLINE_MATH.lastIndex = 0
  if (!INLINE_MATH.test(raw)) return null

  INLINE_MATH.lastIndex = 0
  const children = []
  let cursor = 0
  let match
  while ((match = INLINE_MATH.exec(raw))) {
    const before = unescapeMarkdownPunctuation(raw.slice(cursor, match.index))
    if (before) children.push({ type: 'text', value: before })
    children.push({
      type: 'inlineMath',
      value: match[1],
      data: mathData(false, match[1]),
    })
    cursor = match.index + match[0].length
  }

  const after = unescapeMarkdownPunctuation(raw.slice(cursor))
  if (after) children.push({ type: 'text', value: after })
  return children.length ? children : [node]
}

function transformChildren(parent, file) {
  if (!Array.isArray(parent.children)) return

  const children = []
  for (const child of parent.children) {
    const raw = sourceSlice(child, file)

    if (child.type === 'paragraph' && raw) {
      const flowMatch = raw.match(FLOW_MATH)
      if (flowMatch) {
        children.push({
          type: 'math',
          value: flowMatch[1].trim(),
          data: mathData(true, flowMatch[1].trim()),
          position: child.position,
        })
        continue
      }
    }

    if (child.type === 'text' && raw) {
      const replacement = inlineReplacement(child, raw)
      if (replacement) {
        children.push(...replacement)
        continue
      }
    }

    ensureMathNode(child)
    transformChildren(child, file)
    children.push(child)
  }

  parent.children = children
}

export default function remarkNaradaMath() {
  return function transformNaradaMath(tree, file) {
    transformChildren(tree, file)
  }
}
