# **IR Remote Presentation Controller**

A complete hardware-software solution that transforms any standard infrared remote control into a fully functional presentation controller. This project enables wireless presentation navigation using an Arduino with IR receiver and a Python bridge application.

## **🛠️ System Architecture**

### **Hardware Layer**
- **Arduino Mega** with IR receiver module (pin 53)
- **Standard IR Remote** (TV/DVD/audio remote compatible)
- USB connection to computer

### **Software Layer**
- **Arduino Firmware**: Decodes IR signals into human-readable commands
- **Python Bridge**: Translates IR commands into keyboard inputs for presentation software

## **📡 IR Command Mapping**

| Remote Button | IR Code | Arduino Output | Python Action | Presentation Function |
|--------------|---------|---------------|---------------|----------------------|
| **FORWARD** | 0x43 | "FORWARD" | Right Arrow | Next Slide |
| **BACKWARD** | 0x40 | "BACKWARD" | Left Arrow | Previous Slide |
| **1** | 0xC | "1" | Home | First Slide |
| **2** | 0x18 | "2" | End | Last Slide |
| **MODE** | 0x46 | "MODE" | F5 | Start Presentation |
| **POWER** | 0x45 | "POWER" | ESC | Exit Presentation |

## **🚀 Quick Start Guide**

### **1. Hardware Setup**
```cpp
// Connect IR receiver to Arduino:
// VCC → 5V
// GND → GND
// OUT → Pin 53
```

### **2. Upload Arduino Code**
```cpp
// Upload the provided Arduino sketch
// Open Serial Monitor to verify IR codes
```

### **3. Configure Python Script**
```python
# Install dependencies
pip install pyserial pyautogui

# Update COM port (check Arduino IDE)
arduino = serial.Serial('COM5', 9600)  # Change to your port
```

### **4. Usage**
1. Power Arduino via USB
2. Run Python script
3. Point remote at IR receiver
4. Control presentations wirelessly!

## **🎯 Features & Benefits**

### **Universal Compatibility**
- Works with PowerPoint, Google Slides, Keynote, Canva, and any presentation software
- Compatible with most standard IR remotes
- Cross-platform (Windows, macOS, Linux)

### **Professional Grade**
- Low-latency response (< 50ms)
- Error handling for invalid IR signals
- Scalable architecture for additional functions
- No software installation required on presentation computer

### **Customizable**
- Easy to add new button mappings
- Modify for media control or other applications
- Adjustable delay and sensitivity

## **🔧 Technical Details**

### **Arduino Firmware**
- Uses IRremote library for signal decoding
- Serial communication at 9600 baud

### **Python Bridge**
- Real-time serial monitoring
- PyAutoGUI for system-level keyboard emulation
- Minimal CPU usage (< 1%)

## **🎓 Use Cases**
- **Presenters**: Control slides from anywhere in the room
- **Teachers**: Engage with students while moving freely
- **Business Meetings**: Professional wireless presentation control
- **Accessibility**: Assistive technology for mobility-impaired users
- **DIY Enthusiasts**: Learn about IR communication and HID emulation
**Perfect for**: Presenters, educators, makers, and anyone wanting to repurpose old remotes into useful tools! No soldering required for basic setup.

**⭐ Star this repo if you find it useful for your presentations!**
