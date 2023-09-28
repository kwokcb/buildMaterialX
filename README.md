# buildMaterialX

This repo contains a scripts and Jupyter notebook to build MaterialX from source.

The [buildMaterialX.ipynb](buildMaterialX.ipynb) notebook contains the steps required to:

1. Clone the MaterialX repo
2. Install the required dependencies

    <img src="./images/MaterialX_os_setup_codespace_remote.png">

3. Create a build environment

    <img src="./images/MaterialX_build_setup_linux_codespace_remote.png">

4. Build MaterialX

    <img src="./images/MaterialX_build_linux_codespace_remote.png">

5. Run the MaterialX

    <img src="./images/MaterialX_test_linux_codespace_remote.png">

# Usage

The repo can be cloned or forked from and either run locally or in a GitHub Codespace. The snapshots above are from a GitHub Codespace. 

The cells of the notebook can be (re)run as needed with the caveat that the package imports and the utility to print the logged output be run.

# Caveats

Files can be modified in the source directory and the build rerun to test changes. Note that this will not update the cloned repo.

Remote Codespaces may not support GPU rendering as such trying to execute rendering may result in an error. For example the MaterialX Viewer and Graph Editor cannot be run remotely.


