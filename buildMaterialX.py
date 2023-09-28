# %% [markdown]
# ## Building MaterialX via Python
# 
# The following is a simple example of building MaterialX from within Python.
# It assumes each step will be run once for cloning, and the build step done as many times as needed.
# A test of the build is done by running a MaterialX executable.
# 
# Note that this is example is written for a Windows build. Suitable build setup can be done
# for Linux and Mac as well.

# %% [markdown]
# ### Setup
# 
# Use OS and subprocess to run commands. Cache the root directory so we can return to it as needed

# %%
import os
import subprocess
import sys

rootdir = os.getcwd()
print('Root folder: ', rootdir)

# %%
def printLog(logfile):
    f = open(logfile, 'r')
    print(f.read())
    f.close()

# %% [markdown]
# ### Clone the Repo
# 
# This will clone the ASWF repo into a subfolder called `MaterialX`:

# %%


print('Cloning MaterialX...')
os.chdir(rootdir)
result = os.system('git clone https://github.com/AcademySoftwareFoundation/MaterialX.git > clone.log 2>&1')
print('Finished clone: %s' % ('Success' if result == 0 else 'Failed'))
if result != 0:
    printLog('clone.log')

# %% [markdown]
# # Get Submodules
# 
# Go to the MaterialX folder and get the submodules

# %%
os.chdir(rootdir)
os.chdir('MaterialX')

print('Get submodules...')
result = os.system('git submodule update --init --recursive > submodule.log 2>&1')
print('Finished getting submodules:', result)
if result != 0:
    printLog('submodule.log')

# %% [markdown]
# ### Create a "build" folder

# %%
os.chdir(rootdir)
os.chdir('MaterialX')
if not os.path.exists('build'):
    os.mkdir('build')

os.chdir('build')
print('Build folder is: ', os.getcwd())

# %% [markdown]
# ### Setup Platform / OS Build 
# 
# As required platform / OS pre-requisites should be installed. 
# 
# For example for Linux see [this page](https://code.visualstudio.com/docs/cpp/config-linux) which will be required when running a Codespace on remote host. gcc should already be installed but can be checked using by running `gcc -v`

# %%
# Pre-build setup for Linux
if sys.platform == 'linux':
    os.system('sudo apt-get update')
    os.system('sudo apt-get install xorg-dev mesa-utils')

# %% [markdown]
# ### Setup Build Configuration MaterialX 
# 
# Go to the build folder and run CMake to set up build configuration.

# %%
os.chdir(rootdir)
os.chdir('MaterialX')
os.chdir('build')

# Build setup
buildSetupCmd = 'cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON  -DMATERIALX_BUILD_VIEWER=ON -DMATERIALX_BUILD_GRAPH_EDITOR=ON -DMATERIALX_BUILD_PYTHON=ON -DMATERIALX_WARNINGS_AS_ERRORS=ON'

# Check the current OS for build setup options
osOptions = ''
if sys.platform == 'win32':
    osOptions = ' -G "Visual Studio 16 2019" -A "x64" -DCMAKE_BUILD_TYPE=RelWithDebInfo ' 
# else check if linux
elif sys.platform == 'linux':
    osOptions = ''
else:
    osOptions = ''

result = os.system(buildSetupCmd + osOptions + ' -S .. > buildsetup.log 2>&1')
print('Finished build setup: %s' % ('Success' if result == 0 else 'Failed'))
printLog('buildsetup.log')

# %% [markdown]
# ### Build MaterialX
# 

# %%
os.chdir(rootdir)
os.chdir('MaterialX')
os.chdir('build')
result = os.system('cmake --build . --target install --config RelWithDebInfo > build.log 2>&1')
print('Finished build: %s' % ('Success' if result == 0 else 'Failed'))
printLog('build.log')

# %% [markdown]
# ### Test MaterialX
# 
# Run a few tests to check that the build was successful:
# 1. Run Python script to generate shader code
# 2. Run MaterialX Graph Editor

# %%
# Runr the generateshader.py script on one of the example materials
os.chdir(rootdir)
os.chdir('MaterialX')
result = os.system('python python/Scripts/generateShader.py resources/Materials/Examples/StandardSurface/standard_surface_glass_tinted.mtlx > genshader.log 2>&1')
printLog('genshader.log')

# %%
# Run the MaterialX Editor from the install location
os.chdir(rootdir)
cmd = 'MaterialX/build/installed/bin/MaterialXGraphEditor.exe'
if os.path.exists(cmd):
    result = subprocess.Popen([cmd, '-c 1'], stdout = subprocess.PIPE)
else:
    print('MaterialXGraphEditor.exe not found') 


