import importlib.machinery
import os
import sys
import sysconfig

print(sys.version)
print("EXTENSION_SUFFIXES:", importlib.machinery.EXTENSION_SUFFIXES)
print("EXT_SUFFIX:", sysconfig.get_config_var("EXT_SUFFIX"))

import Cryptodome.Hash
hash_dir = os.path.dirname(Cryptodome.Hash.__file__)
print("installed .pyd files:", sorted(f for f in os.listdir(hash_dir) if f.endswith(".pyd")))

from Cryptodome.Hash import SHA256
print(SHA256.new(b"hello").hexdigest())
