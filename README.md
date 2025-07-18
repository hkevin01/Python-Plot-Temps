# Python Plot Temps

## Overview
This project provides Python scripts for visualizing temperature and earthquake data using matplotlib, pandas, and numpy. It includes tools for data conversion, plotting, and basic testing, aimed at scientific analysis and educational use.

## Project Structure
- `src/`: Main Python scripts
- `tests/`: Unit and integration tests
- `docs/`: Documentation and project plans
- `data/`: CSV and other data files (e.g., `earthquake_data.csv`)
- `assets/`: Images and static assets (e.g., `tutorial01.png`)
- `scripts/`: Automation scripts (build, test, deploy)
- `.github/`: GitHub workflows and templates
- `.copilot/`: Copilot configuration and prompts
- `.vscode/`: Editor settings

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hkevin01/Python-Plot-Temps.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Run main scripts from the `src/` directory:
   ```bash
   python src/plottemps.py
   ```
- Example for converting data:
   ```bash
   python src/convert2dzi.py <input_image> <output_path>
   ```
- Data files are now in `data/`, and images/assets in `assets/`.
- See `docs/` for more details and examples.

## Contribution Guidelines
- Fork the repo and create a feature branch
- Submit pull requests with clear descriptions
- Follow code style and documentation standards
- See `CONTRIBUTING.md` for more info

## License
MIT License
