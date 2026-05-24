from pathlib import Path

from choco_coco_image_to_ascii import image_to_ascii


def photo_pokemon_to_ascci(name_pokemon: str) -> str | None:

    current_dir = Path(__file__).parent

    photo_path = current_dir / "photos" / f"{name_pokemon.lower()}.png"

    try:
        ascci_pokemon = image_to_ascii(str(photo_path), 30, 30)
        return ascci_pokemon
    except Exception:
        return None
