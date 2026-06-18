from pathlib import Path
import os
import yaml

ADDON_DIR = Path("zwave-js-ui-second")
CONFIG_FILE = ADDON_DIR / "config.yaml"

if not CONFIG_FILE.exists():
    raise FileNotFoundError(f"Could not find {CONFIG_FILE}")

with CONFIG_FILE.open("r", encoding="utf-8") as file:
    cfg = yaml.safe_load(file)

# Keep the official release version, for example 7.2.2
upstream_version = os.environ.get("UPSTREAM_VERSION")

if not upstream_version:
    raise RuntimeError("UPSTREAM_VERSION was not supplied by the workflow")

# Make this a separate EU add-on
cfg["name"] = "Z-Wave JS EU"
cfg["version"] = upstream_version
cfg["slug"] = "zwavejs2mqtt_second"
cfg["description"] = (
    "Z-Wave JS UI instance for the EU / Bahrain 868 MHz Z-Wave controller"
)
cfg["url"] = "https://github.com/khalidaljasim/ha-zwave-js-ui-second"
cfg["panel_title"] = "Z-Wave EU"
cfg["panel_icon"] = "mdi:alpha-z-box"

# Avoid both instances advertising the same automatic discovery service
cfg["discovery"] = []

# Separate host ports
cfg["ports"] = cfg.get("ports", {})
cfg["ports"]["3000/tcp"] = 3001
cfg["ports"]["8091/tcp"] = 8092

cfg["ports_description"] = cfg.get("ports_description", {})
cfg["ports_description"]["3000/tcp"] = (
    "Z-Wave JS WebSocket for EU controller"
)
cfg["ports_description"]["8091/tcp"] = (
    "Web interface for Z-Wave JS EU"
)

with CONFIG_FILE.open("w", encoding="utf-8") as file:
    yaml.safe_dump(cfg, file, sort_keys=False)
