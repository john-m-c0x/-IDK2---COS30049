## Workflow for COS30049 Assignment2
## Visualisation for 2 Cleaned Datasets (datasets/cleaned_water_potability.xls, datasets/cleaned_water_potability02.xls)

import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import argparse
import sys

# Load datasets
set1 = pd.read_csv('datasets/cleaned_water_potability.xls')
set2 = pd.read_csv('datasets/cleaned_water_potability02.xls')

# Dict for easy access in dynamic calls 
datasets = {
    'set1': set1,
    'set2': set2
}

# Rewritten in columns for better readability 
def list_datasets_and_features(column_width=3):
    print("Available datasets: \n")
    for dataset_name, dataset in datasets.items():
        print(f"- {dataset_name}: Features (options for x or y values in chart):")
        features = dataset.columns.tolist()

        # Splits into column_width chunks
        for i in range(0, len(features), column_width):
            chunk = features[i:i + column_width]
            print("    " + " | ".join(f"{feature}" for feature in chunk))
        print()  # linebreak

# Command Line Argument Parsing
parser = argparse.ArgumentParser(description="Visualize water potability data.")
parser.add_argument('-d', '--dataset', choices=list(datasets.keys()), required=False, help="Specify the dataset to use: set1 or set2.")
parser.add_argument('-p', '--plot_type', choices=['scatter', 'box', 'histogram'], required=False, help="Specify the type of plot to create: scatter, box, or histogram.")
parser.add_argument('-x', '--x_value', required=False, help="Specify the x-axis value for the plot.")
parser.add_argument('-y', '--y_value', help="Specify the y-axis value for the plot (if applicable).")
parser.add_argument('--list_datasets', action='store_true', help="List available datasets and their features.")
args = parser.parse_args()

# If the user wants to list datasets and features
if args.list_datasets:
    list_datasets_and_features()
    sys.exit(0)

# If dataset is not specified, exit with a message
if not args.dataset:
    print("Error: You must specify a dataset. Use --list_datasets to see available datasets.")
    sys.exit(1)

# Select dataset based on user input
dataset = datasets[args.dataset]

# Get available features
available_features = dataset.columns.tolist()

# Check if x_value and y_value exist in the selected dataset
if args.x_value and args.x_value not in available_features:
    print(f"Error: '{args.x_value}' is not a valid column in the dataset '{args.dataset}'.")
    print(f"Available features: {available_features}")
    sys.exit(1)

if args.y_value and args.y_value not in available_features:
    print(f"Error: '{args.y_value}' is not a valid column in the dataset '{args.dataset}'.")
    print(f"Available features: {available_features}")
    sys.exit(1)

# Create a single HTML file for the plot
output_file = 'visualization.html'
with open(output_file, 'w', encoding='utf-8') as combined_file:
    combined_file.write('<html><head><title>Visualization</title></head><body>\n')

    # Generate the specified plot
    if args.plot_type == 'scatter':
        if not args.y_value:
            print("Error: A y-value must be specified for scatter plots.")
            sys.exit(1)
        fig = px.scatter(dataset, x=args.x_value, y=args.y_value, color='Potability' if args.dataset == 'set1' else 'is_safe', title=f'{args.x_value} vs {args.y_value}')

    elif args.plot_type == 'box':
        if not args.y_value:
            print("Error: A y-value must be specified for box plots.")
            sys.exit(1)
        fig = px.box(dataset, x=args.x_value, y=args.y_value, color='Potability' if args.dataset == 'set1' else 'is_safe', title=f'{args.y_value} Distribution by {args.x_value}')

    elif args.plot_type == 'histogram':
        fig = px.histogram(dataset, x=args.x_value, color='is_safe' if args.dataset == 'set2' else 'Potability', barmode='overlay', title=f'{args.x_value} Distribution')

    combined_file.write(pyo.plot(fig, include_plotlyjs='cdn', output_type='div'))
    combined_file.write('</body></html>')

print(f"Visualization has been saved to {output_file}.")
