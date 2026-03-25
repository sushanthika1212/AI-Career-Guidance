# AI Career Guidance System

# Input
interest = input("Enter your interests: ").lower()

math = int(input("Math score (0-100): "))
physics = int(input("Physics score (0-100): "))
chemistry = int(input("Chemistry score (0-100): "))

# Initialize achievements
coding_ach = 0
science_ach = 0

# Ask achievements based on interest
if "coding" in interest or "data" in interest:
    coding_ach = int(input("Enter coding achievements count: "))

if "electronics" in interest or "machines" in interest or "construction" in interest:
    science_ach = int(input("Enter science/project achievements count: "))

# Initialize scores
software = 0
electronics = 0
mechanical = 0
civil = 0
data_science = 0

# Interest weight
if "coding" in interest:
    software += 3
    data_science += 2

if "electronics" in interest:
    electronics += 3

if "machines" in interest:
    mechanical += 3

if "construction" in interest:
    civil += 3

if "data" in interest:
    data_science += 3

# Academic scores weight
software += (math / 100) * 3
data_science += (math / 100) * 3

electronics += (physics / 100) * 3
mechanical += (physics / 100) * 2
civil += (physics / 100) * 2

civil += (chemistry / 100) * 2

# Achievement weight
software += coding_ach * 2
data_science += coding_ach * 2

electronics += science_ach * 2
mechanical += science_ach * 2
civil += science_ach * 2

# Store scores
scores = {
    "Software Engineer": software,
    "Electronics Engineer": electronics,
    "Mechanical Engineer": mechanical,
    "Civil Engineer": civil,
    "Data Scientist": data_science
}

# Final result
career = max(scores, key=scores.get)

total = sum(scores.values())

print("\n--- Career Probabilities ---")
for k, v in scores.items():
    print(k, ":", round((v/total)*100, 2), "%")

print("\n🎯 Suggested Career:", career)