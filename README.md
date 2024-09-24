# MouseTrack
Coordinate tracker, event speaker, and more

## Purpose
The purpose of **MouseTrack** is to provide speech feedback for the relative position of the mouse, the click of buttons and at which position, and utilization of the mouse in general for blind and low-vision users like myself.

Updates and changes will be made when available, and pull requests are welcome if you wish to contribute or suggest possible changes.

## How to Use
### Script Users
For those running from script, found under `mousetrack/mouse_track.py`, you will need the following libraries:

- `pynput`: Used for handling mouse input.
- `accessible_output2`: Used for relaying speech to screen readers.

You can install them using the following commands:

```bash
pip install pynput
```

```bash
pip install accessible_output2
```

You can also install the required dependencies using the `requirements.txt` file found in the main directory:

```bash
pip install -r requirements.txt
```

## License
MouseTrack has been licensed under the MIT License.

MIT License

Copyright (c) 2024 tunmi13productions

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
