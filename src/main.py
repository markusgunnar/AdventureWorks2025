from sql_helpers import query_df

def main():
    print("Main started successfully!")

    query_1 = """
    SELECT TOP 5 *
    FROM Person.Password
    """

    query_1_df = query_df(query_1)

    query_1_df.head()

if __name__ == "__main__":
    main()