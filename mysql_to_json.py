import mysql.connector
import json
import os
from datetime import datetime
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def mysql_to_json():
    # Set MySQL connection parameters
    config = {
        'host': 'localhost', # Change this to your MySQL server IP address
        'user': 'root', # Change this to your MySQL username
        'password': '', # Change this to your MySQL password
        'database': 'northwind' # Change this to your MySQL database name
    }

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)

        # The folder to save JSON files
        output_folder = "output_folder" # Change this to your desired folder name
        os.makedirs(output_folder, exist_ok=True)

        # List all tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Convert each table to JSON
        for table in tables:
            table_name = list(table.values())[0]

            # Get all rows from the table using backticks
            try:
                cursor.execute(f"SELECT * FROM `{table_name}`")
                rows = cursor.fetchall()

                # Convert datetime objects to string and decimal objects to float
                for row in rows:
                    for key, value in row.items():
                        if isinstance(value, datetime):
                            row[key] = value.isoformat()
                        elif isinstance(value, Decimal):
                            row[key] = float(value)

                            # Write the table data to a JSON file
                json_file = os.path.join(output_folder, f"{table_name}.json")
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(rows, f, indent=4, ensure_ascii=False, cls=DecimalEncoder)

                print(f"Converted table '{table_name}' to JSON file: {json_file}")

            except mysql.connector.Error as table_err:
                print(f"Error processing table '{table_name}': {table_err}")
                continue

        print("\nAll tables successfully converted to JSON format.")
        print(f"All files are saved to the '{output_folder}' folder.")

        # List of created files
        created_files = [f"{table_name}.json" for table in tables]
        print("\nCreated files:")
        for file in created_files:
            print(f"- {file}")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"General Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("\nMySQL connection closed.")

if __name__ == "__main__":
    mysql_to_json()

# Created/Modified files during execution:
# [tablename].json files will be created in the {output_folder} folder
