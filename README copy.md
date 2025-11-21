# Sound Visualizer
An interactive program where sound controls particle effects: louder sounds create more and higher-flying particles, while higher pitches result in warmer-colored particles (red/orange) and lower pitches in cooler colors (blue/purple).

Environment Requirements
- Operating Systems: Windows 10/11, macOS, Linux (tested and compatible)
- Python Version: 3.8 or higher

Files
- `sound_visualizer.py` — main script
- `requirements.txt` — pinned Python dependencies (generated from the venv)

Steps

1. Create a virtual environment (if you haven't already):

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

3. Install Dependencies

```bash
pip install pygame numpy sounddevice
```

How to Interact
- Speak/Clap: Louder sounds generate more particles that fly higher.
- Hum/Sing: Lower pitches create blue/purple particles; higher pitches create red/orange particles

