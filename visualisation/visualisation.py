## Workflow for COS30049 Assignment2
## Visualisation for 2 Cleaned Datasets (datasets/cleaned_water_potability.xls, datasets/cleaned_water_potability02.xls)

import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import argparse
import sys
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np

# Load datasets
set1 = pd.read_csv('datasets/cleaned_water_potability.xls')
set2 = pd.read_csv('datasets/cleaned_water_potability02.xls')

# Dict for easy access in dynamic calls 
datasets = {
    'set1': set1,
    'set2': set2
}

# Adjusted for better readability
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

# Predictive modelling as per assignment spec (How other features: x, affect y:Potability )
# Uses sklearn
def run_regression_and_plot(dataset, x_value, y_value):
    X = dataset[[x_value]]
    y = dataset[y_value]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    # Calculate MSE (SkLearn)
    mse = mean_squared_error(y_test, predictions)
    print(f"Regression MSE for {x_value} vs {y_value}: {mse:.4f}")

    # Create scatter plot with regression line
    fig = px.scatter(dataset, x=x_value, y=y_value, color='Potability' if 'Potability' in dataset.columns else 'is_safe', title=f'{x_value} vs {y_value} with Regression Line')

    # Add regression line to the plot, uses NumPy
    X_range = np.linspace(X[x_value].min(), X[x_value].max(), 100).reshape(-1, 1)
    y_pred = model.predict(X_range)
    fig.add_scatter(x=X_range.flatten(), y=y_pred, mode='lines', name='Regression Line', line=dict(color='red'))

    pyo.plot(fig, filename='regression_visualization.html')

# Classification 
def run_classification_and_plot(dataset, x_value, y_value):
    X = dataset[[x_value]]
    y = dataset[y_value]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # SkLearn
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Classification Accuracy for {x_value} vs {y_value}: {accuracy:.4f}")

    # Create scatter plot for classification
    fig = px.scatter(dataset, x=x_value, y=y_value, color='is_safe' if 'is_safe' in dataset.columns else 'Potability', title=f'{x_value} vs {y_value} Classification')

    # Mark predicted classes (predictive outcomes alongside features values)
    dataset['Predicted'] = model.predict(dataset[[x_value]])
    fig.add_scatter(x=dataset[x_value], y=dataset['Predicted'], mode='markers', name='Predicted Classes', marker=dict(color='green', size=5))

    pyo.plot(fig, filename='classification_visualization.html')

# Command Line Argument Parsing
parser = argparse.ArgumentParser(description="Visualize and model water potability data.")
parser.add_argument('-d', '--dataset', choices=list(datasets.keys()), required=False, help="Specify the dataset to use: set1 or set2.")
parser.add_argument('-p', '--plot_type', choices=['scatter', 'box', 'histogram'], required=False, help="Specify the type of plot to create: scatter, box, or histogram.")
parser.add_argument('-m', '--model_type', choices=['regression', 'classification'], required=False, help="Specify the type of model to run: regression or classification.")
parser.add_argument('-x', '--x_value', required=False, help="Specify the x-axis value for the plot or model.")
parser.add_argument('-y', '--y_value', help="Specify the y-axis value for the plot or model.")
parser.add_argument('-ls','--list_datasets', action='store_true', help="List available datasets and their features.")
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

# Run specified model type and plot results
if args.model_type == 'regression':
    if not args.y_value:
        print("Error: A y-value must be specified for regression.")
        sys.exit(1)
    run_regression_and_plot(dataset, args.x_value, args.y_value)

elif args.model_type == 'classification':
    if not args.y_value:
        print("Error: A y-value must be specified for classification.")
        sys.exit(1)
    run_classification_and_plot(dataset, args.x_value, args.y_value)

# Visualization without models can still be performed
if args.plot_type:
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
