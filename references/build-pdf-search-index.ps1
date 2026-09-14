[CmdletBinding()]
param(
    [string[]] $InputPath = @(
        (Join-Path $PSScriptRoot 'Derived algebraic geometry Vol1.pdf'),
        (Join-Path $PSScriptRoot 'Derived algebraic geometry Vol2.pdf')
    ),
    [string] $OutputDirectory = (Join-Path $PSScriptRoot 'extractions/pdf-search-index'),
    [string] $PdfBossPath = (Join-Path $PSScriptRoot '.local-tools/pdfboss/bin/pdfboss.exe')
)

$ErrorActionPreference = 'Stop'

function Resolve-FromWorkingDirectory([string] $Path) {
    if ([IO.Path]::IsPathRooted($Path)) {
        return [IO.Path]::GetFullPath($Path)
    }
    return [IO.Path]::GetFullPath((Join-Path (Get-Location) $Path))
}

function Normalize-PdfText([string] $Text) {
    $replacements = [ordered]@{
        "`u{FB00}" = 'ff'
        "`u{FB01}" = 'fi'
        "`u{FB02}" = 'fl'
        "`u{FB03}" = 'ffi'
        "`u{FB04}" = 'ffl'
        "`u{00A0}" = ' '
        "`u{00AD}" = ''
    }
    foreach ($entry in $replacements.GetEnumerator()) {
        $Text = $Text.Replace($entry.Key, $entry.Value)
    }

    # Join words split by typographic line wrapping, then make one searchable
    # record per page. The source PDF remains the display authority.
    $Text = [regex]::Replace($Text, '(?<=\p{L})-\s*\r?\n\s*(?=\p{Ll})', '')
    return ([regex]::Replace($Text, '\s+', ' ')).Trim()
}

function Get-PrintedPageLabel([string] $PageText) {
    $candidate = $PageText -split '\r?\n' | Where-Object { $_.Trim() } | Select-Object -First 1
    if ($null -eq $candidate) {
        return ''
    }
    $firstLine = $candidate.Trim()
    if ($firstLine -match '^\s*(\d{1,4})(?:\s|$)') {
        return $Matches[1]
    }
    if ($firstLine -match '(?:^|\s)(\d{1,4})\s*$') {
        return $Matches[1]
    }
    return ''
}

$pdfBoss = Resolve-FromWorkingDirectory $PdfBossPath
if (-not (Test-Path -LiteralPath $pdfBoss -PathType Leaf)) {
    throw "pdfboss executable not found: $pdfBoss"
}

$outputRoot = Resolve-FromWorkingDirectory $OutputDirectory
New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null
$manifest = [Collections.Generic.List[object]]::new()

foreach ($input in $InputPath) {
    $pdf = Resolve-FromWorkingDirectory $input
    if (-not (Test-Path -LiteralPath $pdf -PathType Leaf)) {
        throw "PDF not found: $pdf"
    }

    $slug = [IO.Path]::GetFileNameWithoutExtension($pdf) -replace '[^A-Za-z0-9]+', '-'
    $slug = $slug.Trim('-').ToLowerInvariant()
    $volumeDirectory = Join-Path $outputRoot $slug
    New-Item -ItemType Directory -Force -Path $volumeDirectory | Out-Null

    $raw = (& $pdfBoss text $pdf | Out-String)
    if ($LASTEXITCODE -ne 0) {
        throw "pdfboss failed with exit code $LASTEXITCODE for $pdf"
    }
    $pages = $raw -split "`f", 0, 'SimpleMatch'

    for ($index = 0; $index -lt $pages.Count; $index++) {
        $pdfPage = $index + 1
        $normalized = Normalize-PdfText $pages[$index]
        $name = 'pdf-page-{0:D4}.txt' -f $pdfPage
        $destination = Join-Path $volumeDirectory $name
        [IO.File]::WriteAllText($destination, $normalized + [Environment]::NewLine, [Text.UTF8Encoding]::new($false))
        $detectedPrintedPage = Get-PrintedPageLabel $pages[$index]
        $manifest.Add([pscustomobject]@{
            volume = [IO.Path]::GetFileName($pdf)
            pdf_page = $pdfPage
            printed_page = $detectedPrintedPage
            printed_page_source = if ($detectedPrintedPage) { 'detected' } else { 'unknown' }
            relative_path = [IO.Path]::GetRelativePath($outputRoot, $destination).Replace('\', '/')
        })
    }
}

$manifestPath = Join-Path $outputRoot 'manifest.csv'

# Fill missing printed-page labels from the dominant offset independently for
# each volume. This covers pages whose number is only present in the footer.
foreach ($volumeGroup in ($manifest | Group-Object volume)) {
    $offsets = @(
        $volumeGroup.Group |
            Where-Object { $_.printed_page -match '^\d+$' } |
            ForEach-Object { [int]$_.pdf_page - [int]$_.printed_page } |
            Group-Object |
            Sort-Object Count -Descending
    )
    if ($offsets.Count -eq 0) { continue }
    $dominantOffset = [int]$offsets[0].Name
    foreach ($row in $volumeGroup.Group) {
        if (-not $row.printed_page -and [int]$row.pdf_page -gt $dominantOffset) {
            $row.printed_page = [int]$row.pdf_page - $dominantOffset
            $row.printed_page_source = 'inferred-offset'
        }
    }
}

$manifest | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding utf8
Write-Output "Indexed $($manifest.Count) PDF pages under $outputRoot"
Write-Output "Manifest: $manifestPath"
