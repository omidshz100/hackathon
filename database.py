import sqlite3
import difflib

def init_db():
    conn = sqlite3.connect("lawyers.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS lawyers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT NOT NULL,
            city TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    """)
    c.execute("SELECT COUNT(*) FROM lawyers")
    if c.fetchone()[0] == 0:
        fake_lawyers = [
            ("Alice Smith", "Family Law", "New York", "alice@example.com"),
            ("Bob Johnson", "Criminal", "Los Angeles", "bob@example.com"),
            ("Carol Lee", "Real Estate", "Chicago", "carol@example.com"),
            ("David Kim", "Labor Law", "Houston", "david@example.com"),
            ("Eva Brown", "Immigration", "Phoenix", "eva@example.com"),
            ("Frank White", "Family Law", "Philadelphia", "frank@example.com"),
            ("Grace Green", "Criminal", "San Antonio", "grace@example.com"),
            ("Henry Black", "Real Estate", "San Diego", "henry@example.com"),
            ("Ivy Young", "Labor Law", "Dallas", "ivy@example.com"),
            ("Jack King", "Immigration", "San Jose", "jack@example.com"),
        ]
        c.executemany("INSERT INTO lawyers (name, specialty, city, contact) VALUES (?, ?, ?, ?)", fake_lawyers)
    
    # Create examples table
    c.execute("""
        CREATE TABLE IF NOT EXISTS examples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)
    c.execute("SELECT COUNT(*) FROM examples")
    if c.fetchone()[0] == 0:
        # Generate 100+ example cases
        example_cases = [
            "I need help with my divorce.",
            "I was arrested for theft.",
            "My landlord wants to evict me.",
            "I have not received my salary.",
            "I want to apply for a green card.",
            "I want to adopt a child.",
            "I was fired from my job.",
            "I need help with a property dispute.",
            "I am facing deportation.",
            "I want to file for child custody.",
            "I was accused of fraud.",
            "I need help with my marriage contract.",
            "I want to buy a house.",
            "I have an employment contract issue.",
            "I want to apply for citizenship.",
            "I was a victim of assault.",
            "I need help with alimony.",
            "I want to contest an eviction.",
            "I have overtime payment issues.",
            "I want to sponsor my spouse for immigration.",
            "I was charged with murder.",
            "I want to change my child custody agreement.",
            "I need help with a lease agreement.",
            "I was denied a work visa.",
            "I want to file for adoption.",
            "I was accused of theft.",
            "I need help with a mortgage dispute.",
            "I was not paid for my work.",
            "I want to appeal my deportation.",
            "I want to separate from my spouse.",
            "I was accused of assault.",
            "I need help with a rental contract.",
            "I want to renew my visa.",
            "I want to file for divorce.",
            "I was accused of a crime.",
            "I need help with a landlord dispute.",
            "I was fired without cause.",
            "I want to apply for asylum.",
            "I want to change my name after marriage.",
            "I was accused of fraud.",
            "I need help with a property lease.",
            "I have a salary dispute.",
            "I want to report a workplace injury.",
            "I want to evict my tenant.",
            "I want to get married.",
            "I want to file for overtime pay.",
            "I want to buy commercial property.",
            "I want to report a stolen car.",
            "I want to file for unemployment.",
            "I want to apply for a student visa.",
            "I want to file for bankruptcy.",
            "I want to report domestic violence.",
            "I want to file for legal separation.",
            "I want to dispute a rental increase.",
            "I want to file a discrimination complaint.",
            "I want to apply for permanent residency.",
            "I want to file a restraining order.",
            "I want to report identity theft.",
            "I want to file for wrongful termination.",
            "I want to file for spousal support.",
            "I want to report a hit and run.",
            "I want to file for a work permit.",
            "I want to file for a business license.",
            "I want to report harassment at work.",
            "I want to file for a patent.",
            "I want to file for a trademark.",
            "I want to file for copyright.",
            "I want to file for a zoning change.",
            "I want to file for a building permit.",
            "I want to file for a liquor license.",
            "I want to file for a noise complaint.",
            "I want to file for a parking permit.",
            "I want to file for a dog license.",
            "I want to file for a gun permit.",
            "I want to file for a fishing license.",
            "I want to file for a hunting license.",
            "I want to file for a marriage license.",
            "I want to file for a divorce decree.",
            "I want to file for a birth certificate.",
            "I want to file for a death certificate.",
            "I want to file for a name change.",
            "I want to file for a guardianship.",
            "I want to file for a conservatorship.",
            "I want to file for adoption records.",
            "I want to file for a paternity test.",
            "I want to file for a child support order.",
            "I want to file for a visitation order.",
            "I want to file for a custody modification.",
            "I want to file for a protective order.",
            "I want to file for a civil lawsuit.",
            "I want to file for a small claims case.",
            "I want to file for an appeal.",
            "I want to file for a motion to dismiss.",
            "I want to file for a summary judgment.",
            "I want to file for a continuance.",
            "I want to file for a subpoena.",
            "I want to file for a deposition.",
            "I want to file for a settlement.",
            "I want to file for a plea bargain.",
            "I want to file for bail.",
            "I want to file for parole.",
            "I want to file for probation.",
            "I want to file for expungement.",
            "I want to file for a pardon.",
            "I want to file for clemency.",
            "I want to file for a commutation.",
            "I want to file for a stay of execution.",
            "I want to file for habeas corpus.",
            "I want to file for a writ of mandamus.",
            "I want to file for a writ of certiorari.",
        ]
        c.executemany("INSERT INTO examples (text) VALUES (?)", [(ex,) for ex in example_cases])
    conn.commit()
    conn.close()

def get_example_cases():
    conn = sqlite3.connect("lawyers.db")
    c = conn.cursor()
    c.execute("SELECT text FROM examples")
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_lawyers_by_specialty(specialty):
    conn = sqlite3.connect("lawyers.db")
    c = conn.cursor()
    c.execute("SELECT id, name, specialty, city, contact FROM lawyers WHERE specialty = ?", (specialty,))
    rows = c.fetchall()
    conn.close()
    return rows

def find_closest_example(user_text):
    examples = get_example_cases()
    # Use difflib to find the closest match
    match = difflib.get_close_matches(user_text, examples, n=1, cutoff=0.2)
    return match[0] if match else None