import pathlib

from cellpy.parameters import prmreader

path = pathlib.Path()
prm_path = path.absolute() / "../cellpy/parameters/.cellpy_prms_default.conf"
prm_path = prm_path.resolve()

prmreader._write_prm_file(prm_path)
print(f"saved_prm_file {prm_path}")
