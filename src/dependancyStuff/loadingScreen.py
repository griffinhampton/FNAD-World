"""
Low-Memory Loading Screen for FNAD World
Displays loading progress without heavy graphics or animations
"""
import pygame
import math
import time
import os

class LoadingScreen:
    """Lightweight loading screen with minimal memory footprint"""
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = pygame.time.Clock()
        
        # Colors (RGB tuples - no image loading needed)
        self.bg_color = (25, 25, 35)      # Dark blue-gray
        self.text_color = (200, 200, 200)  # Light gray
        self.progress_bg = (50, 50, 60)    # Darker gray
        self.progress_fill = (100, 150, 200)  # Blue
        self.accent_color = (150, 100, 250)  # Purple
        
        # Font (pygame default font - no file loading)
        self.title_font = None
        self.text_font = None
        self.small_font = None
        
        # Loading state
        self.current_task = "Initializing..."
        self.progress = 0.0
        self.start_time = time.time()
        
        # Animation variables (simple, no textures)
        self.spinner_angle = 0
        self.dots_animation = 0
        
        # Player animation
        self.player_sprites = []
        self.current_sprite_index = 0
        self.animation_timer = 0
        self.sprites_loaded = False
        
    def initialize(self):
        """Initialize pygame components for loading screen"""
        if pygame.get_init():
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("FNAD World - Loading...")
        else:
            pygame.init()
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("FNAD World - Loading...")
            
        # Initialize fonts (using pygame's built-in fonts)
        self.title_font = pygame.font.Font(None, 48)
        self.text_font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        
        # Load player sprites
        self.load_player_sprites()
        
    def get_image(self, sheet, col, row, width, height, scale):
        """Extract individual sprite from sprite sheet (same method as playerSprites.py)"""
        rect = pygame.Rect(col * width, row * height, width, height)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), rect)
        if scale != 1:
            image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def load_player_sprites(self):
        """Load player walking sprites from Down Animations.png"""
        try:
            # Find the image path relative to the loading screen file
            current_dir = os.path.dirname(__file__)
            # Go up from dependancyStuff to src, then to img
            sprite_path = os.path.join(current_dir, '..', 'img', 'Down Animations.png')
            sprite_path = os.path.abspath(sprite_path)  # Resolve the path
            
            if os.path.exists(sprite_path):
                # Load the sprite sheet
                sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
                
                # Extract individual frames using the same method as playerSprites.py
                # Extract 5 frames from the sprite sheet (same as player animation)
                for i in range(5):
                    row = i // 5  # Row index (should be 0 for all frames)
                    col = i % 5   # Column index (0, 1, 2, 3, 4)
                    # Use TILESIZE from config or default to 32
                    try:
                        from src.dependancyStuff.config import TILESIZE
                        tile_size = TILESIZE
                    except:
                        tile_size = 32  # Fallback
                    
                    frame = self.get_image(sprite_sheet, col, row, tile_size, tile_size, 1)
                    self.player_sprites.append(frame)
                
                self.sprites_loaded = True
                print(f"Loaded {len(self.player_sprites)} player animation frames")
            else:
                print(f"Player sprite file not found at: {sprite_path}")
                
        except Exception as e:
            print(f"Failed to load player sprites: {e}")
            self.sprites_loaded = False
    
    def draw_player_animation(self, x, y):
        """Draw animated player walking based on loading progress"""
        if not self.sprites_loaded or not self.player_sprites:
            # Fallback: draw a simple colored rectangle
            pygame.draw.rect(self.screen, self.accent_color, (x-10, y-15, 20, 30))
            return
            
        # Calculate which frame to show based on elapsed time
        # Change frame every 0.25 seconds (4 frames per second)
        elapsed_time = time.time() - self.start_time
        frame_time = elapsed_time / 0.25  # Number of 0.25-second intervals
        current_frame = int(frame_time) % 5  # Cycle through frames 0-4
        
        # Draw current sprite frame
        current_sprite = self.player_sprites[current_frame]
        sprite_rect = current_sprite.get_rect(center=(x, y))
        self.screen.blit(current_sprite, sprite_rect)
        
    def update_progress(self, progress, task_name="Loading..."):
        """Update loading progress and current task"""
        self.progress = max(0.0, min(1.0, progress))  # Clamp between 0-1
        self.current_task = task_name
        
    def draw_spinner(self, center_x, center_y, radius=20):
        """Draw a simple rotating spinner"""
        self.spinner_angle += 8  # Rotation speed
        if self.spinner_angle >= 360:
            self.spinner_angle = 0
            
        # Draw spinner arcs
        for i in range(0, 360, 45):
            alpha = 255 - (i * 3)  # Fade effect
            if alpha < 50:
                alpha = 50
                
            angle_rad = math.radians(i + self.spinner_angle)
            start_x = center_x + math.cos(angle_rad) * (radius - 5)
            start_y = center_y + math.sin(angle_rad) * (radius - 5)
            end_x = center_x + math.cos(angle_rad) * radius
            end_y = center_y + math.sin(angle_rad) * radius
            
            color = (alpha, alpha, alpha)
            pygame.draw.line(self.screen, color, (start_x, start_y), (end_x, end_y), 3)
            
    def draw_progress_bar(self, x, y, width, height):
        """Draw progress bar"""
        # Background
        pygame.draw.rect(self.screen, self.progress_bg, (x, y, width, height))
        pygame.draw.rect(self.screen, self.text_color, (x, y, width, height), 2)
        
        # Progress fill
        fill_width = int(width * self.progress)
        if fill_width > 0:
            pygame.draw.rect(self.screen, self.progress_fill, (x + 2, y + 2, fill_width - 4, height - 4))
            
        # Progress percentage text
        percent_text = f"{int(self.progress * 100)}%"
        text_surface = self.text_font.render(percent_text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)
        
    def draw_loading_dots(self, x, y):
        """Draw animated loading dots"""
        self.dots_animation += 0.2
        dots = "Loading"
        
        # Add animated dots
        num_dots = int(self.dots_animation) % 4
        dots += "." * num_dots
        
        text_surface = self.small_font.render(dots, True, self.text_color)
        self.screen.blit(text_surface, (x, y))
        
    def render(self):
        """Render the loading screen"""
        if not self.screen:
            return
            
        # Clear screen
        self.screen.fill(self.bg_color)
        
        center_x = self.width // 2
        center_y = self.height // 2
        
        # Title
        title_surface = self.title_font.render("FNAD World", True, self.accent_color)
        title_rect = title_surface.get_rect(center=(center_x, center_y - 100))
        self.screen.blit(title_surface, title_rect)
        
        # Subtitle
        subtitle_surface = self.text_font.render("Loading Game World...", True, self.text_color)
        subtitle_rect = subtitle_surface.get_rect(center=(center_x, center_y - 60))
        self.screen.blit(subtitle_surface, subtitle_rect)
        
        # Player walking animation (positioned near progress bar)
        player_x = center_x - 200 + int(self.progress * 200)  # Walk across screen with progress
        player_y = center_y + 10
        self.draw_player_animation(player_x, player_y)
        
        # Spinner
        self.draw_spinner(center_x, center_y - 10)
        
        # Progress bar
        bar_width = 400
        bar_height = 30
        bar_x = center_x - bar_width // 2
        bar_y = center_y + 40
        self.draw_progress_bar(bar_x, bar_y, bar_width, bar_height)
        
        # Current task
        task_surface = self.small_font.render(self.current_task, True, self.text_color)
        task_rect = task_surface.get_rect(center=(center_x, bar_y + 50))
        self.screen.blit(task_surface, task_rect)
        
        # Loading dots animation
        self.draw_loading_dots(center_x - 30, bar_y + 80)
        
        # Elapsed time
        elapsed = time.time() - self.start_time
        time_text = f"Time: {elapsed:.1f}s"
        time_surface = self.small_font.render(time_text, True, self.text_color)
        time_rect = time_surface.get_rect(bottomright=(self.width - 10, self.height - 10))
        self.screen.blit(time_surface, time_rect)
        
        # Tips/hints
        tips = [
            "🎮 Use arrow keys to move around the world",
            "🏠 Press F to interact with buildings", 
            "🗺️ Explore different biomes: Plains, Snow, Mountains",
            "⚔️ Enter buildings to start battle encounters",
            "🌍 Each world has unique terrain and settlements"
        ]
        
        # Rotate through tips based on time
        tip_index = int(elapsed / 3) % len(tips)
        tip_surface = self.small_font.render(tips[tip_index], True, (150, 150, 150))
        tip_rect = tip_surface.get_rect(center=(center_x, self.height - 40))
        self.screen.blit(tip_surface, tip_rect)
        
        # Update display
        pygame.display.flip()
        self.clock.tick(30)  # 30 FPS for smooth animation
        
    def handle_events(self):
        """Handle pygame events during loading"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
        
    def cleanup(self):
        """Clean up loading screen resources"""
        # Don't quit pygame - game will use it
        # Just clear references
        self.screen = None
        self.title_font = None
        self.text_font = None
        self.small_font = None


# Context manager for easy use
class LoadingScreenContext:
    """Context manager for loading screen"""
    
    def __init__(self, width=800, height=600):
        self.loading_screen = LoadingScreen(width, height)
        self.active = False
        
    def __enter__(self):
        self.loading_screen.initialize()
        self.active = True
        return self.loading_screen
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.active:
            self.loading_screen.cleanup()
            self.active = False


# Helper function for quick use
def show_loading_screen_during(func, *args, **kwargs):
    """Show loading screen while executing a function"""
    
    class ProgressTracker:
        def __init__(self, loading_screen):
            self.loading_screen = loading_screen
            
        def update(self, progress, task="Loading..."):
            self.loading_screen.update_progress(progress, task)
            self.loading_screen.render()
            if not self.loading_screen.handle_events():
                raise KeyboardInterrupt("Loading cancelled by user")
    
    with LoadingScreenContext() as loader:
        # Add progress tracker to kwargs if function supports it
        if 'progress_callback' in kwargs or len(args) == 0:
            tracker = ProgressTracker(loader)
            kwargs['progress_callback'] = tracker.update
            
        # Initial render
        loader.render()
        
        # Execute function
        result = func(*args, **kwargs)
        
        # Final update
        loader.update_progress(1.0, "Complete!")
        loader.render()
        pygame.time.wait(500)  # Brief pause to show completion
        
        return result


if __name__ == "__main__":
    # Test the loading screen
    import time
    
    def test_loading():
        with LoadingScreenContext() as loader:
            tasks = [
                "Initializing game engine...",
                "Loading sprite sheets...", 
                "Generating world terrain...",
                "Creating tile maps...",
                "Placing buildings...",
                "Loading audio files...",
                "Finalizing world...",
                "Ready to play!"
            ]
            
            for i, task in enumerate(tasks):
                progress = i / (len(tasks) - 1)
                loader.update_progress(progress, task)
                
                for _ in range(30):  # Simulate work
                    if not loader.handle_events():
                        return
                    loader.render()
                    time.sleep(0.05)
    
    print("🎮 Testing FNAD World Loading Screen...")
    test_loading()
    print("✅ Loading screen test complete!")