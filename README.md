# Media Player Hotkeys

This Python script listens to the Page Up and Page Down keys and simulates the media keys for skipping to the next or previous song system-wide using the `pyautogui` and `keyboard` modules. The script also blocks the Page Up and Page Down keys from any other use while it's running to prevent conflicts with other applications.

## Requirements

- Python 3.x
- `pyautogui` module (install with `pip install pyautogui`)
- `keyboard` module (install with `pip install keyboard`)

## Usage

1. Clone the repository or download the `media_player_hotkeys.py` file.
2. Install the required modules using `pip`.
3. Run the script in a terminal or command prompt:

`python media_player_hotkeys.py`

4. Press the `Page Up` or `Page Down` key to skip to the previous or next song in your media player software.

To stop the script, press `Ctrl+C` in the terminal or command prompt.

## Customization

By default, the script uses the `Page Up` and `Page Down` keys as the hotkeys for skipping to the previous and next song. To use different keys, edit the `NEXT_KEY` and `PREV_KEY` variables at the beginning of the script.

## Notes

- This script works on Windows only, as it uses the standard media keys for skipping to the next or previous song. On other platforms, the media keys may be different or not supported by the media player software.
- While the script is running, the `Page Up` and `Page Down` keys will be blocked from any other use to prevent conflicts with other applications. To unblock the keys, stop the script or add a call to `keyboard.unblock_key()` at the end of the script.
- This script is provided as-is, without any warranty or guarantee of fitness for any particular purpose. Use it at your own risk.
