# Sinkhole Mapping & Measurement

A Python tool for measuring sinkhole dimensions using ArcGIS. This project automates the process of calculating the length and width measurements of sinkholes by computing their minimum bounding geometry.

## 📋 Features

- **Automated Measurement**: Calculates long and short axis measurements for sinkhole polygons
- **Minimum Bounding Geometry**: Uses ArcGIS to determine the longest axis and corresponding width
- **Batch Processing**: Processes multiple sinkhole features in a single execution
- **Attribute Table Integration**: Seamlessly adds MBG_Length and MBG_Width fields to your feature class

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- ArcGIS Desktop (ArcMap) or ArcGIS Pro with ArcPy installed
- An existing sinkhole polygon feature class in a geodatabase or shapefile

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sinkhole-mapping
```

2. Ensure ArcPy is available in your Python environment. If using ArcGIS Desktop Python, no additional installation is needed.

## � Git Basics

Here are the essential git commands you'll use when working with this project:

### Cloning the Repository
```bash
git clone <repository-url>
cd sinkhole-mapping
```
Creates a local copy of the remote repository on your computer.

### Checking Status
```bash
git status
```
Shows which files have been modified, added, or deleted since the last commit.

### Staging Changes
```bash
git add <filename>          # Stage a specific file
git add .                   # Stage all changes
```
Prepares changes to be committed. Staging lets you choose which changes to include in your next commit.

### Committing Changes
```bash
git commit -m "Your descriptive message"
```
Saves your staged changes to the local repository with a message describing what you changed.

### Pushing Changes
```bash
git push 
```
Uploads your committed changes to the remote repository (e.g., GitHub).

### Creating a Feature Branch
```bash
git checkout -b feature/your-feature-name
```
Creates a new branch for your work. Always create a new branch for features or bug fixes instead of working on `main`.

### Viewing Commit History
```bash
git log                     # Show all commits
git log --oneline           # Show commits in a compact format
```
Displays the history of commits in the repository.

### Pulling Latest Changes
```bash
git pull 
```
Downloads and merges the latest changes from the remote repository into your local branch.

### Basic Workflow Example
```bash
# 1. Create and switch to a new branch
git checkout -b feature/add-new-measurement

# 2. Make changes to files (edit, create, delete)

# 3. Check what changed
git status

# 4. Stage your changes
git add .

# 5. Commit with a descriptive message
git commit -m "Add new sinkhole depth measurement feature"

# 6. Push to remote repository
git push origin feature/add-new-measurement
```

## �📂 Project Structure

```
sinkhole-mapping/
├── measure-sinkholes.py    # Main measurement script using ArcPy
├── main.py                 # Additional utilities
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 💻 Usage

### Measure Sinkholes Script

The `measure-sinkholes.py` script calculates the long and short axis measurements for your sinkhole features.

**Steps:**

1. Open `measure-sinkholes.py` and configure the following variables:
   - `arcpy.env.workspace` - Path to your geodatabase or folder
   - `input_sinkholes` - Name of your established sinkhole polygon layer
   - `output_measurements` - Name for the output feature class with measurements

2. Run the script:
```bash
python measure-sinkholes.py
```

3. Upon successful execution, two new fields will be created in your feature class attribute table:
   - `MBG_Length` - The longest axis of the sinkhole
   - `MBG_Width` - The width perpendicular to the longest axis

**Example Configuration:**
```python
arcpy.env.workspace = r"C:\GIS\Projects\Sinkholes.gdb"
input_sinkholes = "Established_Sinkholes"
output_measurements = "Sinkholes_with_Axes"
```

## 📊 Supported Formats

**Input Requirements:**
- ArcGIS Feature Class (polygon geometry)
- Located in a geodatabase (.gdb) or as a shapefile

**Output:**
- Feature class with additional MBG_Length and MBG_Width fields
- Results stored in the same geodatabase or folder as specified

## 🔧 Requirements

This script requires ArcGIS to be installed with the ArcPy module available. ArcPy is automatically available if you are using:
- Python from ArcGIS Desktop (ArcMap)
- Python from ArcGIS Pro

For more information about ArcPy, visit the [ArcGIS Python API Documentation](https://pro.arcgis.com/en/pro-app/latest/arcpy/main/overview.htm).

## 📝 License

[Specify your license here]

Contributions are welcome! Please:
1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Commit your changes (`git commit -am 'Add new feature'`)
3. Push to the branch (`git push origin feature/your-feature`)
4. Open a Pull Request

## ❓ Support

For issues, questions, or suggestions, please open an issue on the project repository.

## 📞 Contact

[Add your contact information or project maintainer details]
