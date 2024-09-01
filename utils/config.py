import os
import importlib
import inspect

def auto_generate_init(subfolder_path):
    subfolder_name = os.path.basename(subfolder_path)
    init_file_path = os.path.join(subfolder_path, "__init__.py")
    all_symbols = []
    import_statements = []

    # Iterate over all files in the subfolder
    for filename in os.listdir(subfolder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Strip the ".py" extension
            module_path = os.path.join(subfolder_path, filename)

            # Dynamically load the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Inspect the module for all members (classes, functions, variables)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) or inspect.isfunction(obj):
                    if obj.__module__ == module_name:
                        all_symbols.append(name)
                        import_statements.append(f"from .{module_name} import {name}")
                elif not inspect.ismodule(obj) and not name.startswith("__"):
                    # For variables (not classes or functions)
                    all_symbols.append(name)
                    import_statements.append(f"from .{module_name} import {name}")

    # Write to __init__.py
    with open(init_file_path, "w") as init_file:
        # Write import statements
        for statement in import_statements:
            init_file.write(f"{statement}\n")

        # Write the __all__ list
        init_file.write("\n__all__ = [\n")
        for symbol_name in all_symbols:
            init_file.write(f"    '{symbol_name}',\n")
        init_file.write("]\n")

def init_project(base_path):
     for root, dirs, _ in os.walk(base_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if "__pycache__" not in dir_path:
                auto_generate_init(dir_path)
