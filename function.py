import re
import random
import string
import matplotlib.pyplot as plt
from io import BytesIO

def check_password_strength(password):
    """check password strength and return score"""
    score = 0
    feedback = []

    # lenghth checker
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")   
    
    # upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include atlease one special character (!@#$%^&*)")
    
    return score, feedback

def generate_strong_password():
    """Generate a strong password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def plot_strength_meter(score):
    """Generate a barometer for password strength"""
    categories = ["Weak","Moderate","Strong"]
    values = [0,0,0]
    if score <= 2:
        values[0] = score
    elif score == 3:
        values[1] = score
    else:
        values[2] = score

    fig, ax = plt.subplots(figsize=(5,1))
    ax.bar(categories, values,color=['red', 'orange', 'green'], width = 0.5 )
    ax.set_ylim(0,5)
    ax.set_xticks(range(len(categories)))  # ✅ Ensures xticklabels are aligned
    ax.set_xticklabels(categories, fontsize=12)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf


