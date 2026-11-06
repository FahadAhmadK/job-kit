name = "Fahad"
title = "AI Engineering"
city = "ilmenau"
email = "you@example.com"

header = f"{name} | {title} | {city}"
print(header)
print(f"Contact: {email}")

skills = ["Python", "Git", "SQL"]
languages = ["English (C1)", "German (A2)"]

print()
print(f"Skills ({len(skills)}):")
for skill in skills:
    print("-", skill)

print("Languages:", ", ".join(languages))