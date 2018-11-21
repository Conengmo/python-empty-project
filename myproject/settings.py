import os


main_dir = os.path.dirname(__file__)
root_dir = os.path.normpath(os.path.join(main_dir, os.pardir))
log_dir = os.path.join(root_dir, '_logs')

for path in (log_dir, ):
    if not os.path.exists(path):
        os.makedirs(path)
