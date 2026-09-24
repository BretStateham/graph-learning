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
`quay.io/jupyter/base-notebook:python-3.13` image with Git installed. It provides
Python 3.13, JupyterLab, an IPython kernel, and the Python and Jupyter extensions
for VS Code.

1. Install Docker Desktop and VS Code's **Dev Containers** extension.
2. Start Docker Desktop with Linux containers enabled, then open this folder in VS Code.
3. Run **Dev Containers: Reopen in Container** from the command palette.

Inside the container, terminals run as the non-root `jovyan` user. Use the Conda
`base` environment at `/opt/conda/bin/python` for scripts and notebook kernels.
To select it explicitly, run **Python: Select Interpreter** or use the notebook's
kernel picker.

If VS Code offers to install Python despite the included Conda environment,
cancel the dialog. Run **Python: Select Interpreter** and select
`/opt/conda/bin/python` (use **Enter interpreter path** if needed). For notebooks,
also select that environment in the kernel picker. The Python Environments
extension can take time to discover Conda; its Output channel shows discovery
progress. A persistent prompt after discovery may be an extension issue rather
than a missing Python installation.

### Run the Python example

From the repository root in the devcontainer terminal:

```bash
python examples/graph_basics.py
```

The script prints the vertex and edge counts, each vertex's degree, and a
breadth-first traversal of a small undirected graph.

### Explore the notebook

Open `notebooks/graph_basics.ipynb` in VS Code inside the container, select the
container's Python kernel, and choose **Run All**. The notebook introduces
adjacency lists, vertex degrees, and the handshaking lemma.

Alternatively, start JupyterLab from the container's terminal for local browser
access without a token or password:

> **Security:** Without authentication, anyone who can access the forwarded port
> can run code in the container. Keep the port private and bound to localhost; do
> not expose it on your network or change the command to `--ip=0.0.0.0`.

```sh
jupyter lab --ip=127.0.0.1 --no-browser --IdentityProvider.token=''
```

Open the local address for port 8888 from VS Code's **Ports** panel, then select
`notebooks/graph_basics.ipynb` in JupyterLab. The devcontainer forwards port 8888;
forward any additional application ports manually through the Ports panel.
