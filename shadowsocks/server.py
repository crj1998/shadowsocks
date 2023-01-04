
from utils import check_python_version, check_platform, get_config

def main():
    check_python_version("3.9.1")
    check_platform("linux")

    config = get_config("../example.yaml")




if __name__ == '__main__':
    main()

