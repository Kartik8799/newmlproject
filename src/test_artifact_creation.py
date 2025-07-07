import os

def create_artifacts_folder():
    path = os.path.join("artifacts", "test.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        f.write("Folder created successfully!")

    print(f"Created: {os.path.abspath(path)}")

if __name__ == "__main__":
    create_artifacts_folder()
