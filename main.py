import shutil
import argparse


def check_awscli_exists(executable="aws"):
    if shutil.which(executable) is None:
        return False
    else:
        return True


def main():
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


if __name__ == "__main__":
    main()
