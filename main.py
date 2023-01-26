import pandas as pd
import argparse
import functions as f

if __name__ == '__main__':
    # Get arguments from CMD
    parser = argparse.ArgumentParser(prog="A360 - Global Value importer",
                                     description='Imports Global Values to A360 CR given a Global Value csv template')
    parser.add_argument("--cr_url", help="url of the control room (without the / at the end!) ")
    parser.add_argument("--username", help="full username with domain if AD")
    parser.add_argument("--api_key", help="API key for user")
    # parser.add_argument("--password", help="password")
    parser.add_argument("--gv_csv_path", help="global value csv file path")

    args = parser.parse_args()

    cr_url = str(args.cr_url)
    user = str(args.username)
    # password = str(args.password)
    api_key = str(args.api_key)
    gv_file_path = str(args.gv_csv_path)

    # Read csv
    df = pd.read_csv(gv_file_path)

    # Substitute NaN by ''
    df = df.fillna('')
    # Get token
    token = f.get_token_apikey(cr_url, user, api_key)

    # Create gv (or overwrite existing) loop:
    for index, global_value in df.iterrows():
        f.create_gv(cr_url, token, global_value)

    print("Global Values imported successfully")
