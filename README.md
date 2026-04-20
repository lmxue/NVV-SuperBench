# NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations
Non-verbal vocalizations (NVVs) like laughter, sighs, and sobs are essential for human-like speech, yet existing TTS benchmarks rarely test whether systems can generate the intended NVV, place it correctly, place it correctly, and keep it salient without harming speech quality. We present **Non-verbal Vocalization 
Benchmark (NVBench)**, a bilingual (English/Chinese) benchmark that evaluates speech synthesis with NVVs. NVBench pairs a unified 45-type taxonomy with a curated bilingual set and introduces a multi-axis protocol that disentangles general speech naturalness and quality from NVV-specific controllability, placement, and salience. We benchmark 15 representative TTS systems using objective metrics, listening tests, and an LLM-based multi-rater evaluation. The results reveal that NVV controllability often decouples from overall quality; structured tags can help but inventories are sparse, while low-SNR oral cues and long-duration affective NVVs remain persistent bottlenecks. NVBench enables fair cross-system comparison across diverse control interfaces under a unified, standardized framework.

## NVV Inventories of Representative Tag-Based TTS Systems and Datasets

NVV inventories of representative tag-based TTS systems and datasets. §: commercial TTS system. †: tags with higher intensity, loudness, or speed. Tags that do not correspond to non-verbal vocalizations (e.g., non-vocal sound-effect tags like `[clapping]` or purely stylistic tags like `[sarcastic]`) are excluded from systems.

<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th align="center">Type</th>
      <th>System / Dataset</th>
      <th>Supported NVV Types</th>
      <th align="center">Count</th>
      <th align="center">Lang.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" rowspan="8"><b>System</b></td>
      <td>ChatTTS</td>
      <td><code>laugh</code></td>
      <td align="center">1</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>Higgs-Audio</td>
      <td><code>laugh</code>, <code>Humming</code>, <code>cough</code></td>
      <td align="center">3</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>Bark</td>
      <td><code>laughter</code>, <code>laughs</code>, <code>sighs</code>, <code>gasps</code>, <code>clears throat</code></td>
      <td align="center">5</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>Fish-Speech</td>
      <td><code>laughing</code>, <code>chuckling</code>, <code>sobbing</code>, <code>crying loudly</code>†, <code>sighing</code>, <code>panting</code>, <code>groaning</code></td>
      <td align="center">7</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>Orpheus TTS</td>
      <td><code>laugh</code>, <code>chuckle</code>, <code>sigh</code>, <code>cough</code>, <code>sniffle</code>, <code>groan</code>, <code>yawn</code>, <code>gasp</code></td>
      <td align="center">8</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>CosyVoice 2</td>
      <td><code>breath</code>, <code>laughter</code>, <code>cough</code>, <code>clucking</code>, <code>quick_breath</code>†, <code>hissing</code>, <code>sigh</code>, <code>lipsmack</code></td>
      <td align="center">8</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>ElevenLabs§</td>
      <td><code>laughs</code>, <code>laughs harder</code>†, <code>starts laughing</code>, <code>wheezing</code>, <code>whispers</code>, <code>sighs</code>, <code>exhales</code>, <code>crying</code>, <code>snorts</code>, <code>giggles</code>, <code>swallows</code>, <code>gulps</code></td>
      <td align="center">12</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>Dia</td>
      <td><code>laughs</code>, <code>clears throat</code>, <code>sighs</code>, <code>gasps</code>, <code>coughs</code>, <code>groans</code>, <code>sniffs</code>, <code>inhales</code>, <code>exhales</code>, <code>burps</code>, <code>humming</code>, <code>sneezes</code>, <code>chuckle</code></td>
      <td align="center">13</td>
      <td align="center">EN</td>
    </tr>
    <tr>
      <td align="center" rowspan="6"><b>Dataset</b></td>
      <td>SMIIP-NV</td>
      <td><code>laughter</code>, <code>crying</code>, <code>cough</code></td>
      <td align="center">3</td>
      <td align="center">ZH</td>
    </tr>
    <tr>
      <td>NVSpeech</td>
      <td><code>breath</code>, <code>crying</code>, <code>laughter</code>, <code>cough</code>, <code>sigh</code></td>
      <td align="center">5</td>
      <td align="center">ZH</td>
    </tr>
    <tr>
      <td>SynParaSpeech</td>
      <td><code>sigh</code>, <code>throat clearing</code>, <code>laugh</code>, <code>tsk</code>, <code>gasp</code></td>
      <td align="center">5</td>
      <td align="center">ZH</td>
    </tr>
    <tr>
      <td>NonverbalTTS</td>
      <td><code>breath</code>, <code>laugh</code>, <code>sniff</code>, <code>cough</code>, <code>throat</code>, <code>sigh</code>, <code>groan</code>, <code>sneeze</code>, <code>snore</code>, <code>grunt</code></td>
      <td align="center">10</td>
      <td align="center">EN</td>
    </tr>
    <tr>
      <td>NonverbalSpeech-38k</td>
      <td><code>laughing</code>, <code>coughing</code>, <code>breath</code>, <code>sniff</code>, <code>crying</code>, <code>throat clearing</code>, <code>sigh</code>, <code>snore</code>, <code>gasp</code>, <code>yawn</code></td>
      <td align="center">10</td>
      <td align="center">EN, ZH</td>
    </tr>
    <tr>
      <td>MNV-17</td>
      <td><code>sighing</code>, <code>sneezing</code>, <code>clapping</code>, <code>hissing</code>, <code>whistling</code>, <code>clearing throat</code>, <code>coughing</code>, <code>lip smacking</code>, <code>exhaling</code>, <code>moaning</code>, <code>panting</code>, <code>sniffling</code>, <code>humming</code>, <code>laughing</code>, <code>applauding</code>, <code>inhaling</code>, <code>chuckling</code></td>
      <td align="center">17</td>
      <td align="center">ZH</td>
    </tr>
  </tbody>
</table>