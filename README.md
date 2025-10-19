# Sound Visualizer

A small Python script to visualize WAV audio files (waveform and spectrogram) and optionally play them.

Features
- Read PCM WAV files (8/16/24/32-bit), mono or stereo
- Plot waveform for all channels
- Optional spectrogram per channel
- Optional playback using `simpleaudio`

Files
- `sound_visualizer.py` — main script
- `requirements.txt` — pinned Python dependencies (generated from the venv)

Quick start (macOS / zsh)

1. Create a virtual environment (if you haven't already):

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

# Sound Visualizer

这是一个轻量的 Python 脚本，用于可视化 WAV 音频文件（波形与谱图），并可选地播放音频。

主要功能
- 支持读取常见 PCM WAV（8/16/24/32-bit），支持单声道和立体声
- 绘制波形（每个通道）
- 可选绘制谱图（specgram），可指定通道
- 可选播放音频（依赖 `simpleaudio`，可选安装）

仓库文件
- `sound_visualizer.py` — 主脚本，包含命令行接口
- `requirements.txt` — 依赖清单（可由虚拟环境中的 `pip freeze` 生成）

快速开始（macOS / zsh）

1) 在项目目录创建并激活虚拟环境（推荐）

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) 安装依赖：

```bash
pip install -r requirements.txt
```

如果 `requirements.txt` 缺失或为空，可以手动安装最小集：

```bash
pip install numpy matplotlib simpleaudio librosa pygame MIDIUtil sounddevice soundfile
```

3) 运行脚本示例：

```bash
python sound_visualizer.py path/to/file.wav --spectrogram --channel 0 --save out.png --play
```

命令行参数说明
- `file` — 必需，WAV 文件路径
- `--spectrogram` — 同时显示谱图
- `--channel N` — 谱图使用的通道索引（0 开始，默认 0）
- `--save FILE` — 将当前图形保存为文件（如 out.png）
- `--play` — 播放音频（需要 `simpleaudio`）

示例用法
- 只看波形：

```bash
python sound_visualizer.py my_audio.wav
```

- 绘制波形并显示第 1 个通道的谱图：

```bash
python sound_visualizer.py my_audio.wav --spectrogram --channel 0
```

- 绘制并保存图像，同时播放：

```bash
python sound_visualizer.py my_audio.wav --spectrogram --channel 0 --save result.png --play
```

常见问题与排查
- 导入错误（ImportError）：请确认已激活虚拟环境并安装依赖：

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

- 播放失败：macOS 上推荐使用 `simpleaudio`，但系统音频设备或权限问题也可能导致失败。若遇到问题可以省略 `--play` 只做可视化。
- 24-bit WAV：脚本会把 24-bit 数据转换为 float，少数非标准 WAV 编码（非 PCM）可能不被支持。

可扩展建议
- 支持更多格式（MP3、FLAC）：可用 `pydub` 或 `soundfile`（libsndfile）扩展
- 实时输入/麦克风可视化：使用 `sounddevice` 进行实时流处理并在 matplotlib 中更新图表
- 添加 GUI：用 PyQt 或 Tkinter 包装，提升交互体验

发布许可
- MIT License

如果你想，我可以：
- 根据你当前 `.venv` 自动生成并更新 `requirements.txt`；
- 把脚本打包成可执行文件（pyinstaller）或做一个简单 GUI。
