import os
import random

import pgpy_backend as pb

from flask import request

# Constants
salt_min, salt_max = 1000, 10000

def private_key_exists(path):
    return os.path.exists(os.path.join(path, "private_key.asc"))

def create_app_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def save_file(content, name, root):
    with open(os.path.join(root, name), "w") as f:
        f.write(content)

    return os.path.join(root, name)

def get_message_or_file():
    response = request.form

    if response['messageformat'] == 'text':
        msg = response['message']
    else:
        msg = str(request.files['file'].stream.read())
    return msg

# pgp functions
def generate_keys(user_id, pwd, save_path):
    salt = pb.get_salt()

    key = pb.key_generation(user_id, pwd, str(salt))
    pr_key = key
    pu_key = key.pubkey

    file_name =  "private_key.asc"
    with open(os.path.join(save_path, file_name), "w") as f:
        f.write(str(pr_key))

    return str(pu_key), salt, True


def Encrypt(msg, pu_key):
    return str(pb.encryption(pu_key, msg))

def Signature(msg_digest, pr_key, pwd, salt):
    return str(pb.sign(pr_key, msg_digest, pwd, salt))

def get_pr_key(username, storage_path):
    filename = os.path.join(storage_path, "private_key.asc")
    with open(filename, "r") as f:
        pr_key = f.read()

    return pr_key
