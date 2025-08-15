# data science container

A collection of data science exercises and tutorials using Python, pandas, scikit-learn, and Jupyter notebooks.

## project structure

```shell
.devcontainer/
├── devcontainer.json
└── Containerfile
notebook/
├── exercise_1/
│   ├── titanic.csv
│   └── titanic_exercise.ipynb
├── exercise_2/
│   ├── airbnb_dirty.csv
│   └── airbnb_exercise.ipynb
└── exercise_3/
    └── derivatives_and_regression.ipynb
pyproject.toml
uv.lock
```

## exercises

### exercise 1: titanic dataset analysis

Statistical analysis of the Titanic disaster dataset exploring:

- Age vs family size correlations
- Gender vs survival patterns  
- Passenger investigation ("Mr. Anderson" case study)
- Advanced missing data reconstruction using passenger titles

### exercise 2: airbnb price prediction

Real-world data cleaning and machine learning with messy Airbnb listing data:

- Data exploration and cleaning
- Feature engineering
- Linear regression modeling
- Model evaluation and interpretation

### exercise 3: derivatives and linear regression

Mathematical foundations covering:

- Single variable derivative calculations
- Multi-variable gradients
- Numerical derivative approximation methods
- Linear regression error functions

## dependencies

Key Python packages used in this project:

- **[ipykernel](https://pypi.org/project/ipykernel/)** - Jupyter notebook kernel
- **[matplotlib](https://matplotlib.org/)** - Data visualization
- **[pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning algorithms
- **[seaborn](https://seaborn.pydata.org/)** - Statistical data visualization
- **[pgeocode](https://pypi.org/project/pgeocode/)** - Geocoding for location data

## development environment

This project includes a [VS Code devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) for a consistent development environment. The devcontainer provides:

- **Custom Arch Linux container** with Python, uv, mise, and development tools pre-installed
- **Pre-configured VS Code extensions** for Python data science workflows
- **Isolated environment** with project dependencies automatically managed

### required vs code extensions

The devcontainer automatically installs these extensions:

- **[Ruff (Astral Software)](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)** - Python linting and formatting
- **[GitHub Copilot Chat (GitHub)](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)** - AI-powered coding assistance
- **[GitHub Pull Requests (GitHub)](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)** - GitHub integration
- **[Git Graph v3 (Gxl)](https://marketplace.visualstudio.com/items?itemName=gxl.git-graph-3)** - Git repository visualization
- **[Rainbow CSV (mechatroner)](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)** - CSV file syntax highlighting
- **[Python Debugger (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)** - Python debugging
- **[Pylance (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - Python language server
- **[Jupyter (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)** - Jupyter notebook support
- **[Python Data Science Extension Pack (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.python-ds-extension-pack)** - Data science extension bundle
- **[Jupyter PowerToys (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-powertoys)** - Advanced Jupyter features
- **[Even Better TOML (tamasfe)](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)** - TOML file support
- **[Error Lens (Alexander)](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)** - Inline error highlighting

### getting started with devcontainer

1. Install [VS Code](https://code.visualstudio.com/) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open this project in VS Code
3. When prompted, click "Reopen in Container" or use `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
4. VS Code will build the container and set up the development environment automatically

For more information, see the [VS Code devcontainer documentation](https://code.visualstudio.com/docs/devcontainers/containers).

## setup

This project uses `uv` for dependency management. Install dependencies with:

```shell
uv sync
```

## usage

Launch Jupyter notebook to explore the exercises:

```shell
jupyter notebook
```

Navigate to the `notebook/` directory and open any of the exercise notebooks to get started.
