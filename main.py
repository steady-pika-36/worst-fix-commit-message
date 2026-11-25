import os

line = "fix 4,000 cron emails to Steve by sending them to his emergency contact, his dentist\n"
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
