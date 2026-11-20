# Arma la página a partir de plantilla.html + datos.json.
# Para actualizar: editar datos.json (y "updated"), correr  python3 armar.py  y publicar:
#   - inside-kora-equipo.html  -> artifact de Claude (copia privada)
#   - sitio/index.html         -> repo de GitHub (GitHub Pages, link público)
import json, pathlib
d = pathlib.Path(__file__).parent
data = json.loads((d/"datos.json").read_text())
txt = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (d/"plantilla.html").read_text().replace("__DATA__", txt)
(d/"index.html").write_text('<!doctype html>\n<html lang="es">\n' + html.replace("<title>Inside KORA Equipo</title>", "<title>Inside KORA</title>", 1))
print("ok")
