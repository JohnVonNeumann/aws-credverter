import shutil
import argparse
import csv


def check_awscli_exists(executable="aws"):
    """ check_awscli_exists
    """
    if shutil.which(executable) is None:
        return False
    else:
        return True


def parse_credentials_csv_file(file):
    """ parse_credentials_csv_file
    """
    with open(file, newline='') as content:
        reader = csv.DictReader(content)
        # not built to handle more than one line in the cred file
        count = 1
        cred_list = []
        while count > 0:
            for row in reader:
                count -= 1
                cred_list.append(
                    row['User name'],
                    row['Password'],
                    row['Access key ID'],
                    row['Secret access key'],
                    row['Console login link']
                )

    return cred_list


def create_aws_profile(list):
    """ create_aws_profile """
    profile = []


def main():
    """ main
    """
    if check_awscli_exists():
        pass
    else:
        raise Exception("aws-cli must be installed for tool to work.")

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv-file', help='Description', required=True)
    parser.add_argument('-p', '--profile', help='Description', required=True)

    args = parser.parse_args()

    print(args.csv_file)
    print(args.profile)

    creds = parse_credentials_csv_file(args.csv_file)

    create_aws_profile(creds)


if __name__ == "__main__":
    main()
