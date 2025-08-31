#!/usr/bin/env python3
from hyprland import Hyprctl, Events

def cleanup():
    workspaces = Hyprctl.get("workspaces")
    clients = Hyprctl.get("clients")

    for ws in workspaces:
        ws_id = ws["id"]
        count = sum(1 for c in clients if c["workspace"]["id"] == ws_id)
        if count == 0 and ws_id != 1:
            Hyprctl.dispatch("moveworkspacetomonitor", f"{ws_id},none")

def on_event(event, data):
    if event in ["workspace", "closewindow"]:
        cleanup()

if __name__ == "__main__":
    Events().listen(on_event)
