# NVV-SuperBench: Beyond Words, Beyond Quality—Benchmarking Nonverbal Vocalizations in Speech Generation

[![Paper](https://img.shields.io/badge/Paper-arXiv%3A2604.16211-b31b1b.svg)](https://arxiv.org/pdf/2604.16211)
[![Project](https://img.shields.io/badge/Project-Page-2ea44f.svg)](https://lmxue.github.io/NVBench/)

Nonverbal vocalizations (NVVs), such as laughing, sighing, and sobbing, are essential for human-like speech, yet standardized evaluation rarely jointly assesses whether systems generate the intended NVVs, place them correctly, and keep them salient without harming speech. We present **NVV-SuperBench**, a bilingual English/Chinese benchmark for speech generation with NVVs. It provides a unified 45-type taxonomy and a multi-axis protocol beyond conventional speech quality assessment, evaluating NVV-specific controllability, placement, and perceptual salience. We benchmark 15 speech generation systems spanning prompt-based and tag-based control paradigms, using objective metrics, human listening tests, and LLM-based multi-rater evaluation. Results show that NVV controllability often decouples from speech quality, while low-SNR oral cues and long-duration affective NVVs remain bottlenecks. NVV-SuperBench highlights current gaps and supports progress toward more human-like speech generation.


## 45-type NVV taxonomy of NVBench
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Category</th>
      <th>NVV Types</th>
      <th align="center">Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Respiratory</b></td>
      <td><code>breath</code>, <code>inhale</code>, <code>exhale</code>, <code>quick breath</code>, <code>sigh</code>, <code>gasp</code>, <code>panting</code>, <code>wheezing</code>, <code>snore</code>, <code>yawn</code></td>
      <td align="center">10</td>
    </tr>
    <tr>
      <td><b>Throat / Physiological</b></td>
      <td><code>cough</code>, <code>sneeze</code>, <code>throat clearing</code>, <code>hiccup</code>, <code>sniff</code>, <code>sniffle</code>, <code>snort</code></td>
      <td align="center">7</td>
    </tr>
    <tr>
      <td><b>Laughter Spectrum</b></td>
      <td><code>chuckle</code>, <code>giggle</code>, <code>laugh</code>, <code>laugh harder</code>, <code>start laughing</code>, <code>stifled laugh</code>, <code>burst of laughter</code></td>
      <td align="center">7</td>
    </tr>
    <tr>
      <td><b>Crying Spectrum</b></td>
      <td><code>crying</code>, <code>sobbing</code>, <code>crying loudly</code>, <code>wail</code>, <code>whimper</code></td>
      <td align="center">5</td>
    </tr>
    <tr>
      <td><b>Emotional Vocalizations</b></td>
      <td><code>hum</code>, <code>humming</code>, <code>groan</code>, <code>moan</code>, <code>grunt</code>, <code>mumble</code>, <code>exclamation (ah, oh, hmm)</code></td>
      <td align="center">7</td>
    </tr>
    <tr>
      <td><b>Oral / Miscellaneous</b></td>
      <td><code>lipsmack</code>, <code>gulp</code>, <code>swallow</code>, <code>burp</code>, <code>tsk</code>, <code>sss</code>, <code>clucking</code>, <code>hissing</code>, <code>whisper</code></td>
      <td align="center">9</td>
    </tr>
    <tr>
      <td><b>Total</b></td>
      <td></td>
      <td align="center"><b>45</b></td>
    </tr>
  </tbody>
</table>

## Resources in This Repository

This repository hosts the **45-type bilingual NVV evaluation set** and the **evaluation toolkit** used in NVV-SuperBench.

### Dataset 

The `dataset/` directory contains the curated 45-type bilingual NVV evaluation set described in the paper: 2,250 English (`nvbench_data_en.json`) and 2,250 Chinese (`nvbench_data_zh.json`) instances, with balanced per-type coverage (45 NVV types × 50 instances per language). Each item follows a unified schema:

| Field | Description |
|---|---|
| `id` | Unique sample identifier |
| `text` | Plain text without NVV markers |
| `text_with_mark` | Text with the target NVV inserted as an inline `<tag>` marker (tag-based control) |
| `caption_with_nvb` | Natural-language caption describing the speaker, style, and the NVV (prompt-based control) |
| `non_verbal_events` | Ground-truth NVV type(s) for this sample |

### Evaluation 

The `evaluation/` directory provides the scripts used for the multi-axis evaluation protocol:

- **`objective_evaluation/`** — automatic, scalable metrics
  - `wer_cer/` — WER (English, Whisper-large-v3) / CER (Chinese, paraformer-zh) for intelligibility
  - `dnsmos/` — DNSMOS P.835 (SIG / BAK / OVRL) for non-intrusive perceptual speech quality
  - `clap_score/` — CLAP score for caption–speech semantic alignment (prompt-based systems)
  - `nvv_precision_recall_f1_distance/` — Coverage, Precision / Recall / F1, and Normalized Tag Distance (NTD) for NVV controllability (tag-based systems)
- **`llm_evaluation/`** — Gemini-based multi-rater LLM-as-a-judge scripts that mirror the human subjective listening protocol (Naturalness, Quality, NVV PE, Overall/NVV Instruction Following, NVV Accuracy, Overall Expression)

Each subfolder includes its own `README.md` with setup and usage instructions.

## NVV Inventories of Representative Tag-Based Speech Generation Systems and Datasets
<!-- 
NVV inventories of representative tag-based systems and datasets, as well as two recent benchmarks. §: commercial system. †: tags with higher intensity, loudness, or speed. Tags that do not correspond to non-verbal vocalizations (e.g., non-vocal sound-effect tags like `[clapping]` or purely stylistic tags like `[sarcastic]`) are excluded from systems.

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
  <tr>
    <td align="center" rowspan="2"><b>Benchmark</b></td>
    <td>WESR</td>
    <td><code>laugh</code>, <code>chuckle</code>, <code>giggle</code>, <code>cough</code>, <code>clear throat</code>, <code>whisper</code>, <code>cry</code>, <code>sob</code>, <code>inhale</code>, <code>pant</code>, <code>breath</code>, <code>sigh</code>, <code>exhale</code>, <code>shout</code>, <code>scream</code>, <code>roar</code></td>
    <td align="center">16</td>
    <td align="center">EN, ZH</td>
  </tr>
<tr>
  <td>NV-Bench</td>
  <td><code>breath</code>, <code>cough</code>, <code>sigh</code>, <code>laughter</code></td>
  <td align="center">4</td>
  <td align="center">EN, ZH</td>
</tr>
  </tbody>
</table> -->


![Word cloud of NVV tags across surveyed speech generation systems and datasets](figs/nvv_word_cloud.png)

*Word cloud of NVV tags across surveyed speech generation systems and datasets. Tag size reflects frequency of occurrence. Laughter-related vocalizations dominate current inventories, while physiological sounds (e.g., snore, hiccup) and subtle oral cues (e.g., lipsmack, gulp) remain underrepresented.* For the detailed per-system and per-dataset supported tags, please refer to the paper.

## Citation

```bibtex
@article{xue2026nvbench,
  title={NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations},
  author={Xue, Liumeng and Bian, Weizhen and Pan, Jiahao and Wang, Wenxuan and Ren, Yilin and Kang, Boyi and Hu, Jingbin and Ma, Ziyang and Wang, Shuai and Qian, Xinyuan and others},
  journal={arXiv preprint arXiv:2604.16211},
  year={2026}
}
```
