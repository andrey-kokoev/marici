<#
.SYNOPSIS
Search every indexed PDF in this directory.

.EXAMPLE
.\pdf-search.ps1 'proper base change'

.EXAMPLE
.\pdf-search.ps1 -Open dag2:p41

.EXAMPLE
.\pdf-search.ps1 'proper\s+base\s+change' -Regex

.EXAMPLE
.\pdf-search.ps1 -ListBooks

.EXAMPLE
.\pdf-search.ps1 -Rebuild
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string] $Query,

    [Alias('b')]
    [string] $Book = '*',
    [string] $IndexDirectory = (Join-Path $PSScriptRoot 'extractions/pdf-search-all'),
    [Alias('n')]
    [ValidateRange(1, 10000)]
    [int] $Limit = 20,
    [ValidateRange(20, 1000)]
    [int] $Context = 100,
    [Alias('r')]
    [switch] $Regex,
    [switch] $CaseSensitive,
    [Alias('j')]
    [switch] $Json,
    [Alias('o')]
    [string] $Open,
    [switch] $ListBooks,
    [switch] $Rebuild
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Resolve-TaskPath([string] $Path) {
    if ([IO.Path]::IsPathRooted($Path)) {
        return [IO.Path]::GetFullPath($Path)
    }
    return [IO.Path]::GetFullPath((Join-Path (Get-Location) $Path))
}

function Get-Snippet {
    param(
        [string] $Text,
        [string] $Pattern,
        [bool] $UseRegex,
        [bool] $MatchCase,
        [int] $Radius
    )

    if ($UseRegex) {
        $options = if ($MatchCase) { [Text.RegularExpressions.RegexOptions]::None } else { [Text.RegularExpressions.RegexOptions]::IgnoreCase }
        try {
            $match = [regex]::Match($Text, $Pattern, $options)
        } catch {
            throw "Invalid regular expression: $($_.Exception.Message)"
        }
        if (-not $match.Success) { return $Text.Substring(0, [Math]::Min($Text.Length, 2 * $Radius)) }
        $start = $match.Index
        $length = $match.Length
    } else {
        $comparison = if ($MatchCase) { [StringComparison]::Ordinal } else { [StringComparison]::OrdinalIgnoreCase }
        $start = $Text.IndexOf($Pattern, $comparison)
        if ($start -lt 0) { return $Text.Substring(0, [Math]::Min($Text.Length, 2 * $Radius)) }
        $length = $Pattern.Length
    }

    $left = [Math]::Max(0, $start - $Radius)
    $right = [Math]::Min($Text.Length, $start + $length + $Radius)
    $prefix = if ($left -gt 0) { '…' } else { '' }
    $suffix = if ($right -lt $Text.Length) { '…' } else { '' }
    $before = $Text.Substring($left, $start - $left)
    $found = $Text.Substring($start, $length)
    $after = $Text.Substring($start + $length, $right - ($start + $length))
    return "$prefix$before>>>$found<<<$after$suffix"
}

function Find-PdfViewer {
    $command = Get-Command SumatraPDF.exe -ErrorAction SilentlyContinue
    if ($command) { return $command.Source }
    $candidates = @(
        (Join-Path $env:LOCALAPPDATA 'SumatraPDF\SumatraPDF.exe'),
        (Join-Path $env:ProgramFiles 'SumatraPDF\SumatraPDF.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'SumatraPDF\SumatraPDF.exe')
    )
    return $candidates | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
}

function Open-PdfPage([string] $PdfPath, [int] $PdfPage) {
    $viewer = Find-PdfViewer
    if ($viewer) {
        Start-Process -FilePath $viewer -ArgumentList @('-page', $PdfPage, $PdfPath)
    } else {
        Write-Warning "No page-aware viewer was found; opening the PDF with the system viewer. Go to PDF page $PdfPage."
        Start-Process -FilePath $PdfPath
    }
}

$indexRoot = Resolve-TaskPath $IndexDirectory
$manifestPath = Join-Path $indexRoot 'manifest.csv'

if ($Rebuild) {
    $builder = Join-Path $PSScriptRoot 'build-pdf-search-index.ps1'
    $pdfs = @(Get-ChildItem -LiteralPath $PSScriptRoot -Filter '*.pdf' -File | Sort-Object Name | ForEach-Object FullName)
    & $builder -InputPath $pdfs -OutputDirectory $indexRoot
    if (-not $Query -and -not $ListBooks) { exit 0 }
}

if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw "Search index not found. Run: $PSCommandPath -Rebuild"
}
if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
    throw 'ripgrep (rg) was not found on PATH.'
}

