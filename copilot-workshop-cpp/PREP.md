# GitHub Copilot C++ Workshop Preparation

## Prerequisites

### GitHub Copilot
- GitHub Account
- GitHub Copilot License
- [VSCode](https://code.visualstudio.com/download) 

<br>(Note: This readme is written for VSCode. If you are using JetBrains IDE, please refer to the [JetBrains IDE](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/configure-personal-settings/configuring-github-copilot-in-your-environment?tool=visualstudio) section of the GitHub Copilot documentation.)

### Workshop Code & C++ basic environment
- Source Code (This repository. Git Clone it to your local machine or get files from your instructor.)
- [CMake](https://cmake.org/download/) 
- [Make](https://www.gnu.org/software/make/) 
- [GCC](https://gcc.gnu.org/) (or [Clang](https://clang.llvm.org/))

## Enable GitHub Copilot Extension
- Install [VSCode GitHub Copilot Extension](vscode:extension/GitHub.copilot) (or [JetBrains IDE GitHub Copilot Plugin](https://plugins.jetbrains.com/plugin/20772-github-copilot))
- Setup netowrking (if neccessary) (Reference: [Configuring your proxy server or firewall for Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-github-copilot-in-your-organization/configuring-your-proxy-server-or-firewall-for-copilot))
- Sign in to GitHub Copilot Extension with your GitHub account

## Verification
### GitHub Copilot is Enabled
- Make sure the Extension is enabled by checking the status bar at the bottom of the VSCode window.
<img src="docs/images/copilot-extension-icon-vscode.png" />

### Build environment
Run the following two commands to prepare the make file and then build the project. You can run the following commands in your terminal or in VSCode Terminal.
```bash
cmake -S . -B build
cmake --build build
```

## Trust Center
- [GitHub Trust Center](https://github.com/trust-center)
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/)
