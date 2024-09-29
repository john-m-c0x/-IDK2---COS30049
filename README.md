# Water Potability Visualization

This project provides a set of visualizations for two cleaned water potability datasets using Plotly. It allows users to explore how various water quality features affect potability through different types of plots. Designed for Assignment 2, this repository serves as the backend for the web product expeceted in Assignment 3.

## Datasets

- **set1**: `cleaned_water_potability.xls`
- **set2**: `cleaned_water_potability02.xls`
- **set3**: `cleaned_water_potability03.xls`

## Installation

Make sure you have the following libraries installed:
- `pandas`
- `plotly`

## Dependencies

To install dependencies, paste this into cmd:
- `pip install pandas plotly`

## Command Line Arguments
`-d, --dataset`: Specify the dataset to use 

`-p, --plot_type`: Specify the type of plot to create.

`-x, --x_value`: Specify the x-axis value for the plot.

`-y, --y_value`: Specify the y-axis value for the plot (if applicable).

`--list_datasets`: Lists available datasets and their features.

## Usage 
To use script, run this command:
`python visualisation.py -d <dataset> -p <plot_type> -x <x_value> [-y <y_value>]`

For example,
`python visualisation.py -d set1 -p box -x Potability -y Solids`

You can also list datasets by using:
`python visualisation.py --list_datasets`

## Output
The script generates an HTML file named visualization.html that contains the visual representation of the selected data.
The following file is created in the local directory.

## Notes
- Box plots work when Potability/is_safe is considered as the x axis.
- Histograms work better when Potability/is_safe is on the y axis
