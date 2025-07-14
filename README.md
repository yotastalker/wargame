# 🚀 WarGames - Global Thermonuclear War Simulation

**"Shall we play a game?"**

A faithful recreation of the WOPR (War Operation Plan Response) computer system from the classic 1983 movie WarGames, built with Amazon Q Developer CLI.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Amazon Q](https://img.shields.io/badge/built%20with-Amazon%20Q-orange.svg)](https://aws.amazon.com/q/developer/)

## 🎮 About

Experience the tension of Cold War nuclear strategy in this authentic recreation of the WarGames movie computer simulation. Take control of either the United States or Soviet Union in a high-stakes game of Global Thermonuclear War, where the only winning move might be not to play at all.

**🤖 Built with Amazon Q Developer CLI - showcasing AI's ability to recreate classic movie experiences through conversation!**

## ⚡ Quick Start

```bash
git clone https://github.com/yotastalker/wargame.git
cd wargame
python3 wargames.py
```

**No dependencies required - just Python 3.7+!**

## 🎯 Game Features

### 🖥️ **Authentic 1980s Experience**
- **Slow-typing terminal interface** - Just like the movie
- **Classic WOPR login sequence** - "SHALL WE PLAY A GAME?"
- **Authentic computer responses** - Period-accurate dialogue
- **Green-screen terminal aesthetic** - True to the era

### ⚔️ **Global Thermonuclear War**
- **USA vs USSR conflict** - Choose your superpower
- **Real cities and targets** - New York, Moscow, and more
- **Strategic missile bases** - Malmstrom AFB, Plesetsk, etc.
- **DEFCON level system** - Escalating tension mechanics

### 🎲 **Strategic Gameplay**
- **Turn-based combat** - Plan your moves carefully
- **Multiple action types** - Attack, defend, negotiate, surrender
- **AI opponent** - WOPR makes strategic decisions
- **Casualty tracking** - Population and infrastructure damage
- **Radiation simulation** - Environmental consequences

### 🎭 **Movie-Accurate Elements**
- **Multiple game scenarios** - Theater European War, Desert Storm, etc.
- **Authentic quotes** - "The only winning move is not to play"
- **Classic ending sequence** - WOPR's famous analysis
- **Period-appropriate interface** - 1980s computer terminal feel

## 🎮 How to Play

### 🚀 **Starting the Simulation**
1. **Run the game** - `python3 wargames.py`
2. **Watch the WOPR boot sequence** - Authentic login experience
3. **Select "Global Thermonuclear War"** - The main simulation
4. **Choose your side** - USA or Soviet Union

### 🕹️ **Game Commands**
- **Launch Nuclear Strike** - Target enemy cities
- **Defensive Posture** - Reduce global tension
- **Negotiate** - Attempt diplomatic solutions
- **Status Report** - View detailed war status
- **Surrender** - End the simulation
- **Exit** - Return to main menu

### ⚔️ **Strategic Elements**
- **Target Selection** - Choose high-value enemy cities
- **Missile Management** - Limited nuclear arsenal
- **Tension Control** - Balance aggression with diplomacy
- **DEFCON Monitoring** - Watch escalation levels

## 🗺️ The Cold War World

### 🇺🇸 **United States Targets**
- **New York** - 8M population, strategic value 10
- **Los Angeles** - 4M population, strategic value 8
- **Washington D.C.** - 700K population, strategic value 10
- **Chicago, Houston, San Francisco** - Major metropolitan areas

### 🇷🇺 **Soviet Union Targets**
- **Moscow** - 8.5M population, strategic value 10
- **Leningrad** - 5M population, strategic value 9
- **Kiev** - 2.6M population, strategic value 7
- **Baku, Kharkov, Gorky** - Industrial centers

### 🚀 **Military Assets**
- **USA**: Malmstrom AFB, Minot AFB, F.E. Warren AFB
- **USSR**: Plesetsk, Baikonur, Strategic Rocket Forces
- **Missile Counts**: Realistic Cold War arsenals
- **Hit Probability**: 80-85% accuracy simulation

## 🎯 Game Mechanics

### 📊 **Tension System**
```
DEFCON 5: Normal readiness (0-29% tension)
DEFCON 4: Increased readiness (30-49% tension)  
DEFCON 3: Round the clock readiness (50-69% tension)
DEFCON 2: Next step to nuclear war (70-89% tension)
DEFCON 1: Nuclear war imminent (90-100% tension)
```

### 💥 **Combat Resolution**
- **Strike Success**: 85% player hit rate, 80% AI hit rate
- **Casualty Calculation**: Based on city population
- **Radiation Effects**: 400-1000 rad contamination
- **Strategic Value**: Affects AI targeting priorities

### 🤖 **AI Behavior**
- **High Tension (70%+)**: 70% chance of retaliation
- **Medium Tension (40-70%)**: Mixed defensive/offensive actions
- **Low Tension (<40%)**: Primarily defensive posture
- **Target Selection**: Prioritizes high-value strategic targets

## 🎬 Movie References

### 🎭 **Authentic Quotes**
- *"Shall we play a game?"*
- *"How about Global Thermonuclear War?"*
- *"The only winning move is not to play."*
- *"How about a nice game of chess?"*

### 🖥️ **Interface Elements**
- **WOPR login sequence**
- **Slow-typing computer responses**
- **Game selection menu**
- **Strategic analysis displays**

## 🛠️ Technical Features

### 🏗️ **Clean Architecture**
```python
class WOPR:
    def __init__(self):
        self.cities = self.create_cities()
        self.missile_bases = self.create_missile_bases()
        self.defcon_level = 5
```

### ⚡ **Real-time Effects**
```python
def slow_type(self, text: str, delay: float = 0.05):
    # Authentic terminal typing effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
```

### 🎲 **Strategic AI**
```python
def ai_turn(self):
    if self.global_tension > 70:
        # High tension - likely to attack
        if random.random() < 0.7:
            self.ai_launch_strike()
```

## 🎯 End Game Scenarios

### 💀 **Mutual Assured Destruction**
- All cities destroyed on both sides
- Human civilization terminated
- Classic MAD doctrine demonstration

### 🏆 **Victory Conditions**
- Complete elimination of enemy cities
- Enemy surrender
- Nuclear arsenal depletion

### 🕊️ **Peaceful Resolution**
- Successful diplomatic negotiations
- Tension reduction below critical levels
- WOPR's wisdom: "Not to play"

## 🎓 Educational Value

### 📚 **Cold War History**
- **Authentic 1980s setting** - Reagan-era tensions
- **Real military installations** - Historical accuracy
- **Nuclear doctrine** - MAD strategy explanation
- **DEFCON system** - Military readiness levels

### 🤔 **Strategic Thinking**
- **Risk assessment** - Weighing attack vs. diplomacy
- **Resource management** - Limited missile supplies
- **Escalation control** - Managing global tension
- **Consequence awareness** - Population casualty impact

## 🚀 Amazon Q Development Showcase

### 🤖 **What This Demonstrates**
- **Cultural recreation** - Faithful movie adaptation
- **Complex game systems** - Multi-layered strategic gameplay
- **Authentic interfaces** - Period-accurate user experience
- **Educational gaming** - Historical and strategic learning

### 💡 **AI Development Insights**
- **Nostalgic recreation** through conversational design
- **Balancing authenticity** with engaging gameplay
- **Historical accuracy** combined with entertainment
- **Classic movie homage** built through AI collaboration

## 🎮 Play Responsibly

This simulation is designed for:
- **Educational purposes** - Understanding Cold War tensions
- **Historical appreciation** - 1980s computer culture
- **Strategic thinking** - Decision-making under pressure
- **Entertainment** - Classic movie recreation

**Remember WOPR's lesson: "The only winning move is not to play."**

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`#WarGames` `#WOPR` `#ColdWar` `#NuclearWar` `#1980s` `#MovieGame` `#Strategy` `#Python` `#Simulation` `#AmazonQ`

---

**Built with Amazon Q Developer CLI - From movie inspiration to playable simulation through AI conversation!**

*"Greetings, Professor Falken. Shall we play a game?"* 🚀💻⚔️
