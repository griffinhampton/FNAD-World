# 🎮 FNAD World 

A 2D top-down RPG-style game built in Python using Pygame, featuring dynamic world generation, user authentication, and tile-based exploration.

## 🌟 Features

### 🎲 **Dynamic World Generation**
- **Multi-biome system** with plains, snow (tundra), and mountain regions
- **CSV-based tile mapping** for flexible world design
- **Procedural tile placement** with randomized terrain variation
- **Modular world sections** (3x3 grid system: topLeft, topMiddle, topRight, etc.)

### 🎭 **Player System**
- **Animated sprite movement** with directional animations (up, down, left, right)
- **Smooth collision detection** with terrain and buildings
- **Interactive gameplay** with buildings and NPCs
- **Battle system integration** for RPG encounters

### 🏠 **Interactive Environment**
- **Building interaction system** - press 'F' to enter buildings
- **Screen switching** between overworld and battle modes
- **Collision-based movement** with realistic physics
- **Layered sprite rendering** for proper visual depth

### 🔐 **User Authentication**
- **Custom login system** with username/password storage
- **Guest mode** for temporary play sessions
- **File-based user data persistence**
- **Modern UI** using CustomTkinter

### 🎵 **Audio Integration**
- **Background music** system with looping audio
- **Music management** for different game states
- **Sound effect framework** (expandable)

### 🎨 **Enhanced Loading Experience**
- **Animated loading screen** with progress tracking
- **Player walking animation** during world loading
- **Progress bar visualization** with loading status messages
- **Smooth frame-by-frame sprite animation** (0.25-second intervals)
- **Professional loading interface** preventing black screen delays

## 🛠️ Technical Implementation

### **CSV-Driven World Design**
The game uses a sophisticated CSV parsing system to generate worlds:
- **Tile mapping** from CSV files to sprite coordinates
- **Symbol-based terrain** (B=borders, R=roads, 1=grass, etc.)
- **Multi-zone rendering** supporting different biomes per region
- **Efficient sprite sheet management** with caching

### **Object-Oriented Architecture**
- **Game class** managing main game loop and state
- **Player class** handling movement, animation, and interactions  
- **Block/Buildings classes** for environment rendering
- **Screen management** for different game modes

### **Advanced File Processing**
- **Multi-row CSV enumeration** for large tile data
- **Sprite sheet parsing** and image extraction
- **Configuration file management** for game settings
- **Error handling** for file operations

### **Loading Screen System**
- **Low-memory loading interface** with minimal resource usage
- **Real-time progress tracking** during world generation
- **Sprite animation engine** using individual frame extraction
- **Context manager pattern** for clean loading screen lifecycle
- **Fallback rendering** with graceful error handling

## 🚀 Getting Started

### Prerequisites
```bash
pip install pygame customtkinter
```

### Running the Game
```bash
cd src
python main.py
```

### Game Controls
- **Arrow Keys**: Move player character
- **F Key**: Interact with buildings/NPCs  
- **ESC**: Exit interactions/menus

## 📁 Project Structure

```
src/
├── main.py                    # Entry point
├── gameLogic.py              # Core game mechanics  
├── introScreen.py            # Login/authentication UI
├── dependancyStuff/
│   ├── config.py             # Game constants
│   ├── loadingScreen.py      # Animated loading interface
│   ├── multipleScreens.py    # Screen management
│   ├── sprites/              # Character & object sprites
│   ├── worldGenStuff/        # World generation system
│   ├── passwordStuff/        # Authentication system
│   └── sound/                # Audio management
└── img/                      # Game assets & sprites
```

## 🎯 Educational Value

Originally created as a **CSE 120 final project**, this game demonstrates:

- **File I/O operations** with large datasets
- **CSV parsing and data enumeration** techniques  
- **Game loop architecture** and state management
- **Sprite-based graphics programming**
- **Animation systems** with frame-based sprite cycling
- **Loading screen development** with progress tracking
- **Context managers** for resource management
- **Object-oriented design patterns**
- **User interface development**

The project showcases practical applications of data processing in game development, proving that complex systems can be built using fundamental programming concepts without relying on external databases or advanced frameworks.

## 🔮 Future Enhancements

- **Battle system completion** with combat mechanics
- **NPC dialogue system** and quest framework  
- **Inventory and item management**
- **Save game functionality** with progress persistence
- **Sound effects integration** and audio improvements
- **Multiplayer support** for cooperative play

---

*Built with ❤️ using Python & Pygame*
