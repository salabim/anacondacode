# anacondacode

__version__ = "0.0.1"


def runner(range):

    import importlib.abc
    import sys
    import types
    import re

    def load_module(module_name, source):
        """
        load a module from memory
        based on:
        https://stackoverflow.com/questions/65009309/dynamically-import-module-from-memory-in-python-3-using-hooks
        """

        class StringLoader(importlib.abc.Loader):
            def __init__(self, modules):
                self._modules = modules

            def has_module(self, fullname):
                return fullname in self._modules

            def create_module(self, spec):
                if self.has_module(spec.name):
                    module = types.ModuleType(spec.name)
                    exec(self._modules[spec.name], module.__dict__)
                    return module

            def exec_module(self, module):
                pass

        class StringFinder(importlib.abc.MetaPathFinder):
            def __init__(self, loader):
                self._loader = loader

            def find_spec(self, fullname, path, target=None):
                if self._loader.has_module(fullname):
                    return importlib.machinery.ModuleSpec(fullname, self._loader)

        if module_name in sys.modules:  # remove from modules
            del sys.modules[module_name]

        for obj in sys.meta_path[:]:  # remove from sys.meta_path
            try:
                if obj._loader.has_module(module_name):
                    sys.meta_path.remove(obj)
            except:
                ...

        sys.meta_path.append(StringFinder(StringLoader({module_name: source})))

    regex = re.compile(r"(?i)#\s*module\s*=\s*(\w+)")
    if isinstance(range,pd.DataFrame):
        range = range.values.tolist()
    elif isinstance(range,np.ndarray):
        range=range.tolist()

    for column in zip(*range):
        module_name = None
        for line in column:
            if line is not None:
                if (match_object := re.match(regex, line)) is not None:
                    module_name = match_object.group(1)
                    break

        source = "\n".join("" if line is None else str(line) for line in column)
        if module_name:
            load_module(module_name, source)
        else:
            exec(source, globals())

    return globals().get("output")


if __name__ == "__main__":
    main()
