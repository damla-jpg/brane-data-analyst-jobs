# Panda Branes
Panda Branes is a small clone of the python package Pandas that we developed with the purpose of understading Brane in mind.

## Functions
| Function | Pandas Equivalent | Parameters | Description |
| --- | --- | --- | --- |
| hello_world() | - | - | Prints "Hello World" |
| shape(data_path: str) | shape | *data_path* - path to dataset | Returns the shape of the data |
| dtypes(data_path: str) | dtypes | *data_path* - path to dataset | Returns the data types of the columns |
| columns(data_path: str) | columns | *data_path* - path to dataset | Returns the columns of the dataset |
| index(data_path: str) | index | *data_path* - path to dataset | Returns the index of the dataset |
| describe(data_path: str) | describe | *data_path* - path to dataset | Returns the description of the dataset |
| head(data_path: str, n: int) | head | *data_path* - path to dataset<br>*n* - number of rows to return | Returns the first n rows of the dataset |
| tail(data_path: str, n: int) | tail | *data_path* - path to dataset<br>*n* - number of rows to return | Returns the last n rows of the dataset |
| loc(data_path: str, row: int, column: str) | loc | *data_path* - path to dataset<br>*row* - row index<br>*column* - column name | Returns the value of the specified row and column |
| iloc(data_path: str, row: int, column: int) | iloc | *data_path* - path to dataset<br>*row* - row index<br>*column* - column index | Returns the value of the specified row and column |
| describe_column(data_path: str, column_name: str) | describe | *data_path* - path to dataset<br>*column_name* - column name | Returns the description of the specified column |
| get_row(data_path: str, row: int) | iloc | *data_path* - path to dataset<br>*row* - row index | Returns the specified row |
| get_column(data_path: str, column_name: str) | loc | *data_path* - path to dataset<br>*column_name* - column name | Returns the specified column |
| get_column_value_counts(data_path: str, column_name: str) | value_counts | *data_path* - path to dataset<br>*column_name* - column name | Returns the value counts of the specified column |
| query(data_path: str, query: str) | query | *data_path* - path to dataset<br>*query* - query string | Returns the rows that match the query |
| sort_index(data_path: str, axis: int, ascending: bool) | sort_index | *data_path* - path to dataset<br>*axis* - axis to sort<br>*ascending* - sort ascending or descending | Returns the path to the saved modified dataset |
| sort_values(data_path: str, by: str, axis: int, ascending: bool) | sort_values | *data_path* - path to dataset<br>*by* - column to sort by<br>*axis* - axis to sort<br>*ascending* - sort ascending or descending | Returns the path to the saved modified dataset |
| drop_row(data_path: str, row: int) | drop | *data_path* - path to dataset<br>*row* - row index | Returns the path to the saved modified dataset |
| drop_columns(data_path: str, column_names: list) | drop | *data_path* - path to dataset<br>*column_names* - list of column names to drop | Returns the path to the saved modified dataset |
| keep_columns(data_path: str, column_names: list) | - | *data_path* - path to dataset<br>*column_names* - list of column names to keep | Returns the path to the saved modified dataset |
| drop_duplicates(data_path: str, keep: str) | drop_duplicates | *data_path* - path to dataset<br>*keep* - keep first or last duplicate | Returns the path to the saved modified dataset |
| dropna(data_path: str, axis: int) | dropna | *data_path* - path to dataset<br>*axis* - axis to dropna | Returns the path to the saved modified dataset |
| fillna(data_path: str, value: str) | fillna | *data_path* - path to dataset<br>*value* - value to fillna | Returns the path to the saved modified dataset |
| replace(data_path: str, old_value: str, new_value: str) | replace | *data_path* - path to dataset<br>*old_value* - value to replace<br>*new_value* - value to replace with | Returns the path to the saved modified dataset |
| cast_column(data_path: str, column_name: str, dtype: str) | astype | *data_path* - path to dataset<br>*column_name* - column name to cast<br>*dtype* - data type to cast to | Returns the path to the saved modified dataset |
| rename_column(data_path: str, rename_dict: dict) | rename | *data_path* - path to dataset<br>*rename_dict* - dictionary of old and new column names | Returns the path to the saved modified dataset |
| query_and_save(data_path: str, query: str) | query | *data_path* - path to dataset<br>*query* - query string | Returns the path to the saved modified dataset |
| exec_custom(data_path: str, func: str) | - | *data_path* - path to dataset<br>*func* - function to execute | Returns the path to the saved modified dataset |
| concat(data_path: str, other_data_path: str, axis: int) | concat | *data_path* - path to dataset<br>*other_data_path* - path to other dataset<br>*axis* - axis to concat | Returns the path to the saved modified dataset |
| merge(data_path: str, other_data_path: str, left_on: list, right_on: list, how: str) | merge | *data_path* - path to dataset<br>*other_data_path* - path to other dataset<br>*left_on* - list of column names to merge on<br>*right_on* - list of column names to merge on<br>*how* - how to merge | Returns the path to the saved modified dataset |

## Passing the correct data types

In order to pass the correct data types to the functions from Brane, we need to use arrays of strings. The `data_path` (first parameter) is always passed to the function as is, it's the other parameters that are more intricate.

Due to limitations in Brane (i.e., not supporting lists of multiple datatypes), the other parameters are passed as arrays of strings. On the bright side, we set up a way to convert these arrays of strings to the correct data types in Python. This is done by the `convert_parameters` function, which is available in the [run.py](./run.py) module. The `convert_parameters` function takes in the parameters as an array of strings and converts each value to the correct data type. The `convert_parameters` function returns a list of parameters of correct data types, which can then be passed to the function.

### Example

Let's say we want to call the `head` function from the `pandas` module. The function signature is as follows:

```python
def head(data_path: str, n: int) -> str:
    ...
```

The `head` function takes two parameters: `data_path` and `n`. The `data_path` is passed as is, but the `n` parameter is passed as an array of strings. This is because the `n` parameter is of type `int` in Python, but Brane doesn't support passing integers to Python functions yet. Therefore, we need to pass the `n` parameter as an array of strings, like so:

```rust
let data := new Data { name := "job_data" };
let number_of_rows := "5";
let result := pandas.head(data, [number_of_rows]);
println(result);
```

### Supported data types

The following data types are supported:

| Data type | Brane declaration |
| --- | --- |
| int | `let int_param := "5";` |
| float | `let float_param := "5.5";` |
| bool | `let bool_param := "True";` |
| str | `let str_param := "Hello world!";` |
| list | `let list_param := "[1, 2, 3]";` |
| dict | `let dict_param := "{\"key\": \"value\"}";` |

### Calling the functions from Brane
```rust
import panda_branes;

let data := new Data { name := "job_data" };
let int_param := "5";
let float_param := "5.5";
let bool_param := "True";
let str_param := "Hello world!";
let list_param := "[1, 2, 3]";
let dict_param := "{\"key\": \"value\"}";

let result := panda_branes.example_function(data, [int_param, float_param, bool_param, str_param, list_param, dict_param]);
```