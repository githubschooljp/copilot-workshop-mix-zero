# GitHub Copilot C++ Workshop

 [:jp: Japanese](README.md) | [:us: English](README.en.md)

This is a hands-on workshop to demonstrate the usage of the [GitHub Copilot](https://github.com/features/copilot). 
<br>It is a CLI tool that allows users to convert between units of different types.

## Getting Started
### Build
Run the following two commands to prepare the make file and then build the project:
```bash
cmake -S . -B build
cmake --build build
```
### Run & Test
- To run the main program:
    ```bash
      ./build/main
    ```
- To execute the tests:
    ```bash
      ./build/run-tests
    ```
### Run as VSCode Tasks
The above commands are also all defined as tasks in the `.vscode/tasks.json` file. You can run them from the VSCode Task Runner from Command Palette (<key>cmd</key>+<key>shift</key>+<key>p</key> or <key>ctrl</key>+<key>shift</key>+<key>p</key>) and typing `Run Task`.:

| Task                | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `prepare`           | Runs `cmake -S . -B build` command. You most likely won't have to run this command manually, use `build` instead. |
| `build`             | Runs `Prepare` followed by `cmake --build build` command                                                          |
| `clean:build`       | Same as `Build`, but Removes the directory before executing the Build step                                        |
| `Start Application` | Runs the `./build/main` command                                                                                   |
| `Run Tests`         | Runs the `./build/run-tests` command                                                                              |

## Hands On
- [ ] Finish the `Distance` Conversion Class and include it in the `main.cpp` (optionally, first implement tests and do a TDD appraoch)
- [ ] Add some Tests for the `Distance::convertDistance`
- [ ] Refactor all `printf` and `scanf` and use `std::cout` and `std::cin` instead
- [ ] Add a new Conversion Class for `Weight` to convert in between Kilos and Pounds
- [ ] Find any issue and fix the issue with the help of Copilot
- [ ] Add new feature with your ideas with the help of Copilot
