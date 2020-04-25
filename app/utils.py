import os

def private_key_exists(path):
    return os.path.exists(os.path.join(path, "private_key.key"))

def create_app_folder(app):
    if not os.path.exists(app.path):
        os.mkdir(app.path)
    if not os.path.exists(app.tmp_path):
        os.mkdir(app.tmp_path)

def save_file(content, name, root):
    with open(os.path.join(root, name), "w") as f:
        f.write(content)

    return os.path.join(root, name)
