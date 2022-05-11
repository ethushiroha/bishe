import os


def main():
    root_dir = "/Users/admin/Documents/bishe/nist/sts-2.1.2/sts-2.1.2/experiments/AlgorithmTesting"
    files = os.listdir(root_dir)
    for file in files:
        file_path = root_dir + f"/{file}"
        if os.path.isdir(file_path):
            file_name = file_path + "/stats.txt"
            f = open(file_name, 'r')
            content = f.read()
            if "FAILURE" in content:
                print(f"{file} ==> FAILURE")
            elif "SUCCESS" in content:
                print(f"{file} ==> SUCCESS")
            f.close()


if __name__ == '__main__':
    main()
    print("fin")
