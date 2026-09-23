# Graph Learning

A personal learning space for exploring graph theory and other topics through
notes, experiments, and code.

## Areas to explore

- Graph fundamentals: vertices, edges, paths, cycles, and connectivity
- Graph representations and traversal algorithms
- Shortest paths, spanning trees, and other graph algorithms
- Related topics as curiosity leads

## Getting started

The first examples use Python. Other languages and tools may be added as needed.

### Python development container

The configuration in `.devcontainer` uses the official Jupyter Docker Stacks
`quay.io/jupyter/base-notebook:python-3.13` image. It includes Python 3.13,
JupyterLab, and an IPython kernel. VS Code also installs the Python and Jupyter
extensions.

1. Install Docker Desktop and VS Code's **Dev Containers** extension.
2. Start Docker Desktop with Linux containers enabled, then open this folder in VS Code.
3. Run **Dev Containers: Reopen in Container** from the command palette.

The first build downloads the prebuilt image from Quay.io and installs Git from
the image's OS package repositories. The notebook tools are already installed,
so setup does not run pip or download packages from `pythonhosted.org`. The
container runs as the non-root `jovyan` user and uses Python at
`/opt/conda/bin/python`. The VS Code configuration explicitly identifies the
Conda executable and environment location for interpreter discovery.
On creation, Git is configured to trust only this mounted workspace path,
avoiding ownership warnings from Windows bind mounts.

If you opened the previous configuration, run **Dev Containers: Rebuild and
Reopen in Container** to apply this change.

Host pip settings are not automatically inherited by containers. If you later
install additional packages behind a managed network, configure your
organization-approved package index inside the container. Keep internal feed
configuration and credentials out of this public repository, and do not disable
TLS verification.

If VS Code offers to install Python despite the included Conda environment,
cancel the dialog. Run **Python: Select Interpreter** and select
`/opt/conda/bin/python` (use **Enter interpreter path** if needed). For notebooks,
also select that environment in the kernel picker. The Python Environments
extension can take time to discover Conda; its Output channel shows discovery
progress. A persistent prompt after discovery may be an extension issue rather
than a missing Python installation.

### Run the Python example

From the repository root in the container's terminal:

```sh
python examples/graph_basics.py
```

The script prints the vertex and edge counts, each vertex's degree, and a
breadth-first traversal of a small undirected graph. It uses only the standard
library, so it can also run locally with Python 3.13:

```powershell
python .\examples\graph_basics.py
```

### Explore the notebook

Open `notebooks/graph_basics.ipynb` in VS Code inside the container, select the
container's Python kernel, and choose **Run All**. The notebook introduces
adjacency lists, vertex degrees, and the handshaking lemma.

Alternatively, start JupyterLab from the container's terminal:

```sh
jupyter lab --ip=0.0.0.0 --no-browser
```

Port 8888 is forwarded by the devcontainer configuration. Open the local forwarded
URL using the token printed in the terminal; leave token authentication enabled.
