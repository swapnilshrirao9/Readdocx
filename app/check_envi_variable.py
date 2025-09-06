import os

# Retrieve the value of the POSTGRES_DB environment variable
# The .get() method returns None if the variable is not set,
# or a specified default value if provided (e.g., os.environ.get("POSTGRES_DB", "default_db_name"))
postgres_db_value = os.environ.get("POSTGRES_DB")

# Print the retrieved value
if postgres_db_value is not None:
    print(f"The value of POSTGRES_DB is: {postgres_db_value}")
else:
    print("The environment variable POSTGRES_DB is not set.")

# You can also directly check if the variable exists in os.environ
if "POSTGRES_DB" in os.environ:
    print("POSTGRES_DB exists in os.environ.")
else:
    print("POSTGRES_DB does not exist in os.environ.")
