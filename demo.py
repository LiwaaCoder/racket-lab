from racquet_lab.racket import Racket
from racquet_lab.advisor import StringsAdvisor, StringMaterial, PlayerProfile, RacketMatcher

# 1. Define some rackets
my_racket = Racket("Pure Aero", mass_g=300, balance_cm=32.0, swingweight=290)
store_db = [
    Racket("Ezone 98", 305, 31.5, 292),
    Racket("Blade 98", 305, 32.0, 295),
    Racket("Boom MP", 295, 32.5, 285)
]

# 2. Physics: Calculate Recoil Weight
print(f"--- Racket Physics ---")
print(f"Racket: {my_racket.name}")
print(f"Recoil Weight (Stability): {my_racket.recoil_weight()}")

# 3. Advisor: Recommend Tension
print(f"\n--- String Consultation ---")
player = PlayerProfile(has_injury_history=True)
material = StringMaterial.POLYESTER

rec_tension = StringsAdvisor.suggest_tension(material, 100, player)
print(f"Player has injury? {player.has_injury_history}")
print(f"Material: {material.name}")
print(f"Recommended Tension: {rec_tension} lbs")

# 4. Matcher: Find Similar Racket
print(f"\n--- Racket Matching ---")
similar = RacketMatcher.find_closest_match(my_racket, store_db)
print(f"If you like {my_racket.name}, you might like: {similar.name}")
