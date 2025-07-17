# Data Science Development Container

> A beginner-friendly template for data science projects using VS Code, Development Containers, and modern Python tooling.

## 🎯 What This Template Provides

This template sets up a complete data science development environment that runs inside a container, ensuring consistency across different machines. Perfect for beginners who want to start data science projects without complex setup.

**Key Features:**
- 🐍 Python 3.11 with essential data science libraries
- 📊 Pre-configured Jupyter notebooks for interactive analysis
- 🚀 UV package manager for fast, reliable dependency management
- 🔧 VS Code extensions for Python development and data science
- 🎨 Code formatting and linting with Ruff
- 📁 Sample datasets and exercises to get started

## 📋 Prerequisites

Before using this template, ensure you have:

1. **VS Code** installed ([Download here](https://code.visualstudio.com/))
2. **Docker Desktop** or **Podman** installed
   - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - [Podman Desktop](https://podman-desktop.io/) (alternative)
3. **Dev Containers extension** for VS Code
   - Install from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 🚀 Getting Started

### 1. Use This Template
Click "Use this template" on GitHub or clone this repository:
```bash
git clone <repository-url>
cd data_science_container
```

### 2. Open in VS Code
```bash
code .
```

### 3. Open in Dev Container
When VS Code opens, you'll see a notification: "Reopen in Container"
- Click "Reopen in Container"
- Or use Command Palette (Ctrl/Cmd + Shift + P) → "Dev Containers: Reopen in Container"

### 4. Wait for Setup
The container will build automatically (first time takes 2-3 minutes). Once complete, you'll have a fully configured data science environment!

## 📁 Project Structure

```shell
data_science_container/
├── .devcontainer/
│   └── devcontainer.json     # Container configuration
├── .uv-cache/                # UV package cache (auto-generated)
├── notebook/                 # Jupyter notebooks
│   └── .gitkeep              # placeholer file for notebook folder
├── main.py                   # Main Python script
├── pyproject.toml            # Project dependencies and metadata
├── uv.lock                   # Locked dependency versions
├── .gitignore                # Git ignore rules
└── readme.md                 # This file
```

### Key Files Explained

- **`pyproject.toml`**: Defines your project dependencies and metadata (like `package.json` for Node.js)
- **`uv.lock`**: Locks exact versions of all dependencies for reproducible builds
- **`.devcontainer/devcontainer.json`**: Configures the development container environment
- **`.uv-cache/`**: Local cache for UV packages (improves performance)

## 🧠 Core Concepts for Beginners

### What is a Development Container?
A development container (devcontainer) is a running container that provides a complete development environment. It includes:
- Your code editor (VS Code)
- Programming language runtime (Python 3.11)
- Tools and extensions
- Dependencies and libraries

**Benefits:**
- ✅ Consistent environment across different machines
- ✅ No "it works on my machine" issues
- ✅ Easy to share and reproduce
- ✅ Isolated from your host system

### Python Virtual Environments vs Containers
- **Virtual Environments**: Isolate Python packages but share the system Python
- **Containers**: Isolate the entire runtime environment, including Python version, system libraries, and tools

### UV vs pip
- **pip**: Traditional Python package installer
- **UV**: Modern, faster alternative that provides:
  - 🚀 10-100x faster than pip
  - 🔒 Deterministic dependency resolution
  - 📦 Better handling of complex dependencies
  - 🎯 Cleaner project structure

## 🛠️ Essential Commands

### Package Management with UV

```bash
# Add a new package
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a package
uv remove package-name

# Install all dependencies
uv sync

# Show installed packages
uv pip list

# Run a Python script
uv run python main.py

# Run a specific command
uv run jupyter notebook
```

### Running Python Code

```bash
# Run the main Python script
uv run python main.py

# Run a specific Python file
uv run python path/to/your/script.py

# Start a Python REPL
uv run python

# Run with specific arguments
uv run python script.py --arg1 value1
```

### Jupyter Notebooks

```bash
# Start Jupyter Lab (recommended)
uv run jupyter lab

# Start classic Jupyter Notebook
uv run jupyter notebook

# Run a notebook from command line
uv run jupyter execute notebook/titanic/titanic_exercise.ipynb
```

### Code Quality Tools

```bash
# Format code with Ruff
uv run ruff format .

# Lint code with Ruff
uv run ruff check .

# Fix linting issues automatically
uv run ruff check --fix .
```

## 📊 Data Science Workflow

### 1. Start with Sample Data
Explore the included examples:
- `notebook/titanic/titanic_exercise.ipynb` - Beginner-friendly data analysis
- `notebook/linear_regression/` - Machine learning examples

### 2. Working with Notebooks
1. Open VS Code in the container
2. Navigate to `notebook/` folder
3. Open any `.ipynb` file
4. Click "Run All" or run cells individually

### 3. Adding New Packages
Common data science packages you might want to add:
```bash
# Visualization
uv add plotly bokeh

# Machine Learning
uv add xgboost lightgbm

# Data Processing
uv add polars dask

# Statistics
uv add scipy statsmodels
```

### 4. Creating New Notebooks
1. Right-click in the `notebook/` folder
2. Select "New File"
3. Name it `your_analysis.ipynb`
4. VS Code will automatically recognize it as a Jupyter notebook

### 5. Best Practices
- 📁 Organize notebooks by topic/project
- 📝 Use markdown cells for documentation
- 🧹 Clean up outputs before committing
- 💾 Save datasets in appropriate folders
- 🔄 Regularly sync dependencies with `uv sync`

## 🔧 Pre-configured Tools

This template includes these VS Code extensions:
- **Python & Pylance**: Core Python support
- **Jupyter**: Notebook support
- **Ruff**: Fast Python linter and formatter
- **Python Data Science Extension Pack**: Complete data science toolkit
- **Even Better TOML**: Better support for configuration files

## 🐛 Troubleshooting

### Container Won't Build
```bash
# Rebuild container from scratch
# Command Palette → "Dev Containers: Rebuild Container"
```

### UV Commands Not Working
```bash
# Ensure you're in the container
# Check if UV is installed
uv --version

# If not working, rebuild the container
```

### Package Installation Issues
```bash
# Clear UV cache
rm -rf .uv-cache
uv sync

# Or set different cache location
export UV_CACHE_DIR=/tmp/uv-cache
```

### Jupyter Kernel Issues
```bash
# Reinstall kernel
uv add --dev ipykernel
uv run python -m ipykernel install --user --name=data-science-container
```

### Permission Issues
```bash
# If you get permission errors, check container user
whoami

# Files should be owned by your user inside container
```

**For Jupyter debugging:**
- Set breakpoints directly in notebook cells
- Use "Debug Cell" in dropdown menu next to "Run Cell" button (left side of cell with Play icon)

## 📚 Next Steps & Resources

### Learning Resources
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

### Customizing This Template
- Edit `pyproject.toml` to change project metadata
- Modify `.devcontainer/devcontainer.json` to add VS Code extensions
- Update dependencies in `pyproject.toml` and run `uv sync`

### Advanced Topics
- [UV Documentation](https://docs.astral.sh/uv/)
- [Development Containers](https://containers.dev/)
- [VS Code Python Guide](https://code.visualstudio.com/docs/python/python-tutorial)

## 🤝 Contributing

This template is designed to be a starting point. Feel free to:
- Add new sample datasets
- Create example notebooks
- Improve documentation
- Share your data science projects built with this template

## 📄 License

This template is open source and available under the [MIT License](LICENSE).

---

**Happy Data Science! 🎉**

*If you find this template helpful, please star the repository and share it with others!*