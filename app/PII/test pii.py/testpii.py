from anonymizer import hide_pii

text = """
My name is Satyam.

Email: satyam@gmail.com

Phone: 9876543210
"""

print(hide_pii(text))