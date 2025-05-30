import folium
from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None  # désactive la limite de sécurité

def lire_jgw(jgw_path):
    with open(jgw_path, 'r') as f:
        lignes = f.readlines()
        pixel_size_x = float(lignes[0])
        pixel_size_y = float(lignes[3])  # attention : souvent négatif
        top_left_x = float(lignes[4])
        top_left_y = float(lignes[5])
    return pixel_size_x, pixel_size_y, top_left_x, top_left_y

def creer_carte_mosaique(image_path, output_html):
    jgw_path = os.path.splitext(image_path)[0] + ".jgw"

    if not os.path.exists(jgw_path):
        print("[⚠️] Fichier .jgw non trouvé.")
        return

    pixel_size_x, pixel_size_y, top_left_x, top_left_y = lire_jgw(jgw_path)

    with Image.open(image_path) as img:
        width, height = img.size

    # Calcul des coins de l’image en coordonnées géo
    bottom_right_x = top_left_x + width * pixel_size_x
    bottom_right_y = top_left_y + height * pixel_size_y

    # 🧭 Bounds = [[lat_min, lon_min], [lat_max, lon_max]]
    bounds = [[bottom_right_y, top_left_x], [top_left_y, bottom_right_x]]

    m = folium.Map(
        location=[(top_left_y + bottom_right_y) / 2, (top_left_x + bottom_right_x) / 2],
        zoom_start=18,
        tiles="OpenStreetMap",
        crs='Simple'  # ✅ important pour afficher une image plane
    )

    folium.raster_layers.ImageOverlay(
        name='Mosaïque',
        image=image_path,  # ✅ chemin local réel du fichier sur le disque
        bounds=bounds,
        opacity=1,
        interactive=True,
        cross_origin=False
    ).add_to(m)

    m.fit_bounds(bounds)
    m.save(output_html)
    print(f"[✅] Carte générée avec coordonnées géo : {output_html}")
