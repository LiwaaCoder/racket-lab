from racquet_lab.racket import Racket

# 1. Initialize Racket
racket = Racket(mass_g=305, balance_cm=32.0, swingweight_kg_cm2=290)
print(f"--- Base Racket ---")
print(f"Mass: {racket.mass_g}g")
print(f"Balance: {racket.balance_cm}cm")
print(f"Swingweight: {racket.swingweight_kg_cm2}")
print(f"Recoil Weight: {racket.recoil_weight():.2f}")
print(f"MGR/I: {racket.mgr_i():.2f}")

# 2. Customize
print(f"\n--- Customization: +4g at 12 o'clock (70cm) ---")
customized = racket.customize(mass_added_g=4, position_cm=70)
print(f"New Mass: {customized.mass_g}g")
print(f"New Balance: {customized.balance_cm:.2f}cm")
print(f"New Swingweight: {customized.swingweight_kg_cm2:.2f}")
print(f"New MGR/I: {customized.mgr_i():.2f}")
