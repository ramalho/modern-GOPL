#!/usr/bin/env python3
"""
Lissajous generates GIF animations of random Lissajous figures.
Python version using Pillow library.
"""

import math
import random
import sys
from PIL import Image, ImageDraw
import io
import time

# Color palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def lissajous(output_file=None):
    """Generate a Lissajous figure animation."""
    # Constants
    cycles = 5  # number of complete x oscillator revolutions
    res = 0.001  # angular resolution
    size = 100  # image canvas covers [-size..+size]
    nframes = 64  # number of animation frames
    delay = 80  # delay between frames in milliseconds (8 * 10ms)

    # Random frequency for y oscillator
    freq = random.random() * 3.0

    # List to store animation frames
    frames = []
    phase = 0.0  # phase difference

    for frame in range(nframes):
        # Create a new image with white background
        img = Image.new('RGB', (2 * size + 1, 2 * size + 1), WHITE)
        draw = ImageDraw.Draw(img)

        # Generate the Lissajous curve points
        points = []
        t = 0.0
        while t < cycles * 2 * math.pi:
            x = math.sin(t)
            y = math.sin(t * freq + phase)

            # Convert to image coordinates
            px = size + int(x * size + 0.5)
            py = size + int(y * size + 0.5)
            points.append((px, py))

            t += res

        # Draw the curve by plotting individual points
        for px, py in points:
            if 0 <= px < 2 * size + 1 and 0 <= py < 2 * size + 1:
                draw.point((px, py), fill=BLACK)

        frames.append(img)
        phase += 0.1

    # Save as animated GIF
    if output_file:
        frames[0].save(
            output_file, save_all=True, append_images=frames[1:], duration=delay, loop=0
        )
    else:
        # Save to stdout-like buffer
        buffer = io.BytesIO()
        frames[0].save(
            buffer,
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            duration=delay,
            loop=0,
        )
        return buffer.getvalue()


def main():
    """Main function with command line argument handling."""
    # Seed random number generator
    random.seed(time.time())

    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        # Web server mode
        try:
            from http.server import HTTPServer, BaseHTTPRequestHandler

            class LissajousHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header('Content-type', 'image/gif')
                    self.end_headers()
                    gif_data = lissajous()
                    self.wfile.write(gif_data)

                def log_message(self, format, *args):
                    # Suppress default logging
                    pass

            server = HTTPServer(('localhost', 8000), LissajousHandler)
            print('Server running on http://localhost:8000')
            print('Press Ctrl+C to stop')
            server.serve_forever()

        except ImportError:
            print('HTTP server not available')
        except KeyboardInterrupt:
            print('\nServer stopped')
    else:
        # Generate GIF to file
        output_file = 'lissajous.gif'
        lissajous(output_file)
        print(f'Generated {output_file}')


if __name__ == '__main__':
    main()
