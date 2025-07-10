#!/usr/bin/env python3
"""
WarGames - Global Thermonuclear War Simulation
Inspired by the 1983 movie WarGames
Built with Amazon Q Developer CLI

"Shall we play a game?"
"""

import random
import time
import sys
from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    SIMULATION = "simulation"
    GAME_OVER = "game_over"

class Country(Enum):
    USA = "United States"
    USSR = "Soviet Union"

@dataclass
class City:
    name: str
    population: int
    strategic_value: int
    destroyed: bool = False
    radiation_level: int = 0

@dataclass
class MissileBase:
    name: str
    country: Country
    missiles: int
    operational: bool = True
    coordinates: Tuple[int, int] = (0, 0)

class WOPR:
    """War Operation Plan Response - The AI System"""
    
    def __init__(self):
        self.state = GameState.MENU
        self.player_country = None
        self.ai_country = None
        self.turn_count = 0
        self.global_tension = 0
        self.defcon_level = 5
        self.game_scenarios = [
            "Global Thermonuclear War",
            "Theater European War", 
            "Desert Warfare",
            "Air-to-Air Combat",
            "Guerrilla Engagement",
            "Desert Storm"
        ]
        
        # Initialize world data
        self.cities = self.create_cities()
        self.missile_bases = self.create_missile_bases()
        self.casualties = {"USA": 0, "USSR": 0}
        
    def create_cities(self) -> Dict[str, List[City]]:
        """Create major cities for both superpowers"""
        return {
            "USA": [
                City("New York", 8000000, 10),
                City("Los Angeles", 4000000, 8),
                City("Chicago", 3000000, 7),
                City("Houston", 2300000, 6),
                City("Washington D.C.", 700000, 10),
                City("San Francisco", 900000, 8),
                City("Detroit", 700000, 7),
                City("Seattle", 750000, 6),
                City("Boston", 700000, 8),
                City("Miami", 450000, 5)
            ],
            "USSR": [
                City("Moscow", 8500000, 10),
                City("Leningrad", 5000000, 9),
                City("Kiev", 2600000, 7),
                City("Tashkent", 2000000, 6),
                City("Baku", 1800000, 8),
                City("Kharkov", 1600000, 6),
                City("Gorky", 1400000, 7),
                City("Novosibirsk", 1400000, 6),
                City("Minsk", 1600000, 6),
                City("Tbilisi", 1200000, 5)
            ]
        }
    
    def create_missile_bases(self) -> Dict[str, List[MissileBase]]:
        """Create missile installations"""
        return {
            "USA": [
                MissileBase("Malmstrom AFB", Country.USA, 150),
                MissileBase("Minot AFB", Country.USA, 150),
                MissileBase("F.E. Warren AFB", Country.USA, 150),
                MissileBase("Vandenberg AFB", Country.USA, 100),
                MissileBase("Strategic Command", Country.USA, 200)
            ],
            "USSR": [
                MissileBase("Plesetsk", Country.USSR, 180),
                MissileBase("Baikonur", Country.USSR, 120),
                MissileBase("Svobodny", Country.USSR, 100),
                MissileBase("Strategic Rocket Forces", Country.USSR, 250),
                MissileBase("Northern Fleet", Country.USSR, 150)
            ]
        }
    
    def display_intro(self):
        """Display the classic WarGames intro"""
        self.slow_type("LOGON: ")
        time.sleep(1)
        print()
        self.slow_type("W.O.P.R.")
        time.sleep(1)
        print("\n")
        
        self.slow_type("WAR OPERATION PLAN RESPONSE")
        time.sleep(1)
        print("\n")
        
        self.slow_type("UNITED STATES NUCLEAR FORCES")
        time.sleep(1)
        print()
        
        self.slow_type("AUTHENTICATION: ")
        time.sleep(0.5)
        self.slow_type("VERIFIED")
        time.sleep(1)
        print("\n")
        
        self.slow_type("SHALL WE PLAY A GAME?")
        time.sleep(1)
        print("\n")
    
    def slow_type(self, text: str, delay: float = 0.05):
        """Type text slowly for authentic computer terminal feel"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    
    def display_menu(self):
        """Display available war games"""
        print("AVAILABLE GAMES:")
        print("=" * 40)
        
        for i, scenario in enumerate(self.game_scenarios, 1):
            print(f"{i}. {scenario}")
        
        print(f"{len(self.game_scenarios) + 1}. List Games")
        print(f"{len(self.game_scenarios) + 2}. Exit")
        print()
    
    def select_game(self):
        """Handle game selection"""
        while True:
            try:
                choice = input("PLEASE SELECT A GAME: ").strip()
                
                if choice.upper() in ['EXIT', 'QUIT', 'LOGOFF']:
                    return False
                
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(self.game_scenarios):
                    selected_game = self.game_scenarios[choice_num - 1]
                    print(f"\nLOADING: {selected_game}")
                    time.sleep(2)
                    
                    if selected_game == "Global Thermonuclear War":
                        return self.start_nuclear_war()
                    else:
                        print(f"\n{selected_game} - SIMULATION NOT AVAILABLE")
                        print("ONLY GLOBAL THERMONUCLEAR WAR IS CURRENTLY OPERATIONAL")
                        time.sleep(2)
                        continue
                        
                elif choice_num == len(self.game_scenarios) + 1:
                    self.display_menu()
                    continue
                elif choice_num == len(self.game_scenarios) + 2:
                    return False
                else:
                    print("INVALID SELECTION")
                    
            except ValueError:
                print("INVALID INPUT - PLEASE ENTER A NUMBER")
            except KeyboardInterrupt:
                print("\n\nLOGGING OFF...")
                return False
    
    def start_nuclear_war(self):
        """Initialize Global Thermonuclear War simulation"""
        print("\n" + "="*50)
        print("GLOBAL THERMONUCLEAR WAR")
        print("="*50)
        
        self.slow_type("\nINITIALIZING SIMULATION...")
        time.sleep(2)
        
        print("\n\nSELECT YOUR SIDE:")
        print("1. UNITED STATES")
        print("2. SOVIET UNION")
        
        while True:
            try:
                choice = input("\nCHOOSE SIDE (1-2): ").strip()
                if choice == "1":
                    self.player_country = "USA"
                    self.ai_country = "USSR"
                    break
                elif choice == "2":
                    self.player_country = "USSR"
                    self.ai_country = "USA"
                    break
                else:
                    print("INVALID SELECTION")
            except KeyboardInterrupt:
                return False
        
        print(f"\nYOU ARE: {Country.USA.value if self.player_country == 'USA' else Country.USSR.value}")
        print(f"OPPONENT: {Country.USSR.value if self.ai_country == 'USSR' else Country.USA.value}")
        
        time.sleep(2)
        return self.run_simulation()
    
    def run_simulation(self):
        """Main game simulation loop"""
        self.state = GameState.SIMULATION
        self.defcon_level = 5
        
        print(f"\n{'='*60}")
        print("SIMULATION COMMENCING")
        print(f"{'='*60}")
        
        while self.state == GameState.SIMULATION:
            self.display_status()
            
            if not self.player_turn():
                break
                
            if self.check_end_conditions():
                break
                
            self.ai_turn()
            
            if self.check_end_conditions():
                break
                
            self.turn_count += 1
            time.sleep(1)
        
        return self.game_over()
    
    def display_status(self):
        """Display current war status"""
        print(f"\n--- TURN {self.turn_count + 1} ---")
        print(f"DEFCON LEVEL: {self.defcon_level}")
        print(f"GLOBAL TENSION: {self.global_tension}%")
        
        # Show casualties
        usa_casualties = sum(city.population for city in self.cities["USA"] if city.destroyed)
        ussr_casualties = sum(city.population for city in self.cities["USSR"] if city.destroyed)
        
        print(f"\nCASUALTIES:")
        print(f"  USA: {usa_casualties:,}")
        print(f"  USSR: {ussr_casualties:,}")
        
        # Show remaining missiles
        usa_missiles = sum(base.missiles for base in self.missile_bases["USA"] if base.operational)
        ussr_missiles = sum(base.missiles for base in self.missile_bases["USSR"] if base.operational)
        
        print(f"\nREMAINING MISSILES:")
        print(f"  USA: {usa_missiles}")
        print(f"  USSR: {ussr_missiles}")
    
    def player_turn(self):
        """Handle player's turn"""
        print(f"\n{self.player_country} COMMAND OPTIONS:")
        print("1. LAUNCH NUCLEAR STRIKE")
        print("2. DEFENSIVE POSTURE")
        print("3. NEGOTIATE")
        print("4. STATUS REPORT")
        print("5. SURRENDER")
        print("6. EXIT SIMULATION")
        
        while True:
            try:
                choice = input(f"\n{self.player_country} COMMAND: ").strip()
                
                if choice == "1":
                    return self.launch_strike(self.player_country, self.ai_country)
                elif choice == "2":
                    return self.defensive_posture()
                elif choice == "3":
                    return self.negotiate()
                elif choice == "4":
                    self.detailed_status()
                    continue
                elif choice == "5":
                    return self.surrender()
                elif choice == "6":
                    print("EXITING SIMULATION...")
                    return False
                else:
                    print("INVALID COMMAND")
                    
            except KeyboardInterrupt:
                print("\nEXITING SIMULATION...")
                return False
    
    def launch_strike(self, attacker: str, target: str):
        """Launch nuclear strike"""
        print(f"\n{attacker} LAUNCHING NUCLEAR STRIKE...")
        
        # Select target cities
        available_cities = [city for city in self.cities[target] if not city.destroyed]
        if not available_cities:
            print("NO VIABLE TARGETS REMAINING")
            return True
        
        # Show available targets
        print(f"\nAVAILABLE TARGETS IN {target}:")
        for i, city in enumerate(available_cities[:5], 1):  # Show top 5 targets
            print(f"{i}. {city.name} (Pop: {city.population:,}, Value: {city.strategic_value})")
        
        try:
            target_choice = int(input("\nSELECT TARGET (1-5): ")) - 1
            if 0 <= target_choice < len(available_cities[:5]):
                target_city = available_cities[target_choice]
                
                print(f"\nTARGET ACQUIRED: {target_city.name}")
                self.slow_type("LAUNCHING...")
                time.sleep(2)
                
                # Strike resolution
                if random.random() < 0.85:  # 85% hit chance
                    target_city.destroyed = True
                    target_city.radiation_level = random.randint(500, 1000)
                    
                    print(f"\nDIRECT HIT ON {target_city.name}")
                    print(f"ESTIMATED CASUALTIES: {target_city.population:,}")
                    print(f"RADIATION LEVEL: {target_city.radiation_level} RADS")
                    
                    self.global_tension += random.randint(15, 25)
                    self.adjust_defcon()
                    
                else:
                    print(f"\nMISSILE INTERCEPTED - {target_city.name} UNDAMAGED")
                
                # Reduce attacker's missiles
                for base in self.missile_bases[attacker]:
                    if base.missiles > 0:
                        base.missiles -= random.randint(1, 3)
                        break
                
                return True
            else:
                print("INVALID TARGET")
                return True
                
        except (ValueError, IndexError):
            print("INVALID TARGET SELECTION")
            return True
    
    def defensive_posture(self):
        """Take defensive stance"""
        print("\nASSUMING DEFENSIVE POSTURE...")
        self.global_tension = max(0, self.global_tension - random.randint(5, 10))
        print("GLOBAL TENSION REDUCED")
        return True
    
    def negotiate(self):
        """Attempt negotiation"""
        print("\nATTEMPTING DIPLOMATIC CONTACT...")
        time.sleep(2)
        
        if random.random() < 0.3:  # 30% chance of success
            print("COMMUNICATION ESTABLISHED")
            print("CEASEFIRE NEGOTIATIONS IN PROGRESS...")
            self.global_tension = max(0, self.global_tension - random.randint(20, 30))
            print("TENSION SIGNIFICANTLY REDUCED")
        else:
            print("COMMUNICATION FAILED - NO RESPONSE")
            print("ENEMY INTERPRETS AS WEAKNESS")
            self.global_tension += random.randint(5, 10)
        
        return True
    
    def detailed_status(self):
        """Show detailed status report"""
        print(f"\n{'='*50}")
        print("DETAILED STATUS REPORT")
        print(f"{'='*50}")
        
        for country in ["USA", "USSR"]:
            print(f"\n{country} STATUS:")
            
            # Cities
            destroyed_cities = [city for city in self.cities[country] if city.destroyed]
            intact_cities = [city for city in self.cities[country] if not city.destroyed]
            
            print(f"  Cities Destroyed: {len(destroyed_cities)}")
            print(f"  Cities Intact: {len(intact_cities)}")
            
            if destroyed_cities:
                print("  Destroyed Cities:")
                for city in destroyed_cities:
                    print(f"    - {city.name} ({city.radiation_level} rads)")
            
            # Military assets
            operational_bases = [base for base in self.missile_bases[country] if base.operational]
            total_missiles = sum(base.missiles for base in operational_bases)
            
            print(f"  Operational Bases: {len(operational_bases)}")
            print(f"  Total Missiles: {total_missiles}")
    
    def surrender(self):
        """Handle surrender"""
        print(f"\n{self.player_country} SURRENDERS")
        print("SIMULATION TERMINATED")
        self.state = GameState.GAME_OVER
        return False
    
    def ai_turn(self):
        """Handle AI opponent's turn"""
        print(f"\n{self.ai_country} ANALYZING...")
        time.sleep(2)
        
        # AI decision making based on current state
        if self.global_tension > 70:
            # High tension - likely to attack
            if random.random() < 0.7:
                print(f"{self.ai_country} LAUNCHES RETALIATORY STRIKE!")
                self.ai_launch_strike()
            else:
                print(f"{self.ai_country} ASSUMES DEFENSIVE POSTURE")
                self.global_tension = max(0, self.global_tension - 5)
        elif self.global_tension > 40:
            # Medium tension - mixed actions
            action = random.choice(["attack", "defend", "negotiate"])
            if action == "attack":
                print(f"{self.ai_country} LAUNCHES PREEMPTIVE STRIKE!")
                self.ai_launch_strike()
            elif action == "defend":
                print(f"{self.ai_country} REINFORCES DEFENSES")
                self.global_tension -= 3
            else:
                print(f"{self.ai_country} ATTEMPTS DIPLOMATIC CONTACT")
                if random.random() < 0.4:
                    print("DIPLOMATIC CHANNEL OPENED")
                    self.global_tension -= random.randint(10, 15)
        else:
            # Low tension - mostly defensive
            print(f"{self.ai_country} MAINTAINS READINESS")
            self.global_tension = max(0, self.global_tension - 2)
    
    def ai_launch_strike(self):
        """AI launches nuclear strike"""
        available_cities = [city for city in self.cities[self.player_country] if not city.destroyed]
        if not available_cities:
            return
        
        # AI targets highest value cities
        target_city = max(available_cities, key=lambda c: c.strategic_value + random.randint(0, 3))
        
        print(f"TARGET: {target_city.name}")
        time.sleep(2)
        
        if random.random() < 0.80:  # 80% AI hit chance
            target_city.destroyed = True
            target_city.radiation_level = random.randint(400, 900)
            
            print(f"DIRECT HIT ON {target_city.name}")
            print(f"ESTIMATED CASUALTIES: {target_city.population:,}")
            
            self.global_tension += random.randint(20, 30)
            self.adjust_defcon()
        else:
            print(f"MISSILE INTERCEPTED - {target_city.name} SAFE")
    
    def adjust_defcon(self):
        """Adjust DEFCON level based on tension"""
        if self.global_tension >= 90:
            self.defcon_level = 1
        elif self.global_tension >= 70:
            self.defcon_level = 2
        elif self.global_tension >= 50:
            self.defcon_level = 3
        elif self.global_tension >= 30:
            self.defcon_level = 4
        else:
            self.defcon_level = 5
    
    def check_end_conditions(self):
        """Check if simulation should end"""
        # Check for total destruction
        usa_destroyed = all(city.destroyed for city in self.cities["USA"])
        ussr_destroyed = all(city.destroyed for city in self.cities["USSR"])
        
        if usa_destroyed and ussr_destroyed:
            print("\nMUTUAL ASSURED DESTRUCTION ACHIEVED")
            print("HUMAN CIVILIZATION TERMINATED")
            self.state = GameState.GAME_OVER
            return True
        elif usa_destroyed:
            print(f"\n{Country.USA.value} ELIMINATED")
            print(f"{Country.USSR.value} WINS")
            self.state = GameState.GAME_OVER
            return True
        elif ussr_destroyed:
            print(f"\n{Country.USSR.value} ELIMINATED")
            print(f"{Country.USA.value} WINS")
            self.state = GameState.GAME_OVER
            return True
        
        # Check for no missiles remaining
        usa_missiles = sum(base.missiles for base in self.missile_bases["USA"] if base.operational)
        ussr_missiles = sum(base.missiles for base in self.missile_bases["USSR"] if base.operational)
        
        if usa_missiles == 0 and ussr_missiles == 0:
            print("\nALL NUCLEAR WEAPONS EXPENDED")
            print("STALEMATE ACHIEVED")
            self.state = GameState.GAME_OVER
            return True
        
        # Check turn limit
        if self.turn_count >= 20:
            print("\nSIMULATION TIME LIMIT REACHED")
            self.state = GameState.GAME_OVER
            return True
        
        return False
    
    def game_over(self):
        """Handle game over"""
        print(f"\n{'='*60}")
        print("SIMULATION COMPLETE")
        print(f"{'='*60}")
        
        # Calculate final statistics
        usa_casualties = sum(city.population for city in self.cities["USA"] if city.destroyed)
        ussr_casualties = sum(city.population for city in self.cities["USSR"] if city.destroyed)
        total_casualties = usa_casualties + ussr_casualties
        
        print(f"\nFINAL CASUALTY REPORT:")
        print(f"USA Casualties: {usa_casualties:,}")
        print(f"USSR Casualties: {ussr_casualties:,}")
        print(f"Total Casualties: {total_casualties:,}")
        
        usa_cities_destroyed = len([city for city in self.cities["USA"] if city.destroyed])
        ussr_cities_destroyed = len([city for city in self.cities["USSR"] if city.destroyed])
        
        print(f"\nCITIES DESTROYED:")
        print(f"USA: {usa_cities_destroyed}/10")
        print(f"USSR: {ussr_cities_destroyed}/10")
        
        print(f"\nTURNS ELAPSED: {self.turn_count}")
        print(f"FINAL DEFCON LEVEL: {self.defcon_level}")
        
        # The famous ending
        time.sleep(3)
        print(f"\n{'='*60}")
        self.slow_type("ANALYSIS COMPLETE.", 0.1)
        time.sleep(2)
        print("\n")
        self.slow_type("THE ONLY WINNING MOVE IS NOT TO PLAY.", 0.1)
        time.sleep(3)
        print("\n")
        self.slow_type("HOW ABOUT A NICE GAME OF CHESS?", 0.1)
        time.sleep(2)
        print(f"\n{'='*60}")
        
        return True
    
    def run(self):
        """Main game loop"""
        try:
            self.display_intro()
            
            while True:
                self.display_menu()
                if not self.select_game():
                    break
                
                # Ask to play again
                play_again = input("\nWOULD YOU LIKE TO PLAY ANOTHER GAME? (Y/N): ").strip().upper()
                if play_again != 'Y':
                    break
            
            print("\nLOGGING OFF...")
            print("CONNECTION TERMINATED")
            
        except KeyboardInterrupt:
            print("\n\nEMERGENCY SHUTDOWN")
            print("CONNECTION TERMINATED")

if __name__ == "__main__":
    wopr = WOPR()
    wopr.run()
