import os
import random
import imageio
import numpy as np
from PIL import Image

def create_animation(gif_path='paws.gif', width=500, height=500, num_frames=100, fps=20):
    """
    Creates a GIF of cartoonish cat paws appearing and disappearing.
    """
    # --- 1. Load Paw Images ---
    paw_files = [f for f in os.listdir('.') if f.startswith('paw_') and f.endswith('.png')]
    if not paw_files:
        print("Error: No paw images found. Please run create_paw.py first.")
        return

    paw_images = [Image.open(f).convert("RGBA") for f in paw_files]

    # --- 2. Animation Setup ---
    frames = []
    # A class to manage each paw's state
    class AnimatedPaw:
        def __init__(self):
            self.image = random.choice(paw_images)
            self.max_opacity = random.randint(180, 255) # Paws can have slightly different transparency
            self.x = random.randint(-50, width - 50)
            self.y = random.randint(-50, height - 50)
            self.birth_frame = len(frames)
            self.lifespan = random.randint(fps // 2, fps * 2) # Lives for 0.5 to 2 seconds
            self.fade_duration = int(self.lifespan * 0.4) # 40% of life is fading in/out

        def get_alpha(self, current_frame):
            age = current_frame - self.birth_frame
            if age < 0 or age > self.lifespan:
                return 0

            # Fade in
            if age < self.fade_duration:
                return int(self.max_opacity * (age / self.fade_duration))
            # Fade out
            elif age > self.lifespan - self.fade_duration:
                return int(self.max_opacity * ((self.lifespan - age) / self.fade_duration))
            # Full visibility
            else:
                return self.max_opacity

    active_paws = []

    # --- 3. Generate Frames ---
    for frame_num in range(num_frames):
        # Create a blank, transparent canvas for the frame
        frame = Image.new('RGBA', (width, height), (0, 0, 0, 0))

        # Add new paws randomly
        if random.random() < 0.25: # 25% chance to add a new paw each frame
            active_paws.append(AnimatedPaw())

        # Draw each paw on the frame
        for paw in active_paws:
            alpha = paw.get_alpha(frame_num)
            if alpha > 0:
                # Create a temporary image for the paw with the current alpha
                paw_copy = paw.image.copy()
                # We need to modify the alpha channel of the paw image itself
                alpha_layer = paw_copy.split()[3]
                new_alpha = Image.fromarray((np.array(alpha_layer) * (alpha / 255.0)).astype(np.uint8))
                paw_copy.putalpha(new_alpha)

                frame.paste(paw_copy, (paw.x, paw.y), paw_copy)

        # Clean up paws that have finished their lifecycle
        active_paws = [p for p in active_paws if (p.birth_frame + p.lifespan) > frame_num]

        # Convert frame to numpy array for imageio
        frames.append(np.array(frame))
        print(f"Generated frame {frame_num + 1}/{num_frames}")


    # --- 4. Save GIF ---
    print("Saving GIF...")
    imageio.mimsave(gif_path, frames, fps=fps, loop=0)
    print(f"Successfully created {gif_path}")


if __name__ == "__main__":
    create_animation()
