import os
import subprocess

def generer_tuiles(image_path, output_folder, epsg_code="EPSG:32619"):
    base = os.path.splitext(os.path.basename(image_path))[0]

    # 🔁 On place le .tif dans le même dossier que le .jpg/.jgw
    image_dir = os.path.dirname(image_path)
    tif_path = os.path.join(output_folder, base + ".tif")

    # 🔁 On vérifie si .tfw existe, sinon on copie le .jgw
    tfw_path = os.path.join(image_dir, f"{base}.tfw")
    jgw_path = os.path.join(image_dir, f"{base}.jgw")

    if os.path.exists(jgw_path) and not os.path.exists(tfw_path):
        os.system(f"cp {jgw_path} {tfw_path}")

    # 📍 Convertir en GeoTIFF avec projection
    subprocess.run([
        "gdal_translate",
        "-a_srs", "EPSG:3857",
        image_path,
        tif_path
    ], check=True)

    # 🧱 Générer les tuiles
    subprocess.run([
        "gdal2tiles.py",
        "-z", "0-5",
        "-w", "none",
        tif_path,
        os.path.join(output_folder, base)
    ], check=True)

    print(f"[✅] Tuiles générées dans {os.path.join(output_folder, base)}")
