import assert from 'node:assert/strict'

// Cloudflare's configured auto-trailing-slash handling canonicalizes index.html.
// Never follow arbitrary redirects or let a redirect stand in for checked bytes.
export async function fetchCuratedViewerAsset(request, base, route) {
  let response = await request.get(base + route, { maxRedirects: 0 })
  let finalRoute = route, redirectStatus = null
  if ([301, 302, 307, 308].includes(response.status())) {
    assert.match(route, /^\/experiments\/(two-attractor-field|simplex-step-span)\/index\.html$/, 'Unexpected viewer asset redirect')
    const expected = base + route.slice(0, -'index.html'.length)
    const location = response.headers().location
    assert(location, 'Viewer redirect has no location')
    assert.equal(new URL(location, base + route).href, expected, 'Unexpected viewer canonical redirect destination')
    redirectStatus = response.status()
    finalRoute = route.slice(0, -'index.html'.length)
    response = await request.get(expected, { maxRedirects: 0 })
  }
  assert.equal(response.status(), 200, 'Viewer asset must end at 200 without a redirect chain: ' + route)
  return { response, finalRoute, redirectStatus }
}
