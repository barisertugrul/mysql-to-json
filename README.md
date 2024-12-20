# MySQL to JSON Converter

This project converts all tables in a MySQL database to JSON files.

## Requirements

- Python 3.x
- `mysql-connector-python` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/barisertugrul/mysql-to-json.git
    cd mysql-to-json
    ```

2. Install the required Python packages:
    ```sh
    pip install mysql-connector-python
    ```

## Usage

1. Update the MySQL connection parameters in `mysql_to_json.py`:
    ```python
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'northwind'
    }
    ```
   
2. Change the `output_folder` variable to the desired output directory:
    ```python
    output_folder = 'output_dir'
    ```

3. Run the script:
    ```sh
    python mysql_to_json.py
    ```

4. JSON files will be saved in the `output_folder` folder.

## License

This project is licensed under the GPL License.