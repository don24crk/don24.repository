import os
import zipfile
import hashlib
import xml.etree.ElementTree as ET

# Sample addon data (can be extended or customized)
ADDONS = [
    {
        "id": "plugin.sample",
        "name": "Sample Plugin",
        "version": "1.0.0",
        "provider_name": "Sample Provider",
        "summary": "A sample addon for Kodi",
        "description": "This is a sample addon description.",
        "icon": "icon.png",
        "fanart": "fanart.jpg",
        "type": "xbmc.addon.video"
    },
    # Add more addons here if needed
]

def create_addons_xml(base_dir, addons):
    root = ET.Element("addons")
    for addon in addons:
        addon_el = ET.SubElement(root, "addon", {
            "id": addon["id"],
            "name": addon["name"],
            "version": addon["version"],
            "provider-name": addon["provider_name"]
        })
        info_el = ET.SubElement(addon_el, "info")
        info_el.text = addon["summary"]
        description_el = ET.SubElement(addon_el, "description")
        description_el.text = addon["description"]
        icon_el = ET.SubElement(addon_el, "icon")
        icon_el.text = addon["icon"]
        fanart_el = ET.SubElement(addon_el, "fanart")
        fanart_el.text = addon["fanart"]
        # Specify the extension point
        ET.SubElement(addon_el, "extension", {
            " point": addon["type"]
        })

    # Write to addons.xml
    addons_xml_path = os.path.join(base_dir, "addons.xml")
    tree = ET.ElementTree(root)
    tree.write(addons_xml_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated {addons_xml_path}")
    return addons_xml_path

def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def create_repo_structure(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    # Create resources and zips directories
    os.makedirs(os.path.join(base_dir, "resources"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "zips"), exist_ok=True)
    print(f"Repository structure created at: {base_dir}")

def generate_addons_xml_and_md5(base_dir, addons):
    addons_xml_path = create_addons_xml(base_dir, addons)
    md5_hash = compute_md5(addons_xml_path)
    md5_path = os.path.join(base_dir, "addons.xml.md5")
    with open(md5_path, "w") as f:
        f.write(md5_hash)
    print(f"Generated {md5_path} with MD5 checksum.")

def package_repo(base_dir, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                zipf.write(full_path, arcname=rel_path)
    print(f"Repository packaged into: {output_zip}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Kodi 21.3 Repo Generator with addons.xml and addons.xml.md5")
    parser.add_argument("output_dir", help="Output directory for the repo")
    parser.add_argument("--package", action="store_true", help="Create a zip package of the repo")
    args = parser.parse_args()

    create_repo_structure(args.output_dir)
    generate_addons_xml_and_md5(args.output_dir, ADDONS)

    if args.package:
        zip_path = f"{args.output_dir.rstrip(os.sep)}.zip"
        package_repo(args.output_dir, zip_path)