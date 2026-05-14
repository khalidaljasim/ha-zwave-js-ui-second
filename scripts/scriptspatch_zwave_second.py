from pathlib import Path
import yaml

ADDON_DIR = Path("zwave-js-ui-second")
CONFIG_FILE = ADDON_DIR / "config.yaml"

with CONFIG_FILE.open("r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

# Identity changes: this makes HA see it as a different add-on
cfg["name"] = "Z-Wave JS UI - Second"
cfg["slug"] = "zwavejs2mqtt_second"
cfg["description"] = "Second Z-Wave JS UI instance for a second Z-Wave controller"
cfg["panel_title"] = "Z-Wave 2"
cfg["panel_icon"] = "mdi:alpha-z-box"

# Make the add-on point to your repo, not the official one
cfg["url"] = "https://github.com/khalidaljasim/ha-zwave-js-ui-second"

# Different exposed ports so it does not clash with your main Z-Wave JS UI
#
# Left side  = port inside the add-on
# Right side = port exposed by Home Assistant OS
cfg["ports"] = cfg.get("ports", {})
cfg["ports"]["8091/tcp"] = 8092
cfg["ports"]["3000/tcp"] = 3001

# Optional but helpful
if "ports_description" in cfg:
    cfg["ports_description"]["8091/tcp"] = "Web interface for second Z-Wave JS UI instance"
    cfg["ports_description"]["3000/tcp"] = "Z-Wave JS WebSocket for second controller"

with CONFIG_FILE.open("w", encoding="utf-8") as f:
    yaml.safe_dump(cfg, f, sort_keys=False)