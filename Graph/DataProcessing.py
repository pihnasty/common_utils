from os import path

from copy import deepcopy

from Graph import show
from Graph.constants import Constants
from Graph.utils.csv.csv_reader import read_csv
from Graph.utils.json.json_reader import read_json


class DataProcessing:
    initial_dimension_flow: None
    __numberExamples = 0

    def __init__(self, file_name):
        self.json_data = read_json(file_name)
        self.plot_parameters = self.json_data[Constants.JsonNames.plot_parameters]
        self.plot_structure = self.json_data[Constants.JsonNames.plot_structure]
        self.model_parameters = self.json_data[Constants.JsonNames.model_parameters]

    def data_shows(self):
        for graph in self.plot_structure:
            self.csv_data_path =self.model_parameters[Constants.JsonNames.output_data_paths][
                graph[Constants.JsonNames.output_data_path]
            ][Constants.JsonNames.path]
            self.output_data_path = graph[Constants.JsonNames.output_data_path]
            self.csv_data = read_csv(self.csv_data_path)

            output_directory_path = path.dirname(self.csv_data_path) + "\\" + graph[Constants.JsonNames.path]
            x_column = graph[Constants.JsonNames.x_column]
            y_columns = graph[Constants.JsonNames.y_columns]
            values = []
            self.add_column_values(values, x_column)
            for y_column in y_columns:
                self.add_column_values(values, y_column)
            plot_name = graph[Constants.JsonNames.plot_template][Constants.JsonNames.plot_name]
            plot_type = graph[Constants.JsonNames.plot_template][Constants.JsonNames.plot_type]
            file_name = graph[Constants.JsonNames.file_name]
            correct_json_data = deepcopy(self.json_data)
            self.override_parameters(correct_json_data, graph, plot_name)

            self.data_show(correct_json_data, output_directory_path, file_name, plot_name, plot_type, values)

    def add_column_values(self, values, x_column):
        for column_name in self.csv_data.columns.values.tolist():
            if column_name.strip() == x_column.strip():
                values.append(self.csv_data[column_name].values)

    @staticmethod
    def override_parameters(correct_json_data, graph, plot_name):
        overridden_parameters = graph[Constants.JsonNames.plot_template].get(Constants.JsonNames.plot_parameters, None)
        if overridden_parameters is not None:
            for key, value in overridden_parameters.items():
                if key in correct_json_data[Constants.JsonNames.plot_parameters][plot_name]:
                    correct_json_data[Constants.JsonNames.plot_parameters][plot_name][key] = value

    @staticmethod
    def data_show(json_data, path, file_name, plot_name, plot_type, plot_values):
        if plot_type == "line":
            show.common_line(json_data, path, plot_values, file_name, plot_name)
        if plot_type == "hist":
            show.common_hist(json_data, path, plot_values, file_name, plot_name)
        if plot_type == "q_q":
            show.common_q_q(json_data, path, plot_values, file_name, plot_name)
