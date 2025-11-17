#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    path = "/tmp/hidden_4.pyc"

    module_name = "hidden_4"

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)

   # __ baslamayan sozleri yaz  
    for name in names:
        if not name.startswith("__"):
            print(name)
