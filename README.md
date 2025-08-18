# 🏀 NBA Python Web Scraping

Scrapes NBA stats from public sources and generates simple charts of team/player performance.

## How to Run
```bash
git clone https://github.com/gaarrano/nba_python_web_scraping.git
cd nba_python_web_scraping
python NBA_web_scraping.py
```

## Requirements
- Python 3.10+
- Packages: `pandas`, `numpy`, `matplotlib`, `requests`, `beautifulsoup4`
  - (Optional) create a virtual env and install via `pip install -r requirements.txt` if you add one.

## Output
- Charts saved to the `Charts/` folder
- Example image: `team_shooting_chart.png`
- See also: **Gabriel Arrano Data Report.pdf** for a full written analysis and methodology behind the scraping and analytics.

## Repo Structure (short)
```
.
├── NBA_web_scraping.py
├── Charts/
├── PlayerTraditionalStats.xlsx
├── PlayerAdvancedStats.xlsx
├── TeamTraditionalStats2020_21.xlsx
├── TeamTraditionalStats2021_22.xlsx
├── TeamAdvancedStats2020_21.xlsx
├── TeamAdvancedStats2021_22.xlsx
├── team_shooting_chart.png
├── Gabriel Arrano Data Report.pdf
└── README.md
```

## Author
Gabriel Arrano — [@gaarrano](https://github.com/gaarrano)
