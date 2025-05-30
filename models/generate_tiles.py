import os
import subprocess

def generer_tuiles(image_path, output_folder, epsg_code="EPSG:32619"):
    base = os.path.splitext(os.path.basename(image_path))[0]
    tif_path = os.path.join(output_folder, f"{base}.tif")
    tfw_path = os.path.splitext(image_path)[0] + ".tfw"
    jgw_path = os.path.splitext(image_path)[0] + ".jgw"

    # Copier .jgw en .tfw si nécessaire
    if os.path.exists(jgw_path):
        if not os.path.exists(tfw_path):
            os.system(f"cp {jgw_path} {tfw_path}")

    # Générer GeoTIFF
    subprocess.run([
        "gdal_translate",
        "-a_srs", epsg_code,
        image_path,
        tif_path
    ], check=True)

    # Générer tuiles avec gdal2tiles.py
    subprocess.run([
        "gdal2tiles.py",
        "-z", "0-5",
        "-w", "none",
        tif_path,
        os.path.join(output_folder, base)
    ], check=True)

    print(f"[✅] Tuiles générées dans {os.path.join(output_folder, base)}")
