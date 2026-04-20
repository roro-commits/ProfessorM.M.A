# ProfessorMMA

The official stats don't tell the whole truth, and neither does the human eye alone. A practitioner sees what casual fans miss. A model finds patterns no human intuition catches unaided. This project puts it all together.

---

## The Result

**70% accuracy vs 50% from community polls on the same 10 live UFC fights.**

Predictions made before each fight. Not backtested. No lookahead bias. Prospective validation.

---

## What It Is

Ensemble classifier with majority voting across Random Forest, XGBoost, and a PyTorch neural network (via Skorch). Data scraped from UFCStats.com, cleaned, and served through a Flask backend with a React frontend.

Three projects in one — machine learning, web development, and CI/CD deployment. The curriculum covered none of them.

---

## Model Performance

| Model | Notes |
|---|---|
| XGBoost | 80% training accuracy, biased toward wins |
| Random Forest | Strong on age and output rate features |
| Neural Network | Sensitive to learning rate, best at lr=0.001 with AdamW |
| Ensemble | 70% prospective accuracy on live fights |

**Top features by importance:** Age (DOB), Strikes Landed per Minute (SLpM), Strikes Absorbed (SApM). Stance was effectively useless.

**Known bias:** XGBoost predicted wins at 95% accuracy but losses at only 59%. Training data had more win labels than loss labels due to inconsistent data entry. Fixed in the refactor.

---

## What the Model Gets Wrong

- **Static snapshots** miss career trajectory. A declining fighter and a peaking fighter look identical if their career averages match
- **Official stats don't capture feints.** Peak Adesanya showed 36% strike accuracy — below average for a champion. He was throwing eight feints before one real strike. The model saw a poor striker. He was dismantling everyone he faced. You only understand this once you've thrown feints yourself
- **Missing values filled with dataset-wide averages** instead of weight class averages. A heavyweight and a flyweight are different athletes. Their missing stats should not be filled with the same number
- **No opponent quality adjustment**

---

## Roadmap

### Refactor
- [x] Clean project structure
- [x] Archive original 2021 system
- [ ] Modular training pipeline
- [ ] Proper train/validation/test split
- [ ] Fix class imbalance — one row per fighter per fight
- [ ] Fill missing values by weight class average
- [ ] Replace React with HTML/CSS/JS
- [ ] Baseline evaluation documented

### Phase 1 — Feature Engineering
- [ ] Automated fight-week data collection pipeline (scheduled, triggered by UFC calendar)
- [ ] Rolling window features (last 3 and 5 fights)
- [ ] Absorbed strikes trend (decline detector)
- [ ] Feint index
- [ ] Accuracy deviation from peer group
- [ ] Pressure index
- [ ] Matchup interaction features

### Phase 2 — Computer Vision
- [ ] OpenCV combat event extraction from video
- [ ] Pose estimation pipeline
- [ ] Validate CV output against UFC official stats

---

## History

| Year | What happened |
|---|---|
| 2021 | Built solo. Taught myself ML, React, and CI/CD in parallel. Prospectively validated on live fights |
| 2021-2025 | Four years training boxing, Muay Thai, and kickboxing. Domain knowledge changed how I see the data |
| 2026 | Refactor. Cleaner architecture, better features, deeper understanding |

---

## Stack

**Current:** Python, Scrapy, Scikit-learn, XGBoost, PyTorch, Skorch, Flask, React

**Adding:** SQLite/Postgres, OpenCV, MediaPipe, scheduled pipeline, HTML/CSS/JS

**Removing** React
 
---

