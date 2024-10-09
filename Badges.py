badges = {"Punctual Techie" : 22, "Marvelous Coder" : 20, "Enthusiastic Explorer" : 14, "Creator Pro" : 27, "Coding Wizard" : 16, "Coding Ninja" : 12, "Code Craftsmen" : 1, "Code Conquerer" : 1, "Code Commander" : 6, "Bug Master" : 1, "Brilliant Builder" : 2}
names = ["Punctual Techie", "Marvelous Coder", "Enthusiastic Explorer", "Creator Pro", "Coding Wizard", "Coding Ninja","Code Craftsmen", "Code Conquerer", "Code Commander", "Bug Master", "Brilliant Builder"]
values = []
badge_names = []
for key in badges:
    values.append(badges[key])
for name in names:
    badge_names.append(name)
for i in range(0, 11):
    print(f"{badge_names[i]}: {values[i]}")