$allManifest = @(Import-Csv -LiteralPath $manifestPath)
$indexedNames = @($allManifest.volume | Sort-Object -Unique)
$currentPdfs = @(Get-ChildItem -LiteralPath $PSScriptRoot -Filter '*.pdf' -File)
$currentNames = @($currentPdfs.Name | Sort-Object -Unique)
$changedNames = @($currentPdfs | Where-Object { $_.LastWriteTimeUtc -gt (Get-Item -LiteralPath $manifestPath).LastWriteTimeUtc } | ForEach-Object Name)
$addedNames = @($currentNames | Where-Object { $_ -notin $indexedNames })
$removedNames = @($indexedNames | Where-Object { $_ -notin $currentNames })
if ($changedNames.Count -or $addedNames.Count -or $removedNames.Count) {
    Write-Warning "The PDF index may be stale (changed: $($changedNames.Count), added: $($addedNames.Count), removed: $($removedNames.Count)). Rebuild with: $PSCommandPath -Rebuild"
}
$books = @($allManifest | Group-Object volume | Sort-Object Name)
$bookRecords = foreach ($group in $books) {
    $directoryAlias = ($group.Group[0].relative_path -split '/')[0]
    $shortAlias = switch -Regex ($group.Name) {
        '^Analytic Geometry - Scholze\.pdf$' { 'scholze'; break }
        '^Beyond edoscope for the relative trace formula 2\.pdf$' { 'trace2'; break }
        '^Beyond edoscope for the relative trace formula\.pdf$' { 'trace'; break }
        '^Bott-Chern Forms and Analytic Torsion\.pdf$' { 'bott-chern'; break }
        '^Boundary Value Problems, Weyl Functions, and Differential Operators\.pdf$' { 'boundary'; break }
        '^Condensed Math and Complex Geometry\.pdf$' { 'condensed-geometry'; break }
        '^Derived algebraic geometry Vol1\.pdf$' { 'dag1'; break }
        '^Derived algebraic geometry Vol2\.pdf$' { 'dag2'; break }
        '^Condensed Mathematics\.pdf$' { 'condensed'; break }
        '^Derive analytic geometry\.pdf$' { 'analytic-dag'; break }
        '^Derived non-archemedian analytic spaces\.pdf$' { 'nonarch'; break }
        '^Direct Images and Bott-Chern Forms\.pdf$' { 'direct-images'; break }
        '^GAGA theorems\.pdf$' { 'gaga'; break }
        '^Generalized Boundary Triples\.pdf$' { 'boundary-triples'; break }
        '^Periods and harmonic analysis on spherical varieties\.pdf$' { 'periods'; break }
        '^Quillen metrics on holomorphic determinants\.pdf$' { 'quillen'; break }
        '^Refined Analytic Torsion as an Element of the Determinant Line\.pdf$' { 'refined-line'; break }
        '^Refined Analytic Torsion\.pdf$' { 'refined'; break }
        '^Spherical varieties and integral representations of L-functions\.pdf$' { 'spherical'; break }
        default { $directoryAlias }
    }
    [pscustomobject]@{ alias = $shortAlias; pages = $group.Count; file = $group.Name }
}

if ($ListBooks) {
    foreach ($record in $bookRecords) {
        Write-Output ("{0,-20} {1,4} pages  {2}" -f $record.alias, $record.pages, $record.file)
    }
    if (-not $Query) { exit 0 }
}

if ($Open -and $Open -match '^([^:]+):p(\d+)$') {
    $openAlias = $Matches[1]
    $openPage = [int]$Matches[2]
    $openBook = $bookRecords | Where-Object alias -eq $openAlias | Select-Object -First 1
    if (-not $openBook) { throw "Unknown book alias '$openAlias'. Run with -ListBooks." }
    if ($openPage -lt 1 -or $openPage -gt $openBook.pages) { throw "Page $openPage is outside $openAlias (1-$($openBook.pages))." }
    Open-PdfPage (Join-Path $PSScriptRoot $openBook.file) $openPage
    if (-not $Query) { exit 0 }
} elseif ($Open) {
    throw "Invalid locator '$Open'. Use the form dag2:p41 shown in search results."
}

