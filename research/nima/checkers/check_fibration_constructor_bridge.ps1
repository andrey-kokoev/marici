$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'fibration-constructor-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module FibrationCodeInterpretation -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-FibrationCodeInterpretation.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('FibrationBadProductDecoder', 'FibrationBadCodeRecovery')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    $Expected = if ($Name -eq 'FibrationBadProductDecoder') { 'false != b' } else { 'maps' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name`n$Text"
    }
    if ($Name -eq 'FibrationBadCodeRecovery' -and !$Text.Contains('atom')) { throw 'Wrong code control' }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='annotated-fiber-section-interpretation-equivalent';
     finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     controls=$Controls;
     scope='Recursive interpretation of all eight old code constructors, complete-package equivalence, transported twelve-rule closure, pointed filler equivalence and composition, retained derivations, and section-based NAND/Wolfram transport. Not equivalence of bare regrouping operations with E/P; constructor metadata and section interpretation are retained.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
