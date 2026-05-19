from pathlib import Path
import os
import yaml

ADDON_DIR = Path("zwave-js-ui-second")
CONFIG_FILE = ADDON_DIR / "config.yaml"

if not CONFIG_FILE.exists():
    raise FileNotFoundError(f"Could not find {CONFIG_FILE}")

with CONFIG_FILE.open("r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

# Identity changes: this makes Home Assistant see it as a separate add-on
cfg["name"] = "Z-Wave JS EU"
cfg["slug"] = "zwavejs2mqtt_second"
cfg["description"] = "Z-Wave JS UI instance for the EU / Bahrain 868 MHz Z-Wave controller"
cfg["panel_title"] = "Z-Wave EU"
cfg["panel_icon"] = "mdi:alpha-z-box"

# Version is based on the upstream official add-on commit
upstream_short_sha = os.environ.get("UPSTREAM_SHORT_SHA", "manual")
cfg["version"] = f"eu-{upstream_short_sha}"

# Point to your custom add-on repo
cfg["url"] = "https://github.com/khalidaljasim/ha-zwave-js-ui-second"

# Prevent duplicate Z-Wave JS auto-discovery confusion with the main add-on
cfg["discovery"] = []

# Different exposed ports so it does not clash with your main Z-Wave JS UI
cfg["ports"] = cfg.get("ports", {})
cfg["ports"]["8091/tcp"] = 8092
cfg["ports"]["3000/tcp"] = 3001

# Port descriptions
cfg["ports_description"] = cfg.get("ports_description", {})
cfg["ports_description"]["8091/tcp"] = "Web interface for second Z-Wave JS UI instance"
cfg["ports_description"]["3000/tcp"] = "Z-Wave JS WebSocket for second controller"

with CONFIG_FILE.open("w", encoding="utf-8") as f:
    yaml.safe_dump(cfg, f, sort_keys=False)