if (-not $Query) {
    $commandName = if ($env:npm_lifecycle_event -eq 'pdf:search') { 'pnpm pdf:search' } else { 'pdf-search' }
    Write-Output 'PDF search'
    Write-Output ''
    Write-Output "  $commandName 'phrase'"
    Write-Output "  $commandName 'phrase' -Book dag2"
    Write-Output "  $commandName -ListBooks"
    Write-Output "  $commandName -Open dag2:p41"
    Write-Output "  $commandName -Rebuild"
    Write-Output ''
    Write-Output 'Search is literal and case-insensitive by default. Add -Regex or -CaseSensitive when needed.'
    exit 0
}

$matchingBooks = @($bookRecords | Where-Object { $_.alias -like $Book -or $_.file -like $Book })
if ($matchingBooks.Count -eq 0) {
    throw "No indexed book matches '$Book'. Run with -ListBooks to see aliases."
}
$selectedNames = @{} 
foreach ($record in $matchingBooks) { $selectedNames[$record.file] = $true }
$manifest = @($allManifest | Where-Object { $selectedNames.ContainsKey($_.volume) })
if ($manifest.Count -eq 0) {
    throw "No indexed book matches '$Book'."
}

$allowed = @{}
foreach ($row in $manifest) {
    $absolute = [IO.Path]::GetFullPath((Join-Path $indexRoot $row.relative_path))
    $allowed[$absolute.ToLowerInvariant()] = $row
}

$rgArgs = @('-l', '--no-messages', '--glob', 'pdf-page-*.txt')
if (-not $CaseSensitive) { $rgArgs += '-i' }
if (-not $Regex) { $rgArgs += '-F' }
$rgArgs += '--'
$rgArgs += $Query
$rgArgs += $indexRoot

$matchedPaths = @(& rg @rgArgs)
if ($LASTEXITCODE -gt 1) {
    throw "ripgrep failed with exit code $LASTEXITCODE."
}

$results = [Collections.Generic.List[object]]::new()
foreach ($path in $matchedPaths) {
    $absolute = [IO.Path]::GetFullPath($path)
    $key = $absolute.ToLowerInvariant()
    if (-not $allowed.ContainsKey($key)) { continue }
    $row = $allowed[$key]
    $text = [IO.File]::ReadAllText($absolute).Trim()
    $results.Add([pscustomobject]@{
        book = $row.volume
        pdf_page = [int]$row.pdf_page
        printed_page = $row.printed_page
        printed_page_source = if ($row.PSObject.Properties.Name -contains 'printed_page_source') { $row.printed_page_source } else { 'unknown' }
        locator = "$((($bookRecords | Where-Object file -eq $row.volume | Select-Object -First 1).alias)):p$([int]$row.pdf_page)"
        snippet = Get-Snippet -Text $text -Pattern $Query -UseRegex $Regex.IsPresent -MatchCase $CaseSensitive.IsPresent -Radius $Context
        source_pdf = Join-Path $PSScriptRoot $row.volume
        index_file = $absolute
    })
}

$ordered = @($results | Sort-Object book, pdf_page | Select-Object -First $Limit)

if ($Json) {
    $ordered | ConvertTo-Json -Depth 3
    exit 0
}

if ($ordered.Count -eq 0) {
    Write-Output "No matches for: $Query"
    exit 1
}

$number = 0
$currentBook = $null
foreach ($result in $ordered) {
    $number++
    if ($result.book -ne $currentBook) {
        if ($null -ne $currentBook) { Write-Output '' }
        Write-Output $result.book
        $currentBook = $result.book
    }
    $printed = if ($result.printed_page) {
        $mark = if ($result.printed_page_source -eq 'inferred-offset') { '~' } else { '' }
        " · printed $mark$($result.printed_page)"
    } else { '' }
    Write-Output ("  [{0}] PDF {1}{2}" -f $result.locator, $result.pdf_page, $printed)
    Write-Output ("      {0}" -f $result.snippet)
}

if ($ordered.printed_page_source -contains 'inferred-offset') {
    Write-Output '  ~ means the printed page was inferred from the book offset.'
}

if ($results.Count -gt $ordered.Count) {
    Write-Output ''
    Write-Output "Showing $($ordered.Count) of $($results.Count) matching pages. Increase -Limit to see more."
} else {
    Write-Output ''
    Write-Output "$($ordered.Count) matching page(s)."
}
