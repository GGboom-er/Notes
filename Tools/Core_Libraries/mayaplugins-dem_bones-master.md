---
tags: [Core_Libraries, Maya_Rigging, tool]
tech_stack: [C++]
---
# 🛠️ mayaplugins-dem_bones-master
> **Autodesk Maya Dem Bones integration**

- 📂 [mayaplugins-dem_bones-master](file:///Y:/GGbommer/scripts/mayaplugins-dem_bones-master)

## 💡 详细说明
# demBones

Autodesk Maya Dem Bones integration

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* [CMake](https://cmake.org/) - Cross Platform compilation

### Generate Project

In order to generate the project for your favourite IDE.

* Create a folder called "build" inside the project folder
* Open a terminal and move to the recently created "build" folder
* Execute the line ```cmake -G "Visual Studio 15 2017" -DMAYA_VERSION=2018 ..``` for x32 project or
* Execute the line ```cmake -G "Visual Studio 15 2017 Win64" -DMAYA_VERSION=2018 ..``` for x64 project

### Compile

In order to compile from the terminal

* Follow the instructions of **Generate Project**
* Execute the line ```cmake --build . --config Release``` or ```cmake --build . --config Debug```

## Authors

* **Gorka Mendieta** [LinkedIn](https://www.linkedin.com/in/gorkamendieta/)

## License

This projec
